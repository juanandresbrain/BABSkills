# dbo.salesaudit_tender_group_dim

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seq_num | int | 4 | 1 |  |  |  |
| tender_group_key | int | 4 | 1 |  |  |  |
| tender_key | int | 4 | 1 |  |  |  |
| tender_amt | decimal | 9 | 1 |  |  |  |
| ratio | decimal | 9 | 1 |  |  |  |
| tax | varchar | 8000 | 1 |  |  |  |
| DW_AuditLoadDt | datetime2 | 8 | 1 |  |  |  |
