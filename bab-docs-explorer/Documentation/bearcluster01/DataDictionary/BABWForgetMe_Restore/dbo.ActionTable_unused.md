# dbo.ActionTable_unused

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ATKey | int | 4 | 0 |  |  |  |
| ServerName | varchar | 32 | 0 |  |  |  |
| DBName | varchar | 64 | 0 |  |  |  |
| SchemaName | varchar | 32 | 0 |  |  |  |
| TableName | varchar | 32 | 0 |  |  |  |
| Action | tinyint | 1 | 0 |  |  |  |
| TablePK | varchar | 100 | 1 |  |  |  |
| DelayTime | int | 4 | 0 |  |  |  |
| IsProduction | tinyint | 1 | 1 |  |  |  |

