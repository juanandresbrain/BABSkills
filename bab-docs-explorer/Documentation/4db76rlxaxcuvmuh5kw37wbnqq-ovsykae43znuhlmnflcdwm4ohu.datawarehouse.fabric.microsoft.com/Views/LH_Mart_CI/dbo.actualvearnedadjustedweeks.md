# dbo.actualvearnedadjustedweeks

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.actualvearnedadjustedweeks"]
    dbo_actualvearnedadjustedweeks(["dbo.actualvearnedadjustedweeks"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.actualvearnedadjustedweeks |

## View Code

```sql
CREATE   VIEW [dbo].[actualvearnedadjustedweeks] AS     SELECT [store] COLLATE Latin1_General_CI_AS AS [store], [year], [week], [startDate], [dpc], [law], [hoo], [eqv], [spp], [msc], [ffh], [wbt_id]     FROM [dbo].[actualvearnedadjustedweeks]
```

