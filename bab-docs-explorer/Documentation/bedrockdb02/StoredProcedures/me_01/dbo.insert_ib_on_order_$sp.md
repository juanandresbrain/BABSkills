# dbo.insert_ib_on_order_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.insert_ib_on_order_$sp"]
    dbo_ib_on_order(["dbo.ib_on_order"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_on_order |

## Stored Procedure Code

```sql
CREATE proc [dbo].[insert_ib_on_order_$sp] 

(@skuId decimal(12,0), 
@locationId decimal(12,0), 
@expectedReceiptDate DATETIME,
@transactionTypeCode decimal(12,0),
@priceStatusId decimal(12,0),
@onOrderUnits decimal(12,0),
@onOrderCost decimal(14,2),
@onOrderCostLocal decimal(14,2),
@onOrderValuationRetail decimal(14,2),
@onOrderSellingRetail decimal(14,2),
@documentNumber nvarchar(20),
@packId decimal(12,0),
@poReceiptId decimal(12,0),
@actualReceiptDate DATETIME,
@receivedQuantity decimal(12,0))
AS 
/*
HISTORY: 
Date       Name         Def#      	Desc

Nov 5, 09  Yan Ding                 support total_on_order_cost_local
*/


insert into ib_on_order (sku_id,location_id,receipt_date,transaction_type_code,price_status_id,on_order_units,
on_order_cost,on_order_cost_local,on_order_valuation_retail,on_order_selling_retail,document_number,pack_id
,po_receipt_id
,actual_receipt_date
,received_quantity 
) values 
(@skuId,@locationId,@expectedReceiptDate,@transactionTypeCode,
@priceStatusId,@onOrderUnits,@onOrderCost,@onOrderCostLocal,
@onOrderValuationRetail,@onOrderSellingRetail,@documentNumber,@packId
,@poReceiptId
,@actualReceiptDate
,@receivedQuantity)
```

