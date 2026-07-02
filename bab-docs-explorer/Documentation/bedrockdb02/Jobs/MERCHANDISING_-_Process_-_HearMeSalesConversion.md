# Job: MERCHANDISING - Process - HearMeSalesConversion

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Convert new HearMe sounds sales over to the blank/master sound in order properly decrement correct sound item and producing sales for the A&R tool while recording/retaining the actual sound item sold. When the sounds are rang at the register, the individually sound files are accounted for, but not the physical sound device. This process allows us to account for the physical sound device.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - HearMeSalesConversion"]
    JOB --> one_1["Step 1: one [TSQL]"]`n```

## Steps

### Step 1: one
**Subsystem:** TSQL  

```sql
exec me_01.dbo.spHearMeSalesConversion
```


