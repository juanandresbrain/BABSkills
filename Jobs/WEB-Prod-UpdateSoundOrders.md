# Job: WEB-Prod-UpdateSoundOrders

**Enabled:** Yes  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB-Prod-UpdateSoundOrders"]
    JOB --> Update_sound_orders_in_OMS_1["Step 1: Update sound orders in OMS [SSIS]"]`n```

## Steps

### Step 1: Update sound orders in OMS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\WebOrderProcessing\UpdateSoundOrders.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 6 /Par StoreSoundTransferRoot;"\"\\stl-devdep-p-01\Deployment\RecordYourVoice\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


