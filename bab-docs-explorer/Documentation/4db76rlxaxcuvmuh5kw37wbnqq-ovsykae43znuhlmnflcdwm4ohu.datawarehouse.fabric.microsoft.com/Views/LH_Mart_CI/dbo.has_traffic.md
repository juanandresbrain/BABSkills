# dbo.has_traffic

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.has_traffic"]
    dbo_has_traffic(["dbo.has_traffic"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.has_traffic |

## View Code

```sql
; CREATE   VIEW [dbo].[has_traffic] AS     SELECT [store_key], [date_key], [Hastraffic]     FROM [dbo].[has_traffic]
```

