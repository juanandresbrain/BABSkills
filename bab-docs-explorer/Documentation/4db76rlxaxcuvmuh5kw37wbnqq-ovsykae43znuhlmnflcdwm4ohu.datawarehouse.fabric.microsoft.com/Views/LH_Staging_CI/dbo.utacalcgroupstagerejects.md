# dbo.utacalcgroupstagerejects

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utacalcgroupstagerejects"]
    dbo_utacalcgroupstagerejects(["dbo.utacalcgroupstagerejects"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utacalcgroupstagerejects |

## View Code

```sql
; CREATE   VIEW [dbo].[utacalcgroupstagerejects] AS SELECT [Calcgrp_ID] COLLATE Latin1_General_CI_AS AS [Calcgrp_ID], [Calcgrp_Name] COLLATE Latin1_General_CI_AS AS [Calcgrp_Name], [ErrorCode], [ErrorColumn], [RejectDate] FROM [dbo].[utacalcgroupstagerejects]
```

