# dbo.inboundloyalty_customermasterde_merge

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customerNumber | varchar | 8000 | 1 |  |  |  |
| status | varchar | 8000 | 1 |  |  |  |
| bonusClubMember | int | 4 | 1 |  |  |  |
| bonusClubMembershipType | varchar | 8000 | 1 |  |  |  |
| bonusClubPointsBalance | int | 4 | 1 |  |  |  |
| bonusClubStartDate | datetime2 | 8 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| bonusClubSignUpSource | varchar | 8000 | 1 |  |  |  |
| Country | varchar | 8000 | 1 |  |  |  |
| address_1 | varchar | 8000 | 1 |  |  |  |
| address_2 | varchar | 8000 | 1 |  |  |  |
| address_3 | varchar | 8000 | 1 |  |  |  |
| address_4 | varchar | 8000 | 1 |  |  |  |
| post_code | varchar | 8000 | 1 |  |  |  |
| mobile | varchar | 8000 | 1 |  |  |  |
| locale | varchar | 8000 | 1 |  |  |  |
| text_opt_in | int | 4 | 1 |  |  |  |
| EmailAddress | varchar | 8000 | 1 |  |  |  |
| LifetimePoints | int | 4 | 1 |  |  |  |
| FirstName | varchar | 8000 | 1 |  |  |  |
| LastName | varchar | 8000 | 1 |  |  |  |
| DataSource | varchar | 8000 | 1 |  |  |  |
