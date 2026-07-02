# Job: MERCHANDISING - StyleAttributes-UK-CA

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sets factory attributes for UK and CA styles to be equal to the factory attributes for the US version of the style.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - StyleAttributes-UK-CA"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandising_Report_StyleAttributes
```


