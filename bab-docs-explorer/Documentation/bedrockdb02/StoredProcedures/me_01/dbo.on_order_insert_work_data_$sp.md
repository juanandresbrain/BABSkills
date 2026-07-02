# dbo.on_order_insert_work_data_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.on_order_insert_work_data_$sp"]
    dbo_ib_on_order(["dbo.ib_on_order"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_on_order |

## Stored Procedure Code

```sql
-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Create Procedure
-----------------------------------------------------------------------------------------------------------------------------

CREATE PROCEDURE dbo.on_order_insert_work_data_$sp

	@Sku_Id DECIMAL(13, 0)
	,@Location_Id SMALLINT
	,@Expected_Receipt_Date SMALLDATETIME
	,@Transaction_Type_Code SMALLINT
	,@Price_Status_Id SMALLINT
	,@Units INT
	,@Cost DECIMAL(14, 2)
	,@Cost_Local DECIMAL(14, 2)
	,@Valuation_Retail DECIMAL(14, 2)
	,@Selling_Retail DECIMAL(14, 2)
	,@PO_Number NVARCHAR(20)
	,@Pack_Id DECIMAL(12, 0)
	,@PO_Receipt_Id DECIMAL(12, 0)
	,@Actual_Receipt_Date SMALLDATETIME = NULL
	,@Received_Quantity INT
	,@PO_Id DECIMAL(12, 0)
	,@PO_Shipment_Id SMALLINT

AS

--SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON

DECLARE @Post_Shipments BIT

IF NOT EXISTS 
	(
		SELECT 1 FROM ib_on_order WHERE document_number = @PO_Number
	)
	OR EXISTS
	(
		SELECT 1 FROM ib_on_order WHERE document_number = @PO_Number AND po_shipment_id IS NOT NULL
	)
	SET @Post_Shipments = 1
ELSE
	SET @Post_Shipments = 0

INSERT INTO #tt_ib_on_order
	(
		sku_id
		,location_id
		,receipt_date
		,transaction_type_code
		,price_status_id
		,on_order_units
		,on_order_cost
		,on_order_cost_local
		,on_order_valuation_retail
		,on_order_selling_retail
		,document_number
		,pack_id
		,po_receipt_id
		,actual_receipt_date
		,received_quantity
		,po_id
		,po_shipment_id
	)
SELECT
	@Sku_Id
	,@Location_Id
	,@Expected_Receipt_Date
	,@Transaction_Type_Code
	,@Price_Status_Id
	,@Units
	,@Cost
	,@Cost_Local
	,@Valuation_Retail
	,@Selling_Retail
	,@PO_Number
	,CASE WHEN @Pack_Id = -1 THEN NULL ELSE @Pack_Id END AS pack_id
	,CASE WHEN @PO_Receipt_Id = -1 THEN NULL ELSE @PO_Receipt_Id END AS po_receipt_id
	,@Actual_Receipt_Date
	,CASE WHEN @Received_Quantity = -1 THEN NULL ELSE @Received_Quantity END AS received_quantity
	,(CASE 
			WHEN @PO_Id = -1 OR @Post_Shipments = 0 THEN NULL
			ELSE @PO_Id END) AS po_id
	,(CASE 
			WHEN @PO_Shipment_Id = -1 OR @Post_Shipments = 0 THEN NULL
			ELSE @PO_Shipment_Id END) AS po_shipment_id
```

