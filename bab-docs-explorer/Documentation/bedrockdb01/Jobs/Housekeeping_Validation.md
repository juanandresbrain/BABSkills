# Job: Housekeeping_Validation

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Housekeeping_Validation"]
    JOB --> S1["Step 1: HouseKeeping Check [TSQL]"]
    S1 --> S2["Step 2: IF Transaction line record count check [TSQL]"]
```

## Steps

### Step 1: HouseKeeping Check
**Subsystem:** TSQL  

```sql
exec spHousekeepingValidation
```

### Step 2: IF Transaction line record count check
**Subsystem:** TSQL  

```sql
exec spIFTransactionTableThresholdCheck
```

