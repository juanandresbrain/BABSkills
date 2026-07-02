# Job: MERCHANDISING - Email-InactiveStyleTransactions

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Reports all transactions logged in ib_inventory over past 7 days for styles with Inactive flag. Sends email to Physical Inventory. Executes spMerchandisingEmailInactiveStyleTransactions

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email-InactiveStyleTransactions"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailInactiveStyleTransactions
```


