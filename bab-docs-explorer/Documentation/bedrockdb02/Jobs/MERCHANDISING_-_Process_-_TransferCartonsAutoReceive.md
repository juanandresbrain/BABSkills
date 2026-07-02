# Job: MERCHANDISING - Process - TransferCartonsAutoReceive

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Generates carton batch receipt file to post receipt for cartons on transfers and shipments to/from specific locations.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - TransferCartonsAutoReceive"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectTransferCartons
```


