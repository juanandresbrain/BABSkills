# Job: Vouchers missing from SalesForce feed

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Vouchers missing from SalesForce feed"]
    JOB --> S1["Step 1: daily [TSQL]"]
```

## Steps

### Step 1: daily
**Subsystem:** TSQL  

```sql
exec [dbo].[spVouchersMissingFromSalesForceLoad]
```

