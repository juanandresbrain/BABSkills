# dbo.CRMCustomerDimStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerID | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| MembershipDate | datetime | 8 | 1 |  |  |  |
| Gender | nchar | 2 | 1 |  |  |  |
| BirthDate | date | 3 | 1 |  |  |  |
| LanguageCode | nchar | 6 | 1 |  |  |  |
| CRMUpdateDate | datetime | 8 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| CountryCode | nvarchar | 6 | 1 |  |  |  |
| PostalCode | nvarchar | 10 | 1 |  |  |  |
| PointsEligible | bit | 1 | 1 |  |  |  |
| MembershipType | nvarchar | 8 | 1 |  |  |  |
| InsertedDate | datetime | 8 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| Emailable | int | 4 | 1 |  |  |  |
| SubscriberKey | int | 4 | 1 |  |  |  |
| DirectMailOptIn | int | 4 | 1 |  |  |  |
| HasPhoneNumber | int | 4 | 1 |  |  |  |
| Locale | varchar | 5 | 1 |  |  |  |
| TextOptIn | int | 4 | 1 |  |  |  |
| PhoneNumber | nvarchar | 32 | 1 |  |  |  |
| EmailOptInDate | datetime | 8 | 1 |  |  |  |
| EmailAddress | nvarchar | 130 | 1 |  |  |  |
| ClubStatus | varchar | 12 | 1 |  |  |  |
| CurrentRewardPoints | int | 4 | 1 |  |  |  |
| SignUpSource | varchar | 6 | 1 |  |  |  |
| address_1 | nvarchar | 80 | 1 |  |  |  |
| address_2 | nvarchar | 80 | 1 |  |  |  |
| address_3 | nvarchar | 80 | 1 |  |  |  |
| address_4 | nvarchar | 80 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| isBonusClubMember | int | 4 | 1 |  |  |  |
| LifetimeTotalPointsEarned | int | 4 | 1 |  |  |  |
| FirstName | nvarchar | 200 | 1 |  |  |  |
| LastName | nvarchar | 200 | 1 |  |  |  |
| MembershipPlan | nvarchar | 200 | 1 |  |  |  |
| OriginDate | datetime | 8 | 1 |  |  |  |
