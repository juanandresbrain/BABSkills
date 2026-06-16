# Job: WMS_ASNCreateConfirmation

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WMS_ASNCreateConfirmation"]
    JOB --> Step_1_1["Step 1: Step 1 [SSIS]"]`n    JOB --> SEND_ASN_EMAIL_2["Step 2: SEND_ASN_EMAIL [TSQL]"]`n```

## Steps

### Step 1: Step 1
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\WMS\WMS_ASNCreateConfirmation\WMS_ASNCreateConfirmation.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"AzureServiceBus_ConnectionString\"";"\"ServiceBusNamespace=bab-wm.servicebus.windows.net/;ServiceEndpoint=;ServiceBusIssuerName=RootManageSharedAccessKey;ServiceBusIssuerKey=\"\"QiRB1kSHHaZ5YRxK6A3MzWpBEvME4FNcwHs1IofxDaQ=\"\";TransportType=NetMessaging;ConnectivityMode=AutoDetect;OperationTimeout=3600;IgnoreCertificateErrors=False;RetryOnIntermittentErrors=True\"" /Par "\"IntegrationStaging_ServerName\"";"\"STL-SSIS-P-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```

### Step 2: SEND_ASN_EMAIL
**Subsystem:** TSQL  

```sql
exec [WMS].[spMergeASNCreateEmails];
```


