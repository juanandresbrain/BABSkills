# dbo.Lg_DependentDesc

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| language_id | int | 4 | 0 |  |  |  |
| resource_id | numeric | 9 | 0 |  |  |  |
| first_pair_text | nvarchar | 510 | 1 |  |  |  |
| second_pair_text | nvarchar | 510 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Md_LoadLanguage](../../StoredProcedures/fn_01/dbo.Md_LoadLanguage.md)
- [smartlook_01: dbo.Md_LoadLanguage](../../StoredProcedures/smartlook_01/dbo.Md_LoadLanguage.md)

