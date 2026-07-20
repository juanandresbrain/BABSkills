# dbo.az_transactiondestage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SkinType | varchar | 4080 | 1 |  |  |  |
| BasePointsEarned | decimal | 9 | 1 |  |  |  |
| CategoryType | varchar | 4080 | 1 |  |  |  |
| ConsumerGroup | varchar | 4080 | 1 |  |  |  |
| Country | varchar | 4080 | 1 |  |  |  |
| CurrencyType | varchar | 16 | 1 |  |  |  |
| CustomerNumber | varchar | 4080 | 1 |  |  |  |
| Department | varchar | 4080 | 1 |  |  |  |
| EmbroideryType | varchar | 4080 | 1 |  |  |  |
| FulfillmentDate | date | 3 | 1 |  |  |  |
| GroupedTendersCash | decimal | 9 | 1 |  |  |  |
| GroupedTendersCreditDebit | decimal | 9 | 1 |  |  |  |
| GroupedTendersGiftCard | decimal | 9 | 1 |  |  |  |
| GroupedTendersKlarna | decimal | 9 | 1 |  |  |  |
| GroupedTendersPayPal | decimal | 9 | 1 |  |  |  |
| GroupedTendersAmazon | decimal | 9 | 1 |  |  |  |
| inDiscountFacts | bit | 1 | 1 |  |  |  |
| IsBundle | bit | 1 | 1 |  |  |  |
| IsSet | bit | 1 | 1 |  |  |  |
| KeyStory | varchar | 4080 | 1 |  |  |  |
| LicensedOrNot | bit | 1 | 1 |  |  |  |
| LifetimeVisitNumber | decimal | 9 | 1 |  |  |  |
| MSTAT | varchar | 4080 | 1 |  |  |  |
| NetRetailAmountwVAT | decimal | 9 | 1 |  |  |  |
| Occasions | varchar | 4080 | 1 |  |  |  |
| OnlineExclusive | bit | 1 | 1 |  |  |  |
| ProductHierarchyCode | varchar | 4080 | 1 |  |  |  |
| ShippingType | varchar | 4080 | 1 |  |  |  |
| ShippingAmount | decimal | 9 | 1 |  |  |  |
| SKU | varchar | 4080 | 1 |  |  |  |
| SoundEligible | bit | 1 | 1 |  |  |  |
| SportsTeams | varchar | 4080 | 1 |  |  |  |
| StoreConcept | varchar | 4080 | 1 |  |  |  |
| StoreNumber | varchar | 4080 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionID | varchar | 4080 | 1 |  |  |  |
| TransactionLineNumber | decimal | 9 | 1 |  |  |  |
| TransactionMonth | decimal | 5 | 1 |  |  |  |
| TransactionYear | varchar | 320 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 9 | 1 |  |  |  |
| Units | decimal | 9 | 1 |  |  |  |
| UpdatedTransaction | bit | 1 | 1 |  |  |  |
| GroupedTendersAliPay | decimal | 9 | 1 |  |  |  |
| GroupedTendersFacebook | decimal | 9 | 1 |  |  |  |
| GroupedTendersOther | decimal | 9 | 1 |  |  |  |
| GroupedTendersPartyDeposit | decimal | 9 | 1 |  |  |  |
| GroupedTendersPOParty | decimal | 9 | 1 |  |  |  |
| GroupedTendersWeChatPay | decimal | 9 | 1 |  |  |  |
| Class | varchar | 320 | 1 |  |  |  |
| SubClass | varchar | 320 | 1 |  |  |  |
| isBundleOrSet | bit | 1 | 1 |  |  |  |
| OrderReference | varchar | 800 | 1 |  |  |  |
| EmployeeID | int | 4 | 1 |  |  |  |
| GAAPSalesAmount | decimal | 17 | 1 |  |  |  |
| MatchedByEmail | varchar | 320 | 1 |  |  |  |
| isWebGift | int | 4 | 1 |  |  |  |
