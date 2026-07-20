# dbo.crmde3

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmde3"]
    dbo_crmde3(["dbo.crmde3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmde3 |

## View Code

```sql
;

CREATE VIEW dbo.crmde3 AS SELECT customerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS customerNumber, transactionID, purchaseDate, purchaseChannel COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS purchaseChannel, purchaseStoreNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS purchaseStoreNumber, purchaseRevenue, purchaseUnitCount, stuffed, unstuffed, licensedORNot, consumerGroup COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS consumerGroup, keyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS keyStory, department COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS department, Country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Country, sku COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS sku, InsertDate, UpdateDate, recID, Emailable FROM LH_Mart.dbo.crmde3;
```

