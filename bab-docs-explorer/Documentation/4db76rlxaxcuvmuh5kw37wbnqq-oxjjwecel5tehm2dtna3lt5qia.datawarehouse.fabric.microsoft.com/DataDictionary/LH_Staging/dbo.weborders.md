# dbo.weborders

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SourceSite | varchar | 8000 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| OrderID | int | 4 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| OrderDate | datetime2 | 8 | 1 |  |  |  |
| ShippingAmount | decimal | 9 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| StatusDate | datetime2 | 8 | 1 |  |  |  |
| Physical | varchar | 8000 | 1 |  |  |  |
| StatusSortOrder | int | 4 | 1 |  |  |  |
| ShipToPostalCode | varchar | 8000 | 1 |  |  |  |
| ShipToState | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| ESReferenceNbr | varchar | 8000 | 1 |  |  |  |
| BillToFirstName | varchar | 8000 | 1 |  |  |  |
| BillToLastName | varchar | 8000 | 1 |  |  |  |
| BillToCity | varchar | 8000 | 1 |  |  |  |
| BillToState | varchar | 8000 | 1 |  |  |  |
| BillToPostCode | varchar | 8000 | 1 |  |  |  |
| BillToCountry | varchar | 8000 | 1 |  |  |  |
| BillToEmailAddress | varchar | 8000 | 1 |  |  |  |
| BillToCustomerNumber | varchar | 8000 | 1 |  |  |  |
