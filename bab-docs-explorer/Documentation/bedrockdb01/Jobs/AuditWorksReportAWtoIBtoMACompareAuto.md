# Job: AuditWorksReportAWtoIBtoMACompareAuto

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["AuditWorksReportAWtoIBtoMACompareAuto"]
    JOB --> S1["Step 1: AuditworksReportAWtoIBtoMACompare [TSQL]"]
```

## Steps

### Step 1: AuditworksReportAWtoIBtoMACompare
**Subsystem:** TSQL  

```sql
EXEC [auditworks].[dbo].[spAuditworksReportAWtoIBtoMACompareUpdateV2]
```

