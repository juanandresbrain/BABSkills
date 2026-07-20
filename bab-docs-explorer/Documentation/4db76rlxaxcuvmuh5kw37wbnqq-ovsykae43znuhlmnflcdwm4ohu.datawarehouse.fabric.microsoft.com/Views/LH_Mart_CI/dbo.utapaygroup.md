# dbo.utapaygroup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utapaygroup"]
    dbo_utapaygroup(["dbo.utapaygroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utapaygroup |

## View Code

```sql
; CREATE   VIEW [dbo].[utapaygroup] AS     SELECT [PayGrp_ID], [PayGrp_Name] COLLATE Latin1_General_CI_AS AS [PayGrp_Name], [InsertDate], [UpdateDate]     FROM [dbo].[utapaygroup]
```

