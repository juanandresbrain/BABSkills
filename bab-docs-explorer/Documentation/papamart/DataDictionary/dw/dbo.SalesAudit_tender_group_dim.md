# dbo.SalesAudit_tender_group_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| seq_num | int | 4 | 0 |  |  |  |
| tender_group_key | int | 4 | 0 |  |  |  |
| tender_key | int | 4 | 0 |  |  |  |
| tender_amt | money | 8 | 1 |  |  |  |
| ratio | decimal | 9 | 1 |  |  |  |
| tax | char | 1 | 1 |  |  |  |
| DW_AuditLoadDt | datetime | 8 | 0 |  |  |  |
