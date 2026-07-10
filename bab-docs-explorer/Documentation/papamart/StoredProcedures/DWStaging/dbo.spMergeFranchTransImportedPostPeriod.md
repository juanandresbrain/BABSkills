# dbo.spMergeFranchTransImportedPostPeriod

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeFranchTransImportedPostPeriod"]
    dbo_FranchTransImportedPostPeriod(["dbo.FranchTransImportedPostPeriod"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.FranchTransImportedPostPeriod |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeFranchTransImportedPostPeriod]

as

set nocount on

merge into dw.dbo.FranchTransImportedPostPeriod as target
Using dwstaging.dbo.FranchTransImportedPostPeriod as source
on 
	(
		isnull(target.Franchisee,'xx') = isnull(source.Franchisee,'xx')
		and 
		isnull(target.TransactionID,'xx') = isnull(source.TransactionID,'xx')
	)
when matched 
	and
		(
			isnull(target.TransactionDate, '3030-12-31') <> isnull(source.TransactionDate, '3030-12-31')
			OR
			isnull(target.ImportDate, '3030-12-31') <> isnull(source.ImportDate, '3030-12-31')
			OR
			isnull(target.PreviousPeriodCutoffDate, '3030-12-31') <> isnull(source.PreviousPeriodCutoffDate, '3030-12-31')
			OR
			isnull(target.TransactionPayment,0) <> isnull(source.TransactionPayment,0)
			OR
			isnull(target.GrossSales,0) <> isnull(source.GrossSales,0)
			OR
			isnull(target.GiftCardAmount,0) <> isnull(source.GiftCardAmount,0)
			OR
			isnull(target.OriginalGrossSales,0) <> isnull(source.OriginalGrossSales,0)
			OR
			isnull(target.OriginalGiftCardAmount,0) <> isnull(source.OriginalGiftCardAmount,0)
			OR 
			isnull(target.OriginalInsertDate, '3030-12-31') <> isnull(source.OriginalInsertDate, '3030-12-31')
		)
	then 
		UPDATE
			SET
				target.TransactionDate=source.TransactionDate,
				target.ImportDate=source.ImportDate,
				target.PreviousPeriodCutoffDate=source.PreviousPeriodCutoffDate,
				target.TransactionPayment=source.TransactionPayment,
				target.GrossSales=source.GrossSales,
				target.GiftCardAmount=source.GiftCardAmount,
				target.UpdateDate=getdate()
when NOT MATCHED by Target
	then
		Insert
			(
				Franchisee,
				TransactionID,
				TransactionDate,
				PreviousPeriodCutoffDate,
				ImportDate,
				TransactionPayment,
				GrossSales,
				GiftCardAmount,
				OriginalGrossSales,
				OriginalGiftCardAmount,
				StoreID,
				OriginalInsertDate,
				InsertDate
			)
		values
			(
				source.Franchisee,
				source.TransactionID,
				source.TransactionDate,
				source.PreviousPeriodCutoffDate,
				source.ImportDate,
				source.TransactionPayment,
				source.GrossSales,
				source.GiftCardAmount,
				source.OriginalGrossSales,
				source.OriginalGiftCardAmount,
				source.StoreID,
				source.OriginalInsertDate,
				getdate()
			)

;
```

