# dbo.view_po_recv_dates

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_po_recv_dates"]
    dbo_po_shipment(["dbo.po_shipment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.po_shipment |

## View Code

```sql
create view dbo.view_po_recv_dates AS
SELECT	po_id,
	MAX(expected_receipt_date) last_receipt_date,
	MIN(expected_receipt_date) first_receipt_date
FROM	po_shipment
GROUP BY po_id
```

