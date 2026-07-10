# dbo.CRMTransactionFactRollups

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionID | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| TransactionYear | int | 4 | 1 |  |  |  |
| TransacionMonth | int | 4 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| StoreConcept | nvarchar | 12 | 1 |  |  |  |
| LifetimeVisitNumber | int | 4 | 1 |  |  |  |
| KeyStory | nvarchar | 60 | 1 |  |  |  |
| ConsumerGroup | varchar | 20 | 1 |  |  |  |
| Department | varchar | 20 | 1 |  |  |  |
| LicensedOrNot | int | 4 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
| Sales | numeric | 17 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| StoreNumber | nvarchar | 20 | 1 |  |  |  |
| JurisdictionCode | varchar | 20 | 1 |  |  |  |
| Country | varchar | 50 | 1 |  |  |  |
