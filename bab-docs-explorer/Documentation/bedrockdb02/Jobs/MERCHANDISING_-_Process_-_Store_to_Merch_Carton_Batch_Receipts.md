# Job: MERCHANDISING - Process - Store to Merch Carton Batch Receipts

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Moves CBR files from pos comm server, transforms to pipeline cbr files

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Store to Merch Carton Batch Receipts"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.SPMerchandisingStoreToMerchCBR
```


