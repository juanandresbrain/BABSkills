# dbo.delete_inv_control_documents_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.delete_inv_control_documents_$sp"]
    dbo_count_import_log(["dbo.count_import_log"]) --> SP
    dbo_i(["dbo.i"]) --> SP
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> SP
    dbo_im_document_deleted(["dbo.im_document_deleted"]) --> SP
    dbo_im_message(["dbo.im_message"]) --> SP
    dbo_im_to_do_worklist(["dbo.im_to_do_worklist"]) --> SP
    dbo_inv_control_merch(["dbo.inv_control_merch"]) --> SP
    dbo_inventory_control(["dbo.inventory_control"]) --> SP
    dbo_inventory_control_loc(["dbo.inventory_control_loc"]) --> SP
    dbo_inventory_count_detail(["dbo.inventory_count_detail"]) --> SP
    dbo_l(["dbo.l"]) --> SP
    dbo_parameter_im(["dbo.parameter_im"]) --> SP
    dbo_parameter_system(["dbo.parameter_system"]) --> SP
    dbo_return_floor_date__sp(["dbo.return_floor_date_$sp"]) --> SP
    dbo_w(["dbo.w"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.count_import_log |
| dbo.i |
| dbo.ib_audit_trail |
| dbo.im_document_deleted |
| dbo.im_message |
| dbo.im_to_do_worklist |
| dbo.inv_control_merch |
| dbo.inventory_control |
| dbo.inventory_control_loc |
| dbo.inventory_count_detail |
| dbo.l |
| dbo.parameter_im |
| dbo.parameter_system |
| dbo.return_floor_date_$sp |
| dbo.w |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[delete_inv_control_documents_$sp]
AS 

/* 
Proc name:  delete_inv_control_documents_$sp
Desc: This procedure is called from delete_im_documents_$sp and it deletes Stock Status Adjustment documents based on parameters stored in table parameter_im.
	  The delete should also comply with some business rules listed below.
History: Creation March 11, 2011
*/
BEGIN
	DECLARE @sql_err_num DECIMAL(38,0), @error_msg NVARCHAR(2000), @cleanup_weeks SMALLINT, @floor_date SMALLDATETIME, @batch_size INT,
		@min_inv_control_id DECIMAL(12,0), @max_inv_control_id DECIMAL(12,0), @done BIT, @counter INT;
		
	-- Make sure this table doesn't exists at the beginning of the process
	IF object_id(N'tempdb..#temp_inv_control') IS NOT NULL
		DROP TABLE #temp_inv_control;
		
	SELECT @done = 0, @batch_size = 500000,
		@min_inv_control_id = MIN(inventory_control_id),
		@max_inv_control_id = MAX(inventory_control_id) 
	FROM inventory_control;

	BEGIN TRY
	
		SELECT @cleanup_weeks = inventory_count_cleanup_weeks FROM parameter_im;
		
		EXEC return_floor_date_$sp @cleanup_weeks, @floor_date OUTPUT
		
		-- Batch the following inserts in case there are a large number  of documents to delete
		WHILE (@min_inv_control_id < @max_inv_control_id)
		BEGIN
				BEGIN TRAN
				
				-- Delete all Cancelled Inventory Control Documents
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT inventory_control_id, document_no, 19, -- document_type for Stock Status Adjustment is 19
					document_status
				FROM inventory_control 
				WHERE inventory_control_id BETWEEN @min_inv_control_id AND @min_inv_control_id + @batch_size
				AND document_status = 7;
				
				-- Delete all Inventory Control documents with a status of Posted and (max) Posted date at least x weeks ago
				INSERT INTO im_document_deleted
					(im_document_id, im_document_no, document_type, document_status)
				SELECT DISTINCT ic.inventory_control_id, ic.document_no, 19, ic.document_status
				FROM inventory_control ic, inventory_control_loc icl 
				WHERE ic.inventory_control_id BETWEEN @min_inv_control_id AND @min_inv_control_id + @batch_size
				AND ic.inventory_control_id = icl.inventory_control_id
				AND document_status = 15
				GROUP BY ic.inventory_control_id, ic.document_no, ic.document_status
				HAVING MAX(icl.posted_date) < @floor_date;
					
				COMMIT TRAN
				
				SET @min_inv_control_id = @min_inv_control_id + @batch_size;
		END;
		
		UPDATE STATISTICS im_document_deleted;
			
		SELECT @counter = COUNT(*), @done = 0, @max_inv_control_id = 0 FROM im_document_deleted WHERE document_type = 19;
		
		IF (@counter > 10000)
		BEGIN
			WHILE (@done = 0)
			BEGIN
				-- We cannot do the delete in one big batch
				SELECT TOP 10000 im_document_id, im_document_no, document_type, document_status
				INTO #temp_inv_control
				FROM im_document_deleted
				WHERE document_type = 19
				AND im_document_id > @max_inv_control_id
				ORDER BY im_document_id;
				
				IF (@@ROWCOUNT > 0)	
					SELECT @max_inv_control_id = MAX(im_document_id) FROM #temp_inv_control;
				ELSE
					SET @done = 1;	
					
				IF (@done = 0)
				BEGIN
					BEGIN TRAN
					
					DELETE i
					FROM #temp_inv_control t, im_message i
					WHERE t.im_document_id = i.parent_id 
					AND i.parent_type = 19;
					
					DELETE l
					FROM #temp_inv_control t, count_import_log l
					WHERE t.im_document_id = l.inventory_control_id;
					
					DELETE i
					FROM #temp_inv_control t, inventory_control_loc i
					WHERE t.im_document_id = i.inventory_control_id;
					
					DELETE i
					FROM #temp_inv_control t, inv_control_merch i
					WHERE t.im_document_id = i.inventory_control_id;
					
					DELETE i
					FROM #temp_inv_control t, inventory_count_detail i
					WHERE t.im_document_id = i.inventory_control_id;
					
					DELETE i
					FROM #temp_inv_control t, inventory_control i
					WHERE t.im_document_id = i.inventory_control_id;
					
					
					IF ( (SELECT COUNT(*) FROM parameter_system WHERE installed_imweb_flag = 1) = 1)
					BEGIN
						--Feng: delete from imweb im_to_do_worklist
						-- 1) check parameter installed_imweb_flag
						-- 2) if installed_imweb_flag, delete it from im_to_do_worklist		
						DELETE w
						FROM #temp_inv_control t, im_to_do_worklist w 
						WHERE t.im_document_id = w.document_id
						AND w.document_type = 19;
					END
					 		
					-- Update Delete Log: ib audit trail				
					DELETE i
					FROM #temp_inv_control t, ib_audit_trail i
					WHERE i.application = N'IM' 
					AND i.application_type = N'InventoryControl' 
					AND t.im_document_no = i.application_identifier;
					
					-- Now do an INSERT to keep trace of documents deleted
					INSERT INTO ib_audit_trail
						   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
						   application_level, application_key, action, field_affected, old_value, new_value, 
						   status, employee_last_name, employee_first_name)
					 SELECT GETDATE(), N'IM', N'Delete', NULL, N'InventoryControl', t.im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
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
					FROM #temp_inv_control t;
					
					COMMIT TRAN;
				END;
				IF object_id(N'tempdb..#temp_inv_control') IS NOT NULL
					DROP TABLE #temp_inv_control;
			END;
		END;
		ELSE
		BEGIN				
			-- Just a small number of documents to delete: do it in one batch
			BEGIN TRAN
			
			DELETE i
			FROM im_document_deleted d, im_message i
			WHERE d.document_type = 19
			AND d.im_document_id = i.parent_id 
			AND i.parent_type = 19;
			
			DELETE l
			FROM im_document_deleted d, count_import_log l
			WHERE d.document_type = 19 
			AND d.im_document_id = l.inventory_control_id;
			
			DELETE i
			FROM im_document_deleted d, inventory_control_loc i
			WHERE d.document_type = 19
			AND d.im_document_id = i.inventory_control_id;
			
			DELETE i
			FROM im_document_deleted d, inv_control_merch i
			WHERE d.document_type = 19 
			AND d.im_document_id = i.inventory_control_id;
			
			DELETE i
			FROM im_document_deleted d, inventory_count_detail i
			WHERE d.document_type = 19  
			AND d.im_document_id = i.inventory_control_id;
			
			DELETE i
			FROM im_document_deleted d, inventory_control i
			WHERE d.document_type = 19  
			AND d.im_document_id = i.inventory_control_id;
			
			IF ( (SELECT COUNT(*) FROM parameter_system WHERE installed_imweb_flag = 1) = 1)
			BEGIN
				--Feng: delete from imweb im_to_do_worklist
				-- 1) check parameter installed_imweb_flag
				-- 2) if installed_imweb_flag, delete it from im_to_do_worklist		
				DELETE w
				FROM im_document_deleted d, im_to_do_worklist w 
				WHERE d.document_type = 19   
				AND d.im_document_id = w.document_id
				AND w.document_type = 19;
			END
			 		
			-- Update Delete Log: ib audit trail				
			DELETE i
			FROM im_document_deleted d, ib_audit_trail i
			WHERE d.document_type = 19
			AND i.application = N'IM' 
			AND i.application_type = N'InventoryControl' 
			AND d.im_document_no = i.application_identifier;
			
			-- Now do an INSERT to keep trace of documents deleted
			INSERT INTO ib_audit_trail
				   (entry_date, application, activity, application_type_id, application_type, application_identifier, 
				   application_level, application_key, action, field_affected, old_value, new_value, 
				   status, employee_last_name, employee_first_name)
			 SELECT GETDATE(), N'IM', N'Delete', NULL, N'InventoryControl', im_document_no, NULL, NULL ,N'Delete', NULL, NULL, NULL, 
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
			WHERE document_type = 19
			
			COMMIT TRAN
		END;
	END TRY

	BEGIN CATCH
		SELECT @error_msg = ERROR_MESSAGE(),
		       @sql_err_num = ERROR_NUMBER();
		 
		IF @@TRANCOUNT <> 0
			ROLLBACK TRANSACTION
			
		SET @error_msg = N'Error in procedure delete_inv_control_documents_$sp: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + N' ' + ERROR_MESSAGE()
		RAISERROR (@error_msg, -- Message text.
               16, -- Severity.
               1) -- State.
	END CATCH
END
```

