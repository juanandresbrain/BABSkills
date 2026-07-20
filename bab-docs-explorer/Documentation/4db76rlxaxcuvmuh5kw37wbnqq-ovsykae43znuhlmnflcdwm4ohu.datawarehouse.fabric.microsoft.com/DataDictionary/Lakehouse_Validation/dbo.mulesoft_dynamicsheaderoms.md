# dbo.mulesoft_dynamicsheaderoms

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| TransactionKey | varchar | 8000 | 1 |  |  |  |
| RetailTerminalId | varchar | 8000 | 1 |  |  |  |
| CustAccount | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| RetailReceiptId | varchar | 8000 | 1 |  |  |  |
| RetailStaffId | varchar | 8000 | 1 |  |  |  |
| RetailTransactionId | varchar | 8000 | 1 |  |  |  |
| BABIntRetailOperatingUnitNumber | varchar | 8000 | 0 |  |  |  |
| TransDate | date | 3 | 1 |  |  |  |
| RetailTransactionType | varchar | 8000 | 0 |  |  |  |
| BABIntRetailProcessed | int | 4 | 1 |  |  |  |
| Entity | varchar | 8000 | 1 |  |  |  |
| DiscAmount | decimal | 17 | 0 |  |  |  |
| TotalDiscAmount | decimal | 17 | 0 |  |  |  |
| CreateTime | datetime2 | 8 | 1 |  |  |  |
| Barcode | varchar | 8000 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| BatchID | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| Exported | int | 4 | 1 |  |  |  |
| DeckOrderRef | varchar | 8000 | 1 |  |  |  |
| DeliveryMode | varchar | 8000 | 1 |  |  |  |
| eCommOrderType | varchar | 8000 | 1 |  |  |  |
| ExtOrderDate | datetime2 | 8 | 1 |  |  |  |
| OrderPoolId | varchar | 8000 | 1 |  |  |  |
| PartyId | varchar | 8000 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1574296668 | bigint | 8 | 0 |  |  |  |
