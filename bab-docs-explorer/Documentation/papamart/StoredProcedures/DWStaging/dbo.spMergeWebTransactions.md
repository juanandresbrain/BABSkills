# dbo.spMergeWebTransactions

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeWebTransactions"]
    dbo_WebTransactions(["dbo.WebTransactions"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WebTransactions |

## Stored Procedure Code

```sql
CREATE proc spMergeWebTransactions

as

-------------------------------------------------------------------------
-- spMergeWebTransactions
-- 2017-10-18- Dan Tweedie - Created Proc
-------------------------------------------------------------------------

set nocount on


Merge into dw.dbo.WebTransactions as target
Using dwstaging.dbo.WebTransactions as source
On (
			target.TransactionID = source.TransactionID
			and
			target.TransactionNum = source.TransactionNum
	)
when matched 
	and
		(
			target.TransactionDateTime <> source.TransactionDateTime
			OR
			target.TaxAmount <> source.TaxAmount
			OR
			target.TaxJurisdiction <> source.TaxJurisdiction
		)
		then UPDATE
			set
				target.TransactionDateTime = source.TransactionDateTime,
				target.TaxAmount = source.TaxAmount,
				target.TaxJurisdiction = source.TaxJurisdiction,
				target.UpdateDate = getdate()
When Not Matched By Target 
	Then 
		Insert (
					TransactionID,
					TransactionNum,
					TransactionDateTime,
					TaxAmount,
					TaxJurisdiction,
					InsertDate,
					UpdateDate
				)
		Values (	
					source.TransactionID,
					source.TransactionNum,
					source.TransactionDateTime,
					source.TaxAmount,
					source.TaxJurisdiction,
					getdate(),
					getdate()
				)
;
```

