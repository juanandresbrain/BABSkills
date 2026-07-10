# dbo.CurrencyExtract_10-17

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | nvarchar | 100 | 1 |  |  |  |
| LoyaltyMember_MembershipNumber | nvarchar | 100 | 1 |  |  |  |
| LoyaltyMember_Contact_Account_LifetimePoints_c | float | 8 | 1 |  |  |  |
| Guest_Locale_c | nvarchar | 100 | 1 |  |  |  |
| PointsBalance | float | 8 | 1 |  |  |  |
| TotalPointsAccrued | float | 8 | 1 |  |  |  |
| TotalPointsRedeemed | float | 8 | 1 |  |  |  |
| TotalPointsExpired | float | 8 | 1 |  |  |  |
| MigratedPointsBalance_c | float | 8 | 1 |  |  |  |
| total_points_earned_since_0831 | float | 8 | 1 |  |  |  |
| total_points_earned_since_0831_divided | float | 8 | 1 |  |  |  |
| True_Error_Count | int | 4 | 1 |  |  |  |
| False_Error_Count | int | 4 | 1 |  |  |  |
