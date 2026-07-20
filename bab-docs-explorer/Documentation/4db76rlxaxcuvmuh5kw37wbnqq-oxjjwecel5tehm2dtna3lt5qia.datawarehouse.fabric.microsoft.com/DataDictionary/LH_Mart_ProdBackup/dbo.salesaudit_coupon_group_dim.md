# dbo.salesaudit_coupon_group_dim

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

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
