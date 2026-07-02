# dbo.location_status

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.location_status"]
    dbo_language(["dbo.language"]) --> VIEW
    dbo_location_status_data(["dbo.location_status_data"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.language |
| dbo.location_status_data |
| dbo.merchdata_lang |

## View Code

```sql
CREATE VIEW [dbo].[location_status]
AS
SELECT a.location_status_id,
       COALESCE(mdl.[description], a.location_status_label) as location_status_label,
       a.updatestamp
  FROM [dbo].[location_status_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'location_status'
       ) mdl
    ON (mdl.parent_id=a.location_status_id);
```

