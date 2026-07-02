# dbo.unit

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.unit"]
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
    dbo_unit_data(["dbo.unit_data"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.language |
| dbo.merchdata_lang |
| dbo.unit_data |

## View Code

```sql
CREATE VIEW [dbo].[unit]
AS
SELECT a.unit_id,
       a.unit_type_id,
       COALESCE(mdl.[code], a.unit_code) as unit_code,
       COALESCE(mdl.[description], a.unit_label) as unit_label,
       a.unit_abbreviation
  FROM [dbo].[unit_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'unit'
       ) mdl
    ON (mdl.parent_id=a.unit_id);
```

