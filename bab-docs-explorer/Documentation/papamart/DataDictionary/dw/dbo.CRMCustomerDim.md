# dbo.CRMCustomerDim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRMCustomerKey | int | 4 | 0 | YES |  |  |
| CustomerID | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 20 | 1 |  |  |  |
| MembershipDate | datetime | 8 | 1 |  |  |  |
| Gender | varchar | 5 | 1 |  |  |  |
| BirthDate | date | 3 | 1 |  |  |  |
| LanguageCode | char | 3 | 1 |  |  |  |
| CRMUpdateDate | datetime | 8 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| CountryCode | nvarchar | 40 | 1 |  |  |  |
| PostalCode | nvarchar | 100 | 1 |  |  |  |
| PointsEligible | bit | 1 | 1 |  |  |  |
| MembershipType | nvarchar | 40 | 1 |  |  |  |
| InsertedDate | datetime | 8 | 1 |  |  |  |
| UpdatedDate | datetime | 8 | 1 |  |  |  |
| InsertedBy | varchar | 50 | 1 |  |  |  |
| UpdatedBy | varchar | 50 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| Emailable | int | 4 | 1 |  |  |  |
| SubscriberKey | int | 4 | 1 |  |  |  |
| DirectMailOptIn | int | 4 | 1 |  |  |  |
| HasPhoneNumber | int | 4 | 1 |  |  |  |
| Locale | nvarchar | 40 | 1 |  |  |  |
| TextOptIn | int | 4 | 1 |  |  |  |
| PhoneNumber | nvarchar | 40 | 1 |  |  |  |
| EmailOptInDate | datetime | 8 | 1 |  |  |  |
| EmailAddress | nvarchar | 510 | 1 |  |  |  |
| ClubStatus | nvarchar | 40 | 1 |  |  |  |
| CurrentRewardPoints | int | 4 | 1 |  |  |  |
| SignUpSource | nvarchar | 40 | 1 |  |  |  |
| address_1 | nvarchar | 510 | 1 |  |  |  |
| address_2 | nvarchar | 510 | 1 |  |  |  |
| address_3 | nvarchar | 510 | 1 |  |  |  |
| address_4 | nvarchar | 510 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| isBonusClubMember | int | 4 | 1 |  |  |  |
| LifetimeTotalPointsEarned | int | 4 | 1 |  |  |  |
| FirstName | nvarchar | 200 | 1 |  |  |  |
| LastName | nvarchar | 200 | 1 |  |  |  |
| MembershipPlan | varchar | 100 | 1 |  |  |  |
| OriginDate | datetime | 8 | 1 |  |  |  |
| DataSource | varchar | 100 | 1 |  |  |  |
