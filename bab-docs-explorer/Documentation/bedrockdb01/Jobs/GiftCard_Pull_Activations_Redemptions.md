# Job: GiftCard_Pull_Activations_Redemptions

**Enabled:** No  
**Server:** bedrockdb01  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GiftCard_Pull_Activations_Redemptions"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec spGiftCard_Pull_Activations_Redemptions
```

