# Job: UTA - Warehouse Payroll Email

**Enabled:** Yes  
**Description:** Email Warehouse Payroll data that represents the last seven days.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["UTA - Warehouse Payroll Email"]
    JOB --> Email_Warehouse_1["Step 1: Email Warehouse [TSQL]"]`n```

## Steps

### Step 1: Email Warehouse
**Subsystem:** TSQL  

```sql
DECLARE @endDate AS DATE  SELECT @endDate = CAST(GETDATE() AS DATE)    EXEC PAPAMART.dw.dbo.spUTAWarehousePayrollCSVEmail @endDate
```


