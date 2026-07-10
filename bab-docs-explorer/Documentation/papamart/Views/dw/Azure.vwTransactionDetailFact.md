# Azure.vwTransactionDetailFact

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwTransactionDetailFact"]
    dbo_currency_dim(["dbo.currency_dim"]) --> VIEW
    dbo_FranchiseeTransactionDetailFact(["dbo.FranchiseeTransactionDetailFact"]) --> VIEW
    dbo_line_object_dim(["dbo.line_object_dim"]) --> VIEW
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
    dbo_Transaction_Type_Dim(["dbo.Transaction_Type_Dim"]) --> VIEW
    dbo_TransactionDetailFact(["dbo.TransactionDetailFact"]) --> VIEW
    Azure_vwDateFilter(["Azure.vwDateFilter"]) --> VIEW
    Azure_vwStores(["Azure.vwStores"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.currency_dim |
| dbo.FranchiseeTransactionDetailFact |
| dbo.line_object_dim |
| dbo.time_dim |
| dbo.Transaction_Type_Dim |
| dbo.TransactionDetailFact |
| Azure.vwDateFilter |
| Azure.vwStores |

## View Code

```sql
/* =============================================================================================================
 Name: [Azure].[vwTransactionDetailFacts]

 Description: Transaction detail at line level.


 Dependencies: Inner joins with vwStores, pulling back only those stores in the view.

 Revision History
		Name:				Date:			Comments:
		Tim Bytnar			4/11/2018		Initial creation
		John Eck			9/25/2018		Added Franchisee details
--		Dan Tweedie			2021-2-24		Updated to use new TransactionDetailFact table which only holds data from 2018-1-1 to present, so processing is hopefully faster
*/
CREATE VIEW [Azure].[vwTransactionDetailFact]

AS
SELECT        tdf.product_key AS ProductKey, cd.currency_code AS CurrencyCode, '0' as TransactionID, tdf.transaction_line_seq AS TransactionLineSeq, tdf.Register_Num AS RegisterNumber, CONVERT(DATE, 
                         dd.actual_date) AS TransactionDate, 
						 CAST(CONVERT(VARCHAR, CONVERT(DATE, dd.actual_date)) + ' ' + LEFT(CONVERT(TIME, CONVERT(VARCHAR, td.hour) + ':' + CONVERT(VARCHAR, td.minute)), 5) 
                         + ':00.000' AS DATETIME) AS TransactionDateTime, ds.StoreID, tdf.unit_gross_amount AS UnitGrossAmount, tdf.units, tdf.unit_disc_amount AS UnitDiscAmount, ISNULL(tdf.party_y_n, 'N') AS PartyFlag, 
                         ttd.transaction_type AS TransactionType, lod.Line_Object_Description AS LineObject, Cast(tdf.transaction_no as varchar(20)) AS TransactionNumber, tdf.reference_no AS ReferenceNumber, tdf.vat_tax_amount AS VatTaxAmount, 
                         tdf.upsell_disc_allocated AS UpsellDiscAllocated, tdf.ext_cost AS ExtCost, tdf.line_action_key AS LineAction, ds.StoreKey
						 , Cast(tdf.transaction_id as varchar(20))  + Cast( ds.StoreKey AS varchar(10)) as TransactionKey
FROM            dbo.TransactionDetailFact AS tdf INNER JOIN
                         Azure.vwStores AS ds ON ds.StoreKey =  tdf.store_key LEFT OUTER JOIN
                         dbo.currency_dim AS cd ON cd.currency_key = tdf.currency_key LEFT OUTER JOIN
                         dbo.time_dim AS td ON td.time_key = tdf.time_key INNER JOIN
                         Azure.vwDateFilter AS dd ON tdf.date_key = dd.date_key LEFT OUTER JOIN
                         dbo.line_object_dim AS lod ON lod.Line_Object_Key = tdf.line_object_key LEFT OUTER JOIN
                         dbo.Transaction_Type_Dim AS ttd ON ttd.transaction_key = tdf.transaction_type_key
WHERE        (tdf.product_key >= 0)


union all


SELECT [product_key]
      ,currency_code
	  ,'0' as Transaction_id
      ,[transaction_line_seq]
	  ,'0' AS REgisterNumber
	  ,CONVERT(DATE, dd.actual_date) AS TransactionDate  
	  ,CAST(CONVERT(VARCHAR,CONVERT(DATE,dd.actual_date)) +' ' + LEFT(CONVERT(TIME,CONVERT(VARCHAR,td.hour) + ':' + CONVERT(VARCHAR,td.minute)),5) + ':00.000' AS DATETIME) AS TransactionDateTime
      ,ds.StoreID
      ,[unit_gross_amount]
      ,[units]
      ,[unit_disc_amount]
      ,ISNULL([party_y_n],'N') AS PartyFlag
	  , ttd.transaction_type AS TransactionType
	  ,lod.Line_Object_Description AS LineObject
      ,[transaction_no]
      ,Cast([reference_no] as varchar(80)) as reference_NO
      ,[vat_tax_amount]
      ,[upsell_disc_allocated]
      ,[ext_cost]
	  ,tdf.line_action_key AS LineAction
	  ,[store_key]
	  ,Cast(transaction_id as Varchar(20)) + cast(ds.StoreKey as Varchar(10)) as TransactionKey
  FROM [dbo].[FranchiseeTransactionDetailFact]  tdf 
INNER JOIN [Azure].[vwStores] ds
	ON ds.StoreKey=tdf.store_key
	LEFT OUTER JOIN [dbo].[currency_dim] cd
		ON cd.currency_key = tdf.currency_key 
	LEFT OUTER JOIN [dbo].[time_dim] td
		ON td.time_key = tdf.time_key 
	Inner JOIN Azure.vwDateFilter dd
		ON tdf.date_key = dd.date_key 
	LEFT OUTER JOIN [dbo].[line_object_dim] lod
		ON lod.Line_Object_Key = tdf.line_object_key 
	LEFT OUTER JOIN [dbo].[Transaction_Type_Dim] ttd
		ON ttd.transaction_key = tdf.transaction_type_key
		AND LEFT(ds.TradingGroup,9) = 'Franchise'
WHERE  tdf.Product_Key>=0
```

