# dbo.configuration_review_area

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| table_maintenance_area_id | numeric | 5 | 0 |  |  |  |
| language_id | smallint | 2 | 0 |  |  |  |
| table_maintenance_area_desc | nvarchar | 510 | 0 |  |  |  |
| priority_no | smallint | 2 | 0 |  |  |  |
| table_name | nvarchar | 60 | 0 |  |  |  |
| group1_heading | nvarchar | 510 | 0 |  |  |  |
| group2_heading | nvarchar | 510 | 0 |  |  |  |
| field_code_heading | nvarchar | 510 | 0 |  |  |  |
| field_setting_heading | nvarchar | 510 | 0 |  |  |  |
| table_maintenance_area_module | nvarchar | 510 | 1 |  |  |  |
