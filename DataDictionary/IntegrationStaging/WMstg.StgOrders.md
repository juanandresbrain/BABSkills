# WMstg.StgOrders

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderId | int | 4 | 0 |  |  |  |
| TransactionID | int | 4 | 0 |  |  |  |
| OrderNum | varchar | 10 | 0 |  |  |  |
| EnterpriseSellingID | varchar | 20 | 1 |  |  |  |
| OrderDate | datetime | 8 | 0 |  |  |  |
| OrderStatus | varchar | 20 | 0 |  |  |  |
| OrderType | varchar | 3 | 1 |  |  |  |
| PickUpStore | varchar | 4 | 1 |  |  |  |
| OrderAuthentication | varchar | 100 | 1 |  |  |  |
| SourceSite | varchar | 7 | 1 |  |  |  |
| BatchNo | int | 4 | 1 |  |  |  |
| SequenceNo | int | 4 | 1 |  |  |  |
| DatePrinted | datetime | 8 | 1 |  |  |  |
| HouseOrder | bit | 1 | 1 |  |  |  |
| HouseOrderReason | varchar | 20 | 1 |  |  |  |
| GiftSender | nvarchar | 60 | 1 |  |  |  |
| GiftMessage | nvarchar | 500 | 1 |  |  |  |
| SpecialInstructions | varchar | 4000 | 1 |  |  |  |
| ServiceRep | varchar | 50 | 1 |  |  |  |
| BillToFName | varchar | 20 | 1 |  |  |  |
| BillToLName | varchar | 50 | 1 |  |  |  |
| BillToAddress1 | varchar | 100 | 1 |  |  |  |
| BillToAddress2 | varchar | 100 | 1 |  |  |  |
| BillToCity | varchar | 50 | 1 |  |  |  |
| BillToState | varchar | 50 | 1 |  |  |  |
| BillToPostalCode | varchar | 20 | 1 |  |  |  |
| BillToCountry | varchar | 30 | 1 |  |  |  |
| BillToPhone | varchar | 20 | 1 |  |  |  |
| BillToEmail | varchar | 100 | 1 |  |  |  |
| ShipToFName | varchar | 20 | 1 |  |  |  |
| ShipToLName | varchar | 50 | 1 |  |  |  |
| ShipToAddress1 | varchar | 100 | 1 |  |  |  |
| ShipToAddress2 | varchar | 100 | 1 |  |  |  |
| ShipToCity | varchar | 50 | 1 |  |  |  |
| ShipToState | varchar | 50 | 1 |  |  |  |
| ShipToPostalCode | varchar | 20 | 1 |  |  |  |
| ShipToCountry | varchar | 30 | 1 |  |  |  |
| ShipToPhone | varchar | 20 | 1 |  |  |  |
| ShipToEmail | varchar | 100 | 1 |  |  |  |
| ShippingMethod | varchar | 20 | 1 |  |  |  |
| ShippingAmount | money | 8 | 1 |  |  |  |
| PickTicketFlag | bit | 1 | 1 |  |  |  |
| OrderId | int | 4 | 0 |  |  |  |
| TransactionID | int | 4 | 0 |  |  |  |
| OrderNum | varchar | 10 | 0 |  |  |  |
| EnterpriseSellingID | varchar | 20 | 1 |  |  |  |
| OrderDate | datetime | 8 | 0 |  |  |  |
| OrderStatus | varchar | 20 | 0 |  |  |  |
| OrderType | varchar | 3 | 1 |  |  |  |
| PickUpStore | varchar | 4 | 1 |  |  |  |
| OrderAuthentication | varchar | 100 | 1 |  |  |  |
| SourceSite | varchar | 7 | 1 |  |  |  |
| BatchNo | int | 4 | 1 |  |  |  |
| SequenceNo | int | 4 | 1 |  |  |  |
| DatePrinted | datetime | 8 | 1 |  |  |  |
| HouseOrder | bit | 1 | 1 |  |  |  |
| HouseOrderReason | varchar | 20 | 1 |  |  |  |
| GiftSender | varchar | 30 | 1 |  |  |  |
| GiftMessage | varchar | 250 | 1 |  |  |  |
| SpecialInstructions | varchar | 4000 | 1 |  |  |  |
| ServiceRep | varchar | 50 | 1 |  |  |  |
| BillToFName | varchar | 20 | 1 |  |  |  |
| BillToLName | varchar | 50 | 1 |  |  |  |
| BillToAddress1 | varchar | 100 | 1 |  |  |  |
| BillToAddress2 | varchar | 100 | 1 |  |  |  |
| BillToCity | varchar | 50 | 1 |  |  |  |
| BillToState | varchar | 50 | 1 |  |  |  |
| BillToPostalCode | varchar | 20 | 1 |  |  |  |
| BillToCountry | varchar | 30 | 1 |  |  |  |
| BillToPhone | varchar | 20 | 1 |  |  |  |
| BillToEmail | varchar | 100 | 1 |  |  |  |
| ShipToFName | varchar | 20 | 1 |  |  |  |
| ShipToLName | varchar | 50 | 1 |  |  |  |
| ShipToAddress1 | varchar | 100 | 1 |  |  |  |
| ShipToAddress2 | varchar | 100 | 1 |  |  |  |
| ShipToCity | varchar | 50 | 1 |  |  |  |
| ShipToState | varchar | 50 | 1 |  |  |  |
| ShipToPostalCode | varchar | 20 | 1 |  |  |  |
| ShipToCountry | varchar | 30 | 1 |  |  |  |
| ShipToPhone | varchar | 20 | 1 |  |  |  |
| ShipToEmail | varchar | 100 | 1 |  |  |  |
| ShippingMethod | varchar | 20 | 1 |  |  |  |
| ShippingAmount | money | 8 | 1 |  |  |  |
| PickTicketFlag | bit | 1 | 1 |  |  |  |

