# Job: zRetired_Load ProductRetailCost

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_Load ProductRetailCost"]
    JOB --> S1["Step 1: spProductRetailCost [TSQL]"]
```

## Steps

### Step 1: spProductRetailCost
**Subsystem:** TSQL  

```sql
exec azure.spProductRetailCost
```

