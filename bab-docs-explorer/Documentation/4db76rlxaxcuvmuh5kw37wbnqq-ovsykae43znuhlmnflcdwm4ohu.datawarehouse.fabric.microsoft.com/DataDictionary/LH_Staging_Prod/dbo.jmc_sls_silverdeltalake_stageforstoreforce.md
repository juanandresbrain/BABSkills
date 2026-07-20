# dbo.jmc_sls_silverdeltalake_stageforstoreforce

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BusinessDate | date | 3 | 1 |  |  |  |
| StoreID | int | 4 | 1 |  |  |  |
| RegisterNumber | int | 4 | 1 |  |  |  |
| trans_nbr | bigint | 8 | 1 |  |  |  |
| total | decimal | 17 | 1 |  |  |  |
| trans_type | varchar | 8000 | 1 |  |  |  |
| trans_status | varchar | 8000 | 1 |  |  |  |
| loyalty_card_number | varchar | 8000 | 1 |  |  |  |
| customer_id | varchar | 8000 | 1 |  |  |  |
| Employee | varchar | 8000 | 1 |  |  |  |
| event_id | varchar | 8000 | 1 |  |  |  |
| event_invoice | varchar | 8000 | 1 |  |  |  |
| party_id | varchar | 8000 | 1 |  |  |  |
