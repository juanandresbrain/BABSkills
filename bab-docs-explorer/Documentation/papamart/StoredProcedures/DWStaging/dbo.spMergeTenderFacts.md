# dbo.spMergeTenderFacts

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeTenderFacts"]
    aw_Transaction_Header(["aw_Transaction_Header"]) --> SP
    SALES_TRN_STG_TNDR(["SALES_TRN_STG_TNDR"]) --> SP
    tdf(["tdf"]) --> SP
    dbo_tender_facts(["dbo.tender_facts"]) --> SP
    tmpAWTenderMergeSource(["tmpAWTenderMergeSource"]) --> SP
    tmpTenderFactsKey(["tmpTenderFactsKey"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| aw_Transaction_Header |
| SALES_TRN_STG_TNDR |
| tdf |
| dbo.tender_facts |
| tmpAWTenderMergeSource |
| tmpTenderFactsKey |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeTenderFacts] 

as

set nocount on

--==========================================================================================================================================
-- Dan Tweedie 2020-07-01	Created proc to replace SCD plugin for SSIS 2008 to merge inserts/updates/deletes into tender_facts
--==========================================================================================================================================

--Stage the Merge Source Data
IF (Object_ID('dwstaging..tmpAWTenderMergeSource') IS NOT NULL) DROP TABLE tmpAWTenderMergeSource
SELECT
	CAST(STST.Transaction_ID AS int) AS Transaction_ID,
	STST.tender_key,
	MAX(ath.store_key) AS store_key,
	MAX(ath.date_key) AS date_key,
	SUM(STST.Gross_Line_Amount) AS tender_amt,
	COUNT(*) AS tender_count
into tmpAWTenderMergeSource
FROM
	SALES_TRN_STG_TNDR STST WITH (NOLOCK)
	INNER JOIN aw_Transaction_Header ath WITH (NOLOCK)
		ON STST.Transaction_ID = ath.Transaction_ID
GROUP BY	STST.Transaction_ID,
			STST.tender_key
	
---=========================
-- BEGIN DELETE PROCEDURE --
---=========================
--stage the tender_facts_key for transactions in DW that are within the same date range as the merge source, but transactions are not in the merge source
--these transactions will be deleted from tender_facts
IF (Object_ID('dwstaging..tmpTenderFactsKey') IS NOT NULL) DROP TABLE tmpTenderFactsKey;
with MinDate as
	(
		select --:
			min(date_key) MinDate,
			max(date_key) MaxDate
		from tmpAWTenderMergeSource
	)
select tdf.tender_facts_key 
into tmpTenderFactsKey
from MinDate md 
join dw.dbo.tender_facts tdf with (nolock) on tdf.date_key between md.MinDate and md.MaxDate
left join tmpAWTenderMergeSource ms on
	tdf.transaction_id=ms.transaction_id
	and
	tdf.tender_key=ms.tender_key
where ms.transaction_id is null
group by tdf.tender_facts_key

--if there are transaction in tender_facts which are not in the stage data, but are for the same date range, delete from tender_facts
if (select count(*) from tmpTenderFactsKey) > 0
begin
	delete tdf
	from dw.dbo.tender_facts tdf
	join tmpTenderFactsKey tdfk on tdf.tender_facts_key=tdfk.tender_facts_key
end
---=========================
-- END DELETE PROCEDURE --
---=========================
;
---======================================
-- BEGIN MERGE FOR INSERTS AND UPDATES --
---======================================
merge into dw.dbo.tender_facts as target
using tmpAWTenderMergeSource as source
on
	target.transaction_id=source.transaction_id
	and
	target.tender_key=source.tender_key
when matched 
	and 
	(
		isnull(target.store_key,0)<>isnull(source.store_key,0) or					
		isnull(target.date_key,0)<>isnull(source.date_key,0) or
		isnull(target.tender_amt,0)<>isnull(source.tender_amt,0) or
		isnull(target.tender_count,0)<>isnull(source.tender_count,0)
	)
then update
	set
		target.store_key=source.store_key,					
		target.date_key=source.date_key,
		target.tender_amt=source.tender_amt,
		target.tender_count=source.tender_count,
		target.updt_dt=getdate()
when not matched by target
then insert
	(
		transaction_id,
		tender_key,
		store_key,
		date_key,
		tender_amt,
		tender_count,
		ins_dt
	)
values
	(
		source.transaction_id,
		source.tender_key,
		source.store_key,
		source.date_key,
		source.tender_amt,
		source.tender_count,
		getdate()
	)
;
---======================================
-- END MERGE FOR INSERTS AND UPDATES --
---======================================



IF (Object_ID('dwstaging..tmpAWTenderMergeSource') IS NOT NULL) DROP TABLE tmpAWTenderMergeSource
IF (Object_ID('dwstaging..tmpTenderFactsKey') IS NOT NULL) DROP TABLE tmpTenderFactsKey;
```

