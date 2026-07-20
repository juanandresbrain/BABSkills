# dbo.tender_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tender_dim"]
    dbo_tender_dim(["dbo.tender_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tender_dim |

## View Code

```sql
; CREATE  VIEW [dbo].[tender_dim] AS      SELECT [tender_key]       ,[tender_code]   COLLATE Latin1_General_CI_AS AS [tender_code]       ,[tender_desc] COLLATE Latin1_General_CI_AS AS [tender_desc]       ,[process_name] COLLATE Latin1_General_CI_AS AS [process_name]       ,[process_date]       ,[INS_DT]       ,[UPDT_DT]       ,[ETL_LOG_ID]       ,[ETL_EVNT_ID]        FROM LH_Mart.[dbo].[tender_dim]
```

