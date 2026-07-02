# Job: TXTDataLoad_Phase1_6EB9CD20-7020-4D73-A14A-951FD1BACD3D

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["TXTDataLoad_Phase1_6EB9CD20-7020-4D73-A14A-951FD1BACD3D"]
    JOB --> Step1_1["Step 1: Step1 [TSQL]"]`n```

## Steps

### Step 1: Step1
**Subsystem:** TSQL  

```sql
EXEC ma_01.[MerchandisingPlanning].[spTXTDataLoad_Measure_hs Sales Value Base_SingleFiscalWeek] 2025, 1, 60322, TXTDB01
```


