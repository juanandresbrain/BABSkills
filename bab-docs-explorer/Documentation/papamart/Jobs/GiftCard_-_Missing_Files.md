# Job: GiftCard - Missing Files

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GiftCard - Missing Files"]
    JOB --> S1["Step 1: GiftCard - ParseValueLink - Missing Files [TSQL]"]
```

## Steps

### Step 1: GiftCard - ParseValueLink - Missing Files
**Subsystem:** TSQL  

```sql
exec dw..spGiftCard_MissingFiles
```

