# dbo.actualvearnedpayrolllaborgrid

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.actualvearnedpayrolllaborgrid"]
    dbo_actualvearnedpayrolllaborgrid(["dbo.actualvearnedpayrolllaborgrid"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.actualvearnedpayrolllaborgrid |

## View Code

```sql
; CREATE   VIEW [dbo].[actualvearnedpayrolllaborgrid] AS     SELECT [USSales], [CNSales], [HOURS]     FROM [dbo].[actualvearnedpayrolllaborgrid]
```

