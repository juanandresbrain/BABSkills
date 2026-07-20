# dbo.utacalcgroupstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utacalcgroupstage"]
    dbo_utacalcgroupstage(["dbo.utacalcgroupstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utacalcgroupstage |

## View Code

```sql
; CREATE   VIEW [dbo].[utacalcgroupstage] AS SELECT [Calcgrp_ID], [Calcgrp_Name] COLLATE Latin1_General_CI_AS AS [Calcgrp_Name] FROM [dbo].[utacalcgroupstage]
```

