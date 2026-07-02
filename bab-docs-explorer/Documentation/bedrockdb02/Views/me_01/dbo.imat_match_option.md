# dbo.imat_match_option

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.imat_match_option"]
    dbo_imat_match_option_data(["dbo.imat_match_option_data"]) --> VIEW
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.imat_match_option_data |
| dbo.language |
| dbo.merchdata_lang |

## View Code

```sql
CREATE VIEW [dbo].[imat_match_option]
AS
SELECT a.imat_match_option_id,
       a.imat_flow_option_code,
       COALESCE(mdl.[description], a.imat_flow_option_desc) as imat_flow_option_desc
  FROM [dbo].[imat_match_option_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'imat_match_option'
       ) mdl
    ON (mdl.parent_id=a.imat_match_option_id);
```

