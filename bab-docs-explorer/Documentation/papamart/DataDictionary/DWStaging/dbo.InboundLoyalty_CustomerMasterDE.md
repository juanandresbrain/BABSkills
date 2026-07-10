# dbo.InboundLoyalty_CustomerMasterDE

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customerNumber | varchar | 20 | 0 |  |  |  |
| SubscriberKey | nvarchar | 510 | 1 |  |  |  |
| status | nvarchar | 40 | 1 |  |  |  |
| LastSentDate | datetime | 8 | 1 |  |  |  |
| LastOpenDate | datetime | 8 | 1 |  |  |  |
| LastClickDate | datetime | 8 | 1 |  |  |  |
| bonusClubMember | int | 4 | 1 |  |  |  |
| bonusClubMembershipType | nvarchar | 40 | 1 |  |  |  |
| bonusClubPointsBalance | int | 4 | 1 |  |  |  |
| bonusClubStartDate | datetime | 8 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| bonusClubSignUpSource | nvarchar | 40 | 1 |  |  |  |
| Country | nvarchar | 40 | 1 |  |  |  |
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
| MonetarySum3m | numeric | 17 | 1 |  |  |  |
| MonetarySum6m | numeric | 17 | 1 |  |  |  |
| MonetarySum12m | numeric | 17 | 1 |  |  |  |
| MonetarySum18m | numeric | 17 | 1 |  |  |  |
| MonetarySum24m | numeric | 17 | 1 |  |  |  |
| MonetarySumTTL | numeric | 17 | 1 |  |  |  |
| FrequencyCount1m | int | 4 | 1 |  |  |  |
| RecencyCount1m | int | 4 | 1 |  |  |  |
| MonetarySum1m | numeric | 17 | 1 |  |  |  |
| address_1 | nvarchar | 510 | 1 |  |  |  |
| address_2 | nvarchar | 510 | 1 |  |  |  |
| address_3 | nvarchar | 510 | 1 |  |  |  |
| address_4 | nvarchar | 510 | 1 |  |  |  |
| post_code | nvarchar | 100 | 1 |  |  |  |
| mobile | nvarchar | 40 | 1 |  |  |  |
| locale | nvarchar | 40 | 1 |  |  |  |
| text_opt_in | int | 4 | 1 |  |  |  |
| DWInsertDate | datetime | 8 | 1 |  |  |  |
| DWUpdateDate | datetime | 8 | 1 |  |  |  |
| EmailAddress | nvarchar | 510 | 1 |  |  |  |
| LastTransactionDate | date | 3 | 1 |  |  |  |
| LastTransactionStore | nvarchar | 40 | 1 |  |  |  |
| PreferredStory | nvarchar | 200 | 1 |  |  |  |
| Emailable | int | 4 | 1 |  |  |  |
| EmailOptInDate | datetime | 8 | 1 |  |  |  |
| FrequencyCount36m | int | 4 | 1 |  |  |  |
| RecencyCount36m | int | 4 | 1 |  |  |  |
| MonetarySum36m | numeric | 17 | 1 |  |  |  |
| LifetimePoints | int | 4 | 1 |  |  |  |
| FirstTransactionDate | datetime | 8 | 1 |  |  |  |
| FirstStoreConcept | nvarchar | 200 | 1 |  |  |  |
| FirstName | nvarchar | 200 | 1 |  |  |  |
| LastName | nvarchar | 200 | 1 |  |  |  |
| DWUpdateDateRecency | datetime | 8 | 1 |  |  |  |
| InsertDate | datetime | 8 | 1 |  |  |  |
| UpdateDate | datetime | 8 | 1 |  |  |  |
| IsDeleted | bit | 1 | 1 |  |  |  |
| LastModifiedDate | datetime | 8 | 1 |  |  |  |
| SalesforceID | nvarchar | 36 | 0 |  |  |  |
| MembershipPlan | nvarchar | 200 | 1 |  |  |  |
| LoyaltyStatus | nvarchar | 100 | 1 |  |  |  |
