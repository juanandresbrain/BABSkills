# Job: ERP_ShipmentInvoiceToD365

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ERP_ShipmentInvoiceToD365"]
    JOB --> ERP_ShipmentInvoiceToD365_1["Step 1: ERP_ShipmentInvoiceToD365 [SSIS]"]`n```

## Steps

### Step 1: ERP_ShipmentInvoiceToD365
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\ERP_ShipmentInvoiceToD365\ERP_ShipmentInvoiceToD365.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10106 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


