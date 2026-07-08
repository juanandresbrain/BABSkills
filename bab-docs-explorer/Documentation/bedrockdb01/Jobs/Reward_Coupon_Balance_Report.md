# Job: Reward Coupon Balance Report

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Send Reward Coupon Balance Report to Finance at period end  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["Reward Coupon Balance Report"]
    JOB --> S1["Step 1: step 1 [TSQL]"]
```

## Steps

### Step 1: step 1
**Subsystem:** TSQL  

```sql
exec spRewardCouponBalanceReport
```

