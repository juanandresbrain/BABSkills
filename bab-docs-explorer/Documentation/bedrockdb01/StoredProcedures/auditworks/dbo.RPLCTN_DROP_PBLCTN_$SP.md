# dbo.RPLCTN_DROP_PBLCTN_$SP

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPLCTN_DROP_PBLCTN_$SP"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[RPLCTN_DROP_PBLCTN_$SP]
(
  @application_name varchar(100)
)
AS

DECLARE

  @rpl_user_pwd         sysname,  
  @publication_name     varchar(100),
  @subscriber_db_name   varchar(100),
  @subscriber_srvr_name varchar(100),
  @replication_user     varchar(100),
  @error_msg            varchar(1000),
  @exists               int
  
BEGIN
   
  /*
    Procedure : RPLCTN_DROP_PBLCTN_$SP
    Purpose   : Drops the current publication
    

    HISTORY:
    Date     Name         Def# Desc
    Dec04,14 Ian K       95105 Add ability to remove only single application when multiple replication
                               exists on the same server.    
    Jul14,14 Ian k             Initial Creation

  */
 
  SELECT @publication_name = @application_name + '_Publication';
    
  /* Drop specified publisher */
  BEGIN TRY
--    IF NOT EXISTS (select 1 from sys.databases
--                    where is_published = 1)
--     BEGIN
       
--       PRINT 'Stopping the publication on ' + @@servername;                      

         PRINT 'Removing the publication ' + @publication_name;                      
         PRINT '';
                
       EXEC sp_droppublication @publication = @publication_name
       
--     END
--    ELSE
--     PRINT 'Publications still exist on ' + @@servername + ' - Leaving publisher in place ';
    
  END TRY
  BEGIN CATCH
    SELECT @error_msg = 'Failed to drop publication  - ' + ERROR_MESSAGE();
    GOTO error_handler;
  END CATCH
  
  RETURN;
	
error_handler:

    IF @@TRANCOUNT > 0 
      ROLLBACK;
      
    RAISERROR (@error_msg, 16, 1); /* System Errors will be reported with SQL error code = 50000 */
      
END
```

