# dbo.cmn_product_style_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.cmn_product_style_dim"]
    dbo_cmn_product_style_dim(["dbo.cmn_product_style_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cmn_product_style_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[cmn_product_style_dim] AS     SELECT [cmn_style_code] COLLATE Latin1_General_CI_AS AS [cmn_style_code], [description] COLLATE Latin1_General_CI_AS AS [description], [cmn_subclass_code] COLLATE Latin1_General_CI_AS AS [cmn_subclass_code]     FROM [dbo].[cmn_product_style_dim]
```

