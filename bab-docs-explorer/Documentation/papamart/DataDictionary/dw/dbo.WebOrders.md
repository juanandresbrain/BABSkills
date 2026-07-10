# dbo.WebOrders

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SourceSite | varchar | 2 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderNum | varchar | 10 | 1 |  |  |  |
| OrderDate | datetime | 8 | 1 |  |  |  |
| ShippingAmount | money | 8 | 1 |  |  |  |
| OrderStatus | varchar | 20 | 1 |  |  |  |
| StatusDate | datetime | 8 | 1 |  |  |  |
| Physical | varchar | 3 | 1 |  |  |  |
| StatusSortOrder | int | 4 | 1 |  |  |  |
| ShipToPostalCode | varchar | 12 | 1 |  |  |  |
| ShipToState | varchar | 52 | 1 |  |  |  |
| ShipToCountry | varchar | 52 | 1 |  |  |  |
| ESReferenceNbr | varchar | 19 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| BillToFirstName | varchar | 100 | 1 |  |  |  |
| BillToLastName | varchar | 100 | 1 |  |  |  |
| BillToCity | varchar | 100 | 1 |  |  |  |
| BillToState | varchar | 100 | 1 |  |  |  |
| BillToPostCode | varchar | 20 | 1 |  |  |  |
| BillToCountry | varchar | 100 | 1 |  |  |  |
| BillToEmailAddress | varchar | 100 | 1 |  |  |  |
| BillToCustomerNumber | varchar | 20 | 1 |  |  |  |
