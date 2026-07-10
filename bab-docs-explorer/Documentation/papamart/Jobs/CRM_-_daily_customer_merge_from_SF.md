# Job: CRM - daily customer merge from SF

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CRM - daily customer merge from SF"]
    JOB --> S1["Step 1: daily [TSQL]"]
```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
exec [dbo].[spMergeCRMCustomerDimFromSalesForce]
```

