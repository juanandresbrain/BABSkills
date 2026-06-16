# Job: WMS_EmailCostCoGiftCardInventory

**Enabled:** No  
**Description:** Finds current inventory levels of CostCo Gift Cards at Bearhouse - Sends e-mails.  Typically on enabled during certain parts of the year at the discretion of Bryce Ahrens

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_EmailCostCoGiftCardInventory"]
    JOB --> Step_Uno_1["Step 1: Step Uno [TSQL]"]`n```

## Steps

### Step 1: Step Uno
**Subsystem:** TSQL  

```sql
exec WMS.[spEmailCostcoInventory]
```


