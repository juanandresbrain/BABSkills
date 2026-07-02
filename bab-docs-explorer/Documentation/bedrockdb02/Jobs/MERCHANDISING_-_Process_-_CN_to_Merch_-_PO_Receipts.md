# Job: MERCHANDISING - Process - CN to Merch - PO Receipts

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - CN to Merch - PO Receipts"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spMerchandisingImportCNPOReceipts


```


