# dbo.spAuditDiscountFix

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAuditDiscountFix"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE procedure [dbo].[spAuditDiscountFix]
as
-- =====================================================================================================
-- Name: spAuditDiscountFix
--
-- Description:	
--
-- Input:	
--			N/A
--
-- Output: Resultset with the following columns:
--			N/A
--
-- Dependencies: None
--
-- Revision History
--		Name:				Date:			Comments:
--		?					08/24/2010		Initial version source control
--		Paul Beckman		04/02/2013		Remarked out Delete, Flag as Audit, a Log sections due to this
--											causing data integrity issues in SA.
-- =====================================================================================================

--*****************CURRENT tables*****************************************************************
if exists (select * from tempdb..sysobjects where name like '#tline%' and sysstat & 0xf = 3)
	begin	
		drop table dbo.#tline
	end

/*  === THESE SECTIONS REMARKED OUT 02 APR 2013 ===
select h.store_no, h.transaction_date, l.transaction_id, l.line_id, max(l.line_sequence) as line_sequence, sum(COALESCE(l.gross_line_amount,0)) as gross_line_amount, sum(COALESCE(d.pos_discount_amount,0)) as pos_discount_amount
into #tline
from transaction_header h
	join transaction_line l on h.transaction_id = l.transaction_id
	 left join discount_detail d on l.transaction_id = d.transaction_id and l.line_id = d.applied_by_line_id 
where --h.store_no = 13 and 
l.line_object_type in (16,17,18,19)
and d.transaction_id is null  
and l.line_void_flag = 0
and l.gross_line_amount <> 0
group by h.store_no, h.transaction_date, l.transaction_id, l.line_id, l.line_sequence
order by h.store_no, h.transaction_date, l.transaction_id, l.line_id, l.line_sequence

-- select * from #tline 
-- select * from transaction_header where transaction_id = 27136517
-- select * from transaction_line l
-- where l.transaction_id = 27136517
-- select * from audit_dw_extradiscounts

--Delete the incorrect transaction_line row
delete l
from transaction_line l
	join #tline t on l.transaction_id = t.transaction_id
		and l.line_id = t.line_id
		and l.line_sequence = t.line_sequence

--flag as an AUDIT--
update transaction_header
set last_modified_date_time = getdate()
where transaction_id in (select transaction_id from #tline)

--log------
INSERT INTO auditworks.dbo.audit_dw_extradiscounts(store_no, transaction_date, transaction_id, line_id, line_sequence, gross_line_amount, pos_discount_amount)
select store_no, transaction_date, transaction_id, line_id, line_sequence, gross_line_amount, pos_discount_amount
from #tline
*/


--*****************HISTORICAL tables****************************************************************
-- if exists (select * from tempdb..sysobjects where name like '#avtline%' and sysstat & 0xf = 3)
-- 	begin	
-- 		drop table dbo.#avtline
-- 	end
-- 
-- 
-- select h.store_no, h.transaction_date, l.av_transaction_id, l.line_id, max(l.line_sequence) as line_sequence, sum(COALESCE(l.gross_line_amount,0)) as gross_line_amount, sum(COALESCE(d.pos_discount_amount,0)) as pos_discount_amount
-- into #avtline
-- from av_transaction_header h
-- 	join av_transaction_line l on h.av_transaction_id = l.av_transaction_id
-- 	 left join av_discount_detail d on l.av_transaction_id = d.av_transaction_id and l.line_id = d.applied_by_line_id 
-- where h.store_no in (13, 136) and 
-- l.line_object_type in (16,17,18,19)
-- and d.av_transaction_id is null  
-- and l.line_void_flag = 0
-- and l.gross_line_amount <> 0
-- group by h.store_no, h.transaction_date, l.av_transaction_id, l.line_id, l.line_sequence
-- --order by h.store_no, h.transaction_date, l.av_transaction_id, l.line_id, l.line_sequence
-- 
-- 
-- --Delete the incorrect transaction_line row
-- delete l
-- from av_transaction_line l
-- 	join #avtline t on l.av_transaction_id = t.av_transaction_id
-- 		and l.line_id = t.line_id
-- 		and l.line_sequence = t.line_sequence
-- 
-- --flag as an AUDIT--
-- update av_transaction_header
-- set last_modified_date_time = getdate()
-- where av_transaction_id in (select av_transaction_id from #avtline)
```

