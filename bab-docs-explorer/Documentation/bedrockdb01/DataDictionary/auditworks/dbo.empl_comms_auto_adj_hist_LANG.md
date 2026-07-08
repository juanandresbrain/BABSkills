# dbo.empl_comms_auto_adj_hist_LANG

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| adj_hist_posting_datetime | datetime | 8 | 0 |  |  |  |
| auto_commission_adj_id | numeric | 5 | 0 |  |  |  |
| language_id | smallint | 2 | 0 |  |  |  |
| cond_description | nvarchar | 6000 | 1 |  |  |  |
| adj_description | nvarchar | 6000 | 1 |  |  |  |
