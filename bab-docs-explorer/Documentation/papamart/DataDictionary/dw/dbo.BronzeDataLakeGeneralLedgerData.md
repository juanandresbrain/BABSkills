# dbo.BronzeDataLakeGeneralLedgerData

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| InventLocationId | nvarchar | 16 | 1 |  |  |  |
| MainAccountId | nvarchar | 40 | 1 |  |  |  |
| MainAccountName | nvarchar | 120 | 1 |  |  |  |
| AccountCategory | nvarchar | 40 | 1 |  |  |  |
| AccountingDate | date | 3 | 1 |  |  |  |
| DocumentDate | date | 3 | 1 |  |  |  |
| Voucher | nvarchar | 40 | 1 |  |  |  |
| DocumentNumber | nvarchar | 40 | 1 |  |  |  |
| JournalNumber | nvarchar | 40 | 1 |  |  |  |
| Entity | nvarchar | 8 | 1 |  |  |  |
| LedgerAccount | nvarchar | 1000 | 1 |  |  |  |
| PostingType | int | 4 | 1 |  |  |  |
| IsCredit | int | 4 | 1 |  |  |  |
| AccountingCurrencyAmount | numeric | 17 | 1 |  |  |  |
| ReportingCurrencyAmount | numeric | 17 | 1 |  |  |  |
| TransactionCurrencyAmount | numeric | 17 | 1 |  |  |  |
| TransactionCurrencyCode | nvarchar | 6 | 1 |  |  |  |
| GLEntryProcessingDate | datetime2 | 8 | 1 |  |  |  |
