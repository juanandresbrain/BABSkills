# dbo.StagingBearPivoted

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StagingBearPivotedId | int | 4 | 0 | YES |  |  |
| BearId | nvarchar | 7000 | 1 |  |  |  |
| StoreNumber | int | 4 | 1 |  |  |  |
| ItemNumber | nvarchar | 40 | 1 |  |  |  |
| TransactionDate | datetime | 8 | 1 |  |  |  |
| AttributeType | nvarchar | 256 | 1 |  |  |  |
| AttributeValues | nvarchar | 7000 | 1 |  |  |  |
| Items | nvarchar | 7000 | 1 |  |  |  |
