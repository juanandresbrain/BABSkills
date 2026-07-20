# dbo.attribute_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.attribute_dim"]
    dbo_attribute_dim(["dbo.attribute_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute_dim |

## View Code

```sql
;

CREATE VIEW dbo.attribute_dim AS SELECT entity_key COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS entity_key, style_code, AttributeName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS AttributeName, AttributeValue COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS AttributeValue, INS_DT, UPDT_DT FROM LH_Mart.dbo.attribute_dim;;
```

