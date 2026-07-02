# dbo.sp_ssis_startup

**Database:** master  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_startup"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_startup]
    AS
    SET NOCOUNT ON
        /* Currently, the IS Store name is 'SSISDB' */
        IF DB_ID('SSISDB') IS NULL
            RETURN
        
        IF NOT EXISTS(SELECT name FROM [SSISDB].sys.procedures WHERE name=N'startup')
            RETURN
         
        /*Invoke the procedure in SSISDB  */
		/* Use dynamic sql to handle AlwaysOn non-readable mode*/
        DECLARE @script nvarchar(500)
		SET @script = N'EXEC [SSISDB].[catalog].[startup]'
        EXECUTE sp_executesql @script
```

