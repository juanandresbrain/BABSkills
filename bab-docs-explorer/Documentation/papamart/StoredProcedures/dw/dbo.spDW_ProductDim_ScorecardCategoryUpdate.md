# dbo.spDW_ProductDim_ScorecardCategoryUpdate

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDW_ProductDim_ScorecardCategoryUpdate"]
    dbo_product_dim(["dbo.product_dim"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDW_ProductDim_ScorecardCategoryUpdate]
AS
BEGIN
	SET NOCOUNT ON;

	UPDATE dbo.product_dim
	SET ScorecardCategory = CASE
							WHEN LEFT(department_code, 1) = 'W'
								-- new hierarchy 2015-01-27
								THEN CASE
									WHEN RIGHT(department_code, 2) = '02'
										THEN 'Animal'
									WHEN RIGHT(department_code, 2) = '10'
										THEN 'Footwear'
									WHEN RIGHT(department_code, 2) = '08'
										THEN 'Accessories'
									WHEN RIGHT(department_code, 2) = '12' AND SUBSTRING(subclass_code, 10, 2) = '01'
										THEN 'Sounds'
									WHEN RIGHT(department_code, 2) = '06' AND SUBSTRING(subclass_code, 10, 2) <> '07'
										THEN 'Clothing'
									WHEN RIGHT(department_code, 2) = '06' AND SUBSTRING(subclass_code, 10, 2) = '07'
										THEN 'Sports'
									WHEN RIGHT(department_code, 2) = '04' AND SUBSTRING(subclass_code, 10, 2) = '02'
										THEN 'Prestuffed'
									-- below are not in current scorecard 2015-01-13
									WHEN RIGHT(department_code, 2) = '04' AND SUBSTRING(subclass_code, 10, 2) = '01'
										THEN 'Buddies'
									WHEN RIGHT(department_code, 2) = '12' AND SUBSTRING(subclass_code, 10, 2) = '02'
										THEN 'Scents'
									WHEN RIGHT(department_code, 2) = '16'
										THEN 'Pets'
									WHEN RIGHT(department_code, 2) = '18'
										THEN 'Human'
									WHEN RIGHT(department_code, 2) = '45'
										THEN 'Bearbucks OR Coupons'
									WHEN RIGHT(department_code, 2) = '46'
										THEN 'Donation OR Discount'
									WHEN RIGHT(department_code, 2) = '47'
										THEN 'Transaction Flags'
									WHEN RIGHT(department_code, 2) = '50'
										THEN 'Web'
									WHEN RIGHT(department_code, 2) = '51'
										THEN 'Kit'
									WHEN RIGHT(department_code, 2) = '55'
										THEN 'Corporate'
									WHEN RIGHT(department_code, 2) = '60'
										THEN 'Supplies'
									WHEN RIGHT(department_code, 2) = '65'
										THEN 'Embroidery'
									WHEN RIGHT(department_code, 2) = '70'
										THEN 'Former Business'
									WHEN RIGHT(department_code, 2) = '75'
										THEN 'Promotion'
									WHEN RIGHT(department_code, 2) = '80'
										THEN 'Giftcard'
									WHEN RIGHT(department_code, 2) = '85'
										THEN 'Blank'
									WHEN RIGHT(department_code, 2) = '99'
										THEN 'Test'
									ELSE 'Unknown'
									END
							WHEN LEFT(department_code, 1) = 'R'
								-- old hierarchy 200? to 2015-01-23
								THEN CASE
									WHEN LEFT(department_code, 5) = 'R-B-L'
										THEN 'LMM'
									WHEN LEFT(department_code, 5) = 'R-B-R'
										THEN 'Ridemakerz'
									WHEN LEFT(department_code, 5) = 'R-B-Z'
										THEN 'Branded'
									ELSE  -- WHEN LEFT(department_code, 5) NOT IN ('R-B-Z', 'R-B-L')
										CASE
										WHEN (RIGHT(department_code, 2) = '25' OR RIGHT(subclass_code, 2) = '25')
											THEN 'Animal'
										WHEN (RIGHT(department_code, 2) = '15' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Footwear'
										WHEN (RIGHT(department_code, 2) = '05' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Accessories'
										WHEN (RIGHT(department_code, 2) = '20' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Sounds'
										WHEN (RIGHT(department_code, 2) = '10' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Clothing'
										WHEN (RIGHT(department_code, 2) = '12' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Sports'
										WHEN (RIGHT(department_code, 2) = '30' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Prestuffed'
										-- below are not in current scorecard 2015-01-13
										WHEN (RIGHT(department_code, 2) = '06' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Furniture'
										WHEN ((RIGHT(department_code, 2) = '07' OR department = 'Pets') AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Pets'
										WHEN (RIGHT(department_code, 2) IN ('12', '33', '38') AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Licensing'
										WHEN (RIGHT(department_code, 2) = '21' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Scents'
										WHEN (RIGHT(department_code, 2) = '32' AND SUBSTRING(subclass_code, 10, 2) = '01' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Buddies'
										WHEN (RIGHT(department_code, 2) = '35' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Human'
										WHEN (RIGHT(department_code, 2) IN ('40', '48') AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Parties'
										WHEN (RIGHT(department_code, 2) = '45' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Bearbucks OR Coupons'
										WHEN (RIGHT(department_code, 2) = '46' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Donation OR Discount'
										WHEN (RIGHT(department_code, 2) = '47' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Transaction Flags'
										WHEN (RIGHT(department_code, 2) = '50' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Web'
										WHEN (RIGHT(department_code, 2) = '51' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Kit'
										WHEN (RIGHT(department_code, 2) = '55' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Corporate'
										WHEN (RIGHT(department_code, 2) = '60' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Supplies'
										WHEN (RIGHT(department_code, 2) = '65' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Embroidery'
										WHEN (RIGHT(department_code, 2) = '70' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Former Business'
										WHEN (RIGHT(department_code, 2) = '75' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Promotion'
										WHEN (RIGHT(department_code, 2) = '80' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Giftcard'
										WHEN (RIGHT(department_code, 2) = '85' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Blank'
										WHEN (RIGHT(department_code, 2) = '99' AND RIGHT(subclass_code, 2) <> '25')
											THEN 'Test'
										ELSE 'Unknown'
										END
									END
							ELSE 'Unknown'
							END
END
```

