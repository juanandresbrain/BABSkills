# dbo.CachePolicy

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CachePolicyID | uniqueidentifier | 16 | 0 |  |  |  |
| ReportID | uniqueidentifier | 16 | 0 |  |  |  |
| ExpirationFlags | int | 4 | 0 |  |  |  |
| CacheExpiration | int | 4 | 1 |  |  |  |
