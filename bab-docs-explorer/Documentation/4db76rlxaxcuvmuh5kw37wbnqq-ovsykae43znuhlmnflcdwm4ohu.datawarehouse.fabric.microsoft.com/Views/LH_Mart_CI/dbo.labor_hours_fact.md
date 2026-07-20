# dbo.labor_hours_fact

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.labor_hours_fact"]
    dbo_labor_hours_fact(["dbo.labor_hours_fact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.labor_hours_fact |

## View Code

```sql
; CREATE   VIEW [dbo].[labor_hours_fact] AS     SELECT [recID], [store_key], [date_key], [emp_key], [job_key], [HOURTYPE_KEY], [timecode_key], [start_Time], [end_Time], [wrkd_minutes], [source_system], [INS_DT], [ETL_LOG_ID], [ETL_EVNT_ID], [UpdateDate], [wrkd_id]     FROM [dbo].[labor_hours_fact]
```

