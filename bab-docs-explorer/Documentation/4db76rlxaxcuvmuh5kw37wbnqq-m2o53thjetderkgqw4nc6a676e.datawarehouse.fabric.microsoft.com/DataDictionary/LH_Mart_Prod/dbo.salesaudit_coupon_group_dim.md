# dbo.salesaudit_coupon_group_dim

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_group_key | int | 4 | 1 |  |  |  |
| coupon_key | int | 4 | 1 |  |  |  |
| seq_num | int | 4 | 1 |  |  |  |
| ratio | decimal | 9 | 1 |  |  |  |
| Coupon_amount | decimal | 9 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| DW_AuditLoadDt | datetime2 | 8 | 1 |  |  |  |
