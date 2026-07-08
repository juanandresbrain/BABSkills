# dbo.vwDW_Extract_Line_Notes_BAK20240202

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Extract_Line_Notes_BAK20240202"]
    av_line_note(["av_line_note"]) --> VIEW
    av_tax_detail(["av_tax_detail"]) --> VIEW
    dwETL_Transactions_To_Pull(["dwETL_Transactions_To_Pull"]) --> VIEW
    line_note(["line_note"]) --> VIEW
    tax_detail(["tax_detail"]) --> VIEW
    transaction_header(["transaction_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| av_line_note |
| av_tax_detail |
| dwETL_Transactions_To_Pull |
| line_note |
| tax_detail |
| transaction_header |

## View Code

```sql
-- =====================================================================================================
-- Name: vwDW_Extract_Line_Notes
--
-- Description:	Extract Line Notes from Audit works based upon the
--			transaction numbers loaded into 
--
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Gary Murrish	4/20/2013		Created
--		Gary Murrish	12/31/2013		Blocked duplicates from Archive
--		Dan Tweedie		07/28/2016		Cast line_note as nvarchar to aid in handling Chinese characters in SSIS load
--		Dan Tweedie		2023-08-08		Derived new line_note by removing 'PRM', 'DM', 'CPN' which are from Jump Mind and not in our coupon dim
--		Tim Callahan	2023-10-05		Added CTE\UNION to Get UK VAT Tax Data from Tax Detail Tables
--										This is due to instances where VAT Tax Line notes did not come through via a non Aptos sales interface
-- =====================================================================================================
CREATE VIEW [dbo].[vwDW_Extract_Line_Notes_BAK20240202]
AS

--with
--Prep as
--	(
--		SELECT
--			trig.transaction_id,
--			ln.line_id,
--			ln.note_type,
--			cast(ln.line_note as nvarchar) as line_note
--		FROM
--			dwETL_Transactions_To_Pull trig WITH (NOLOCK)
--			INNER JOIN line_note ln WITH (NOLOCK)
--				ON trig.transaction_id = ln.transaction_id
--		UNION ALL
--		SELECT
--			trig.transaction_id,
--			ln.line_id,
--			ln.note_type,
--			cast(ln.line_note as nvarchar) as line_note
--		FROM
--			dwETL_Transactions_To_Pull trig WITH (NOLOCK)
--			INNER JOIN av_line_note ln WITH (NOLOCK)
--				ON trig.transaction_id = ln.av_transaction_id
--			LEFT JOIN transaction_header th WITH (NOLOCK)
--				ON trig.transaction_id = th.transaction_id
--			WHERE th.transaction_id IS null
--	)
-- Replaced Above on 10/5/2023

with 
Prep as

(


		SELECT
			trig.transaction_id,
			ln.line_id,
			ln.note_type,
			cast(ln.line_note as nvarchar) as line_note
		FROM dwETL_Transactions_To_Pull trig WITH (NOLOCK)	
				INNER JOIN line_note ln WITH (NOLOCK) ON trig.transaction_id = ln.transaction_id
		where ln.note_type <> 35 -- 35 = VAT Note Type 
			UNION ALL
			-- Union in VAT Line Notes 
		SELECT
			trig.transaction_id,
			ln.line_id,
			ln.note_type,
			cast (cast(ln.line_note as numeric (35,6)) as nvarchar) as line_note
		FROM dwETL_Transactions_To_Pull trig WITH (NOLOCK)
			INNER JOIN line_note ln WITH (NOLOCK)ON trig.transaction_id = ln.transaction_id
		where ln.note_type = 35 -- 35 = VAT Note Type 
		
			-- Union In Archive TAbles 
			union all 
			
		SELECT
			trig.transaction_id,
			ln.line_id,
			ln.note_type,
			cast(ln.line_note as nvarchar) as line_note 					
		FROM dwETL_Transactions_To_Pull trig WITH (NOLOCK)
			INNER JOIN av_line_note ln WITH (NOLOCK) ON trig.transaction_id = ln.av_transaction_id
			LEFT JOIN transaction_header th WITH (NOLOCK) ON trig.transaction_id = th.transaction_id
		WHERE th.transaction_id IS null		
			and ln.note_type <> 35-- 35 = VAT Note Type 

			union all 
			-- Union in Archive VAT Line Notes 
		SELECT
			trig.transaction_id,
			ln.line_id,
			ln.note_type,
			cast (cast(ln.line_note as numeric (35,6)) as nvarchar) as line_note
		FROM dwETL_Transactions_To_Pull trig WITH (NOLOCK)
			INNER JOIN av_line_note ln WITH (NOLOCK) ON trig.transaction_id = ln.av_transaction_id
			LEFT JOIN transaction_header th WITH (NOLOCK) ON trig.transaction_id = th.transaction_id
		WHERE th.transaction_id IS null		
			and ln.note_type = 35 -- 35 = VAT Note Type 

) 


-- Added on 10/5/2023
,VatFromTaxDetail  as
(

	select 
	td.transaction_id, 
	td.line_id, 
	cast (35 as int) as note_type, 
	cast (cast (sum (td.tax_amount_expected) as nvarchar)as numeric (35,6)) as line_note
	from tax_detail td (nolock) 
	join dwETL_Transactions_To_Pull trig (NOLOCK) on trig.transaction_id=td.transaction_id
	where 1=1
	and td.tax_jurisdiction in ('GBP') -- Ireland (EIRE) include? They dont have JM pos yet so fix should be in before then 
	and td.applied_by_line_id is null  -- A None full value is Indicative of Discount Tax Detail - These do not appear to be in the Aptos POS line notes 
	--and td.transaction_id in ('481464873')  -- Testing Only
	group by 
	td.transaction_id, 
	td.line_id
		union
	select 
	td.av_transaction_id as transaction_id , 
	td.line_id, 
	cast (35 as int) as note_type, 
	cast (cast (sum (td.tax_amount_expected) as nvarchar)as numeric (35,6)) as line_note
	from av_tax_detail td (nolock) 
	join dwETL_Transactions_To_Pull trig (nolock) on trig.transaction_id=td.av_transaction_id
	left join transaction_header th (nolock) on trig.transaction_id = th.transaction_id
	where 1=1
	and th.transaction_id is null 
	and td.tax_jurisdiction in ('GBP') -- Ireland (EIRE) include? They dont have JM pos yet so fix should be in before then 
	and td.applied_by_line_id is null  -- A None full value is Indicative of Discount Tax Detail - These do not appear to be in the Aptos POS line notes 
	--and td.av_transaction_id in ('481464873') -- Testing Only
	group by 
	td.av_transaction_id,
	td.line_id

), 


Summary1 as
(

select
	transaction_id,
	line_id,
	note_type,
	cast(replace(replace(replace(line_note, 'PRM',''), 'DM',''), 'CPN','') as nvarchar) as line_note
from Prep
where line_note<>' '
	union 
select 
	transaction_id, 
	line_id, 
	note_type, 
	cast (line_note as nvarchar) as line_note
from VatFromTaxDetail v

) 

select
transaction_id, 
line_id, 
note_type, 
max (line_note) as line_note -- With the alternate VAT source it seems like some rounding is in play with non aptos sales interface feed, so I will except the higher value
from Summary1 s
group by
transaction_id, 
line_id, 
note_type
```

