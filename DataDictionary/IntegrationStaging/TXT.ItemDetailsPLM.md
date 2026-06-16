# TXT.ItemDetailsPLM

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| style_code | varchar | 512 | 1 |  |  |  |
| StyleShortDesc | varchar | 20 | 1 |  |  |  |
| babcompletecode | nvarchar | 200 | 1 |  |  |  |
| ConceptCode | nvarchar | 100 | 1 |  |  |  |
| ChainLabel | nvarchar | 100 | 1 |  |  |  |
| DepartmentLabel | nvarchar | 100 | 1 |  |  |  |
| ClassLabel | nvarchar | 100 | 1 |  |  |  |
| SubClassLabel | nvarchar | 100 | 1 |  |  |  |
| StyleCustomPropertyValue | nvarchar | 100 | 1 |  |  |  |
| StyleAttributeSetCodeO | nvarchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: TXT.spItemDetailsPLM](../../StoredProcedures/IntegrationStaging/TXT.spItemDetailsPLM.md)

