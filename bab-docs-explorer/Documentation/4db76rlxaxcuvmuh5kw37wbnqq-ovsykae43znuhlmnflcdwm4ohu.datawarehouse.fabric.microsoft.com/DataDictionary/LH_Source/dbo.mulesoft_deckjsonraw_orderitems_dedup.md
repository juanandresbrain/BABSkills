# dbo.mulesoft_deckjsonraw_orderitems_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| TaxCode | varchar | 8000 | 1 |  |  |  |
| GetItemExtendedHash | varchar | 8000 | 1 |  |  |  |
| ItemTypeID | bigint | 8 | 1 |  |  |  |
| EstimatedShipDate | varchar | 8000 | 1 |  |  |  |
| EndEstimatedShipDate | varchar | 8000 | 1 |  |  |  |
| ItemStatusChangeDate | datetime2 | 8 | 1 |  |  |  |
| ProcessOnDateUTC | varchar | 8000 | 1 |  |  |  |
| RequestedDeliveryDateUTC | varchar | 8000 | 1 |  |  |  |
| CustomerSKU | varchar | 8000 | 1 |  |  |  |
| ReturnAuthNumber | varchar | 8000 | 1 |  |  |  |
| GiftMessage | varchar | 8000 | 1 |  |  |  |
| AlternateStyle | varchar | 8000 | 1 |  |  |  |
| ReturnTypeID | varchar | 8000 | 1 |  |  |  |
| ReturnReasonID | varchar | 8000 | 1 |  |  |  |
| ReturnReasonText | varchar | 8000 | 1 |  |  |  |
| ShippingErrorID | varchar | 8000 | 1 |  |  |  |
| ShippingProblemID | varchar | 8000 | 1 |  |  |  |
| SendReplacement | bit | 1 | 1 |  |  |  |
| IsExpectingPayment | bit | 1 | 1 |  |  |  |
| IsExpectingReturn | bit | 1 | 1 |  |  |  |
| IsChanged | bit | 1 | 1 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| ExternalItemID | varchar | 8000 | 1 |  |  |  |
| OrderID | bigint | 8 | 1 |  |  |  |
| ItemStatusID | bigint | 8 | 1 |  |  |  |
| ItemStatusName | varchar | 8000 | 1 |  |  |  |
| ItemStatusCode | varchar | 8000 | 1 |  |  |  |
| ItemTypeLocalizeName | varchar | 8000 | 1 |  |  |  |
| GTIN | varchar | 8000 | 1 |  |  |  |
| DeckSKU | varchar | 8000 | 1 |  |  |  |
| StyleNumber | varchar | 8000 | 1 |  |  |  |
| MasterNumber | varchar | 8000 | 1 |  |  |  |
| ProductSize | varchar | 8000 | 1 |  |  |  |
| Attribute | varchar | 8000 | 1 |  |  |  |
| NewRoutingID | bigint | 8 | 1 |  |  |  |
| RoutingID | bigint | 8 | 1 |  |  |  |
| Route | varchar | 8000 | 1 |  |  |  |
| WarehouseCode | varchar | 8000 | 1 |  |  |  |
| WarehousePostalCode | varchar | 8000 | 1 |  |  |  |
| GrossPrice | real | 4 | 1 |  |  |  |
| NetPrice | real | 4 | 1 |  |  |  |
| Custom1 | varchar | 8000 | 1 |  |  |  |
| Custom2 | varchar | 8000 | 1 |  |  |  |
| Custom3 | varchar | 8000 | 1 |  |  |  |
| Custom4 | varchar | 8000 | 1 |  |  |  |
| Custom5 | varchar | 8000 | 1 |  |  |  |
| ImageURL | varchar | 8000 | 1 |  |  |  |
| MSRP | real | 4 | 1 |  |  |  |
| OrderShippingID | bigint | 8 | 1 |  |  |  |
| ShippingReferenceID | bigint | 8 | 1 |  |  |  |
| DeliveryType | bigint | 8 | 1 |  |  |  |
| MarketingPrice | varchar | 8000 | 1 |  |  |  |
| MarketingText | varchar | 8000 | 1 |  |  |  |
| TotalNonAdvancedGrossAdjustments | real | 4 | 1 |  |  |  |
| TotalGrossAdjustments | real | 4 | 1 |  |  |  |
| TotalNonAdvancedNetAdjustments | real | 4 | 1 |  |  |  |
| TotalNetAdjustments | real | 4 | 1 |  |  |  |
| TaxExempt | bit | 1 | 1 |  |  |  |
| TaxExemptStringList | varchar | 8000 | 1 |  |  |  |
| ShippingMethodID | bigint | 8 | 1 |  |  |  |
| ShippingMethodDescription | varchar | 8000 | 1 |  |  |  |
| PaymentID | bigint | 8 | 1 |  |  |  |
| InitialItemStatusID | bigint | 8 | 1 |  |  |  |
| Returnable | bit | 1 | 1 |  |  |  |
| EstimatedDeliveryDateUTC | varchar | 8000 | 1 |  |  |  |
| EndEstimatedDeliveryDateUTC | varchar | 8000 | 1 |  |  |  |
| PickupNode | varchar | 8000 | 1 |  |  |  |
| PickupNodeCode | varchar | 8000 | 1 |  |  |  |
| CancelReasonCode | varchar | 8000 | 1 |  |  |  |
| CancelReasonText | varchar | 8000 | 1 |  |  |  |
| Brand | varchar | 8000 | 1 |  |  |  |
| Cost | varchar | 8000 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
