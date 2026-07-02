# dbo.imat_flow

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.imat_flow"]
    dbo_imat_flow_data(["dbo.imat_flow_data"]) --> VIEW
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.imat_flow_data |
| dbo.language |
| dbo.merchdata_lang |

## View Code

```sql
CREATE VIEW [dbo].[imat_flow]
AS
SELECT a.imat_flow_id,
       a.matching_flow_option,
       COALESCE(mdl.[description], a.matching_flow_desc) as matching_flow_desc,
       a.active_flag,
       a.updatestamp,
       a.last_item_id
  FROM [dbo].[imat_flow_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'imat_flow'
       ) mdl
    ON (mdl.parent_id=a.imat_flow_id);
```

