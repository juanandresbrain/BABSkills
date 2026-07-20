# dbo.azure_customer_master_data

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| isBonusClubTY | int | 4 | 1 |  |  |  |
| isBonusClubLY | int | 4 | 1 |  |  |  |
| isBonusClubActive5YearsTY | int | 4 | 1 |  |  |  |
| isBonusClubActive3YearsTY | int | 4 | 1 |  |  |  |
| isBonusClubActive2YearsTY | int | 4 | 1 |  |  |  |
| isBonusClubActive1YearsTY | int | 4 | 1 |  |  |  |
| isBonusClubActive5YearsLY | int | 4 | 1 |  |  |  |
| isBonusClubActive3YearsLY | int | 4 | 1 |  |  |  |
| isBonusClubActive2YearsLY | int | 4 | 1 |  |  |  |
| isBonusClubActive1YearsLY | int | 4 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| DaysSinceLastOpen | int | 4 | 1 |  |  |  |
| MonthsSinceLastOpen | float | 8 | 1 |  |  |  |
| isBonusClubOptInText | int | 4 | 1 |  |  |  |
| isBonusClubOptInEmail | int | 4 | 1 |  |  |  |
| hasEmailOpen | int | 4 | 1 |  |  |  |
| isBonusClubEmailorTextOpenLast12Month | int | 4 | 1 |  |  |  |
| isBonusClubEmailorTextOpenLast365Day | int | 4 | 1 |  |  |  |
| isBonusClubEmailorTextOpenLast24Month | int | 4 | 1 |  |  |  |
| isBonusClubEmailorTextOpenLast729Day | int | 4 | 1 |  |  |  |
| isBonusClubWEmailOpen | int | 4 | 1 |  |  |  |
| isOptInText | int | 4 | 1 |  |  |  |
| isOptInEmail | int | 4 | 1 |  |  |  |
| bonusClubMembershipType | varchar | 8000 | 1 |  |  |  |
| bonusClubSignUpSource | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| isActive | int | 4 | 1 |  |  |  |
| isNotActive | int | 4 | 1 |  |  |  |
| isBonusClubMemberDescr | varchar | 8000 | 1 |  |  |  |
| isBounced | int | 4 | 1 |  |  |  |
| isUnsubscribed | int | 4 | 1 |  |  |  |
| JoinDate | date | 3 | 1 |  |  |  |
| joinFiscalYear | varchar | 8000 | 1 |  |  |  |
| joinFiscalQtr | int | 4 | 1 |  |  |  |
| joinFiscalYearQtr | varchar | 8000 | 1 |  |  |  |
| joinFiscaYearPeriod | varchar | 8000 | 1 |  |  |  |
| joinFiscalPeriod | int | 4 | 1 |  |  |  |
| joinFiscalMonth | varchar | 8000 | 1 |  |  |  |
| LastSentDate | date | 3 | 1 |  |  |  |
| LastClickDate | date | 3 | 1 |  |  |  |
| LastOpenDate | date | 3 | 1 |  |  |  |
| LastTransactionDate | date | 3 | 1 |  |  |  |
| LastTransactionStore | varchar | 8000 | 1 |  |  |  |
| PreferredStory | varchar | 8000 | 1 |  |  |  |
| FrequencyCount1m | int | 4 | 1 |  |  |  |
| FrequencyCount3m | int | 4 | 1 |  |  |  |
| FrequencyCount6m | int | 4 | 1 |  |  |  |
| FrequencyCount12m | int | 4 | 1 |  |  |  |
| FrequencyCount18m | int | 4 | 1 |  |  |  |
| FrequencyCount24m | int | 4 | 1 |  |  |  |
| FrequencyCount36m | int | 4 | 1 |  |  |  |
| FrequencyCountTTL | int | 4 | 1 |  |  |  |
| RecencyCount1m | int | 4 | 1 |  |  |  |
| RecencyCount3m | int | 4 | 1 |  |  |  |
| RecencyCount6m | int | 4 | 1 |  |  |  |
| RecencyCount12m | int | 4 | 1 |  |  |  |
| RecencyCount18m | int | 4 | 1 |  |  |  |
| RecencyCount24m | int | 4 | 1 |  |  |  |
| RecencyCount36m | int | 4 | 1 |  |  |  |
| RecencyCountTTL | int | 4 | 1 |  |  |  |
| MonetarySum1m | decimal | 17 | 1 |  |  |  |
| MonetarySum3m | decimal | 17 | 1 |  |  |  |
| MonetarySum6m | decimal | 17 | 1 |  |  |  |
| MonetarySum12m | decimal | 17 | 1 |  |  |  |
| MonetarySum18m | decimal | 17 | 1 |  |  |  |
| MonetarySum24m | decimal | 17 | 1 |  |  |  |
| MonetarySum36m | decimal | 17 | 1 |  |  |  |
| MonetarySumTTL | decimal | 17 | 1 |  |  |  |
| CurrentPointsBalance | int | 4 | 1 |  |  |  |
| LifetimePoints | int | 4 | 1 |  |  |  |
| FirstTransactionDate | datetime2 | 8 | 1 |  |  |  |
| FirstStoreConcept | varchar | 8000 | 1 |  |  |  |
