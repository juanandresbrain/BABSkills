# Job: MERCHANDISING - Process - WebStore 0013 - Receive as Sent CBR

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Replacing "WM SQL Agent Job Web Carton Receiving" as it was unreliable due to AutoSub LPN functionality in WM. Business was aligned with a received as sent approach for 0980 to 0013 shipments as the inventory is allocated\reserved at item of inventory movement bridge in WM and just waiting for invenotry to moved within warehouse. Nightly Sync will deal with timing issues of inventory movement within warehouse.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - WebStore 0013 - Receive as Sent CBR"]
    JOB --> One_1["Step 1: One [TSQL]"]`n```

## Steps

### Step 1: One
**Subsystem:** TSQL  

```sql
exec spMerchandisingOutputWebstoreCBR
```


