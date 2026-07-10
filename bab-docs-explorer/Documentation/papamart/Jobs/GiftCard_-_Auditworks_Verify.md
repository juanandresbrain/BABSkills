# Job: GiftCard - Auditworks Verify

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GiftCard - Auditworks Verify"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec spGiftcardAuditworksVerify
```

