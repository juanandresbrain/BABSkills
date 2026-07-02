# Job: WEB - Email Record Your Voice Process Counts

**Enabled:** Yes  
**Server:** STL-SSIS-P-01  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["WEB - Email Record Your Voice Process Counts"]
    JOB --> Exec_spEmailRecordYourVoiceProcessSummary_1["Step 1: Exec spEmailRecordYourVoiceProcessSummary [TSQL]"]`n```

## Steps

### Step 1: Exec spEmailRecordYourVoiceProcessSummary
**Subsystem:** TSQL  

```sql
EXEC Kodiak.RecordYourVoice.dbo.spEmailRecordYourVoiceProcessSummary
```


