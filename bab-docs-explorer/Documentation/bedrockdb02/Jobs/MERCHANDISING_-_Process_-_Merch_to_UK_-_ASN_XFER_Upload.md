# Job: MERCHANDISING - Process - Merch to UK - ASN\XFER Upload

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Generates and Uploads ASN files for Purchase Orders and Transfers destined to 2013 and 2970

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to UK - ASN\XFER Upload"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n    JOB --> dos_2["Step 2: dos [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputClipperXFER_ASN

```

### Step 2: dos
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spMerchandisingOutputClipperPO_ASN
```


