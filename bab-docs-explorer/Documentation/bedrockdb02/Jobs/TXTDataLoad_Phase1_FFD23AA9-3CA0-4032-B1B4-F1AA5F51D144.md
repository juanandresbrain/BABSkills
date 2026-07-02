# Job: TXTDataLoad_Phase1_FFD23AA9-3CA0-4032-B1B4-F1AA5F51D144

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["TXTDataLoad_Phase1_FFD23AA9-3CA0-4032-B1B4-F1AA5F51D144"]
    JOB --> Step1_1["Step 1: Step1 [TSQL]"]`n```

## Steps

### Step 1: Step1
**Subsystem:** TSQL  

```sql
EXEC ma_01.[MerchandisingPlanning].[spTXTDataLoad_Measure_hs Inv EOP Value_SingleFiscalWeek] 2025, 1, 60330, TXTDB01
```


