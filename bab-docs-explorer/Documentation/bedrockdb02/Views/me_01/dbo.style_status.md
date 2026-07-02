# dbo.style_status

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.style_status"]
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
    dbo_style_status_data(["dbo.style_status_data"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.language |
| dbo.merchdata_lang |
| dbo.style_status_data |

## View Code

```sql
CREATE VIEW [dbo].[style_status]
AS
SELECT a.style_status_code,
       COALESCE(mdl.description, a.style_status_descr) as style_status_descr,
       COALESCE(mdl.code, a.style_status_short_descr) as style_status_short_descr
  FROM [dbo].[style_status_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'style_status'
       ) mdl
    ON (mdl.parent_id=a.style_status_code);
```

