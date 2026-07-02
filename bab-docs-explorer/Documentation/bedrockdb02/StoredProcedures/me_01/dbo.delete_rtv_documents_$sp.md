# dbo.delete_rtv_documents_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.delete_rtv_documents_$sp"]
    dbo_carton_document_map(["dbo.carton_document_map"]) --> SP
    dbo_d(["dbo.d"]) --> SP
    dbo_extension_queue(["dbo.extension_queue"]) --> SP
    dbo_i(["dbo.i"]) --> SP
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> SP
    dbo_im_attribute(["dbo.im_attribute"]) --> SP
    dbo_im_document_deleted(["dbo.im_document_deleted"]) --> SP
    dbo_im_message(["dbo.im_message"]) --> SP
    dbo_m(["dbo.m"]) --> SP
    dbo_parameter_im(["dbo.parameter_im"]) --> SP
    dbo_r(["dbo.r"]) --> SP
    dbo_return_floor_date__sp(["dbo.return_floor_date_$sp"]) --> SP
    dbo_rtv(["dbo.rtv"]) --> SP
    dbo_rtv_detail(["dbo.rtv_detail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.carton_document_map |
| dbo.d |
| dbo.extension_queue |
| dbo.i |
| dbo.ib_audit_trail |
| dbo.im_attribute |
| dbo.im_document_deleted |
| dbo.im_message |
| dbo.m |
| dbo.parameter_im |
| dbo.r |
| dbo.return_floor_date_$sp |
| dbo.rtv |
| dbo.rtv_detail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[delete_rtv_documents_$sp]
AS 

/* 
Proc name:  delete_rtv_documents_$sp
Desc: This procedure is called from delete_im_documents_$sp, it deletes Return To Vendor documents based on parameters stored in table parameter_im.
	  The delete should also comply with some business rules listed below.
History: Creation March 03, 2011
*/
BEGIN
	DECLARE @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000), @cleanup_weeks SMALLINT, @floor_date SMALLDATETIME, @batch_size INT,
		@min_rtv_id DECIMAL(12,0), @max_rtv_id DECIMAL(12,0), @done BIT, @counter INT;
		
	-- Make sure this table doesn't exists at the beginning of the process
	IF object_id(N'tempdb..#temp_rtv') IS NOT NULL
		DROP TABLE #temp_rtv;
		
	SELECT @done = 0, @batch_size = 500000,
		@min_rtv_id = MIN(rtv_id),
		@max_rtv_id = MAX(rtv_id) 
	FROM rtv;

	BEGIN TRY
	
		SELECT @cleanup_weeks = rtv_cleanup_weeks FROM parameter_im;
		
		EXEC return_floor_date_$sp @cleanup_weeks, @floor_date OUTPUT
		
		-- Batch the following inserts in case there are a large number  of documents to delete
		WHILE (@min_rtv_id < @max_rtv_id)
		BEGIN
				BEGIN TRAN
				
				-- Rule # IMRTV121 - Delete all Cancelled RTVs
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT rtv_id, document_no, 10, -- document_type for rtv is 10
					document_status
				FROM rtv 
				WHERE rtv_id BETWEEN @min_rtv_id AND @min_rtv_id + @batch_size
				AND document_status = 7;
				
				-- Rule # IMTRA122 - Delete all RTVs with a status of Fully Matched and return date at least x weeks ago
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT rtv_id, document_no, 10, document_status
				FROM rtv 
				WHERE rtv_id BETWEEN @min_rtv_id AND @min_rtv_id + @batch_size 
				AND match_status = 5
				AND returned_date < @floor_date;
							
				COMMIT TRAN
				
				SET @min_rtv_id = @min_rtv_id + @batch_size;
		END;
		
		UPDATE STATISTICS im_document_deleted;
			
		SELECT @counter = COUNT(*), @done = 0, @max_rtv_id = 0 FROM im_document_deleted WHERE document_type = 10;
		
		IF (@counter > 10000)
		BEGIN
			WHILE (@done = 0)
			BEGIN
				-- We cannot do the delete in one big batch
				SELECT TOP 10000 im_document_id, im_document_no, document_type, document_status
				INTO #temp_rtv
				FROM im_document_deleted
				WHERE document_type = 10
				AND im_document_id > @max_rtv_id
				ORDER BY im_document_id;
				
				IF (@@ROWCOUNT > 0)	
					SELECT @max_rtv_id = MAX(im_document_id) FROM #temp_rtv;
				ELSE
					SET @done = 1;	
					
				IF (@done = 0)
				BEGIN
					BEGIN TRAN
					
					DELETE i
					FROM #temp_rtv t, im_attribute i
					WHERE i.parent_id = t.im_document_id
					AND i.parent_type = 10;
					
					DELETE i
					FROM #temp_rtv t,  im_message i
					WHERE i.parent_id = t.im_document_id
					AND i.parent_type = 10;

					DELETE m
					FROM #temp_rtv t, carton_document_map m
					WHERE m.document_type = 4
					AND m.document_id = t.im_document_id;
					
					DELETE d
					FROM #temp_rtv t, rtv_detail d
					WHERE d.rtv_id = t.im_document_id;
					
					DELETE r
					FROM #temp_rtv t, rtv r
					WHERE r.rtv_id = t.im_document_id;

					DELETE i
					FROM #temp_rtv t, ib_audit_trail i
					WHERE i.application = N'IM' 
					AND i.application_type = N'RTV' 
					AND i.application_identifier = t.im_document_no;
					
					-- Now do an INSERT to keep trace of documents deleted
					INSERT INTO ib_audit_trail
						   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
						   application_level, application_key, action, field_affected, old_value, new_value, 
						   status, employee_last_name, employee_first_name)
					 SELECT GETDATE(), N'IM', N'Delete', NULL, N'RTV', t.im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
						     CASE WHEN t.document_status = 1 THEN N'Preliminary'
								  WHEN t.document_status = 2 THEN N'Ready to Send'
								  WHEN t.document_status = 3 THEN N'Sent'
								  WHEN t.document_status = 4 THEN N'Received'
								  WHEN t.document_status = 5 THEN N'Partially Matched'
								  WHEN t.document_status = 6 THEN N'Fully Matched'
								  WHEN t.document_status = 7 THEN N'Cancelled'
								  WHEN t.document_status = 8 THEN N'Requested'
								  WHEN t.document_status = 9 THEN N'Returned'
								  WHEN t.document_status = 10 THEN N'Submitted'
								  WHEN t.document_status = 11 THEN N'Released'
								  WHEN t.document_status = 12 THEN N'Unmatched'
								  WHEN t.document_status = 13 THEN N'Counted'
								  WHEN t.document_status = 14 THEN N'Partially Posted'
								  WHEN t.document_status = 15 THEN N'Posted'
								  WHEN t.document_status = 16 THEN N'In Transit'
								  WHEN t.document_status = 17 THEN N'Partially Returned'
								  ELSE N'Undefined'
							 END status
						   , N'Batch Delete'
						   , N'Pipeline Segment 3004'
					FROM #temp_rtv t;
					
					/* WriteMessage
					INSERT INTO extension_queue
						(type, entity_id, method_id, entity_name)
					SELECT 1, t.im_document_id, N'A5994481-5C58-4c7b-95FB-7764D06B3228', t.im_document_no
					FROM #temp_rtv t
					ORDER BY t.im_document_id; */
						
					COMMIT TRAN;
				END;
				IF object_id(N'tempdb..#temp_rtv') IS NOT NULL
					DROP TABLE #temp_rtv;
			END;
		END;
		ELSE
		BEGIN				
			-- Just a small number of documents to delete: do it in one batch
			BEGIN TRAN
			
				DELETE i
				FROM im_document_deleted d, im_attribute i
				WHERE d.document_type = 10 
				AND d.im_document_id = i.parent_id
				AND i.parent_type = 10;
				
				DELETE i
				FROM im_document_deleted d, im_message i
				WHERE d.document_type = 10 
				AND d.im_document_id = i.parent_id
				AND i.parent_type = 10;

				DELETE m
				FROM im_document_deleted d, carton_document_map m
				WHERE d.document_type = 10
				AND d.im_document_id = m.document_id
				AND m.document_type = 4;
				
				DELETE rd
				FROM im_document_deleted d, rtv_detail rd
				WHERE d.document_type = 10 
				AND d.im_document_id = rd.rtv_id;
				
				DELETE r
				FROM im_document_deleted d, rtv r
				WHERE d.document_type = 10 
				AND d.im_document_id = r.rtv_id;

				DELETE i
				FROM im_document_deleted d, ib_audit_trail i
				WHERE d.document_type = 10  
				AND i.application = N'IM' 
				AND i.application_type = N'RTV' 
				AND d.im_document_no = i.application_identifier;
				
				-- Now do an INSERT to keep trace of documents deleted
				INSERT INTO ib_audit_trail
					   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
					   application_level, application_key, action, field_affected, old_value, new_value, 
					   status, employee_last_name, employee_first_name)
				 SELECT GETDATE(), N'IM', N'Delete', NULL, N'RTV', d.im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
					     CASE WHEN d.document_status = 1 THEN N'Preliminary'
							  WHEN d.document_status = 2 THEN N'Ready to Send'
							  WHEN d.document_status = 3 THEN N'Sent'
							  WHEN d.document_status = 4 THEN N'Received'
							  WHEN d.document_status = 5 THEN N'Partially Matched'
							  WHEN d.document_status = 6 THEN N'Fully Matched'
							  WHEN d.document_status = 7 THEN N'Cancelled'
							  WHEN d.document_status = 8 THEN N'Requested'
							  WHEN d.document_status = 9 THEN N'Returned'
							  WHEN d.document_status = 10 THEN N'Submitted'
							  WHEN d.document_status = 11 THEN N'Released'
							  WHEN d.document_status = 12 THEN N'Unmatched'
							  WHEN d.document_status = 13 THEN N'Counted'
							  WHEN d.document_status = 14 THEN N'Partially Posted'
							  WHEN d.document_status = 15 THEN N'Posted'
							  WHEN d.document_status = 16 THEN N'In Transit'
							  WHEN d.document_status = 17 THEN N'Partially Returned'
							  ELSE N'Undefined'
						 END status
					   , N'Batch Delete'
					   , N'Pipeline Segment 3004'
				FROM im_document_deleted d
				WHERE d.document_type = 10;
				
				-- WriteMessage
				INSERT INTO extension_queue
					(type, entity_id, method_id, entity_name)
				SELECT 1, d.im_document_id, N'A5994481-5C58-4c7b-95FB-7764D06B3228', d.im_document_no
				FROM im_document_deleted d
				WHERE d.document_type = 10 
				ORDER BY d.im_document_id;
				
			COMMIT TRAN
		END;
	END TRY

	BEGIN CATCH
		SELECT @error_msg = ERROR_MESSAGE(),
		       @sql_err_num = ERROR_NUMBER();
		 
		IF @@TRANCOUNT <> 0
			ROLLBACK TRANSACTION
			
		SET @error_msg = N'Error in procedure delete_rtv_documents_$sp: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + N' ' + ERROR_MESSAGE()
		RAISERROR (@error_msg, -- Message text.
               16, -- Severity.
               1) -- State.
	END CATCH
END
```

