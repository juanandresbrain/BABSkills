# Job: Avalara_VAT_File_Export

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Creates Export VAT file for UK Accouting team to process  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Avalara_VAT_File_Export"]
    JOB --> S1["Step 1: Daily Run [TSQL]"]
```

## Steps

### Step 1: Daily Run
**Subsystem:** TSQL  

```sql
exec spAvalaraMonthlyVATTaxExport
```

