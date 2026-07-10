# dbo.TransactionDEStage_Staging

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SkinType | nvarchar | 510 | 1 |  |  |  |
| BasePointsEarned | numeric | 9 | 1 |  |  |  |
| CategoryType | nvarchar | 510 | 1 |  |  |  |
| ConsumerGroup | nvarchar | 510 | 1 |  |  |  |
| Country | nvarchar | 510 | 1 |  |  |  |
| CurrencyType | nvarchar | 8 | 1 |  |  |  |
| CustomerNumber | nvarchar | 510 | 1 |  |  |  |
| Department | nvarchar | 510 | 1 |  |  |  |
| EmbroideryType | nvarchar | 510 | 1 |  |  |  |
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
| KeyStory | nvarchar | 510 | 1 |  |  |  |
| LicensedOrNot | bit | 1 | 1 |  |  |  |
| LifetimeVisitNumber | numeric | 9 | 1 |  |  |  |
| MSTAT | nvarchar | 510 | 1 |  |  |  |
| NetRetailAmountwVAT | decimal | 9 | 1 |  |  |  |
| Occasions | nvarchar | 510 | 1 |  |  |  |
| OnlineExclusive | bit | 1 | 1 |  |  |  |
| ProductHierarchyCode | nvarchar | 510 | 1 |  |  |  |
| ShippingType | nvarchar | 510 | 1 |  |  |  |
| ShippingAmount | decimal | 9 | 1 |  |  |  |
| SKU | nvarchar | 510 | 1 |  |  |  |
| SoundEligible | bit | 1 | 1 |  |  |  |
| SportsTeams | nvarchar | 510 | 1 |  |  |  |
| StoreConcept | nvarchar | 510 | 1 |  |  |  |
| StoreNumber | nvarchar | 510 | 1 |  |  |  |
| TransactionDate | date | 3 | 1 |  |  |  |
| TransactionID | nvarchar | 510 | 1 |  |  |  |
| TransactionLineNumber | numeric | 9 | 1 |  |  |  |
| TransactionMonth | numeric | 5 | 1 |  |  |  |
| TransactionYear | nvarchar | 40 | 1 |  |  |  |
| UnitDiscountAmount | decimal | 9 | 1 |  |  |  |
| Units | numeric | 9 | 1 |  |  |  |
| UpdatedTransaction | bit | 1 | 1 |  |  |  |
| GroupedTendersAliPay | decimal | 9 | 1 |  |  |  |
| GroupedTendersFacebook | decimal | 9 | 1 |  |  |  |
| GroupedTendersOther | decimal | 9 | 1 |  |  |  |
| GroupedTendersPartyDeposit | decimal | 9 | 1 |  |  |  |
| GroupedTendersPOParty | decimal | 9 | 1 |  |  |  |
| GroupedTendersWeChatPay | decimal | 9 | 1 |  |  |  |
| Class | varchar | 20 | 1 |  |  |  |
| SubClass | varchar | 20 | 1 |  |  |  |
| isBundleOrSet | bit | 1 | 1 |  |  |  |
| OrderReference | varchar | 50 | 1 |  |  |  |
| EmployeeID | int | 4 | 1 |  |  |  |
