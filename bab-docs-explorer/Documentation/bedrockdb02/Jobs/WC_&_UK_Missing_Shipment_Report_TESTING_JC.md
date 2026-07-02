# Job: WC & UK Missing Shipment Report TESTING JC

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WC & UK Missing Shipment Report TESTING JC"]
    JOB --> UK_SHIPMENT_REPORT_1["Step 1: UK SHIPMENT REPORT [TSQL]"]`n    JOB --> WC_SHIPMENT_REPORT_2["Step 2: WC SHIPMENT REPORT [TSQL]"]`n```

## Steps

### Step 1: UK SHIPMENT REPORT
**Subsystem:** TSQL  

```sql
EXEC[me_01]. [dbo].[spMissingUKShipmentReportD365]
```

### Step 2: WC SHIPMENT REPORT
**Subsystem:** TSQL  

```sql
EXEC [me_01]. [dbo].[spMissingWCShipmentReportD365]
```


