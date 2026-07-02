# Job: ES Aged Orders Check

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["ES Aged Orders Check"]
    JOB --> Step_1_1["Step 1: Step 1 [TSQL]"]`n```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spES_Aged_Orders_Check
```


