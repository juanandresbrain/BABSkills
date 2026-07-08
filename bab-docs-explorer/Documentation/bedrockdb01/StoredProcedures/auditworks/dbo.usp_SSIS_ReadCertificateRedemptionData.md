# dbo.usp_SSIS_ReadCertificateRedemptionData

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_SSIS_ReadCertificateRedemptionData"]
    dbo_Ld_POS_Audits(["dbo.Ld_POS_Audits"]) --> SP
    av_transaction_header(["av_transaction_header"]) --> SP
    dbo_av_transaction_header(["dbo.av_transaction_header"]) --> SP
    av_transaction_line(["av_transaction_line"]) --> SP
    dbo_avtransactions_2004(["dbo.avtransactions_2004"]) --> SP
    dbo_avtransactions_2005(["dbo.avtransactions_2005"]) --> SP
    dbo_avtransactions_2006(["dbo.avtransactions_2006"]) --> SP
    dbo_avtransactions_2007(["dbo.avtransactions_2007"]) --> SP
    transaction_header(["transaction_header"]) --> SP
    dbo_transaction_header(["dbo.transaction_header"]) --> SP
    transaction_line(["transaction_line"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Ld_POS_Audits |
| av_transaction_header |
| dbo.av_transaction_header |
| av_transaction_line |
| dbo.avtransactions_2004 |
| dbo.avtransactions_2005 |
| dbo.avtransactions_2006 |
| dbo.avtransactions_2007 |
| transaction_header |
| dbo.transaction_header |
| transaction_line |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[usp_SSIS_ReadCertificateRedemptionData]

	@prev_max_transaction_id int

AS
-- =====================================================================================================
-- Name: usp_SSIS_ReadCertificateRedemptionData
--
-- Description:	
--
-- Input:	
--			
--
-- Output: Resultset with the following columns:
--			
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Garyd			08/30/2010		Initial version in source control
-- exec usp_SSIS_ReadCertificateRedemptionData  @prev_max_transaction_id = 167026010
-- =====================================================================================================

BEGIN

	SET NOCOUNT ON;

	SELECT transaction_id, store_no, transaction_no, reference_no, CAST(SUBSTRING(reference_no, PATINDEX('%[1-9]%', reference_no), 9) AS int) AS reference_no_for_crm, transaction_date
		,gross_line_amount
	FROM
	(
		SELECT tl.av_transaction_id AS transaction_id, th.store_no, th.transaction_no, tl.reference_no, th.transaction_date, tl.gross_line_amount - ISNULL(tl_adj.gross_line_amount, 0) AS gross_line_amount
		FROM (SELECT DISTINCT transaction_id FROM dbo.Ld_POS_Audits) a
		INNER JOIN dbo.av_transaction_header th ON th.av_transaction_id = a.transaction_id
			AND th.transaction_void_flag = 0
		INNER JOIN av_transaction_line tl ON tl.av_transaction_id = th.av_transaction_id
			AND line_void_flag = 0
			-- line action of 25 is a redemption
			AND line_action = 25
		LEFT JOIN av_transaction_line tl_adj ON tl_adj.av_transaction_id = tl.av_transaction_id
			AND tl_adj.line_action = 13
			AND tl_adj.line_object = 1130
			AND tl.reference_no = (SELECT MAX(tl2.reference_no) FROM av_transaction_line tl2 WHERE tl2.av_transaction_id = th.av_transaction_id AND tl2.line_void_flag = 0 AND tl2.line_action = 25 AND tl2.reference_type = 31)
		WHERE tl.reference_type = 31
			AND th.store_no <> 990

		UNION

		SELECT tl.av_transaction_id AS transaction_id, th.store_no, th.transaction_no, tl.reference_no, th.transaction_date, tl.gross_line_amount - ISNULL(tl_adj.gross_line_amount, 0) AS gross_line_amount
		FROM av_transaction_header th
		INNER JOIN av_transaction_line tl ON tl.av_transaction_id = th.av_transaction_id
			AND line_void_flag = 0
			-- line action of 25 is a redemption
			AND line_action = 25
		LEFT JOIN av_transaction_line tl_adj ON tl_adj.av_transaction_id = tl.av_transaction_id
			AND tl_adj.line_action = 13
			AND tl_adj.line_object = 1130
			AND tl.reference_no = (SELECT MAX(tl2.reference_no) FROM av_transaction_line tl2 WHERE tl2.av_transaction_id = th.av_transaction_id AND tl2.line_void_flag = 0 AND tl2.line_action = 25 AND tl2.reference_type = 31)
		WHERE tl.reference_type = 31
			AND th.store_no <> 990
			AND tl.av_transaction_id > @prev_max_transaction_id
			AND th.transaction_void_flag = 0
	) t

	UNION ALL

	SELECT transaction_id, store_no, transaction_no, reference_no, CAST(SUBSTRING(reference_no, PATINDEX('%[1-9]%', reference_no), 9) AS int) AS reference_no_for_crm, transaction_date
		,gross_line_amount
	FROM
	(
		SELECT tl.transaction_id, th.store_no, th.transaction_no, tl.reference_no, th.transaction_date, tl.gross_line_amount - ISNULL(tl_adj.gross_line_amount, 0) AS gross_line_amount
		FROM (SELECT DISTINCT transaction_id FROM dbo.Ld_POS_Audits) a
		INNER JOIN dbo.transaction_header th ON th.transaction_id = a.transaction_id
			AND th.transaction_void_flag = 0
		INNER JOIN transaction_line tl ON tl.transaction_id = th.transaction_id
			AND line_void_flag = 0
			-- line action of 25 is a redemption
			AND line_action = 25
		LEFT JOIN transaction_line tl_adj ON tl_adj.transaction_id = tl.transaction_id
			AND tl_adj.line_action = 13
			AND tl_adj.line_object = 1130
			AND tl.reference_no = (SELECT MAX(tl2.reference_no) FROM transaction_line tl2 WHERE tl2.transaction_id = th.transaction_id AND tl2.line_void_flag = 0 AND tl2.line_action = 25 AND tl2.reference_type = 31)
		WHERE tl.reference_type = 31
			AND th.store_no <> 990

		UNION

		SELECT tl.transaction_id, th.store_no, th.transaction_no, tl.reference_no, th.transaction_date, tl.gross_line_amount - ISNULL(tl_adj.gross_line_amount, 0) AS gross_line_amount
		FROM transaction_header th
		INNER JOIN transaction_line tl ON tl.transaction_id = th.transaction_id
			AND line_void_flag = 0
			-- line action of 25 is a redemption
			AND line_action = 25
		LEFT JOIN transaction_line tl_adj ON tl_adj.transaction_id = tl.transaction_id
			AND tl_adj.line_action = 13
			AND tl_adj.line_object = 1130
			AND tl.reference_no = (SELECT MAX(tl2.reference_no) FROM transaction_line tl2 WHERE tl2.transaction_id = th.transaction_id AND tl2.line_void_flag = 0 AND tl2.line_action = 25 AND tl2.reference_type = 31)
		WHERE tl.reference_type = 31
			AND th.store_no <> 990
			AND tl.transaction_id > @prev_max_transaction_id
			AND th.transaction_void_flag = 0
	) t


UNION 

select * FROM auditworks.dbo.avtransactions_2006 --209471 (OURSBLANC)
	where transaction_id > @prev_max_transaction_id

UNION

select * from auditworks.dbo.avtransactions_2004  --16904 (OURSBLANC)
	where transaction_id > @prev_max_transaction_id

UNION 

select * from auditworks.dbo.avtransactions_2005  --57697 (OURSBLANC)
	where transaction_id > @prev_max_transaction_id

UNION 

select * from auditworks.dbo.avtransactions_2007 --138820 
	where transaction_id > @prev_max_transaction_id




END
```

