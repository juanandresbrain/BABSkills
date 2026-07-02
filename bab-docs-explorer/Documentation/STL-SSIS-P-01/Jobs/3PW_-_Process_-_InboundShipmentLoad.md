# Job: 3PW - Process - InboundShipmentLoad

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["3PW - Process - InboundShipmentLoad"]
    JOB --> Process_UK_Shipment_Files_1["Step 1: Process UK Shipment Files [TSQL]"]`n    JOB --> Process_West_Coast_Shipments_2["Step 2: Process West Coast Shipments [TSQL]"]`n    JOB --> Process_CN_Warehouse_Shipment_Files_3["Step 3: Process CN Warehouse Shipment Files [TSQL]"]`n    JOB --> SSIS___WMS_InboundShipmentLoad3PL_4["Step 4: SSIS - WMS_InboundShipmentLoad3PL [SSIS]"]`n    JOB --> Call_ERP_ShipmentInvoiceToD365_5["Step 5: Call ERP_ShipmentInvoiceToD365 [TSQL]"]`n```

## Steps

### Step 1: Process UK Shipment Files
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingProcessUKStoreShipments]  
```

### Step 2: Process West Coast Shipments
**Subsystem:** TSQL  

```sql
exec [WMS].[spMerchandisingProcessWCStoreShipments]  
```

### Step 3: Process CN Warehouse Shipment Files
**Subsystem:** TSQL  

```sql
exec  [WMS].[spMerchandisingProcessCNStoreShipments]
```

### Step 4: SSIS - WMS_InboundShipmentLoad3PL
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_InboundShipmentLoad3PL\WMS_InboundShipmentLoad3PL.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10172 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: Call ERP_ShipmentInvoiceToD365
**Subsystem:** TSQL  

```sql
EXEC msdb.dbo.sp_start_job @job_name='ERP_ShipmentInvoiceToD365'
```


