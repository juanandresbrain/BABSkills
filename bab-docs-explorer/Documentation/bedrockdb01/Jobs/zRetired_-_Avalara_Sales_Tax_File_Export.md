# Job: zRetired - Avalara_Sales_Tax_File_Export

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Creates Export file for Tax Department for Avalara import. Retired on 7/29/2022 by TimC Replaced with SSIS package : AuditworkstoAvalaraSalesTaxFileExport  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired - Avalara_Sales_Tax_File_Export"]
    JOB --> S1["Step 1: Daily Run - USA and CAN [TSQL]"]
```

## Steps

### Step 1: Daily Run - USA and CAN
**Subsystem:** TSQL  

```sql
exec spAvalaraMonthySalesTaxExport
```

