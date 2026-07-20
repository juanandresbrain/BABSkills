# dbo.dw_monitor_audittransactionloadstatus

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| dateKey | int | 4 | 1 |  |  |  |
| ActualDate | datetime2 | 8 | 1 |  |  |  |
| TransactionCount | int | 4 | 1 |  |  |  |
| TransactionDetailFactCount | int | 4 | 1 |  |  |  |
| TenderFactCount | int | 4 | 1 |  |  |  |
| DiscountFactCount | int | 4 | 1 |  |  |  |
| GiftcardActivatedCount | int | 4 | 1 |  |  |  |
| GiftcardRedeemedCount | int | 4 | 1 |  |  |  |
