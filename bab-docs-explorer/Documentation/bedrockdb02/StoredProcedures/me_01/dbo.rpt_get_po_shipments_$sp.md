# dbo.rpt_get_po_shipments_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_get_po_shipments_$sp"]
    dbo_po_shipment(["dbo.po_shipment"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.po_shipment |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[rpt_get_po_shipments_$sp] @po_id decimal(12, 0)

AS

/*
Proc name:		rpt_get_po_shipments_$sp
Description:	Gets the PO shipment data for a PO
*/


SELECT expected_receipt_date, estimated_shipment_percent, po_id, po_shipment_id
FROM po_shipment WITH (NOLOCK)
WHERE po_id = @po_id
ORDER BY expected_receipt_date, po_shipment_id

RETURN 0
```

