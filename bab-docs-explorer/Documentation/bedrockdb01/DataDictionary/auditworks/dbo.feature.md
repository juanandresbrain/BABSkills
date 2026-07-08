# dbo.feature

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| entity | char | 6 | 0 |  |  |  |
| feature_code | char | 4 | 0 |  |  |  |
| feature_description | varchar | 255 | 0 |  |  |  |
| feature_code_group | varchar | 12 | 1 |  |  |  |
| timestamp | timestamp | 8 | 1 |  |  |  |
| last_audit_datetime | smalldatetime | 4 | 0 |  |  |  |
| resource_id | numeric | 9 | 1 |  |  |  |
| HRCHY_LVL_GRP_IDNTY | smallint | 2 | 0 | YES |  |  |
