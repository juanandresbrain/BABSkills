# dbo.country_currency_xref

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.country_currency_xref"]
    dbo_country_currency_xref(["dbo.country_currency_xref"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.country_currency_xref |

## View Code

```sql
; CREATE   VIEW country_currency_xref AS SELECT * FROM LH_Mart.dbo.country_currency_xref;
```

