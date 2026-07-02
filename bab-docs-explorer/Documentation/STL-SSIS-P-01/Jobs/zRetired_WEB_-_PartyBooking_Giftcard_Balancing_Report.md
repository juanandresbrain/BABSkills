# Job: zRetired_WEB - PartyBooking Giftcard Balancing Report

**Enabled:** No  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_WEB - PartyBooking Giftcard Balancing Report"]
    JOB --> PartyGiftCardBalancing_SSIS_1["Step 1: PartyGiftCardBalancing-SSIS [SSIS]"]`n```

## Steps

### Step 1: PartyGiftCardBalancing-SSIS
**Subsystem:** SSIS  

```sql
/ISSERVER "\"\SSISDB\SSIS\PartyReports\PartyGiftCardBalancing.dtsx\"" /SERVER "\"stl-ssis-p-01\"" /Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";0 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E
```


