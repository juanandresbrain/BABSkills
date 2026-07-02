# Job: MERCHANDISING - Process - UK to Merch Process Webstore CBR Files

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Renames Carton Batch Receipt file received from Clipper, Copies to Pipeline directory for processing

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - UK to Merch Process Webstore CBR Files"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectUKCartonBatchReceipts
```


