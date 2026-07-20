# MulesoftTest.DeckJsonRaw_OrderItems

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| TaxCode | varchar | -1 | 1 |  |  |  |
| GetItemExtendedHash | varchar | -1 | 1 |  |  |  |
| ItemTypeID | bigint | 8 | 1 |  |  |  |
| EstimatedShipDate | varchar | -1 | 1 |  |  |  |
| EndEstimatedShipDate | varchar | -1 | 1 |  |  |  |
| ItemStatusChangeDate | datetime2 | 8 | 1 |  |  |  |
| ProcessOnDateUTC | varchar | -1 | 1 |  |  |  |
| RequestedDeliveryDateUTC | varchar | -1 | 1 |  |  |  |
| CustomerSKU | varchar | -1 | 1 |  |  |  |
| ReturnAuthNumber | varchar | -1 | 1 |  |  |  |
| GiftMessage | varchar | -1 | 1 |  |  |  |
| AlternateStyle | varchar | -1 | 1 |  |  |  |
| ReturnTypeID | varchar | -1 | 1 |  |  |  |
| ReturnReasonID | varchar | -1 | 1 |  |  |  |
| ReturnReasonText | varchar | -1 | 1 |  |  |  |
| ShippingErrorID | varchar | -1 | 1 |  |  |  |
| ShippingProblemID | varchar | -1 | 1 |  |  |  |
| SendReplacement | bit | 1 | 1 |  |  |  |
| IsExpectingPayment | bit | 1 | 1 |  |  |  |
| IsExpectingReturn | bit | 1 | 1 |  |  |  |
| IsChanged | bit | 1 | 1 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| ExternalItemID | varchar | -1 | 1 |  |  |  |
| OrderID | bigint | 8 | 1 |  |  |  |
| ItemStatusID | bigint | 8 | 1 |  |  |  |
| ItemStatusName | varchar | -1 | 1 |  |  |  |
| ItemStatusCode | varchar | -1 | 1 |  |  |  |
| ItemTypeLocalizeName | varchar | -1 | 1 |  |  |  |
| GTIN | varchar | -1 | 1 |  |  |  |
| DeckSKU | varchar | -1 | 1 |  |  |  |
| StyleNumber | varchar | -1 | 1 |  |  |  |
| MasterNumber | varchar | -1 | 1 |  |  |  |
| ProductSize | varchar | -1 | 1 |  |  |  |
| Attribute | varchar | -1 | 1 |  |  |  |
| NewRoutingID | bigint | 8 | 1 |  |  |  |
| RoutingID | bigint | 8 | 1 |  |  |  |
| Route | varchar | -1 | 1 |  |  |  |
| WarehouseCode | varchar | -1 | 1 |  |  |  |
| WarehousePostalCode | varchar | -1 | 1 |  |  |  |
| GrossPrice | real | 4 | 1 |  |  |  |
| NetPrice | real | 4 | 1 |  |  |  |
| Custom1 | varchar | -1 | 1 |  |  |  |
| Custom2 | varchar | -1 | 1 |  |  |  |
| Custom3 | varchar | -1 | 1 |  |  |  |
| Custom4 | varchar | -1 | 1 |  |  |  |
| Custom5 | varchar | -1 | 1 |  |  |  |
| ImageURL | varchar | -1 | 1 |  |  |  |
| MSRP | real | 4 | 1 |  |  |  |
| OrderShippingID | bigint | 8 | 1 |  |  |  |
| ShippingReferenceID | bigint | 8 | 1 |  |  |  |
| DeliveryType | bigint | 8 | 1 |  |  |  |
| MarketingPrice | varchar | -1 | 1 |  |  |  |
| MarketingText | varchar | -1 | 1 |  |  |  |
| TotalNonAdvancedGrossAdjustments | real | 4 | 1 |  |  |  |
| TotalGrossAdjustments | real | 4 | 1 |  |  |  |
| TotalNonAdvancedNetAdjustments | real | 4 | 1 |  |  |  |
| TotalNetAdjustments | real | 4 | 1 |  |  |  |
| TaxExempt | bit | 1 | 1 |  |  |  |
| TaxExemptStringList | varchar | -1 | 1 |  |  |  |
| ShippingMethodID | bigint | 8 | 1 |  |  |  |
| ShippingMethodDescription | varchar | -1 | 1 |  |  |  |
| PaymentID | bigint | 8 | 1 |  |  |  |
| InitialItemStatusID | bigint | 8 | 1 |  |  |  |
| Returnable | bit | 1 | 1 |  |  |  |
| EstimatedDeliveryDateUTC | varchar | -1 | 1 |  |  |  |
| EndEstimatedDeliveryDateUTC | varchar | -1 | 1 |  |  |  |
| PickupNode | varchar | -1 | 1 |  |  |  |
| PickupNodeCode | varchar | -1 | 1 |  |  |  |
| CancelReasonCode | varchar | -1 | 1 |  |  |  |
| CancelReasonText | varchar | -1 | 1 |  |  |  |
| Brand | varchar | -1 | 1 |  |  |  |
| Cost | varchar | -1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1817773533 | bigint | 8 | 0 |  |  |  |
