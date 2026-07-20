# dbo.bear_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.bear_dim"]
    dbo_bear_dim(["dbo.bear_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.bear_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[bear_dim] AS     SELECT [BearKey], [BearID] COLLATE Latin1_General_CI_AS AS [BearID], [store_key], [date_key], [Product_Key], [tdf_key], [TKF_ID]     FROM [dbo].[bear_dim]
```

