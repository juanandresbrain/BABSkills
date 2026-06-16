# Job: zRetired_WEB_StoreInventoryArchiveDelete7Days

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB_StoreInventoryArchiveDelete7Days"]
    JOB --> delete_from_StoreInventoryFactArchive_1["Step 1: delete from StoreInventoryFactArchive [TSQL]"]`n```

## Steps

### Step 1: delete from StoreInventoryFactArchive
**Subsystem:** TSQL  

```sql
begin   delete from web.StoreInventoryFactArchive   where datediff(dd, InsertDate, getdate()) >= 7  end
```


