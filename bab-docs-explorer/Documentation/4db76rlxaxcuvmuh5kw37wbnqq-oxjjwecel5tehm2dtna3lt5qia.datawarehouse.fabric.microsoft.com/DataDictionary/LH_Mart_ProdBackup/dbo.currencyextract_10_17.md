# dbo.currencyextract_10_17

**Database:** LH_Mart_ProdBackup  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| LoyaltyMember_MembershipNumber | varchar | 8000 | 1 |  |  |  |
| LoyaltyMember_Contact_Account_LifetimePoints_c | float | 8 | 1 |  |  |  |
| Guest_Locale_c | varchar | 8000 | 1 |  |  |  |
| PointsBalance | float | 8 | 1 |  |  |  |
| TotalPointsAccrued | float | 8 | 1 |  |  |  |
| TotalPointsRedeemed | float | 8 | 1 |  |  |  |
| TotalPointsExpired | float | 8 | 1 |  |  |  |
| MigratedPointsBalance_c | float | 8 | 1 |  |  |  |
| total_points_earned_since_0831 | float | 8 | 1 |  |  |  |
| total_points_earned_since_0831_divided | float | 8 | 1 |  |  |  |
| True_Error_Count | int | 4 | 1 |  |  |  |
| False_Error_Count | int | 4 | 1 |  |  |  |
