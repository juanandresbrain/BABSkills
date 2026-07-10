# dbo.AzureDataDictionaryStageThree

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TableName | nvarchar | 510 | 1 |  |  |  |
| DisplayFolder | nvarchar | 510 | 1 |  |  |  |
| Expression | nvarchar | 8000 | 1 |  |  |  |
| SourceView | varchar | 100 | 1 |  |  |  |
| ViewDefinition | nvarchar | -1 | 1 |  |  |  |
| ColumnOrMeasure | varchar | 7 | 1 |  |  |  |
| ColumnName | nvarchar | 510 | 1 |  |  |  |
