# dbo.giftcard_currency_code

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_currency_code"]
    dbo_giftcard_currency_code(["dbo.giftcard_currency_code"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_currency_code |

## View Code

```sql
; CREATE   VIEW giftcard_currency_code AS SELECT * FROM LH_Mart.dbo.giftcard_currency_code;
```

