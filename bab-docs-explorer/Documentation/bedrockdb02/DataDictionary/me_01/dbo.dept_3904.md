# dbo.dept_3904

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| pos_department_id | int | 4 | 0 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| Number | decimal | 5 | 1 |  |  |  |
| DivisionNum | decimal | 5 | 1 |  |  |  |
| StoreNum | bigint | 8 | 1 |  |  |  |
| GroupNum | bigint | 8 | 1 |  |  |  |
| Name | nvarchar | 60 | 1 |  |  |  |
| SellLinearSize | decimal | 9 | 1 |  |  |  |
| SellAreaSize | decimal | 9 | 1 |  |  |  |
| ToleranceTypeCode | nvarchar | 8 | 1 |  |  |  |
| ToleranceMinQty | decimal | 9 | 1 |  |  |  |
| ToleranceMaxQty | decimal | 9 | 1 |  |  |  |
| ToleranceLvlQty | decimal | 9 | 1 |  |  |  |
| ToleranceMinAmt | decimal | 9 | 1 |  |  |  |
| ToleranceMaxAmt | decimal | 9 | 1 |  |  |  |
| ToleranceLvlAmt | decimal | 9 | 1 |  |  |  |
| TaxGroup | decimal | 5 | 1 |  |  |  |
| MarkDownCode | smallint | 2 | 1 |  |  |  |
| PriceOverrideCode | smallint | 2 | 1 |  |  |  |
| DiscountCode | smallint | 2 | 1 |  |  |  |
| EmplDiscountCode | smallint | 2 | 1 |  |  |  |
| DepartmentTypeCode | nvarchar | 8 | 1 |  |  |  |
| AdditionalInfoFlag | smallint | 2 | 1 |  |  |  |
| Code | nvarchar | 20 | 1 |  |  |  |
| Desc | nvarchar | 100 | 1 |  |  |  |
| AllowQtyKeyFlg | smallint | 2 | 1 |  |  |  |
| AllowReturnFlg | smallint | 2 | 1 |  |  |  |

