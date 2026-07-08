# dbo.spDW_DetermineTransactionsToPull_Dynamics

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDW_DetermineTransactionsToPull_Dynamics"]
    av_transaction_header(["av_transaction_header"]) --> SP
    av_transaction_line(["av_transaction_line"]) --> SP
    dwETL_Transactions_To_Pull_Dynamics(["dwETL_Transactions_To_Pull_Dynamics"]) --> SP
    transaction_header(["transaction_header"]) --> SP
    transaction_line(["transaction_line"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| av_transaction_header |
| av_transaction_line |
| dwETL_Transactions_To_Pull_Dynamics |
| transaction_header |
| transaction_line |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spDW_DetermineTransactionsToPull_Dynamics]
    @numDaysHorizon int = 15
AS
	-- =====================================================================================================
	-- Name: spAuditReload
	--
	-- Description:	Determine the transactions which need to be pulled back to the Data Warehouse.
	--				They are stored in the table dwETL_Transactions_To_Pull
	--
	-- Input:	
	--			Days Horizon - The number of days to go back
	--
	-- Output: Resultset with the following columns:
	--			N/A
	--
	-- Dependencies: None
	--
	--GRANT  SELECT ,  UPDATE ,  INSERT ,  DELETE  ON [dbo].[dwETL_Transactions_To_Pull]  TO [pm_repo]
	--GRANT  SELECT ,  UPDATE ,  INSERT ,  DELETE  ON [dbo].[dwETL_Transactions_To_Pull]  TO [link_readonly]
	--
	-- Revision History
	--		Name:			Date:			Comments:
	--		Gary Murrish	7/8/2013		Initial Deployment
	--		Gary Murrish	12/31/2013		Added two stage insert because of dups.
	--		Dan Tweedie		06/15/2016		Added inclusion of transaction_series 'C' when the line_object is 106 and line_action in (8,90,99) (Enterprise Selling)
	-- =====================================================================================================

DECLARE @asOfDate datetime
SET @asOfDate = DATEADD(D, -1 * @numDaysHorizon, DATEDIFF(dd, 0, GETDATE()))

-- NOTE THAT THERE ARE TWO SETS OF EXTRACTION FROM AUDITWORKS,
--	1. The current records
--	2. The archived records

-- ---------------------------------------------------------
-- Get the records from the "Active" tables
-- ---------------------------------------------------------
SELECT
	th.transaction_id,
	th.store_no,
	th.register_no,
	th.transaction_no,
	th.cashier_no,
	th.transaction_category,
	th.transaction_series,
	th.transaction_date,
	th.entry_date_time,
	th.tender_total
INTO #tmpTrans
FROM
	transaction_header th WITH (NOLOCK)
	--WHERE
	--	th.transaction_date >= @asOfDate
	--	AND th.transaction_series IN ('P', '', 'D', 'F', 'W', 'A')
	--	AND th.transaction_void_flag = 0
	--	AND th.transaction_category IN (1, 2, 10)
	--	AND NOT (th.store_no = 13
	--	AND th.register_no = 3
	--	AND th.transaction_date <= '1/31/2012'
	--	) -- Block for Web transactions per Jack McCormick 12/8/2011
WHERE
	(th.transaction_date >= @asOfDate) --or th.transaction_id=446853867)
	AND th.transaction_series IN ('P', '', 'D', 'F', 'W', 'A', 'C','B') --2022-10-30-- added B for Dynamics--2016-04-19 - Added C, Customer Liability (Customer Liability Maintenance), which happens when ES order is shipped (not picked up) 
	AND th.transaction_void_flag = 0
	AND th.transaction_category IN (1, 2, 10, 242) --2016-04-19 - Added 242 (C/L Import)
	AND NOT (th.store_no = 13 AND th.register_no = 3 AND th.transaction_date <= '1/31/2012') -- Block for Web transactions per Jack McCormick 12/8/2011
	and th.transaction_id<>458164492
	and th.transaction_id not in (471637209, 471640362) -- Temp Add on 4/13/2023
--	and th.transaction_date <= '08/30/2025' ---- Added as Part of Aptos Decom --Cutover Date as of Aug 14 2025 -- This will prevent sales from going to DW-Papamart
-- Now only pull the ones which have at least one of a certain type
-- drop table #hasLineObjects
SELECT
	t.transaction_id
INTO #hasLineObjects
FROM
	#tmpTrans t WITH (NOLOCK)
	INNER JOIN transaction_line tl WITH (NOLOCK)
		ON t.transaction_id = tl.transaction_id
		AND tl.line_void_flag = 0
	--WHERE
	--	(t.transaction_category IN (1, 2)
	--	AND tl.line_object_type <> 12)
	--	OR (t.transaction_category IN (10)
	--	AND (tl.line_object_type = 7
	--	OR tl.line_object BETWEEN 700 AND 799))
	--GROUP BY t.transaction_id
WHERE
	(t.transaction_category IN (1, 2) AND tl.line_object_type <> 12 and t.transaction_series <> 'C')
	OR 
	(t.transaction_category IN (10) AND (tl.line_object_type = 7 OR tl.line_object BETWEEN 700 AND 799) and t.transaction_series <> 'C')
	OR
	(t.transaction_category = 242 and tl.line_object = 106 and tl.line_action in (8,90,99) and t.transaction_series = 'C')  --new to include shipment cancels, fulfillments, returns
GROUP BY t.transaction_id

-- ---------------------------------------------------------
-- Get the records from the "Archive" tables
-- ---------------------------------------------------------
SELECT
	th.av_transaction_id AS transaction_id,
	th.store_no,
	th.register_no,
	th.transaction_no,
	th.cashier_no,
	th.transaction_category,
	th.transaction_series,
	th.transaction_date,
	th.entry_date_time,
	th.tender_total
INTO #tmpTransARC
FROM
	av_transaction_header th WITH (NOLOCK)
	--WHERE
	--	th.transaction_date >= @asOfDate
	--	AND th.transaction_series IN ('P', '', 'D', 'F', 'W', 'A')
	--	AND th.transaction_void_flag = 0
	--	AND th.transaction_category IN (1, 2, 10)
	--	AND NOT (th.store_no = 13
	--	AND th.register_no = 3
	--	AND th.transaction_date <= '1/31/2012'
	--	) -- Block for Web transactions per Jack McCormick 12/8/2011
WHERE
	(th.transaction_date >= @asOfDate) --or th.av_transaction_id=446853867)
	AND th.transaction_series IN ('P', '', 'D', 'F', 'W', 'A','C','B') --2016-04-19 - Added C, Customer Liability (Customer Liability Maintenance), which happens when ES order is shipped (not picked up) )
	AND th.transaction_void_flag = 0
	AND th.transaction_category IN (1, 2, 10, 242) --2016-04-19 - Added 242 (C/L Import)
	AND NOT (th.store_no = 13 AND th.register_no = 3 AND th.transaction_date <= '1/31/2012') -- Block for Web transactions per Jack McCormick 12/8/2011
--	and th.transaction_date <= '07/05/2025' -- Aptos Decom Cutover Date as of Jun 20 2025 -- This will prevent sales from going to DW-Papamart
-- Now only pull the ones which have at least one of a certain type
SELECT
	t.transaction_id
INTO #hasLineObjectsARC
FROM
	#tmpTransARC t WITH (NOLOCK)
	INNER JOIN av_transaction_line tl WITH (NOLOCK)
		ON t.transaction_id = tl.av_transaction_id
		AND tl.line_void_flag = 0
	--WHERE
	--	(t.transaction_category IN (1, 2)
	--	AND tl.line_object_type <> 12)
	--	OR (t.transaction_category IN (10)
	--	AND (tl.line_object_type = 7
	--	OR tl.line_object BETWEEN 700 AND 799))
	--GROUP BY t.transaction_id
WHERE
	(t.transaction_category IN (1, 2) AND tl.line_object_type <> 12 and t.transaction_series <> 'C')
	OR 
	(t.transaction_category IN (10) AND (tl.line_object_type = 7 OR tl.line_object BETWEEN 700 AND 799) and t.transaction_series <> 'C')
	OR 
	(t.transaction_category = 242 and tl.line_object = 106 and tl.line_action in (8,90,99) and t.transaction_series = 'C')  --new to include shipment cancels, fulfillments, returns
GROUP BY t.transaction_id

-- ---------------------------------------------------------
--	Now put the surviving records into 
--		dwETL_Transactions_To_Pull to get them working
-- ---------------------------------------------------------

TRUNCATE TABLE dwETL_Transactions_To_Pull_Dynamics

INSERT INTO dwETL_Transactions_To_Pull_Dynamics
	(	transaction_id,
		store_no,
		register_no,
		transaction_no,
		cashier_no,
		transaction_category,
		transaction_series,
		transaction_date,
		entry_date_time,
		tender_total)
	SELECT
		t.*
	FROM
		#tmpTrans t
		INNER JOIN #hasLineObjects lo WITH (NOLOCK)
			ON t.transaction_id = lo.transaction_id

-- Now insert the records from the archive table. It is done this way
--		because of duplicate transactions in the archive tables and the primary tables
INSERT INTO dwETL_Transactions_To_Pull_Dynamics
	(	transaction_id,
		store_no,
		register_no,
		transaction_no,
		cashier_no,
		transaction_category,
		transaction_series,
		transaction_date,
		entry_date_time,
		tender_total)
	SELECT
		t.*
	FROM
		#tmpTransARC t
		INNER JOIN #hasLineObjectsARC lo WITH (NOLOCK)
			ON t.transaction_id = lo.transaction_id
		--LEFT JOIN dwETL_Transactions_To_Pull ettp WITH (NOLOCK)
		LEFT JOIN dwETL_Transactions_To_Pull_Dynamics ettp WITH (NOLOCK) -- Replaced above on 1/11/2023
		ON t.transaction_id = ettp.transaction_id
		WHERE ettp.transaction_id IS null
			
--temp fix to prevent known bad transactions from going to DW
if (select count(*) from dwETL_Transactions_To_Pull_Dynamics where transaction_id = 378671016) > 0
	begin

		delete 
		from dwETL_Transactions_To_Pull_Dynamics
		where transaction_id = 378671016

	end
```

