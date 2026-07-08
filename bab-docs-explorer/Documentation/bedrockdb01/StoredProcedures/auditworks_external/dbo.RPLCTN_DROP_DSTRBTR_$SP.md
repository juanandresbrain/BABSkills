# dbo.RPLCTN_DROP_DSTRBTR_$SP

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.RPLCTN_DROP_DSTRBTR_$SP"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[RPLCTN_DROP_DSTRBTR_$SP]
(
  @application_name varchar(100)
)
AS

DECLARE
 
  @database_name        varchar(100),
  @error_msg            varchar(1000),
  @distributor_name     varchar(100),
  @main_distributor     varchar(100),
  @SQLString            nvarchar(500),
  @ParmDefinition       nvarchar(500),  
  @exists               int
  
BEGIN
   
  /*
    Procedure : RPLCTN_DROP_DSTRBTR_$SP
    Purpose   : Un-installs the server from replication
    

    HISTORY:
    Date     Name         Def# Desc
    Dec04,14 Ian K       95105 Add ability to remove only single application when multiple replication
                               exists on the same server.
    Jul14,14 Ian K             Initial Creation

  */
  
  /* Set up variables */
  
  SELECT @database_name = db_name();
  
  SELECT @distributor_name = @application_name + '_Distributor'    

  /* Switch off replication */
  
  PRINT 'Turning off publication for database ' + @database_name;
  PRINT '';

  BEGIN TRY
  
    EXEC sp_replicationdboption @dbname  = @database_name, 
                                @optname = N'publish', 
                                @value   = N'false';
  END TRY
  BEGIN CATCH
    SELECT @error_msg = 'Failed to turn off publication  - ' + ERROR_MESSAGE();
    GOTO error_handler;
  END CATCH

  BEGIN TRY
  
    SELECT TOP 1 @main_distributor = name
      FROM sys.databases
     WHERE is_distributor <> 0
     ORDER BY create_date;

  END TRY
  BEGIN CATCH
    SELECT @error_msg = 'Failed to get main distribution database name  - ' + ERROR_MESSAGE();
    GOTO error_handler;
  END CATCH
	     
  /* Check to see if the current distribution DB has any publications - if no remove it */

  IF @main_distributor <> @distributor_name
  BEGIN
  
    BEGIN TRY
			                
      SET @SQLString = N'SELECT @result = count(*) FROM [' + @distributor_name + '].dbo.MSpublications'
              
      SET @ParmDefinition = N'@result int OUTPUT';

      EXECUTE sp_executesql @SQLString, @ParmDefinition, @result=@exists OUTPUT;
      
      IF @exists = 0
      BEGIN
    
        PRINT 'Dropping the distribution database ' + @distributor_name;  
        PRINT '';
      
        EXEC sp_dropdistributiondb @database = @distributor_name;           
    
      END       

    END TRY
    BEGIN CATCH
      SELECT @error_msg = 'Failed to test for publications in distributor  - ' + ERROR_MESSAGE();
      GOTO error_handler;
    END CATCH
  
  END
                        
  /* Finally stop the server from being a distributor if no publications exist*/

  BEGIN TRY

    /* Check to see if the main distribution DB has any publications - if no remove it */
			                
    SET @SQLString = N'SELECT @result = count(*) FROM [' + @main_distributor + '].dbo.MSpublications'
              
    SET @ParmDefinition = N'@result int OUTPUT';

    EXECUTE sp_executesql @SQLString, @ParmDefinition, @result=@exists OUTPUT;
       
  END TRY
  BEGIN CATCH
    SELECT @error_msg = 'Failed to test for publications in main distributor  - ' + ERROR_MESSAGE();
    GOTO error_handler;
  END CATCH  
  
  IF @exists = 0
  BEGIN
   
    /* Drop publisher */

    PRINT 'Dropping the publisher on ' + @@servername;  
    PRINT '';
       
    BEGIN TRY
  
       EXEC sp_dropdistpublisher @publisher = @@servername;
    
    END TRY
    BEGIN CATCH
      SELECT @error_msg = 'Failed to drop publisher  - ' + ERROR_MESSAGE();
      GOTO error_handler;
    END CATCH 
    
    PRINT 'Dropping the main distribution database ' + @main_distributor;  
    PRINT '';
 
    BEGIN TRY
          
      EXEC sp_dropdistributiondb @database = @main_distributor;

    END TRY
    BEGIN CATCH
      SELECT @error_msg = 'Failed to drop distribution db  - ' + ERROR_MESSAGE();
      GOTO error_handler;
    END CATCH       
       
    PRINT 'Stopping the distributor on ' + @@servername;                      
    PRINT '';

    BEGIN TRY
                    
      EXEC sp_dropdistributor;
  
    END TRY
    BEGIN CATCH
      SELECT @error_msg = 'Failed to stop distribution  - ' + ERROR_MESSAGE();
      GOTO error_handler;
    END CATCH            
    
   END
    
  ELSE
     
   BEGIN
      PRINT 'Publications still exist on ' + @@servername + ' - Leaving distributor in place ';
      PRINT '';
   END

  RETURN;
	
error_handler:

    IF @@TRANCOUNT > 0 
      ROLLBACK;
      
    RAISERROR (@error_msg, 16, 1); /* System Errors will be reported with SQL error code = 50000 */

END
```

