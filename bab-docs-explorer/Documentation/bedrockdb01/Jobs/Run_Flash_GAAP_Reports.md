# Job: Run Flash GAAP Reports

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Run Flash GAAP Reports without running ETL for data warehouse. By default, this will report on yesterday's sales. Adding a date to the stored proc will run it for that particular day.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Run Flash GAAP Reports"]
    JOB --> S1["Step 1: Execute papamart.dw.dbo.usp_flashgaapsales [CmdExec]"]
```

## Steps

### Step 1: Execute papamart.dw.dbo.usp_flashgaapsales
**Subsystem:** CmdExec  

```sql
osql -Spapamart -ddw -Uosql -P05ql -Q"exec usp_FlashGAAPSales @transaction_date=NULL"
```

