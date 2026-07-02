# Job: MERCHANDISING - Process - WC Receipts

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures PO and Shipment receipts from data provided by DDC, sends to Pipeline to integrate into Merchandising.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WC Receipts"]
    JOB --> UNO_1["Step 1: UNO [TSQL]"]`n```

## Steps

### Step 1: UNO
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandising_Report_wcReceipts
```


