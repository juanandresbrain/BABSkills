# Job: MERCHANDISING - Validation - Mismatched Std Pack Qty

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** Compares Std Pack Qty between Merch and WM, sends email for mismatch

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Validation - Mismatched Std Pack Qty"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingSelectMismatchedStdPackQty 
```


