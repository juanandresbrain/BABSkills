# Loyalty.TransactionDE

**Database:** IntegrationStaging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SkinType | varchar | -1 | 1 |  |  |  |
| BasePointsEarned | decimal | 9 | 1 |  |  |  |
| CategoryType | varchar | -1 | 1 |  |  |  |
| ConsumerGroup | varchar | -1 | 1 |  |  |  |
| Country | varchar | -1 | 1 |  |  |  |
| CurrencyType | varchar | -1 | 1 |  |  |  |
| CustomerNumber | varchar | -1 | 1 |  |  |  |
| Department | varchar | -1 | 1 |  |  |  |
| EmbroideryType | varchar | -1 | 1 |  |  |  |
| FulfillmentDate | date | 3 | 1 |  |  |  |
| GroupedTendersCash | decimal | 9 | 1 |  |  |  |
| GroupedTendersCredit/Debit | decimal | 9 | 1 |  |  |  |
| GroupedTendersGiftCard | decimal | 9 | 1 |  |  |  |
| GroupedTendersKlarna | decimal | 9 | 1 |  |  |  |
| GroupedTendersPayPal | decimal | 9 | 1 |  |  |  |
| GroupedTendersAmazon | decimal | 9 | 1 |  |  |  |
| inDiscountFacts | bit | 1 | 1 |  |  |  |
| IsBundle | bit | 1 | 1 |  |  |  |
| IsSet | bit | 1 | 1 |  |  |  |
| KeyStory | varchar | -1 | 1 |  |  |  |
| LicensedOrNot | bit | 1 | 1 |  |  |  |
| LifetimeVisitNumber | decimal | 9 | 1 |  |  |  |
| MSTAT | varchar | -1 | 1 |  |  |  |
| NetRetailAmountwVAT | decimal | 9 | 1 |  |  |  |
| Occasions | varchar | -1 | 1 |  |  |  |
| OnlineExclusive | bit | 1 | 1 |  |  |  |
| ProductHierarchyCode | varchar | -1 | 1 |  |  |  |
| ShippingType | varchar | -1 | 1 |  |  |  |
| ShippingAmount | decimal | 9 | 1 |  |  |  |
| SKU | varchar | -1 | 1 |  |  |  |
| SoundEligible | bit | 1 | 1 |  |  |  |
| SportsTeams | varchar | -1 | 1 |  |  |  |
| StoreConcept | varchar | -1 | 1 |  |  |  |
| StoreNumber | varchar | -1 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionID | varchar | -1 | 1 |  |  |  |
| TransactionLineNumber | decimal | 9 | 1 |  |  |  |
| TransactionMonth | decimal | 5 | 1 |  |  |  |
| TransactionYear | varchar | -1 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 9 | 1 |  |  |  |
| Units | decimal | 9 | 1 |  |  |  |
| UpdatedTransaction | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| GroupedTendersAliPay | decimal | 9 | 1 |  |  |  |
| GroupedTendersFacebook | decimal | 9 | 1 |  |  |  |
| GroupedTendersOther | decimal | 9 | 1 |  |  |  |
| GroupedTendersPartyDeposit | decimal | 9 | 1 |  |  |  |
| GroupedTendersPOParty | decimal | 9 | 1 |  |  |  |
| GroupedTendersWeChatPay | decimal | 9 | 1 |  |  |  |
| Class | varchar | -1 | 1 |  |  |  |
| SubClass | varchar | -1 | 1 |  |  |  |
| isBundleOrSet | bit | 1 | 1 |  |  |  |
| NetRetailAmountwVATorig | decimal | 9 | 1 |  |  |  |
| BasePointsEarnedOrig | decimal | 9 | 1 |  |  |  |
| BasePointsUpdatedCount | decimal | 5 | 1 |  |  |  |
| BasePointsEarnedDelta | decimal | 9 | 1 |  |  |  |
| BasePointsEarnedPrevious | decimal | 9 | 1 |  |  |  |
| NetRetailAmountwVATdelta | decimal | 9 | 1 |  |  |  |
| NetRetailAmountwVATprevious | decimal | 9 | 1 |  |  |  |
| Id | int | 4 | 0 |  |  |  |
| OrderReference | varchar | -1 | 1 |  |  |  |
| EmployeeID | int | 4 | 1 |  |  |  |
| ExternalID | varchar | -1 | 1 |  |  |  |
| MatchedByEMail | varchar | -1 | 1 |  |  |  |
| GAAPSalesAmount | decimal | 17 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
