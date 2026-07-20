# dbo.cmn_product_xref

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.cmn_product_xref"]
    dbo_cmn_product_xref(["dbo.cmn_product_xref"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cmn_product_xref |

## View Code

```sql
; CREATE   VIEW [dbo].[cmn_product_xref] AS     SELECT [product_key], [cmn_style_code] COLLATE Latin1_General_CI_AS AS [cmn_style_code]     FROM [dbo].[cmn_product_xref]
```

