# dbo.postgrescoupondim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.postgrescoupondim"]
    dbo_postgrescoupondim(["dbo.postgrescoupondim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.postgrescoupondim |

## View Code

```sql
;

CREATE VIEW dbo.postgrescoupondim AS 


SELECT tag_country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS tag_country
      ,campaignid COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS campaignid
      ,campaignname COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS campaignname
      ,promotion_id COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS promotion_id
      ,promotion_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS promotion_name
      ,long_description COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS long_description
      ,promotion_type COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS promotion_type
      ,create_by COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS create_by
      ,effective_start_time
      ,effective_end_time
      ,InsertDate
      ,UpdateDate
  FROM LH_Mart.dbo.postgrescoupondim;
```

