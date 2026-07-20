# dbo.utaworksummarystage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.utaworksummarystage"]
    dbo_utaworksummarystage(["dbo.utaworksummarystage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.utaworksummarystage |

## View Code

```sql
; CREATE   VIEW [dbo].[utaworksummarystage] AS SELECT [Wrks_ID], [Emp_ID], [Wrks_Work_Date], [Paygrp_ID] FROM [dbo].[utaworksummarystage]
```

