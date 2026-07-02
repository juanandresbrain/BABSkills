# dbo.delete_avg_cost_adj_documents_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.delete_avg_cost_adj_documents_$sp"]
    dbo_a(["dbo.a"]) --> SP
    dbo_average_cost_adj_style(["dbo.average_cost_adj_style"]) --> SP
    dbo_average_cost_adjustment(["dbo.average_cost_adjustment"]) --> SP
    dbo_avg_cost_adj_style_loc(["dbo.avg_cost_adj_style_loc"]) --> SP
    dbo_i(["dbo.i"]) --> SP
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> SP
    dbo_im_document_deleted(["dbo.im_document_deleted"]) --> SP
    dbo_im_message(["dbo.im_message"]) --> SP
    dbo_parameter_im(["dbo.parameter_im"]) --> SP
    dbo_return_floor_date__sp(["dbo.return_floor_date_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.a |
| dbo.average_cost_adj_style |
| dbo.average_cost_adjustment |
| dbo.avg_cost_adj_style_loc |
| dbo.i |
| dbo.ib_audit_trail |
| dbo.im_document_deleted |
| dbo.im_message |
| dbo.parameter_im |
| dbo.return_floor_date_$sp |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[delete_avg_cost_adj_documents_$sp]
AS 

/* 
Proc name:  delete_rtv_documents_$sp
Desc: This procedure is called from delete_im_documents_$sp, it deletes AVERAGE COST ADJUSTMENTS documents based on parameters stored in table parameter_im.
	  The delete should also comply with some business rules listed below.
History: Creation March 03, 2011
*/
BEGIN
	DECLARE @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000), @cleanup_weeks SMALLINT, @floor_date SMALLDATETIME, @batch_size INT,
		@min_avg_cost_adj_id DECIMAL(12,0), @max_avg_cost_adj_id DECIMAL(12,0), @done BIT, @counter INT;
		
	-- Make sure this table doesn't exists at the beginning of the process
	IF object_id(N'tempdb..#temp_avg_cost_adj') IS NOT NULL
		DROP TABLE #temp_avg_cost_adj;
		
	SELECT @done = 0, @batch_size = 500000,
		@min_avg_cost_adj_id = MIN(average_cost_adjustment_id),
		@max_avg_cost_adj_id = MAX(average_cost_adjustment_id) 
	FROM average_cost_adjustment;

	BEGIN TRY
	
		SELECT @cleanup_weeks = avg_cost_adj_cleanup_weeks FROM parameter_im;
		
		EXEC return_floor_date_$sp @cleanup_weeks, @floor_date OUTPUT
		
		-- Batch the following inserts in case there are a large number  of documents to delete
		WHILE (@min_avg_cost_adj_id < @max_avg_cost_adj_id)
		BEGIN
				BEGIN TRAN
				
				-- Rule # IMDRA108 - Delete all Average Cost Adjustments with a status of Submitted and submitted date at least x weeks ago
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT average_cost_adjustment_id, document_no, 21, -- document_type for Average Cost Adjustments is 21
					document_status
				FROM average_cost_adjustment
				WHERE average_cost_adjustment_id BETWEEN @min_avg_cost_adj_id AND @min_avg_cost_adj_id + @batch_size
				AND document_status = 10
				AND submit_date < @floor_date;
				
				COMMIT TRAN
				
				SET @min_avg_cost_adj_id = @min_avg_cost_adj_id + @batch_size;
		END;
		
		UPDATE STATISTICS im_document_deleted;
			
		SELECT @counter = COUNT(*), @done = 0, @max_avg_cost_adj_id = 0 FROM im_document_deleted WHERE document_type = 21;
		
		IF (@counter > 10000)
		BEGIN
			WHILE (@done = 0)
			BEGIN
				-- We cannot do the delete in one big batch
				SELECT TOP 10000 im_document_id, im_document_no, document_type, document_status
				INTO #temp_avg_cost_adj
				FROM im_document_deleted
				WHERE document_type = 21
				AND im_document_id > @max_avg_cost_adj_id
				ORDER BY im_document_id;
				
				IF (@@ROWCOUNT > 0)	
					SELECT @max_avg_cost_adj_id = MAX(im_document_id) FROM #temp_avg_cost_adj;
				ELSE
					SET @done = 1;	
					
				IF (@done = 0)
				BEGIN
					BEGIN TRAN
					
					DELETE i
					FROM #temp_avg_cost_adj t, im_message i
					WHERE t.im_document_id = i.parent_id 
					AND i.parent_type = 21;
					
					DELETE a
					FROM #temp_avg_cost_adj t, avg_cost_adj_style_loc a
					WHERE t.im_document_id = a.average_cost_adjustment_id;
					
					DELETE a
					FROM #temp_avg_cost_adj t, average_cost_adj_style a
					WHERE t.im_document_id = a.average_cost_adjustment_id;
					
					DELETE a
					FROM #temp_avg_cost_adj t, average_cost_adjustment a
					WHERE t.im_document_id = a.average_cost_adjustment_id;
					
					-- Update Delete Log: ib audit trail				
					DELETE i
					FROM #temp_avg_cost_adj t, ib_audit_trail i
					WHERE i.application = N'IM' 
					AND i.application_type = N'AverageCostAdjustment' 
					AND t.im_document_no = i.application_identifier;
					
					-- Now do an INSERT to keep trace of documents deleted
					INSERT INTO ib_audit_trail
						   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
						   application_level, application_key, action, field_affected, old_value, new_value, 
						   status, employee_last_name, employee_first_name)
					 SELECT GETDATE(), N'IM', N'Delete', NULL, N'AverageCostAdjustment', t.im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
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
					FROM #temp_avg_cost_adj t;
					
					COMMIT TRAN;
				END;
				IF object_id(N'tempdb..#temp_avg_cost_adj') IS NOT NULL
					DROP TABLE #temp_avg_cost_adj;
			END;
		END;
		ELSE
		BEGIN				
			-- Just a small number of documents to delete: do it in one batch
			BEGIN TRAN
			
			DELETE i
			FROM im_document_deleted d, im_message i
			WHERE d.document_type = 21
			AND d.im_document_id = i.parent_id 
			AND i.parent_type = 21;
			
			DELETE a
			FROM im_document_deleted d, avg_cost_adj_style_loc a
			WHERE d.document_type = 21 
			AND d.im_document_id = a.average_cost_adjustment_id;
			
			DELETE a
			FROM im_document_deleted d, average_cost_adj_style a
			WHERE d.document_type = 21  
			AND d.im_document_id = a.average_cost_adjustment_id;
			
			DELETE a
			FROM im_document_deleted d, average_cost_adjustment a
			WHERE d.document_type = 21   
			AND d.im_document_id = a.average_cost_adjustment_id;
			
			-- Update Delete Log: ib audit trail				
			DELETE i
			FROM im_document_deleted d, ib_audit_trail i
			WHERE d.document_type = 21    
			AND i.application = N'IM' 
			AND i.application_type = N'AverageCostAdjustment' 
			AND d.im_document_no = i.application_identifier;
			
			-- Now do an INSERT to keep trace of documents deleted
			INSERT INTO ib_audit_trail
				   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
				   application_level, application_key, action, field_affected, old_value, new_value, 
				   status, employee_last_name, employee_first_name)
			 SELECT GETDATE(), N'IM', N'Delete', NULL, N'AverageCostAdjustment', im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
				     CASE WHEN document_status = 1 THEN N'Preliminary'
						  WHEN document_status = 2 THEN N'Ready to Send'
						  WHEN document_status = 3 THEN N'Sent'
						  WHEN document_status = 4 THEN N'Received'
						  WHEN document_status = 5 THEN N'Partially Matched'
						  WHEN document_status = 6 THEN N'Fully Matched'
						  WHEN document_status = 7 THEN N'Cancelled'
						  WHEN document_status = 8 THEN N'Requested'
						  WHEN document_status = 9 THEN N'Returned'
						  WHEN document_status = 10 THEN N'Submitted'
						  WHEN document_status = 11 THEN N'Released'
						  WHEN document_status = 12 THEN N'Unmatched'
						  WHEN document_status = 13 THEN N'Counted'
						  WHEN document_status = 14 THEN N'Partially Posted'
						  WHEN document_status = 15 THEN N'Posted'
						  WHEN document_status = 16 THEN N'In Transit'
						  WHEN document_status = 17 THEN N'Partially Returned'
						  ELSE N'Undefined'
					 END status
				   , N'Batch Delete'
				   , N'Pipeline Segment 3004'
			FROM im_document_deleted 
			WHERE document_type = 21;
					
			COMMIT TRAN
		END;
	END TRY

	BEGIN CATCH
		SELECT @error_msg = ERROR_MESSAGE(),
		       @sql_err_num = ERROR_NUMBER();
		 
		IF @@TRANCOUNT <> 0
			ROLLBACK TRANSACTION
			
		SET @error_msg = N'Error in procedure delete_avg_cost_adj_documents_$sp: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + N' ' + ERROR_MESSAGE()
		RAISERROR (@error_msg, -- Message text.
               16, -- Severity.
               1) -- State.
	END CATCH
END
```

