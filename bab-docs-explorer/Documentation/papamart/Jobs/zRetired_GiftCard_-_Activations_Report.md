# Job: zRetired_GiftCard - Activations Report

**Enabled:** No  
**Server:** papamart  
**Description:** Execute package: GiftCard_Report  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_GiftCard - Activations Report"]
    JOB --> S1["Step 1: spGiftCard_Activations [TSQL]"]
```

## Steps

### Step 1: spGiftCard_Activations
**Subsystem:** TSQL  

```sql
EXEC dw.dbo.spGiftCard_Activations
```

