# dbo.serializedvouchercounts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.serializedvouchercounts"]
    dbo_serializedvouchercounts(["dbo.serializedvouchercounts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.serializedvouchercounts |

## View Code

```sql
; CREATE   VIEW [dbo].[serializedvouchercounts] AS     SELECT [processDate], [vouchersSent], [vouchersProcessed], [vouchersSentXML]     FROM [dbo].[serializedvouchercounts]
```

