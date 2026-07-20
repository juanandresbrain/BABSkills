# dbo.postgrescoupondim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
CREATE   VIEW [dbo].[postgrescoupondim] AS    SELECT tag_country COLLATE Latin1_General_CI_AS AS [tag_country]       ,campaignid COLLATE Latin1_General_CI_AS AS [campaignid]       ,campaignname COLLATE Latin1_General_CI_AS AS [campaignname]       ,promotion_id COLLATE Latin1_General_CI_AS AS [promotion_id]       ,promotion_name COLLATE Latin1_General_CI_AS AS [promotion_name]       ,long_description COLLATE Latin1_General_CI_AS AS [long_description]       ,promotion_type COLLATE Latin1_General_CI_AS AS [promotion_type]       ,create_by COLLATE Latin1_General_CI_AS AS [create_by]       ,[effective_start_time]       ,[effective_end_time]       ,[InsertDate]       ,[UpdateDate]   FROM LH_Mart.[dbo].[postgrescoupondim]
```

