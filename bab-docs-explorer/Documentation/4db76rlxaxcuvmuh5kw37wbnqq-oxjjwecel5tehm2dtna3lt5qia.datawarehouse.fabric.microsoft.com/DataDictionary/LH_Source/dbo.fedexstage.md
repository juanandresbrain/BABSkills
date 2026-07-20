# dbo.fedexstage

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PayerAccount | varchar | 8000 | 1 |  |  |  |
| NationalAccount | varchar | 8000 | 1 |  |  |  |
| NationalSubGroup | varchar | 8000 | 1 |  |  |  |
| InvoiceMonth_yyyymm | varchar | 8000 | 1 |  |  |  |
| OPCO | varchar | 8000 | 1 |  |  |  |
| ServiceType | varchar | 8000 | 1 |  |  |  |
| ServiceDescription | varchar | 8000 | 1 |  |  |  |
| PayType | varchar | 8000 | 1 |  |  |  |
| ShipmentDate_mmddyyyy | varchar | 8000 | 1 |  |  |  |
| ShipmentDeliveryDate_mmddyyyy | varchar | 8000 | 1 |  |  |  |
| ShipmentTrackingNumber | varchar | 8000 | 1 |  |  |  |
| ShipperName | varchar | 8000 | 1 |  |  |  |
| ShipperCompanyName | varchar | 8000 | 1 |  |  |  |
| ShipperAddress | varchar | 8000 | 1 |  |  |  |
| ShipperCity | varchar | 8000 | 1 |  |  |  |
| ShipperStateProvince | varchar | 8000 | 1 |  |  |  |
| ShipperCountryTerritory | varchar | 8000 | 1 |  |  |  |
| ShipperPostalCode | varchar | 8000 | 1 |  |  |  |
| ShipmentFreightChargeAmountUSD | varchar | 8000 | 1 |  |  |  |
| ShipmentMiscellaneousChargeUSD | varchar | 8000 | 1 |  |  |  |
| ShipmentDutyandTaxChargeUSD | varchar | 8000 | 1 |  |  |  |
| ShipmentDiscountAmountUSD | varchar | 8000 | 1 |  |  |  |
| NetChargeAmountUSD | varchar | 8000 | 1 |  |  |  |
| PiecesinShipment | varchar | 8000 | 1 |  |  |  |
| ShipmentRatedWeight_Pounds | varchar | 8000 | 1 |  |  |  |
| OriginalWeight_Pounds | varchar | 8000 | 1 |  |  |  |
| ProofofDeliveryRecipient | varchar | 8000 | 1 |  |  |  |
| RecipientName | varchar | 8000 | 1 |  |  |  |
| RecipientCompanyName | varchar | 8000 | 1 |  |  |  |
| RecipientAddress | varchar | 8000 | 1 |  |  |  |
| RecipientCity | varchar | 8000 | 1 |  |  |  |
| RecipientStateProvince | varchar | 8000 | 1 |  |  |  |
| RecipientCountryTerritory | varchar | 8000 | 1 |  |  |  |
| RecipientPostalCode | varchar | 8000 | 1 |  |  |  |
| ReferenceNotesLine1 | varchar | 8000 | 1 |  |  |  |
| ReferenceNotesLine2 | varchar | 8000 | 1 |  |  |  |
| ReferenceNotesLine3 | varchar | 8000 | 1 |  |  |  |
| DepartmentNumber | varchar | 8000 | 1 |  |  |  |
| PONumber | varchar | 8000 | 1 |  |  |  |
| PricingZone | varchar | 8000 | 1 |  |  |  |
| ShipmentDIMFlag_YorN | varchar | 8000 | 1 |  |  |  |
| DimmedHeight_in | varchar | 8000 | 1 |  |  |  |
| DimmedWidth_in | varchar | 8000 | 1 |  |  |  |
| DimmedLength_in | varchar | 8000 | 1 |  |  |  |
| RecipientOriginalAddress | varchar | 8000 | 1 |  |  |  |
| RecipientOriginalCity | varchar | 8000 | 1 |  |  |  |
| RecipientOriginalStateProvince | varchar | 8000 | 1 |  |  |  |
| RecipientOriginalPostalCode | varchar | 8000 | 1 |  |  |  |
| RecipientOriginalCountryTerritory | varchar | 8000 | 1 |  |  |  |
| ShipmentDeclaredValueAmount | varchar | 8000 | 1 |  |  |  |
| CustomsValue | varchar | 8000 | 1 |  |  |  |
| CustomsValueCurrencyCode | varchar | 8000 | 1 |  |  |  |
| InvoiceDate_mmddyyyy | varchar | 8000 | 1 |  |  |  |
| InvoiceNumber | varchar | 8000 | 1 |  |  |  |
| MasterTrackingNumber | varchar | 8000 | 1 |  |  |  |
| DomesticIntl | varchar | 8000 | 1 |  |  |  |
| PackageType | varchar | 8000 | 1 |  |  |  |
| ShipmentDeliveryTime_24Hours | varchar | 8000 | 1 |  |  |  |
| FileName | varchar | 8000 | 1 |  |  |  |
