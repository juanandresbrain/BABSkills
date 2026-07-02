# dbo.delete_imrd_documents_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.delete_imrd_documents_$sp"]
    dbo_d(["dbo.d"]) --> SP
    dbo_i(["dbo.i"]) --> SP
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> SP
    dbo_im_attribute(["dbo.im_attribute"]) --> SP
    dbo_im_document_deleted(["dbo.im_document_deleted"]) --> SP
    dbo_im_message(["dbo.im_message"]) --> SP
    dbo_im_to_do_worklist(["dbo.im_to_do_worklist"]) --> SP
    dbo_inv_move_req_from_loc(["dbo.inv_move_req_from_loc"]) --> SP
    dbo_inv_move_request_detail(["dbo.inv_move_request_detail"]) --> SP
    dbo_inventory_move_request(["dbo.inventory_move_request"]) --> SP
    dbo_parameter_im(["dbo.parameter_im"]) --> SP
    dbo_parameter_system(["dbo.parameter_system"]) --> SP
    dbo_return_floor_date__sp(["dbo.return_floor_date_$sp"]) --> SP
    dbo_rtv(["dbo.rtv"]) --> SP
    dbo_transfer(["dbo.transfer"]) --> SP
    dbo_w(["dbo.w"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.d |
| dbo.i |
| dbo.ib_audit_trail |
| dbo.im_attribute |
| dbo.im_document_deleted |
| dbo.im_message |
| dbo.im_to_do_worklist |
| dbo.inv_move_req_from_loc |
| dbo.inv_move_request_detail |
| dbo.inventory_move_request |
| dbo.parameter_im |
| dbo.parameter_system |
| dbo.return_floor_date_$sp |
| dbo.rtv |
| dbo.transfer |
| dbo.w |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[delete_imrd_documents_$sp]
AS 

/* 
Proc name:  delete_rtv_documents_$sp
Desc: This procedure is called from delete_im_documents_$sp and it deletes Inventory Management Request documents based on parameters stored in table parameter_im.
	  The delete should also comply with some business rules listed below.
History: Creation March 03, 2011
*/
BEGIN
	DECLARE @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000), @cleanup_weeks SMALLINT, @floor_date SMALLDATETIME, @batch_size INT,
		@min_imrd_id DECIMAL(12,0), @max_imrd_id DECIMAL(12,0), @done BIT, @counter INT;
		
	-- Make sure this table doesn't exists at the beginning of the process
	IF object_id(N'tempdb..#temp_imrd') IS NOT NULL
		DROP TABLE #temp_imrd;
		
	SELECT @done = 0, @batch_size = 500000,
		@min_imrd_id = MIN(inventory_move_request_id),
		@max_imrd_id = MAX(inventory_move_request_id) 
	FROM inventory_move_request ;

	BEGIN TRY
	
		SELECT @cleanup_weeks = inventory_move_cleanup_weeks FROM parameter_im;
		
		EXEC return_floor_date_$sp @cleanup_weeks, @floor_date OUTPUT
		
		-- Batch the following inserts in case there are a large number  of documents to delete
		WHILE (@min_imrd_id < @max_imrd_id)
		BEGIN
				BEGIN TRAN
				
				-- Rule #: IMIMR156 - Delete all Cancelled IMRDs
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT inventory_move_request_id, document_no, 12, -- document_type for IMRD is 12
					document_status
				FROM inventory_move_request
				WHERE inventory_move_request_id BETWEEN @min_imrd_id AND @min_imrd_id + @batch_size
				AND document_status = 7;
				
				-- Rule #: IMIMR157 - Delete Submitted IMRDs if create date is at least x weeks ago, and IMRD is not referenced on an RTV
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT inventory_move_request_id, document_no, 12, document_status
				FROM inventory_move_request imr 
				WHERE inventory_move_request_id BETWEEN @min_imrd_id AND @min_imrd_id + @batch_size 
				AND document_status = 10
				AND create_date < @floor_date
				AND document_type = 1
				AND NOT EXISTS (SELECT 1 FROM rtv WHERE rtv.inventory_move_request_id = imr.inventory_move_request_id)
					
				-- Rule #: IMIMR157 - Delete Submitted IMRDs if create date is at least x weeks ago, and IMRD is not referenced on an Transfer		
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT inventory_move_request_id, document_no, 12, document_status
				FROM inventory_move_request imr 
				WHERE inventory_move_request_id BETWEEN @min_imrd_id AND @min_imrd_id + @batch_size 
				AND document_status = 10
				AND create_date < @floor_date
				AND document_type = 2
				AND NOT EXISTS (SELECT 1 FROM transfer t WHERE t.inventory_move_request_id = imr.inventory_move_request_id)
				
				COMMIT TRAN
				
				SET @min_imrd_id = @min_imrd_id + @batch_size;
		END;
		
		UPDATE STATISTICS im_document_deleted;
			
		SELECT @counter = COUNT(*), @done = 0, @max_imrd_id = 0 FROM im_document_deleted WHERE document_type = 12;
		
		IF (@counter > 10000)
		BEGIN
			WHILE (@done = 0)
			BEGIN
				-- We cannot do the delete in one big batch
				SELECT TOP 10000 im_document_id, im_document_no, document_type, document_status
				INTO #temp_imrd
				FROM im_document_deleted
				WHERE document_type = 12
				AND im_document_id > @max_imrd_id
				ORDER BY im_document_id;
				
				IF (@@ROWCOUNT > 0)	
					SELECT @max_imrd_id = MAX(im_document_id) FROM #temp_imrd;
				ELSE
					SET @done = 1;	
					
				IF (@done = 0)
				BEGIN
					BEGIN TRAN
					
					DELETE i
					FROM #temp_imrd t, im_attribute i
					WHERE t.im_document_id = i.parent_id 
					AND i.parent_type = 12;
					
					DELETE i
					FROM #temp_imrd t, im_message i
					WHERE t.im_document_id = i.parent_id 
					AND i.parent_type = 12
					
					-- delete from imweb im_to_do_worklist
					-- 1) check parameter installed_imweb_flag
					-- 2) if installed_imweb_flag, delete it from im_to_do_worklist
					IF ( (SELECT COUNT(*) FROM parameter_system WHERE installed_imweb_flag = 1) = 1)
					BEGIN
						DELETE w
						FROM #temp_imrd t, inventory_move_request imr, im_to_do_worklist w 
						WHERE t.im_document_id = imr.inventory_move_request_id
						AND imr.document_type = 1
						AND imr.inventory_move_request_id = w.document_id
						AND w.document_type = 30;
						
						DELETE w
						FROM #temp_imrd t, inventory_move_request imr, im_to_do_worklist w 
						WHERE t.im_document_id = imr.inventory_move_request_id
						AND imr.document_type = 2
						AND imr.inventory_move_request_id = w.document_id
						AND w.document_type = 31;
					END
	
					DELETE i
					FROM #temp_imrd t, inv_move_req_from_loc i
					WHERE t.im_document_id = i.inventory_move_request_id;
					
					DELETE d
					FROM #temp_imrd t, inv_move_request_detail d
					WHERE t.im_document_id = d.inventory_move_request_id 
					
					DELETE i
					FROM #temp_imrd t, inventory_move_request i
					WHERE t.im_document_id = i.inventory_move_request_id;
					
					-- Update Delete Log: ib audit trail				
					DELETE i
					FROM #temp_imrd t, ib_audit_trail i
					WHERE i.application = N'IM' 
					AND i.application_type = N'InventoryMovementRequest' 
					AND t.im_document_no = i.application_identifier;
					
					-- Now do an INSERT to keep trace of documents deleted
					INSERT INTO ib_audit_trail
						   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
						   application_level, application_key, action, field_affected, old_value, new_value, 
						   status, employee_last_name, employee_first_name)
					 SELECT GETDATE(), N'IM', N'Delete', NULL, N'InventoryMovementRequest', t.im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
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
					FROM #temp_imrd t;
					
					COMMIT TRAN;
				END;
				IF object_id(N'tempdb..#temp_imrd') IS NOT NULL
					DROP TABLE #temp_imrd;
			END;
		END;
		ELSE
		BEGIN				
			-- Just a small number of documents to delete: do it in one batch
			BEGIN TRAN
			
			DELETE i
			FROM im_document_deleted d, im_attribute i
			WHERE d.document_type = 12
			AND d.im_document_id = i.parent_id 
			AND i.parent_type = 12;
			
			DELETE i
			FROM im_document_deleted d, im_message i
			WHERE d.document_type = 12 
			AND d.im_document_id = i.parent_id 
			AND i.parent_type = 12
			
			-- delete from imweb im_to_do_worklist
			-- 1) check parameter installed_imweb_flag
			-- 2) if installed_imweb_flag, delete it from im_to_do_worklist
			IF ( (SELECT installed_imweb_flag FROM parameter_system) = 1)
			BEGIN
				DELETE w
				FROM im_document_deleted d, inventory_move_request imr, im_to_do_worklist w 
				WHERE d.document_type = 12  
				AND d.im_document_id = imr.inventory_move_request_id
				AND imr.document_type = 1
				AND imr.inventory_move_request_id = w.document_id
				AND w.document_type = 30;
				
				DELETE w
				FROM im_document_deleted d, inventory_move_request imr, im_to_do_worklist w 
				WHERE d.document_type = 12   
				AND d.im_document_id = imr.inventory_move_request_id
				AND imr.document_type = 2
				AND imr.inventory_move_request_id = w.document_id
				AND w.document_type = 31;
			END

			DELETE i
			FROM im_document_deleted d, inv_move_req_from_loc i
			WHERE d.document_type = 12  
			AND d.im_document_id = i.inventory_move_request_id;
			
			DELETE i
			FROM im_document_deleted d, inv_move_request_detail i
			WHERE d.document_type = 12 
			AND d.im_document_id = i.inventory_move_request_id;
			
			DELETE i
			FROM im_document_deleted d, inventory_move_request i
			WHERE d.document_type = 12  
			AND d.im_document_id = i.inventory_move_request_id;
			
			-- Update Delete Log: ib audit trail				
			DELETE i
			FROM im_document_deleted d, ib_audit_trail i
			WHERE d.document_type = 12   
			AND i.application = N'IM' 
			AND i.application_type = N'InventoryMovementRequest' 
			AND i.application_identifier = d.im_document_no;
			
			-- Now do an INSERT to keep trace of documents deleted
			INSERT INTO ib_audit_trail
				   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
				   application_level, application_key, action, field_affected, old_value, new_value, 
				   status, employee_last_name, employee_first_name)
			 SELECT GETDATE(), N'IM', N'Delete', NULL, N'InventoryMovementRequest', d.im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
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
			WHERE d.document_type = 12;
			
			COMMIT TRAN
		END;
	END TRY

	BEGIN CATCH
		SELECT @error_msg = ERROR_MESSAGE(),
		       @sql_err_num = ERROR_NUMBER();
		 
		IF @@TRANCOUNT <> 0
			ROLLBACK TRANSACTION
			
		SET @error_msg = N'Error in procedure delete_imrd_documents_$sp: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + N' ' + ERROR_MESSAGE()
		RAISERROR (@error_msg, -- Message text.
               16, -- Severity.
               1) -- State.
	END CATCH
END
```

