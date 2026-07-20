# dbo.weborderprocessing_wm_orders

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderId | int | 4 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  |  |  |
| OrderNum | varchar | 8000 | 1 |  |  |  |
| EnterpriseSellingID | varchar | 8000 | 1 |  |  |  |
| OrderDate | datetime2 | 8 | 1 |  |  |  |
| OrderStatus | varchar | 8000 | 1 |  |  |  |
| OrderType | varchar | 8000 | 1 |  |  |  |
| PickupStore | varchar | 8000 | 1 |  |  |  |
| OrderAuthentication | varchar | 8000 | 1 |  |  |  |
| SourceSite | varchar | 8000 | 1 |  |  |  |
| BatchNo | int | 4 | 1 |  |  |  |
| SequenceNo | int | 4 | 1 |  |  |  |
| DatePrinted | datetime2 | 8 | 1 |  |  |  |
| HouseOrder | bit | 1 | 1 |  |  |  |
| HouseOrderReason | varchar | 8000 | 1 |  |  |  |
| GiftSender | varchar | 8000 | 1 |  |  |  |
| GiftMessage | varchar | 8000 | 1 |  |  |  |
| SpecialInstructions | varchar | 8000 | 1 |  |  |  |
| ServiceRep | varchar | 8000 | 1 |  |  |  |
| BillToFName | varchar | 8000 | 1 |  |  |  |
| BillToLName | varchar | 8000 | 1 |  |  |  |
| BillToAddress1 | varchar | 8000 | 1 |  |  |  |
| BillToAddress2 | varchar | 8000 | 1 |  |  |  |
| BillToCity | varchar | 8000 | 1 |  |  |  |
| BillToState | varchar | 8000 | 1 |  |  |  |
| BillToPostalCode | varchar | 8000 | 1 |  |  |  |
| BillToCountry | varchar | 8000 | 1 |  |  |  |
| BillToPhone | varchar | 8000 | 1 |  |  |  |
| BillToEmail | varchar | 8000 | 1 |  |  |  |
| ShipToFName | varchar | 8000 | 1 |  |  |  |
| ShipToLName | varchar | 8000 | 1 |  |  |  |
| ShipToAddress1 | varchar | 8000 | 1 |  |  |  |
| ShipToAddress2 | varchar | 8000 | 1 |  |  |  |
| ShipToCity | varchar | 8000 | 1 |  |  |  |
| ShipToState | varchar | 8000 | 1 |  |  |  |
| ShipToPostalCode | varchar | 8000 | 1 |  |  |  |
| ShipToCountry | varchar | 8000 | 1 |  |  |  |
| ShipToPhone | varchar | 8000 | 1 |  |  |  |
| ShipToEmail | varchar | 8000 | 1 |  |  |  |
| ShippingAmount | decimal | 9 | 1 |  |  |  |
| ShippingMethod | varchar | 8000 | 1 |  |  |  |
| PickTicketFlag | bit | 1 | 1 |  |  |  |
| OrderNumber | varchar | 8000 | 1 |  |  |  |
| ShipmentNumber | varchar | 8000 | 1 |  |  |  |
