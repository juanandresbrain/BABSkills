# dbo.tmpTaxSummaryResults2

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProcessCode | varchar | 1 | 1 |  |  |  |
| DocCode | varchar | 50 | 1 |  |  |  |
| DocType | varchar | 1 | 1 |  |  |  |
| DocDate | varchar | 30 | 1 |  |  |  |
| CompanyCode | varchar | 50 | 1 |  |  |  |
| CustomerCode | int | 4 | 1 |  |  |  |
| EntityUseCode | varchar | 1 | 1 |  |  |  |
| LineNo | bigint | 8 | 1 |  |  |  |
| TaxCode | varchar | 50 | 1 |  |  |  |
| TaxDate | varchar | 1 | 1 |  |  |  |
| ItemCode | varchar | 1 | 1 |  |  |  |
| Description | varchar | 1 | 1 |  |  |  |
| Qty | varchar | 2 | 1 |  |  |  |
| Amount | numeric | 17 | 1 |  |  |  |
| Discount | varchar | 1 | 1 |  |  |  |
| Ref1 | varchar | 1 | 1 |  |  |  |
| Ref2 | varchar | 1 | 1 |  |  |  |
| ExemptionNo | varchar | 1 | 1 |  |  |  |
| RevAcct | varchar | 1 | 1 |  |  |  |
| DestAddress | varchar | 150 | 1 |  |  |  |
| DestCity | varchar | 50 | 1 |  |  |  |
| DestRegion | nvarchar | 4 | 1 |  |  |  |
| DestPostalCode | varchar | 50 | 1 |  |  |  |
| DestCountry | varchar | 50 | 1 |  |  |  |
| OrigAddress | varchar | 255 | 1 |  |  |  |
| OrigCity | varchar | 50 | 1 |  |  |  |
| OrigRegion | varchar | 2 | 1 |  |  |  |
| OrigPostalCode | varchar | 50 | 1 |  |  |  |
| OrigCountry | varchar | 1 | 1 |  |  |  |
| LocationCode | int | 4 | 1 |  |  |  |
| SalesPersonCode | varchar | 1 | 1 |  |  |  |
| PurchaseOrderNo | varchar | 1 | 1 |  |  |  |
| CurrencyCode | varchar | 1 | 1 |  |  |  |
| ExchangeRate | varchar | 1 | 1 |  |  |  |
| ExchangeRateEffDate | varchar | 1 | 1 |  |  |  |
| PaymentDate | varchar | 1 | 1 |  |  |  |
| TaxIncluded | varchar | 1 | 1 |  |  |  |
| DestTaxRegion | varchar | 1 | 1 |  |  |  |
| OrigTaxRegion | varchar | 1 | 1 |  |  |  |
| Taxable | varchar | 1 | 1 |  |  |  |
| TaxType | varchar | 1 | 1 |  |  |  |
| TotalTax | numeric | 17 | 1 |  |  |  |
| CountryName | varchar | 1 | 1 |  |  |  |
| CountryCode | varchar | 1 | 1 |  |  |  |
| CountryRate | varchar | 1 | 1 |  |  |  |
| CountryTax | varchar | 1 | 1 |  |  |  |
| StateName | varchar | 1 | 1 |  |  |  |
| StateCode | varchar | 1 | 1 |  |  |  |
| StateRate | varchar | 1 | 1 |  |  |  |
| StateTax | varchar | 1 | 1 |  |  |  |
| CountyName | varchar | 1 | 1 |  |  |  |
| CountyCode | varchar | 1 | 1 |  |  |  |
| CountyRate | varchar | 1 | 1 |  |  |  |
| CountyTax | varchar | 1 | 1 |  |  |  |
| CityName | varchar | 1 | 1 |  |  |  |
| CityCode | varchar | 1 | 1 |  |  |  |
| CityRate | varchar | 1 | 1 |  |  |  |
| CityTax | varchar | 1 | 1 |  |  |  |
| Other1Name | varchar | 1 | 1 |  |  |  |
| Other1Code | varchar | 1 | 1 |  |  |  |
| Other1Rate | varchar | 1 | 1 |  |  |  |
| Other1Tax | varchar | 1 | 1 |  |  |  |
| Other2Name | varchar | 1 | 1 |  |  |  |
| Other2Code | varchar | 1 | 1 |  |  |  |
| Other2Rate | varchar | 1 | 1 |  |  |  |
| Other2Tax | varchar | 1 | 1 |  |  |  |
| Other3Name | varchar | 1 | 1 |  |  |  |
| Other3Code | varchar | 1 | 1 |  |  |  |
| Other3Rate | varchar | 1 | 1 |  |  |  |
| Other3Tax | varchar | 1 | 1 |  |  |  |
| Other4Name | varchar | 1 | 1 |  |  |  |
| Other4Code | varchar | 1 | 1 |  |  |  |
| Other4Rate | varchar | 1 | 1 |  |  |  |
| Other4Tax | varchar | 1 | 1 |  |  |  |
| ReferenceCode | varchar | 1 | 1 |  |  |  |
| BuyersVATNo | varchar | 1 | 1 |  |  |  |
| IsSellerImporterOfRecord | varchar | 1 | 1 |  |  |  |
| BRBuyerType | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExemptOrCannotWH_IRRF | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExemptOrCannotWH_PISRF | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExemptOrCannotWH_COFINSRF | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExemptOrCannotWH_CSLLRF | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExempt_PIS | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExempt_COFINS | varchar | 1 | 1 |  |  |  |
| BRBuyer_IsExempt_CSLL | varchar | 1 | 1 |  |  |  |
| Header_Description | varchar | 1 | 1 |  |  |  |
| Email | varchar | 1 | 1 |  |  |  |
| StrCountry | varchar | 3 | 1 |  |  |  |
