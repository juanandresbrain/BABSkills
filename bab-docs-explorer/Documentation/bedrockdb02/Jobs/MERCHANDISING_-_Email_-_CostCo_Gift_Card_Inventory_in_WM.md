# Job: MERCHANDISING - Email - CostCo Gift Card Inventory in WM

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Finds current inventory levels of CostCo Gift Cards at Bearhouse - Sends e-mails. Disabled on 12/13/2016 per Bryce Ahrens for 2016 holiday year. Likely will enable again next holiday.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email - CostCo Gift Card Inventory in WM"]
    JOB --> Uno_1["Step 1: Uno [TSQL]"]`n```

## Steps

### Step 1: Uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spWMSelectCostCoGiftCardInventory
```


