# dbo.on_order_reinstate_pack_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.on_order_reinstate_pack_$sp"]
    dbo_ib_pack_on_order(["dbo.ib_pack_on_order"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_pack_on_order |

## Stored Procedure Code

```sql
-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Create Procedure

-----------------------------------------------------------------------------------------------------------------------------

CREATE PROCEDURE dbo.on_order_reinstate_pack_$sp

	@PO_Number NVARCHAR(20)
	,@Return_Affected BIT = 0

AS

-- Called by:
	-- Class: STSIBOnOrder
	-- Method: OnOrderReInstate
	-- Assumption: the temp table #tt_ib_on_order has already been created

/*
CREATE TABLE #tt_ib_pack_on_order
   ( ib_pack_on_order_id DECIMAL(12,0) IDENTITY(1,1) NOT NULL
   , document_number NVARCHAR(20) NOT NULL
   , pack_id DECIMAL(12,0) NOT NULL, location_id SMALLINT NOT NULL
   , receipt_date SMALLDATETIME
   , transaction_type_code SMALLINT NOT NULL
	, on_order_units INT NOT NULL )
*/

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON

-----------------------------------------------------------------------------------------------------------------------------
--	Error Trapping: Check If Temp Table(s) Already Exist(s) And Drop If Applicable
-----------------------------------------------------------------------------------------------------------------------------

IF OBJECT_ID (N'tempdb.dbo.#cancelled_records', N'U') IS NOT NULL
BEGIN

	DROP TABLE dbo.#cancelled_records

END

DECLARE @Max_IB_Pack_On_Order_Id AS DECIMAL(13, 0)

SET @Max_IB_Pack_On_Order_Id = COALESCE((SELECT MAX (IPOO.ib_pack_on_order_id) FROM dbo.ib_pack_on_order IPOO WHERE IPOO.document_number = @PO_Number AND IPOO.transaction_type_code = 1130), 0)

SELECT
	IPOO.pack_id
	,IPOO.location_id
	,IPOO.receipt_date
	,SUM(IPOO.on_order_units) AS on_order_units

INTO dbo.#cancelled_records

FROM
	dbo.ib_pack_on_order IPOO
WHERE
	IPOO.document_number = @PO_Number
	AND IPOO.transaction_type_code = 1120
	AND ( @Max_IB_Pack_On_Order_Id = 0 OR IPOO.ib_pack_on_order_id > @Max_IB_Pack_On_Order_Id )
GROUP BY
	IPOO.pack_id
	,IPOO.location_id
	,IPOO.receipt_date
HAVING
	SUM(IPOO.on_order_units) <> 0	

INSERT INTO #tt_ib_pack_on_order
	(
		pack_id
		,document_number
		,location_id
		,receipt_date
		,transaction_type_code
		,on_order_units
	)
SELECT
	CR.pack_id
	,@PO_Number AS document_number
	,CR.location_id
	,CR.receipt_date
	,1130 AS transaction_type_code
	,-1 * CR.on_order_units AS on_order_units
FROM
	dbo.#cancelled_records CR

IF @Return_Affected = 1
BEGIN

	-- return following result set to IB which will convert this to an array to send back to POM
	-- this should only be done for a release PO
	SELECT
		CR.pack_id
		,CR.location_id
		,CR.receipt_date
		,CR.on_order_units AS on_order_units
	FROM
		dbo.#cancelled_records CR

END
ELSE
BEGIN

	SELECT
		CR.pack_id
		,CR.location_id
		,CR.receipt_date
		,CR.on_order_units AS on_order_units
	FROM
		dbo.#cancelled_records CR
	WHERE
		1 = 2

END
```

