# Job: MERCHANDISING - Process - ItemMasterHTS

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Captures Item Master HTS data from Merch and WM, outputs to CSV files, sends email

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - ItemMasterHTS"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputItemMasterHTS
```


