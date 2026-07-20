# dbo.discount_category_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.discount_category_dim"]
    dbo_discount_category_dim(["dbo.discount_category_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.discount_category_dim |

## View Code

```sql
;

CREATE VIEW dbo.discount_category_dim AS SELECT categoryTypeID, categoryType COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS categoryType, categoryTypeRelSeq, channelType COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS channelType, channelTypeRelSeq, financialGroup COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS financialGroup, financialGroupRelSeq FROM LH_Mart.dbo.discount_category_dim;
```

