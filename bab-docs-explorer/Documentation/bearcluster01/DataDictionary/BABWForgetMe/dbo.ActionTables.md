# dbo.ActionTables

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ATKey | int | 4 | 0 | YES |  |  |
| ServerName | varchar | 32 | 0 |  |  |  |
| DBName | varchar | 64 | 0 |  |  |  |
| SchemaName | varchar | 32 | 0 |  |  |  |
| TableName | varchar | 32 | 0 |  |  |  |
| Action | tinyint | 1 | 0 |  |  |  |
| TablePK | varchar | 100 | 1 |  |  |  |
| DelayTime | int | 4 | 0 |  |  |  |
| IsProduction | bit | 1 | 1 |  |  |  |

