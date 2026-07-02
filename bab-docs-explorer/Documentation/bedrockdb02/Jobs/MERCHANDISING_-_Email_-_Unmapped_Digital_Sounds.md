# Job: MERCHANDISING - Email - Unmapped Digital Sounds

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Execute spMerchandisingEmailUnmappedDigitalSounds

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Email - Unmapped Digital Sounds"]
    JOB --> uno_1["Step 1: uno [TSQL]"]`n```

## Steps

### Step 1: uno
**Subsystem:** TSQL  

```sql
exec spMerchandisingEmailUnmappedDigitalSounds
```


