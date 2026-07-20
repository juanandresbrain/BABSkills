# dbo.crmcustomerdim

**Database:** LH_Mart_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRMCustomerKey | int | 4 | 1 |  |  |  |
| CustomerID | int | 4 | 1 |  |  |  |
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| MembershipDate | datetime2 | 8 | 1 |  |  |  |
| Gender | varchar | 8000 | 1 |  |  |  |
| BirthDate | date | 3 | 1 |  |  |  |
| LanguageCode | varchar | 8000 | 1 |  |  |  |
| CRMUpdateDate | datetime2 | 8 | 1 |  |  |  |
| StoreKey | int | 4 | 1 |  |  |  |
| CountryCode | varchar | 8000 | 1 |  |  |  |
| PostalCode | varchar | 8000 | 1 |  |  |  |
| PointsEligible | bit | 1 | 1 |  |  |  |
| MembershipType | varchar | 8000 | 1 |  |  |  |
| InsertedDate | datetime2 | 8 | 1 |  |  |  |
| UpdatedDate | datetime2 | 8 | 1 |  |  |  |
| InsertedBy | varchar | 8000 | 1 |  |  |  |
| UpdatedBy | varchar | 8000 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ETLEventID | int | 4 | 1 |  |  |  |
| Emailable | int | 4 | 1 |  |  |  |
| SubscriberKey | int | 4 | 1 |  |  |  |
| DirectMailOptIn | int | 4 | 1 |  |  |  |
| HasPhoneNumber | int | 4 | 1 |  |  |  |
| Locale | varchar | 8000 | 1 |  |  |  |
| TextOptIn | int | 4 | 1 |  |  |  |
| PhoneNumber | varchar | 8000 | 1 |  |  |  |
| EmailOptInDate | datetime2 | 8 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| ClubStatus | varchar | 8000 | 1 |  |  |  |
| CurrentRewardPoints | int | 4 | 1 |  |  |  |
| SignUpSource | varchar | 8000 | 1 |  |  |  |
| address_1 | varchar | 8000 | 1 |  |  |  |
| address_2 | varchar | 8000 | 1 |  |  |  |
| address_3 | varchar | 8000 | 1 |  |  |  |
| address_4 | varchar | 8000 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| isBonusClubMember | int | 4 | 1 |  |  |  |
| LifetimeTotalPointsEarned | int | 4 | 1 |  |  |  |
| FirstName | varchar | 8000 | 1 |  |  |  |
| LastName | varchar | 8000 | 1 |  |  |  |
| MembershipPlan | varchar | 8000 | 1 |  |  |  |
| OriginDate | datetime2 | 8 | 1 |  |  |  |
| DataSource | varchar | 8000 | 1 |  |  |  |
