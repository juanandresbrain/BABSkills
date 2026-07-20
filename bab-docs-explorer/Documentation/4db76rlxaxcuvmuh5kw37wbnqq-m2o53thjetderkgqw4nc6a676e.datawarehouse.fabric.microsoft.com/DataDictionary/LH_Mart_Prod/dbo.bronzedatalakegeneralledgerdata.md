# dbo.bronzedatalakegeneralledgerdata

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| MainAccountId | varchar | 8000 | 1 |  |  |  |
| MainAccountName | varchar | 8000 | 1 |  |  |  |
| AccountCategory | varchar | 8000 | 1 |  |  |  |
| AccountingDate | date | 3 | 1 |  |  |  |
| DocumentDate | date | 3 | 1 |  |  |  |
| Voucher | varchar | 8000 | 1 |  |  |  |
| DocumentNumber | varchar | 8000 | 1 |  |  |  |
| JournalNumber | varchar | 8000 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| LedgerAccount | varchar | 8000 | 1 |  |  |  |
| PostingType | int | 4 | 1 |  |  |  |
| IsCredit | int | 4 | 1 |  |  |  |
| AccountingCurrencyAmount | decimal | 17 | 1 |  |  |  |
| ReportingCurrencyAmount | decimal | 17 | 1 |  |  |  |
| TransactionCurrencyAmount | decimal | 17 | 1 |  |  |  |
| TransactionCurrencyCode | varchar | 8000 | 1 |  |  |  |
| GLEntryProcessingDate | datetime2 | 8 | 1 |  |  |  |
