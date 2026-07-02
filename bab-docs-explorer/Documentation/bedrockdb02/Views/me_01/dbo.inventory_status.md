# dbo.inventory_status

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.inventory_status"]
    dbo_inventory_status_data(["dbo.inventory_status_data"]) --> VIEW
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.inventory_status_data |
| dbo.language |
| dbo.merchdata_lang |

## View Code

```sql
CREATE VIEW [dbo].[inventory_status]
AS
SELECT a.inventory_status_id,
       a.inventory_status_code,
       COALESCE(mdl.[description], a.inventory_status_desc) as inventory_status_desc,
       a.user_defined_flag,
       a.active_flag,
       a.include_on_hand_totals_flag,
       a.updatestamp
  FROM [dbo].[inventory_status_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'inventory_status'
       ) mdl
    ON (mdl.parent_id=a.inventory_status_id);
```

