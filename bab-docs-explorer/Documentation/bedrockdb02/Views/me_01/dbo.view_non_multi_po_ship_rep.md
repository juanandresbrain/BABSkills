# dbo.view_non_multi_po_ship_rep

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_non_multi_po_ship_rep"]
    dbo_po_shipment(["dbo.po_shipment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.po_shipment |

## View Code

```sql
CREATE view dbo.view_non_multi_po_ship_rep

AS

/*
View name: view_non_multi_po_ship_rep

Description: 

HISTORY (available through VC_UTIL prior to this date):
Date       			Name         		Def#			Desc
Jan. 30, 2013		Feng Li				141497		view_po_line_location_rep in CP220 result double line when print PO
*/


SELECT ps1.po_id, ps1.po_shipment_id, ps1.expected_receipt_date
FROM po_shipment ps1, 
     (SELECT po_id, count(*) [row_count]
      FROM po_shipment
      GROUP BY po_id) ps2
WHERE ps1.po_id = ps2.po_id
AND ps2.[row_count] = 1
```

