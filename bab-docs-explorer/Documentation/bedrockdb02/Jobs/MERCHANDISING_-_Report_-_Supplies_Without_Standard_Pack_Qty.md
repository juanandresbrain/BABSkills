# Job: MERCHANDISING - Report - Supplies Without Standard Pack Qty

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Reports styles in Merch which do not have a standard pack qty defined, emails purchasing team members.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Report - Supplies Without Standard Pack Qty"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingEmailSuppliesWithoutPackQty
```


