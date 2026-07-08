# Job: NoReferenceNoInAW

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** Checks for Transactions in AW with no Reference_No  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["NoReferenceNoInAW"]
    JOB --> S1["Step 1: NoRefNum [TSQL]"]
    S1 --> S2["Step 2: Post Void NoRefNum [TSQL]"]
```

## Steps

### Step 1: NoRefNum
**Subsystem:** TSQL  

```sql
exec spNoReferenceNoInAW
```

### Step 2: Post Void NoRefNum
**Subsystem:** TSQL  

```sql
exec spPostVoidNoReferenceNoInAW
```

