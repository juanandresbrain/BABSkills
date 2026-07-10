# Job: zRetire - GuestLoad - Validation

**Enabled:** No  
**Server:** papamart  
**Description:** This job verifies the guest information from the data warehouse to that in the CRM database.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetire - GuestLoad - Validation"]
    JOB --> S1["Step 1: physical validation [TSQL]"]
    S1 --> S2["Step 2: email validation [TSQL]"]
    S2 --> S3["Step 3: Purge old EMail Requests [TSQL]"]
    S3 --> S4["Step 4: Purge old DMail Requests [TSQL]"]
```

## Steps

### Step 1: physical validation
**Subsystem:** TSQL  

```sql
exec dbo.spGuestLoad_VLDTN_Physical_Addr
```

### Step 2: email validation
**Subsystem:** TSQL  

```sql
exec dbo.spGuestLoad_VLDTN_Email_Addr
```

### Step 3: Purge old EMail Requests
**Subsystem:** TSQL  

```sql
exec spGuestLoad_Generate_EMail_Purge_Tables
```

### Step 4: Purge old DMail Requests
**Subsystem:** TSQL  

```sql
exec spGuestLoad_Generate_DMail_Purge_Tables
```

