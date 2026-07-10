# dbo.SalesAudit_coupon_group_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| coupon_group_key | int | 4 | 0 |  |  |  |
| coupon_key | int | 4 | 0 |  |  |  |
| seq_num | int | 4 | 0 |  |  |  |
| ratio | decimal | 9 | 1 |  |  |  |
| Coupon_amount | money | 8 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| DW_AuditLoadDt | datetime | 8 | 0 |  |  |  |
