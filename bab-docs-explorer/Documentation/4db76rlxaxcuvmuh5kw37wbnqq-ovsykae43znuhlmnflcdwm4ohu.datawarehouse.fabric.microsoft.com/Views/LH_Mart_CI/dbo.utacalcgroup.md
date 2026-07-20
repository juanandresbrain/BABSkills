# dbo.utacalcgroup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utacalcgroup"]
    dbo_utacalcgroup(["dbo.utacalcgroup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utacalcgroup |

## View Code

```sql
; CREATE   VIEW [dbo].[utacalcgroup] AS     SELECT [Calcgrp_ID], [Calcgrp_Name] COLLATE Latin1_General_CI_AS AS [Calcgrp_Name], [InsertDate], [UpdateDate]     FROM [dbo].[utacalcgroup]
```

