# Job: Lease_Mgmt_Monthy_Sales_File_Export

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Monthly Sales Export for manual upload to Lucernex (LXContracts) by the Acct department for Lease Mgmt  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Lease_Mgmt_Monthy_Sales_File_Export"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spLeaseMgmtMonthySalesExport
```

