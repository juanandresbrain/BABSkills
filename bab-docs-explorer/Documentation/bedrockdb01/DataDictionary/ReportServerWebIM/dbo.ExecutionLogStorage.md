# dbo.ExecutionLogStorage

**Database:** ReportServerWebIM  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogEntryId | bigint | 8 | 0 | YES |  |  |
| InstanceName | nvarchar | 76 | 0 |  |  |  |
| ReportID | uniqueidentifier | 16 | 1 |  |  |  |
| UserName | nvarchar | 520 | 1 |  |  |  |
| ExecutionId | nvarchar | 128 | 1 |  |  |  |
| RequestType | tinyint | 1 | 0 |  |  |  |
| Format | nvarchar | 52 | 1 |  |  |  |
| Parameters | ntext | 16 | 1 |  |  |  |
| ReportAction | tinyint | 1 | 1 |  |  |  |
| TimeStart | datetime | 8 | 0 |  |  |  |
| TimeEnd | datetime | 8 | 0 |  |  |  |
| TimeDataRetrieval | int | 4 | 0 |  |  |  |
| TimeProcessing | int | 4 | 0 |  |  |  |
| TimeRendering | int | 4 | 0 |  |  |  |
| Source | tinyint | 1 | 0 |  |  |  |
| Status | nvarchar | 80 | 0 |  |  |  |
| ByteCount | bigint | 8 | 0 |  |  |  |
| RowCount | bigint | 8 | 0 |  |  |  |
| AdditionalInfo | xml | -1 | 1 |  |  |  |
