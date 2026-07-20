# dbo.customermasterdestage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customerNumber | varchar | 8000 | 1 |  |  |  |
| SubscriberKey | varchar | 8000 | 1 |  |  |  |
| status | varchar | 8000 | 1 |  |  |  |
| LastSentDate | datetime2 | 8 | 1 |  |  |  |
| LastOpenDate | datetime2 | 8 | 1 |  |  |  |
| LastClickDate | datetime2 | 8 | 1 |  |  |  |
| bonusClubMember | int | 4 | 1 |  |  |  |
| bonusClubMembershipType | varchar | 8000 | 1 |  |  |  |
| bonusClubPointsBalance | int | 4 | 1 |  |  |  |
| bonusClubStartDate | datetime2 | 8 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| bonusClubSignUpSource | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| FrequencyCount3m | int | 4 | 1 |  |  |  |
| FrequencyCount6m | int | 4 | 1 |  |  |  |
| FrequencyCount12m | int | 4 | 1 |  |  |  |
| FrequencyCount18m | int | 4 | 1 |  |  |  |
| FrequencyCount24m | int | 4 | 1 |  |  |  |
| FrequencyCountTTL | int | 4 | 1 |  |  |  |
| RecencyCount3m | int | 4 | 1 |  |  |  |
| RecencyCount6m | int | 4 | 1 |  |  |  |
| RecencyCount12m | int | 4 | 1 |  |  |  |
| RecencyCount18m | int | 4 | 1 |  |  |  |
| RecencyCount24m | int | 4 | 1 |  |  |  |
| RecencyCountTTL | int | 4 | 1 |  |  |  |
| MonetarySum3m | decimal | 17 | 1 |  |  |  |
| MonetarySum6m | decimal | 17 | 1 |  |  |  |
| MonetarySum12m | decimal | 17 | 1 |  |  |  |
| MonetarySum18m | decimal | 17 | 1 |  |  |  |
| MonetarySum24m | decimal | 17 | 1 |  |  |  |
| MonetarySumTTL | decimal | 17 | 1 |  |  |  |
| FrequencyCount1m | int | 4 | 1 |  |  |  |
| RecencyCount1m | int | 4 | 1 |  |  |  |
| MonetarySum1m | decimal | 17 | 1 |  |  |  |
| address_1 | varchar | 8000 | 1 |  |  |  |
| address_2 | varchar | 8000 | 1 |  |  |  |
| address_3 | varchar | 8000 | 1 |  |  |  |
| address_4 | varchar | 8000 | 1 |  |  |  |
| post_code | varchar | 8000 | 1 |  |  |  |
| mobile | varchar | 8000 | 1 |  |  |  |
| locale | varchar | 8000 | 1 |  |  |  |
| text_opt_in | int | 4 | 1 |  |  |  |
| DWInsertDate | datetime2 | 8 | 1 |  |  |  |
| DWUpdateDate | datetime2 | 8 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| LastTransactionDate | date | 3 | 1 |  |  |  |
| LastTransactionStore | varchar | 8000 | 1 |  |  |  |
| PreferredStory | varchar | 8000 | 1 |  |  |  |
| Emailable | int | 4 | 1 |  |  |  |
| EmailOptInDate | datetime2 | 8 | 1 |  |  |  |
| FrequencyCount36m | int | 4 | 1 |  |  |  |
| RecencyCount36m | int | 4 | 1 |  |  |  |
| MonetarySum36m | decimal | 17 | 1 |  |  |  |
| LifetimePoints | int | 4 | 1 |  |  |  |
| FirstTransactionDate | datetime2 | 8 | 1 |  |  |  |
| FirstStoreConcept | varchar | 8000 | 1 |  |  |  |
| FirstName | varchar | 8000 | 1 |  |  |  |
| LastName | varchar | 8000 | 1 |  |  |  |
| DWUpdateDateRecency | datetime2 | 8 | 1 |  |  |  |
| MembershipPlan | varchar | 8000 | 1 |  |  |  |
