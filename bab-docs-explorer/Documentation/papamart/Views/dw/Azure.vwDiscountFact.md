# Azure.vwDiscountFact

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwDiscountFact"]
    dbo_coupon_dim(["dbo.coupon_dim"]) --> VIEW
    dbo_date_dim(["dbo.date_dim"]) --> VIEW
    dbo_Discount_Category_DIM(["dbo.Discount_Category_DIM"]) --> VIEW
    dbo_discount_facts(["dbo.discount_facts"]) --> VIEW
    Azure_vwStores(["Azure.vwStores"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.coupon_dim |
| dbo.date_dim |
| dbo.Discount_Category_DIM |
| dbo.discount_facts |
| Azure.vwStores |

## View Code

```sql
CREATE VIEW [Azure].[vwDiscountFact] AS

SELECT  
		'0' AS TransactionID,
		cast(d.actual_date as date) AS TransactionDate,
		ds.StoreID ,
		df.reference_no AS ReferenceNumber,
		df.line_object_key AS LineObject, 
		df.units DiscountUnits, 
		df.unit_gross_amount AS DiscountUnitGrossAmount, 
		df.isExpired AS ExpiredFlag,
		cd.CategoryType AS DiscountCategoryType,
		cd.channelType AS DiscountChannelType,
		cd.financialGroup AS DiscountFinancialGroup,
		c.Retail_Pro AS RetailPro, 
		c.coupon_desc AS CouponDesc,
		ds.StoreKey,
		Cast(df.transaction_id as varchar(30)) + Cast(ds.StoreKey as varchar(10)) as TransactionKey
FROM dw.dbo.discount_facts df
INNER JOIN dw.dbo.coupon_dim c
	ON c.coupon_key=df.coupon_key
LEFT OUTER JOIN dw.dbo.Discount_Category_DIM cd
	ON cd.categoryTypeID=df.categoryTypeID
--INNER JOIN dw.DOMO.vwDOMOStores ds
--	ON ds.StoreKey=df.store_key
INNER JOIN Azure.vwStores ds
	ON ds.StoreKey=df.store_key
INNER JOIN dw.dbo.date_dim d
	ON d.date_key=df.date_key
WHERE d.actual_date>=DATEADD(year, -2, DATEADD(yy, DATEDIFF(yy, 0, GETDATE()), 0))
AND d.actual_date<CONVERT(DATE,GETDATE())
```

