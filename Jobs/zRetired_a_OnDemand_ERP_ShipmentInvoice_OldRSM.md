# Job: zRetired_a_OnDemand_ERP_ShipmentInvoice_OldRSM

**Enabled:** No  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_a_OnDemand_ERP_ShipmentInvoice_OldRSM"]
    JOB --> ERP_ShipmentInvoice_1["Step 1: ERP_ShipmentInvoice [SSIS]"]`n```

## Steps

### Step 1: ERP_ShipmentInvoice
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\ERP_ShipmentInvoiceToD365\ERP_ShipmentInvoiceToD365.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 20 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /SET "\"\Package.Variables[User::Entity]\"";1100 /CALLERINFO SQLAGENT /REPORTING E
```


