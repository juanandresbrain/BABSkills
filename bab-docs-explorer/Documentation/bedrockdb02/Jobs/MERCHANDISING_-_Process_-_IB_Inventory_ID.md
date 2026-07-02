# Job: MERCHANDISING - Process - IB Inventory ID

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** keeps track of starting and ending ib_inventory_id each day

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - IB Inventory ID"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingInsertIbInventoryID
```


