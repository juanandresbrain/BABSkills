# dbo.spStopJob_StoreSalesCheck

**Database:** DBAUtility  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spStopJob_StoreSalesCheck"]
    dbo_sp_stop_job(["dbo.sp_stop_job"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_stop_job |

## Stored Procedure Code

```sql
CREATE PROC [dbo].[spStopJob_StoreSalesCheck] --WITH EXECUTE AS 'pm_repo'  as  EXEC msdb.[dbo].[sp_stop_job] @job_name =  'StoreSalesCheck'
```

