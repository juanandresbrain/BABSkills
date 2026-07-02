# Job: StoreForceHoursOfOperationExtract

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** Runs nightly at 11pm, gets store hours from Storeforce, pushes to StoreMDM into temporarary hours, another job pushes hours to the web, that is called Web - StoresExports and runs at 11:30pm

## Architecture Diagram

```mermaid
flowchart LR
    JOB["StoreForceHoursOfOperationExtract"]
    JOB --> StoreForceHoursOfOperationExtract_1["Step 1: StoreForceHoursOfOperationExtract [SSIS]"]`n```

## Steps

### Step 1: StoreForceHoursOfOperationExtract
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\StoreForce\StoreForceHoursOfOperationExtract\StoreForceHoursOfOperationExtract.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /ENVREFERENCE 10058 /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


