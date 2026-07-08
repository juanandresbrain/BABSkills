# dbo.location

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| location_type | tinyint | 1 | 0 |  |  |  |
| location_code | nchar | 6 | 0 |  |  |  |
| location_name | nvarchar | 510 | 0 |  |  |  |
| pos_location_code | nvarchar | 6 | 1 |  |  |  |
| in_location_code | nchar | 6 | 1 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| gmt_offset_hrs_daylight | smallint | 2 | 0 |  |  |  |
| gmt_offset_hrs_standard | smallint | 2 | 0 |  |  |  |
| in_location_type | tinyint | 1 | 1 |  |  |  |
