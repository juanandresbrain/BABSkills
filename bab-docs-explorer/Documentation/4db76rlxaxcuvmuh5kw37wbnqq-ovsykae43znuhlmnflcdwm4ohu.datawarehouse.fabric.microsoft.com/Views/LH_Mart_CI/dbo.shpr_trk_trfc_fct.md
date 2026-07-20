# dbo.shpr_trk_trfc_fct

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.shpr_trk_trfc_fct"]
    dbo_shpr_trk_trfc_fct(["dbo.shpr_trk_trfc_fct"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.shpr_trk_trfc_fct |

## View Code

```sql
; CREATE   VIEW [dbo].[shpr_trk_trfc_fct] AS     SELECT [SHPR_TRK_TRFC_FCT_KEY], [SHPR_TRK_FL_LOG_ID], [SHPR_TRK_ORG_ID], [STR_KEY], [DT_KEY], [TM_KEY], [ENTERS], [EXITS], [DATA_IND_NM] COLLATE Latin1_General_CI_AS AS [DATA_IND_NM], [ETL_LOG_ID], [ETL_EVNT_ID], [INS_DT]     FROM [dbo].[shpr_trk_trfc_fct]
```

