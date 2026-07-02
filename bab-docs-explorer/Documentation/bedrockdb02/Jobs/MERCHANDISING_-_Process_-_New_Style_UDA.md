# Job: MERCHANDISING - Process - New Style UDA

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Will look for styles in New status with Active flag and a Current Cost, then generate a UDA document to adjust 1 unit for location 9990, then create another UDA document to adjust -1 unit for location 9990. The end result is that the styles will flip from New to Received.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - New Style UDA"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandising_Report_NewStyleUDA
```


