# dbo.startup_discrepancy_ib_cfd_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.startup_discrepancy_ib_cfd_$sp"]
    dbo_ib_cost_factor_discount(["dbo.ib_cost_factor_discount"]) --> SP
    dbo_parameter_system(["dbo.parameter_system"]) --> SP
    dbo_startup_mc_discr_log(["dbo.startup_mc_discr_log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_cost_factor_discount |
| dbo.parameter_system |
| dbo.startup_mc_discr_log |

## Stored Procedure Code

```sql
-- Copy of original added to R2 build 18 after build was released

CREATE PROCEDURE [dbo].[startup_discrepancy_ib_cfd_$sp] AS

SET NOCOUNT ON

BEGIN
	DECLARE @sku_id_completed DECIMAL(13,0), @current_sku_id DECIMAL(13,0), @discrepancy INT, @multi_jurisdiction_flag BIT, @crs_sku_flag BIT,
		@error_msg NVARCHAR(4000), @crs_sku_key_flag bit, @current_location_id SMALLINT, @current_cost_factor_disc_id SMALLINT, 
		@local_cost DECIMAL(14,2), @number_of_rows TINYINT, @crs_sku_cost_flag BIT, @current_ext_cost_local DECIMAL(14,2),
		@cost_factor_disc_id DECIMAL(12,0)

	-- Processing 
	BEGIN TRY
		SELECT @multi_jurisdiction_flag = multi_sales_jurisdiction_flag FROM parameter_system
		
		-- there is no point going further because transaction cost = transaction_cost_local
		IF @multi_jurisdiction_flag = 0 
			RETURN 

		SELECT @sku_id_completed = MAX(sku_id)
		FROM startup_mc_discr_log
		WHERE proc_name = N'startup_discrepancy_ib_cfd_$sp'
		AND completed_flag = 1

	   IF @sku_id_completed IS NULL
		  SET @sku_id_completed = 0
		
		-- Process by sku
		DECLARE crs_sku CURSOR FOR
		SELECT DISTINCT sku_id
	  	FROM ib_cost_factor_discount
		WHERE sku_id > @sku_id_completed
	  	ORDER BY sku_id

	  	OPEN crs_sku
		SET @crs_sku_flag = 1

		FETCH NEXT FROM crs_sku INTO @current_sku_id

		WHILE @@FETCH_STATUS = 0
		BEGIN
			-- For the current sku get the group key to update
			DECLARE crs_sku_key CURSOR FOR
			SELECT location_id, cost_factor_discount_id, SUM(extended_cost_local) local_cost
			FROM ib_cost_factor_discount
			WHERE sku_id = @current_sku_id
			GROUP BY location_id, cost_factor_discount_id
			HAVING SUM(extended_cost) = 0 AND SUM(extended_cost_local) <> 0
			ORDER BY location_id, cost_factor_discount_id
			
			OPEN crs_sku_key
			SET @crs_sku_key_flag = 1
			
			FETCH NEXT FROM crs_sku_key INTO @current_location_id, @current_cost_factor_disc_id, @local_cost

			WHILE @@FETCH_STATUS = 0
			BEGIN
				-- For each row here where local_cost is <> 0, I need to adjust some or all the rows that belong to this group 
				-- by pro-rating the discrepancy until the total of extended_cost_local equals extended_cost = 0.
				
				-- Get the rows from ib_cost_factor_discount that will be affected by pro-rating the current discrepancy 
				-- Open a third cursor: loop through the row(s) until the discrepancy stored in @local_cost reached 0.
				SET @number_of_rows = ABS(@local_cost * 100)
				
				DECLARE crs_sku_cost CURSOR FOR
				SELECT TOP(@number_of_rows) ib_cost_factor_discount_id, extended_cost_local
				FROM ib_cost_factor_discount
				WHERE sku_id = @current_sku_id
				AND location_id = @current_location_id
				AND cost_factor_discount_id = @current_cost_factor_disc_id
				ORDER BY extended_cost_local 

				BEGIN TRANSACTION
				
				WHILE (@local_cost <> 0)
				BEGIN
					OPEN crs_sku_cost
					SET @crs_sku_cost_flag = 1
					
					FETCH NEXT FROM crs_sku_cost INTO @cost_factor_disc_id, @current_ext_cost_local

					WHILE @@FETCH_STATUS = 0
					BEGIN
						IF @local_cost > 0
						BEGIN
							-- We need to reduce the row of 0.01 until there is no discrepancy
							UPDATE ib_cost_factor_discount
							SET extended_cost_local = extended_cost_local - 0.01
							WHERE ib_cost_factor_discount_id = @cost_factor_disc_id
							
							SET @local_cost = @local_cost - 0.01

						END
						ELSE 
						BEGIN
							-- We need to add each row of 0.01 until there is no discrepancy
							UPDATE ib_cost_factor_discount
							SET extended_cost_local = extended_cost_local + 0.01
							WHERE ib_cost_factor_discount_id = @cost_factor_disc_id
							
							SET @local_cost = @local_cost + 0.01
							
						END
						IF (@local_cost = 0)
							BREAK
						ELSE
							FETCH NEXT FROM crs_sku_cost INTO @cost_factor_disc_id, @current_ext_cost_local
					END
					CLOSE crs_sku_cost
					SET @crs_sku_cost_flag = 0
				END
				
				IF @crs_sku_cost_flag = 1
					CLOSE crs_sku_cost
					
				DEALLOCATE crs_sku_cost
				SET @crs_sku_cost_flag = 0
				
				-- INSERT a row in the log because we'll pick up the next sku to adjust
				INSERT INTO startup_mc_discr_log
					(proc_name, sku_id, location_id, third_key_id, end_time, completed_flag)
				VALUES (N'startup_discrepancy_ib_cfd_$sp', @current_sku_id, @current_location_id, @current_cost_factor_disc_id, GETDATE(), 1)
			
				COMMIT TRANSACTION			
				
				FETCH NEXT FROM crs_sku_key INTO @current_location_id, @current_cost_factor_disc_id, @local_cost
			END
			
			CLOSE crs_sku_key
			DEALLOCATE crs_sku_key
			SET @crs_sku_key_flag = 0
			
			FETCH NEXT FROM crs_sku INTO @current_sku_id
		END
      
      CLOSE crs_sku
	  DEALLOCATE crs_sku
	  SET @crs_sku_flag = 0

	END TRY
	BEGIN CATCH
	
	IF @@TRANCOUNT <> 0
		ROLLBACK TRANSACTION
		
	IF (@crs_sku_cost_flag = 1)
    BEGIN
		CLOSE crs_sku_cost
		DEALLOCATE crs_sku_cost
    END
    
	IF (@crs_sku_key_flag = 1)
    BEGIN
		CLOSE crs_sku_key
		DEALLOCATE crs_sku_key
    END
    
    IF (@crs_sku_flag = 1)
    BEGIN
		CLOSE crs_sku
		DEALLOCATE crs_sku
    END
   
	SET @error_msg = N'Error in procedure startup_discrepancy_ib_cfd_$sp: ' + CAST(ERROR_NUMBER() AS NVARCHAR) + N' ' + ERROR_MESSAGE()
	RAISERROR (@error_msg, -- Message text.
           16, -- Severity.
           1) -- State.

	END CATCH
END
```

