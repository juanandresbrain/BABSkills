# dbo.ds_email_rollup

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| sendid_key | int | 4 | 1 |  |  |  |
| emailname | varchar | 8000 | 1 |  |  |  |
| targeted_count | bigint | 8 | 1 |  |  |  |
| opened_count | bigint | 8 | 1 |  |  |  |
| clicked_count | bigint | 8 | 1 |  |  |  |
| bounced_count | bigint | 8 | 1 |  |  |  |
| unsub_count | bigint | 8 | 1 |  |  |  |
| actual_date | date | 3 | 1 |  |  |  |
| trimmed_emailname | varchar | 8000 | 1 |  |  |  |
