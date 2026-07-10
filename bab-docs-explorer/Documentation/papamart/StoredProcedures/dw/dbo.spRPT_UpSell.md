# dbo.spRPT_UpSell

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_UpSell"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRPT_UpSell] 
@BeginDate datetime
,@EndDate datetime
AS

DECLARE @SQL nvarchar(4000)

/* GET counts by store hierarchy*/

SET @SQL = N'
SELECT sd.store_id,sd.store_name,
		sd.bearritory,
		sd.region,
		COUNT(distinct discount_transaction_id) as ttlDiscountTrans,
		COUNT(distinct JackFact_transaction_id) as ttlTrans
FROM ('
	/*	
	JOIN transactions that had GAAP sale of $35 or more 
	OR that were GC only and $35 or more to transactions that had an UPSELL line object
	*/
SET @SQL = @SQL +'
	SELECT	discount_fact.transaction_id as discount_transaction_id,
			a.store_key, 
			a.JackFact_transaction_id, 
			a.GAAP_Sale, 
			a.Gift_Card_Sold, 
			a.gift_card_only

	FROM ('
/*get transactions that had were a GC only sale of $35 or more*/
SET @SQL = @SQL +'
		SELECT	tsf.store_key,
				tsf.transaction_id as JackFact_transaction_id, 
				tsf.GAAP_Sale, 
				tsf.Gift_Card_Sold, 
				tsf.gift_card_only
		FROM dbo.Transaction_Summary_Facts tsf (nolock)
		JOIN dbo.date_dim d on tsf.date_key = d.date_key
		JOIN dbo.store_dim s on tsf.store_key = s.store_key
		    
		WHERE
		  (d.actual_date  BETWEEN '''+ CONVERT(char(10),@BeginDate,101) +''' AND '''+ CONVERT(char(10),@EndDate,101)+''')
		  AND  tsf.gift_card_only  =  1

		GROUP BY
		  s.region, 
		  tsf.store_key,
		  tsf.transaction_id, 
		  tsf.GAAP_Sale,
		  tsf.Gift_Card_Sold,
		  tsf.gift_card_only
		HAVING
		  ( 
		  sum(tsf.Gift_Card_Sold)  >=  35
		  )
		UNION '
	/*get transactions that had GAAP sale of $35 or more*/
SET @SQL = @SQL +'
		SELECT	tsf.store_key,
				tsf.transaction_id as JackFact_transaction_id, 
				tsf.GAAP_Sale, 
				tsf.Gift_Card_Sold, 
				tsf.gift_card_only	

		FROM dbo.Transaction_Summary_Facts tsf (nolock)
		JOIN dbo.date_dim d on tsf.date_key = d.date_key
		JOIN dbo.store_dim s on tsf.store_key = s.store_key
		    
		WHERE
		  (d.actual_date  BETWEEN '''+ CONVERT(char(10),@BeginDate,101) +''' AND '''+ CONVERT(char(10),@EndDate,101)+''')
		GROUP BY
		  s.region, 
		  tsf.store_key,
		  tsf.transaction_id, 
		  tsf.GAAP_Sale,
		  tsf.Gift_Card_Sold,
		  tsf.gift_card_only
		HAVING
		  ( 
		  sum(tsf.GAAP_Sale)  >=  35
		  )

		
	) a


	LEFT JOIN (	SELECT DISTINCT transaction_id
				FROM dbo.discount_facts df (nolock)
				JOIN dbo.Line_Object_Dim lo on df.line_object_key = lo.line_object_key
				WHERE lo.Line_Object  IN  (1625, 1626)
			  ) discount_fact 

	ON discount_fact.transaction_id = a.JackFact_transaction_id

	--ORDER BY a.JackFact_transaction_id
) b

JOIN dbo.store_dim sd on b.store_key = sd.store_key
GROUP BY	sd.store_id,sd.store_name,
			sd.bearritory,
			sd.region'
--select @SQL
exec sp_executesql @SQL
```

