# Job: CL_Serialized_Cpn_WriteOff

**Enabled:** Yes  
**Server:** bedrockdb01  
**Description:** Creates Serialized Coupon write-off file and moves files for processing  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["CL_Serialized_Cpn_WriteOff"]
    JOB --> S1["Step 1: Step 1 [TSQL]"]
```

## Steps

### Step 1: Step 1
**Subsystem:** TSQL  

```sql
exec spCL_WriteOffSerializedCoupons
```

