# Job: WMS_PurchaseOrderReceipt

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_PurchaseOrderReceipt"]
    JOB --> WMS_PurchaseOrderReceipt_1["Step 1: WMS_PurchaseOrderReceipt [SSIS]"]`n```

## Steps

### Step 1: WMS_PurchaseOrderReceipt
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_PurchaseOrderReceipt\WMS_PurchaseOrderReceipt.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10066 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


