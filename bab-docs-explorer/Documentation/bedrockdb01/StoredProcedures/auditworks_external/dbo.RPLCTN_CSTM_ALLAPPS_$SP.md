# dbo.RPLCTN_CSTM_ALLAPPS_$SP

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPLCTN_CSTM_ALLAPPS_$SP"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROC [dbo].[RPLCTN_CSTM_ALLAPPS_$SP]
AS
DECLARE

  /* Proc Name: RPLCTN_CSTM_ALLAPPS_$SP
     Desc: Called remotely by replication installation
     
           Finds any stored procs named by the following mask and executes then
           1 by 1
           
           MASK  =  ‘RPLCTN!_CSTM!_%!_$SP’ 
           
           **** NOTE - DO NOT MODIFY THIS CODE ****
  
     HISTORY:

     Date     Name		Def#     Desc
     Aug21,14 Ian K               Initial Creation
                                     
  
 */
 
  @error_msg         nvarchar(1000),
  @sql               nvarchar(100),
  @proc_name         nvarchar(100),
  @cursor_open          int 
      
BEGIN
 
  DECLARE find_custom_procs CURSOR FAST_FORWARD FOR
    SELECT name 
      FROM sys.procedures 
     WHERE name LIKE 'RPLCTN!_CSTM!_%!_$SP' ESCAPE '!'
       AND name <> 'RPLCTN_CSTM_ALLAPPS_$SP';

  /* Loop through all local custom procs */
  
  BEGIN TRY
       
    OPEN find_custom_procs;
  
  END TRY
  BEGIN CATCH
    SELECT @error_msg = 'Failed to open custom proc cursor - ' + ERROR_MESSAGE();
    GOTO error_handler;
  END CATCH
  
  SELECT @cursor_open = 1;
  
  BEGIN TRY
        
    FETCH NEXT FROM find_custom_procs
     INTO @proc_name;
    
  END TRY
  BEGIN CATCH
    SELECT @error_msg = 'Failed to fetch next customer proc record - ' + ERROR_MESSAGE();
    GOTO error_handler;
  END CATCH
                            
  WHILE @@FETCH_STATUS = 0
  BEGIN      
  
    BEGIN TRY
    
      SELECT @sql = 'EXEC ' + @proc_name;
                                  
      EXEC sp_executesql @sql;
      
    END TRY
    BEGIN CATCH
      SELECT @error_msg = 'Failed to execute remote store procedure - ' + ERROR_MESSAGE();
      GOTO error_handler;
    END CATCH

    BEGIN TRY
        
      FETCH NEXT FROM find_custom_procs
       INTO @proc_name;
    
    END TRY
    BEGIN CATCH
      SELECT @error_msg = 'Failed to fetch next customer proc record - ' + ERROR_MESSAGE();
      GOTO error_handler;
    END CATCH
      
  END

  CLOSE find_custom_procs;
  DEALLOCATE find_custom_procs;

  SELECT @cursor_open = 0;
    
  RETURN;
	
error_handler:

    IF @cursor_open = 1
    BEGIN
      CLOSE find_custom_procs;
      DEALLOCATE find_custom_procs;    
    END

    IF @@TRANCOUNT > 0 
      ROLLBACK;
        
    RAISERROR (@error_msg, 16, 1); /* System Errors will be reported with SQL error code = 50000 */

END
```

