# Job: GoFileCountError

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GoFileCountError"]
    JOB --> S1["Step 1: Sales GO File Check [TSQL]"]
    S1 --> S2["Step 2: CL GO Files Check [TSQL]"]
```

## Steps

### Step 1: Sales GO File Check
**Subsystem:** TSQL  

```sql
exec dbo.usp_GoFileCountError
```

### Step 2: CL GO Files Check
**Subsystem:** TSQL  

```sql
exec dbo.usp_CLGoFileCountError
```

