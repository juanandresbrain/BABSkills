# Job: StoresNoSalesInSA

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Reports stores that are not showing Sale transactions in Sales Audit for yesterday and highlights any if no sales for more than the last two consecutive days  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["StoresNoSalesInSA"]
    JOB --> S1["Step 1: Step1 [TSQL]"]
```

## Steps

### Step 1: Step1
**Subsystem:** TSQL  

```sql
exec spStoresNoSales @DaysBack = 1
```

