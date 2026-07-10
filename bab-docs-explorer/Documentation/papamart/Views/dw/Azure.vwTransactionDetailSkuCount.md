# Azure.vwTransactionDetailSkuCount

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwTransactionDetailSkuCount"]
    dbo_time_dim(["dbo.time_dim"]) --> VIEW
    dbo_TransactionDetailFact(["dbo.TransactionDetailFact"]) --> VIEW
    Azure_vwDateFilter(["Azure.vwDateFilter"]) --> VIEW
    azure_vwProducts(["azure.vwProducts"]) --> VIEW
    Azure_vwStores(["Azure.vwStores"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.time_dim |
| dbo.TransactionDetailFact |
| Azure.vwDateFilter |
| azure.vwProducts |
| Azure.vwStores |

## View Code

```sql
CREATE VIEW [Azure].[vwTransactionDetailSkuCount]

AS
-- =============================================================================================================
-- Name: [Azure].[vwTransactionDetailskucOUNT]
--
-- Description: Finds transactions with only a single unstuffed sku.  
--
--
-- Dependencies: Stores, date filter view and product dim
--
-- Revision History
--		Name:				Date:			Comments:
--		JOhn Eck			8/9/2018		Initial creation
--
-- =============================================================================================================


SELECT  Transaction_ID 
      ,count(Distinct(Product_Key)) as AnimalCount

  FROM  dbo.TransactionDetailFact tdf 
	LEFT OUTER JOIN [dbo].[time_dim] td
		ON td.time_key = tdf.time_key 
	Inner JOIN Azure.vwDateFilter dd
		ON tdf.date_key = dd.date_key  
	INNER JOIN
          Azure.vwStores AS ds ON ds.StoreKey = CONVERT(VARCHAR, tdf.store_key)
	inner join azure.vwProducts P on tdf.product_Key = p.ProductKey
where department = 'Unstuffed' and tdf.Product_Key>=0
Group By Transaction_ID
Having count(Distinct(Product_Key)) = 1
```

