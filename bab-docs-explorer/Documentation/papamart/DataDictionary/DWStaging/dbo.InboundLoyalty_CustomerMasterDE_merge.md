# dbo.InboundLoyalty_CustomerMasterDE_merge

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| customerNumber | varchar | 20 | 0 |  |  |  |
| status | nvarchar | 40 | 1 |  |  |  |
| bonusClubMember | int | 4 | 1 |  |  |  |
| bonusClubMembershipType | nvarchar | 40 | 1 |  |  |  |
| bonusClubPointsBalance | int | 4 | 1 |  |  |  |
| bonusClubStartDate | datetime | 8 | 1 |  |  |  |
| hasOnlineAccount | int | 4 | 1 |  |  |  |
| bonusClubSignUpSource | nvarchar | 40 | 1 |  |  |  |
| Country | nvarchar | 40 | 1 |  |  |  |
| address_1 | nvarchar | 510 | 1 |  |  |  |
| address_2 | nvarchar | 510 | 1 |  |  |  |
| address_3 | nvarchar | 510 | 1 |  |  |  |
| address_4 | nvarchar | 510 | 1 |  |  |  |
| post_code | nvarchar | 100 | 1 |  |  |  |
| mobile | nvarchar | 40 | 1 |  |  |  |
| locale | nvarchar | 40 | 1 |  |  |  |
| text_opt_in | int | 4 | 1 |  |  |  |
| EmailAddress | nvarchar | 510 | 1 |  |  |  |
| LifetimePoints | int | 4 | 1 |  |  |  |
| FirstName | nvarchar | 200 | 1 |  |  |  |
| LastName | nvarchar | 200 | 1 |  |  |  |
| DataSource | varchar | 100 | 1 |  |  |  |
