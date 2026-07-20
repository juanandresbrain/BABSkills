# dbo.mulesoft_deckjsonraw_ordershipments

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| SubTotal | real | 4 | 1 |  |  |  |
| OriginalShipping | real | 4 | 1 |  |  |  |
| Shipping | real | 4 | 1 |  |  |  |
| Discount | real | 4 | 1 |  |  |  |
| Tax | real | 4 | 1 |  |  |  |
| Total | real | 4 | 1 |  |  |  |
| ProcessingFee | real | 4 | 1 |  |  |  |
| TrackingNumber | varchar | 8000 | 1 |  |  |  |
| OrderShipmentID | bigint | 8 | 1 |  |  |  |
| OrderID | bigint | 8 | 1 |  |  |  |
| Shipped | bit | 1 | 1 |  |  |  |
| DateShipped | datetime2 | 8 | 1 |  |  |  |
| SendEmailWhenShipped | bit | 1 | 1 |  |  |  |
| ShippingMethodID | bigint | 8 | 1 |  |  |  |
| ShippingMethod | varchar | 8000 | 1 |  |  |  |
| ShippingAddressID | bigint | 8 | 1 |  |  |  |
| GroupedShipmentItems | varchar | 8000 | 1 |  |  |  |
| OrderTransactionIdentifier | bigint | 8 | 1 |  |  |  |
| WarehouseCountNumber | bigint | 8 | 1 |  |  |  |
| PaymentApplied | bit | 1 | 1 |  |  |  |
| PaymentError | bit | 1 | 1 |  |  |  |
| PaymentPending | bit | 1 | 1 |  |  |  |
| PODate | datetime2 | 8 | 1 |  |  |  |
| PONumber | varchar | 8000 | 1 |  |  |  |
| InternalSalesNumber | varchar | 8000 | 1 |  |  |  |
| InternalStatusCode | varchar | 8000 | 1 |  |  |  |
| WarehouseID | bigint | 8 | 1 |  |  |  |
| PaymentSkipped | bit | 1 | 1 |  |  |  |
| PathToShippingLabel | varchar | 8000 | 1 |  |  |  |
| PathToReturnShippingLabel | varchar | 8000 | 1 |  |  |  |
| MerchandiseNetTotal | real | 4 | 1 |  |  |  |
| MerchandiseGrossTotal | real | 4 | 1 |  |  |  |
| AdjustedMerchandiseNetTotal | real | 4 | 1 |  |  |  |
| AdjustedMerchandiseGrossTotal | real | 4 | 1 |  |  |  |
| ShippingNetTotal | real | 4 | 1 |  |  |  |
| ShippingGrossTotal | real | 4 | 1 |  |  |  |
| AdjustedShippingNetTotal | real | 4 | 1 |  |  |  |
| AdjustedShippingGrossTotal | real | 4 | 1 |  |  |  |
| TotalNetTotal | real | 4 | 1 |  |  |  |
| TotalGrossTotal | real | 4 | 1 |  |  |  |
| ProcessingFee1 | real | 4 | 1 |  |  |  |
| InvoiceNumber | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1769773362 | bigint | 8 | 0 |  |  |  |
