# Job: CreditSettlementTotals

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CreditSettlementTotals"]
    JOB --> S1["Step 1: Step 1 - PTEC [TSQL]"]
```

## Steps

### Step 1: Step 1 - PTEC
**Subsystem:** TSQL  

```sql
--SA 5.0 (CURRENT)
exec spCreditSettlementTotalsPTEC

--SA 4.1 (OLD)
--exec usp_CreditSettlementTotalsPTEC
```

