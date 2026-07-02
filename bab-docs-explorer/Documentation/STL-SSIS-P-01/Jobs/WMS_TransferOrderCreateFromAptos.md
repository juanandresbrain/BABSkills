# Job: WMS_TransferOrderCreateFromAptos

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** JOB IS DISABLED, IT IS CALLED FROM SQL JOB MERCHANDISING - DISTRO IMPORT | EXPORT | SPLIT ON BEDROCKDB02

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_TransferOrderCreateFromAptos"]
    JOB --> WMS_TransferOrderCreateFromGS_Inbound_1["Step 1: WMS_TransferOrderCreateFromGS_Inbound [SSIS]"]`n    JOB --> WMS_TransferOrderCreateFromAptos_2["Step 2: WMS_TransferOrderCreateFromAptos [SSIS]"]`n    JOB --> Call_SQL_Agent_ERP_TransfersAndSalesOrderDistros_3["Step 3: Call SQL Agent ERP_TransfersAndSalesOrderDistros [TSQL]"]`n    JOB --> WMS_TransferOrderCreateFromGS_Outbound_4["Step 4: WMS_TransferOrderCreateFromGS_Outbound [SSIS]"]`n    JOB --> LoadOrderIdForPartyESOrder_5["Step 5: LoadOrderIdForPartyESOrder [TSQL]"]`n```

## Steps

### Step 1: WMS_TransferOrderCreateFromGS_Inbound
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_TransferOrderCreateFromGS\WMS_TransferOrderCreateFromGS.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: WMS_TransferOrderCreateFromAptos
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_TransferOrderCreateFromAptos\WMS_TransferOrderCreateFromAptos.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10068 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 3: Call SQL Agent ERP_TransfersAndSalesOrderDistros
**Subsystem:** TSQL  

```sql
EXEC msdb.dbo.sp_start_job @job_name='ERP_TransfersAndSalesOrderDistros'
```

### Step 4: WMS_TransferOrderCreateFromGS_Outbound
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_TransferOrderCreateFromGS\WMS_TransferOrderCreateFromGS.dtsx\"" /SERVER "\"STL-SSIS-P-01\"" /Par InboundOrOutbound;Outbound /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 5: LoadOrderIdForPartyESOrder
**Subsystem:** TSQL  

```sql
EXEC [BEARCLUSTER01.SQL.BUILDABEAR.COM].BABWPartyPlanner.dbo.spLoadOrderIdForPartyESOrder
```


