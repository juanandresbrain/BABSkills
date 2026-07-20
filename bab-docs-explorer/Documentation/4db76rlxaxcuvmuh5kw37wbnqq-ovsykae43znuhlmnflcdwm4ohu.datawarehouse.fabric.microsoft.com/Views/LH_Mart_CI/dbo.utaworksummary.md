# dbo.utaworksummary

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworksummary"]
    dbo_utaworksummary(["dbo.utaworksummary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworksummary |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworksummary] AS     SELECT [Wrks_ID], [Emp_ID], [Wrks_Work_Date], [Paygrp_ID], [InsertDate], [UpdateDate]     FROM [dbo].[utaworksummary]
```

