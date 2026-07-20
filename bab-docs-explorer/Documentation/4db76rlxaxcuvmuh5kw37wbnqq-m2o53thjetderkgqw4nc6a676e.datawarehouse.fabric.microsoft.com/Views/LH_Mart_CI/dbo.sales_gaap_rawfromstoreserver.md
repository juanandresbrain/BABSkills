# dbo.sales_gaap_rawfromstoreserver

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sales_gaap_rawfromstoreserver"]
    dbo_sales_gaap_rawfromstoreserver(["dbo.sales_gaap_rawfromstoreserver"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sales_gaap_rawfromstoreserver |

## View Code

```sql
;

;
CREATE VIEW dbo.sales_gaap_rawfromstoreserver AS SELECT * FROM LH_Mart.dbo.sales_gaap_rawfromstoreserver;;
```

