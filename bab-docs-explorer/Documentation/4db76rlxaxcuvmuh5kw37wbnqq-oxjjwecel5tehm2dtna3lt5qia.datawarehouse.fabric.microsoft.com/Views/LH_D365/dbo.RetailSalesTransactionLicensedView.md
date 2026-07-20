# dbo.RetailSalesTransactionLicensedView

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.RetailSalesTransactionLicensedView"]
    ProductDim_attribute(["ProductDim_attribute"]) --> VIEW
    d365LocationMapping_View(["d365LocationMapping_View"]) --> VIEW
    ecorescategory(["ecorescategory"]) --> VIEW
    product_dim_le(["product_dim_le"]) --> VIEW
    retailtransactiondiscounttrans(["retailtransactiondiscounttrans"]) --> VIEW
    dbo_retailtransactionsalestrans(["dbo.retailtransactionsalestrans"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ProductDim_attribute |
| d365LocationMapping_View |
| ecorescategory |
| product_dim_le |
| retailtransactiondiscounttrans |
| dbo.retailtransactionsalestrans |

## View Code

```sql
/****** Object:  View [dbo].[RetailSalesTransactionLicensedView]    Script Date: 4/1/2026 1:25:22 PM ******/

CREATE   VIEW [dbo].[RetailSalesTransactionLicensedView]
AS
WITH retailtransactionsalestrans AS (
    SELECT
--        pd.product_key,
		rt.transactionid,
        rt.itemid,
        rt.dataareaid,
        rt.store,
		rt.inventlocationid,
--        pd.jurisdiction_code,
        rt.currency,
--        l.accountingcurrency,
        --CONCAT(DATEPART(YEAR, rt.businessdate), '', RIGHT('0' + CAST(DATEPART(WEEK, rt.businessdate) AS VARCHAR(2)), 2)) AS merch_year_wk,
		rt.businessdate,
		rt.qty,
		rt.netamountincltax,
		rt.netamount,
		rt.costamount,
		rt.discamount,
		rt.discamountwithouttax,
		rt.transdate,
		rt.custaccount,
		rt.netprice,
		rt.originalprice,
		rt.price,
		rt.taxamount,
		rt.totaldiscamount,
		rt.totaldiscpct,
		rt.linenum
    FROM dbo.retailtransactionsalestrans AS rt
    WHERE rt.businessdate >= DATEADD(MONTH, -12, GETDATE())	
	AND (rt.[IsDelete] IS NULL OR rt.[IsDelete] = 0)   
     
	-- AND NOT EXISTS 
	-- (Select 1 from transformedretailsalestransactions tr 
	-- 	where 
	-- 	tr.transactionid = rt.transactionid 
	-- 	--and tr.itemid = rt.itemid
	-- 	and tr.store = rt.store
	-- 	and tr.dataareaid = rt.dataareaid)    
    
)

SELECT DISTINCT
    RoyaltyType,
    Licensor,
    pa.AttributeValue AS LICEN,
    [product_dim_le].product_key,
    [product_dim_le].jurisdiction_code,
    [product_dim_le].style_desc,
    [product_dim_le].department_code,
    [product_dim_le].department,
    [product_dim_le].class_code,
    [product_dim_le].class,
    [product_dim_le].subclass_code,
    [product_dim_le].subclass,
	[product_dim_le].color_code,
	[product_dim_le].color_desc,
    consumer_group.code AS consumergroup_code,
    consumer_group.name AS consumergroup,
    retailtransactionsalestrans.[store],
    retailtransactionsalestrans.[businessdate],
    retailtransactionsalestrans.transdate,
    [retailtransactionsalestrans].[itemid],
    retailtransactionsalestrans.transactionid,
    [retailtransactionsalestrans].[inventlocationid] + '-' + [retailtransactionsalestrans].[dataareaid] AS LocationKey,
    SUM([retailtransactionsalestrans].[costamount]) AS [costamount],
    MIN([retailtransactionsalestrans].[currency]) AS [currency],
    MIN([retailtransactionsalestrans].[custaccount]) AS [custaccount],
    SUM([retailtransactionsalestrans].[discamount]) AS [discamount],
    SUM([retailtransactionsalestrans].[discamountwithouttax]) AS [discamountwithouttax],
    MIN([retailtransactiondiscounttrans].[periodicdiscountofferid]) AS [periodicdiscountofferid],
    SUM([retailtransactionsalestrans].[netamount]) AS [netamount],
    SUM([retailtransactionsalestrans].[netamountincltax]) AS [netamountincltax],
    AVG([retailtransactionsalestrans].[netprice]) AS [netprice],
    AVG([retailtransactionsalestrans].[originalprice]) AS [originalprice],
    AVG([retailtransactionsalestrans].[price]) AS [price],
    SUM([retailtransactionsalestrans].[qty]) AS [qty],
    SUM([retailtransactionsalestrans].[taxamount]) AS [taxamount],
    SUM([retailtransactionsalestrans].[totaldiscamount]) AS [totaldiscamount],
    SUM([retailtransactionsalestrans].[totaldiscpct]) AS [totaldiscpct],
    [retailtransactionsalestrans].[dataareaid] AS [dataareaid]
FROM
    [retailtransactionsalestrans]
    LEFT JOIN d365LocationMapping_View lm
        ON lm.inventlocationid = [retailtransactionsalestrans].inventlocationid
        AND lm.legalentity = [retailtransactionsalestrans].dataareaid
    LEFT JOIN [product_dim_le]
        ON [product_dim_le].style_code = [retailtransactionsalestrans].itemid 
        AND [product_dim_le].LegalEntity = [retailtransactionsalestrans].dataareaid
        AND product_dim_le.jurisdiction_code = lm.JurisidictionCode
    outer apply (
            select top 1 p.AttributeValue
            from ProductDim_attribute p
            where p.s
```

