# admin.Configurations

**Database:** SSISTemplates  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Config_ID | int | 4 | 0 | YES |  |  |
| ConfigurationFilter | nvarchar | 510 | 0 |  |  |  |
| ConfiguredValue | nvarchar | 8000 | 1 |  |  |  |
| PackagePath | nvarchar | 510 | 0 |  |  |  |
| ConfiguredValueType | nvarchar | 40 | 0 |  |  |  |
