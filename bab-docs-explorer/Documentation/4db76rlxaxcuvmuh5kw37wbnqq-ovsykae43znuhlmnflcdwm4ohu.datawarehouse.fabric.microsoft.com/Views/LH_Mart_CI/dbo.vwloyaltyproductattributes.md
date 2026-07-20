# dbo.vwloyaltyproductattributes

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwloyaltyproductattributes"]
    dbo_vwloyaltyproductattributes(["dbo.vwloyaltyproductattributes"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwloyaltyproductattributes |

## View Code

```sql
; CREATE   VIEW vwloyaltyproductattributes AS SELECT * FROM LH_Mart.dbo.vwloyaltyproductattributes;
```

