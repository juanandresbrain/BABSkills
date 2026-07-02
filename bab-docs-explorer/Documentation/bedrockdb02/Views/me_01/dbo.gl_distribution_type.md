# dbo.gl_distribution_type

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.gl_distribution_type"]
    dbo_gl_distribution_type_data(["dbo.gl_distribution_type_data"]) --> VIEW
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.gl_distribution_type_data |
| dbo.language |
| dbo.merchdata_lang |

## View Code

```sql
CREATE VIEW [dbo].[gl_distribution_type]
AS
SELECT a.gl_distribution_type_id,
       a.gl_distribution_type,
       COALESCE(mdl.[description], a.gl_distribution_type_desc) as gl_distribution_type_desc,
       a.distribution_set_handling,
       a.gl_effect,
       a.discount_applicability_group
  FROM [dbo].[gl_distribution_type_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'gl_distribution_type'
       ) mdl
    ON (mdl.parent_id=a.gl_distribution_type_id);
```

