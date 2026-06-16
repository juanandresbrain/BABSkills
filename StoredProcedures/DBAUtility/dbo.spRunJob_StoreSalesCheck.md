# dbo.spRunJob_StoreSalesCheck

**Database:** DBAUtility  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRunJob_StoreSalesCheck"]
    dbo_sp_start_job(["dbo.sp_start_job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_start_job |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spRunJob_StoreSalesCheck] --WITH EXECUTE AS 'pm_repo' AS  EXEC msdb.dbo.sp_start_job 'StoreSalesCheck'
```

