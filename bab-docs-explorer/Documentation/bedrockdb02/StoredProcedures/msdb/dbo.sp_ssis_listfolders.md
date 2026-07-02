# dbo.sp_ssis_listfolders

**Database:** msdb  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_ssis_listfolders"]
    dbo_sysssispackagefolders(["dbo.sysssispackagefolders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sysssispackagefolders |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[sp_ssis_listfolders]
  @parentfolderid uniqueidentifier = NULL
AS
  SELECT
   folderid,
   parentfolderid,
   foldername
  FROM
      sysssispackagefolders
  WHERE
      [parentfolderid] = @parentfolderid OR 
      (@parentfolderid IS NULL AND [parentfolderid] IS NULL)
  ORDER BY 
      foldername
```

