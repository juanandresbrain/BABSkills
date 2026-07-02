# Job: zRetired - MERCHANDISING - NightlySync_Stores_DynamicsToAptos

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Syncs store inventory from Dynamics to Aptos, is triggered by sql agent MERCHANDISING - Process - Nightly Sync All Whse and Web

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired - MERCHANDISING - NightlySync_Stores_DynamicsToAptos"]
    JOB --> Nightly_Sync_1["Step 1: Nightly Sync [TSQL]"]`n```

## Steps

### Step 1: Nightly Sync
**Subsystem:** TSQL  

```sql
exec spMerchandisingSelectNonWhseInventoryShrink
```


