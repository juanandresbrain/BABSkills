# dbo.transaction_type

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transaction_type"]
    dbo_language(["dbo.language"]) --> VIEW
    dbo_merchdata_lang(["dbo.merchdata_lang"]) --> VIEW
    dbo_transaction_type_data(["dbo.transaction_type_data"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.language |
| dbo.merchdata_lang |
| dbo.transaction_type_data |

## View Code

```sql
CREATE VIEW [dbo].[transaction_type]
AS
SELECT a.transaction_type_id,
       a.transaction_type_code,
       COALESCE(mdl.[description], a.transaction_type_desc) as transaction_type_desc,
       a.stock_ledger_affect
  FROM [dbo].[transaction_type_data] a
  LEFT OUTER JOIN
      (SELECT * FROM [dbo].[merchdata_lang] mdl2
        WHERE mdl2.language_id = (SELECT [dbo].[language].language_id
                                    FROM [dbo].[language]
                                   WHERE [dbo].[language].default_desc_language_flag = 1)
          AND mdl2.parent_type=N'transaction_type'
       ) mdl
    ON (mdl.parent_id=a.transaction_type_id);
```

