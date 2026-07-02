# dbo.reason_type

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.reason_type"]
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
    dbo_reason_type_data(["dbo.reason_type_data"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.language |
| dbo.merchdata_lang |
| dbo.reason_type_data |

## View Code

```sql
CREATE VIEW [dbo].[reason_type]
AS
SELECT a.reason_type_id,
       a.reason_type_code,
       COALESCE(mdl.[description], a.reason_type_desc) as reason_type_desc,
       a.user_defined_flag,
       a.active_flag,
       a.updatestamp
  FROM [dbo].[reason_type_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'reason_type'
       ) mdl
    ON (mdl.parent_id=a.reason_type_id);
```

