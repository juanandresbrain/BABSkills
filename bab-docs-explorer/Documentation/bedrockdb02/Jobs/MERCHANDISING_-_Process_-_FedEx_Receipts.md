# Job: MERCHANDISING - Process - FedEx Receipts

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Processes receipt data from FedEx, outputs carton batch receipt file to post to Merchandising.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - FedEx Receipts"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputFedExReceipts
```


