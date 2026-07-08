# dbo.ServerParametersInstance

**Database:** ReportServerESell  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServerParametersID | nvarchar | 64 | 0 |  |  |  |
| ParentID | nvarchar | 64 | 1 |  |  |  |
| Path | nvarchar | 850 | 0 |  |  |  |
| CreateDate | datetime | 8 | 0 |  |  |  |
| ModifiedDate | datetime | 8 | 0 |  |  |  |
| Timeout | int | 4 | 0 |  |  |  |
| Expiration | datetime | 8 | 0 |  |  |  |
| ParametersValues | image | 256 | 0 |  |  |  |
