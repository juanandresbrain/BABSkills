# dbo.JMC_SLS_SilverDeltaLake_StageforStoreforce

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| RegisterNumber | int | 4 | 1 |  |  |  |
| trans_nbr | bigint | 8 | 1 |  |  |  |
| total | numeric | 17 | 1 |  |  |  |
| trans_type | nvarchar | -1 | 1 |  |  |  |
| trans_status | nvarchar | -1 | 1 |  |  |  |
| loyalty_card_number | nvarchar | -1 | 1 |  |  |  |
| customer_id | nvarchar | -1 | 1 |  |  |  |
| Employee | nvarchar | -1 | 1 |  |  |  |
| event_id | nvarchar | -1 | 1 |  |  |  |
| event_invoice | nvarchar | -1 | 1 |  |  |  |
| party_id | nvarchar | -1 | 1 |  |  |  |
