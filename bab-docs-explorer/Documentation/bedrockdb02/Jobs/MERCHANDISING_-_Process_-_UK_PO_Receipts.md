# Job: MERCHANDISING - Process - UK PO Receipts

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Bulk Inserts PO Receipt file from UK warehouse, outputs PO Receipt file to Pipeline

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - UK PO Receipts"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectUKPOReceipts
```


