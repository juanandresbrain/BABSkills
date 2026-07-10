# dbo.WebDemandOrdersUSStageRejects

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Flat File Source Error Output Column | varchar | -1 | 1 |  |  |  |
| ErrorCode | int | 4 | 1 |  |  |  |
| ErrorColumn | int | 4 | 1 |  |  |  |
| FileName | nvarchar | 1000 | 1 |  |  |  |
| FileDate | nvarchar | 28 | 1 |  |  |  |
