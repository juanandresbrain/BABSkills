# dbo.aw_Load_Audit

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Package Name | nvarchar | 510 | 1 |  |  |  |
| Execution Instance | uniqueidentifier | 16 | 1 |  |  |  |
| Machine Name | nvarchar | 510 | 1 |  |  |  |
| Start Time | datetime | 8 | 1 |  |  |  |
| Existing Dimension Input Row Count | int | 4 | 1 |  |  |  |
| Special Members Input Row Count | int | 4 | 1 |  |  |  |
| Source System Input Row Count | int | 4 | 1 |  |  |  |
| Unchanged Output Row Count | int | 4 | 1 |  |  |  |
| New Output Row Count | int | 4 | 1 |  |  |  |
| Deleted Output Row Count | int | 4 | 1 |  |  |  |
| SCD2 Expired Output Row Count | int | 4 | 1 |  |  |  |
| SCD2 New Output Row Count | int | 4 | 1 |  |  |  |
| SCD1 Updated Output Row Count | int | 4 | 1 |  |  |  |
| Invalid Input Output Row Count | int | 4 | 1 |  |  |  |
| Time First Existing Dimension Row Received | datetime | 8 | 1 |  |  |  |
| Time Last Existing Dimension Row Received | datetime | 8 | 1 |  |  |  |
| Time First Special Members Row Received | datetime | 8 | 1 |  |  |  |
| Time Last Special Members Row Received | datetime | 8 | 1 |  |  |  |
| Time First Source System Row Received | datetime | 8 | 1 |  |  |  |
| Time Last Source System Row Received | datetime | 8 | 1 |  |  |  |
| Milliseconds until first key match | int | 4 | 1 |  |  |  |
| Number of rows held in cache on first key match | int | 4 | 1 |  |  |  |
| Maximum number of rows held in cache | int | 4 | 1 |  |  |  |
| Average number of rows held in cache | int | 4 | 1 |  |  |  |
| Milliseconds of Upstream Backpressure Generated | int | 4 | 1 |  |  |  |
| Sort Optimization Cache Hit Percentage | numeric | 5 | 1 |  |  |  |
| Time First Output Row Produced | datetime | 8 | 1 |  |  |  |
| Time Last Output Row Produced | datetime | 8 | 1 |  |  |  |
| Milliseconds of Downstream Backpressure Experienced | int | 4 | 1 |  |  |  |
| Maximum Output Rows per Second | int | 4 | 1 |  |  |  |
