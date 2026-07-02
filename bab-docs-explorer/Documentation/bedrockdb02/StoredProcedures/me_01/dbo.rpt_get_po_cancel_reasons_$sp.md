# dbo.rpt_get_po_cancel_reasons_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.rpt_get_po_cancel_reasons_$sp"]
    dbo_po_cancellation_reason(["dbo.po_cancellation_reason"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.po_cancellation_reason |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[rpt_get_po_cancel_reasons_$sp]

AS

/*
Proc name:		rpt_get_po_cancel_reasons_$sp
Description:	Gets a list of PO Cancellation Reasons
*/


SELECT po_cancellation_reason_id, reason_code + N'  ' + description AS description
FROM po_cancellation_reason WITH (NOLOCK)
ORDER BY po_cancellation_reason_id

RETURN 0
```

