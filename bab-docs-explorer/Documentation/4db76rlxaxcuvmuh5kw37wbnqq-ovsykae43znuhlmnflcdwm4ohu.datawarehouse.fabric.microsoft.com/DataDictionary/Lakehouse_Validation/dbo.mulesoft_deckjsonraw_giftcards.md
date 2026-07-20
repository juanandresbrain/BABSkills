# dbo.mulesoft_deckjsonraw_giftcards

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| ExternalItemID | varchar | 8000 | 1 |  |  |  |
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
| ProcessingFee | real | 4 | 1 |  |  |  |
| GiftCardType | bigint | 8 | 1 |  |  |  |
| Message | varchar | 8000 | 1 |  |  |  |
| FromEmail | varchar | 8000 | 1 |  |  |  |
| FromName | varchar | 8000 | 1 |  |  |  |
| OrderTransactionIdentifier | bigint | 8 | 1 |  |  |  |
| ToEmail | varchar | 8000 | 1 |  |  |  |
| PaymentError | bit | 1 | 1 |  |  |  |
| PaymentApplied | bit | 1 | 1 |  |  |  |
| Processed | bit | 1 | 1 |  |  |  |
| GiftCardPinNumber | varchar | 8000 | 1 |  |  |  |
| GiftCardNumber | varchar | 8000 | 1 |  |  |  |
| OrderItemID | bigint | 8 | 1 |  |  |  |
| OrderID | bigint | 8 | 1 |  |  |  |
| ToName | varchar | 8000 | 1 |  |  |  |
| DeliveryType | bigint | 8 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1897773818 | bigint | 8 | 0 |  |  |  |
