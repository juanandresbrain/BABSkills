# dbo.promotion_7148

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| id | int | 4 | 0 |  |  |  |
| row_type | tinyint | 1 | 0 |  |  |  |
| Number | nvarchar | 40 | 0 |  |  |  |
| StoreNum | bigint | 8 | 1 |  |  |  |
| Name | nvarchar | 60 | 1 |  |  |  |
| Description | nvarchar | 510 | 1 |  |  |  |
| ReferenceNum | bigint | 8 | 1 |  |  |  |
| ScheduleBeginDate | datetime | 8 | 1 |  |  |  |
| ScheduleEndDate | datetime | 8 | 1 |  |  |  |
| Status | nvarchar | 8 | 1 |  |  |  |
| BeginTime | datetime | 8 | 1 |  |  |  |
| EndTime | datetime | 8 | 1 |  |  |  |
| PromoDiscountNumber | bigint | 8 | 1 |  |  |  |
| PromoDiscountName | nvarchar | 60 | 1 |  |  |  |
| PromoDiscountType | nvarchar | 8 | 1 |  |  |  |
| PromoDiscountDescription | nvarchar | 100 | 1 |  |  |  |
| DiscountLevel | int | 4 | 1 |  |  |  |
| CouponNumberMin | nvarchar | 40 | 1 |  |  |  |
| CouponNumberMax | nvarchar | 40 | 1 |  |  |  |
| CouponNumberLength | smallint | 2 | 1 |  |  |  |
| ItemReqNumber | bigint | 8 | 1 |  |  |  |
| IdentityType | nvarchar | 8 | 1 |  |  |  |
| ItemNum | nvarchar | 40 | 1 |  |  |  |
| DivisionNum | bigint | 8 | 1 |  |  |  |
| DepartmentNum | bigint | 8 | 1 |  |  |  |
| DeptGroupNum | bigint | 8 | 1 |  |  |  |
| ClassNum | bigint | 8 | 1 |  |  |  |
| ItemGroupNum | bigint | 8 | 1 |  |  |  |
| Quantity | decimal | 9 | 1 |  |  |  |
| TierDefNumber | bigint | 8 | 1 |  |  |  |
| ThresholdType | nvarchar | 8 | 1 |  |  |  |
| ThresholdQty | decimal | 9 | 1 |  |  |  |
| ThresholdAmt | decimal | 9 | 1 |  |  |  |
| DiscType | nvarchar | 8 | 1 |  |  |  |
| DiscPct | decimal | 5 | 1 |  |  |  |
| DiscAmt | decimal | 9 | 1 |  |  |  |
| DiscAppliesTo | nvarchar | 8 | 1 |  |  |  |
| DiscQty | decimal | 9 | 1 |  |  |  |
| AddlInfo | nvarchar | 510 | 1 |  |  |  |
| ItemDiscSpecNumber | bigint | 8 | 1 |  |  |  |
| ItemDiscSpecIdentityType | nvarchar | 8 | 1 |  |  |  |
| ItemDiscSpecItemNum | nvarchar | 40 | 1 |  |  |  |
| ItemDiscSpecDivisionNum | bigint | 8 | 1 |  |  |  |
| ItemDiscSpecDepartmentNum | bigint | 8 | 1 |  |  |  |
| ItemDiscSpecDeptGroupNum | bigint | 8 | 1 |  |  |  |
| ItemDiscSpecClassNum | bigint | 8 | 1 |  |  |  |
| ItemDiscSpecItemGroupNum | bigint | 8 | 1 |  |  |  |
| ItemDiscSpecQuantity | decimal | 9 | 1 |  |  |  |
| ItemDiscSpecType | nvarchar | 8 | 1 |  |  |  |
| ItemDiscSpecPct | decimal | 5 | 1 |  |  |  |
| ItemDiscSpecAmt | decimal | 9 | 1 |  |  |  |
| ItemDiscSpecAppliesTo | nvarchar | 8 | 1 |  |  |  |

