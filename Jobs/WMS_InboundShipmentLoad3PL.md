# Job: WMS_InboundShipmentLoad3PL

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_InboundShipmentLoad3PL"]
    JOB --> SSIS___WMS_InboundShipmentLoad3PL_1["Step 1: SSIS - WMS_InboundShipmentLoad3PL [SSIS]"]`n```

## Steps

### Step 1: SSIS - WMS_InboundShipmentLoad3PL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InboundShipmentLoad3PL\WMS_InboundShipmentLoad3PL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10172 /Par "\"DaysToGoBack(Int32)\"";30 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


