# dbo.vwDW_fact_vwmetrics

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_fact_vwmetrics"]
    dbo_BVILLE_MTRC_SUM(["dbo.BVILLE_MTRC_SUM"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.BVILLE_MTRC_SUM |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_fact_vwmetrics]
AS

	select 
	ms.trn_dt_id, 
	ms.str_id, 
	 SUM(ms.BVILLE_ACTVN_CNT) as bville_activations,
	SUM(ms.STR_TRN_CNT) as POS_transactions,
	 SUM(ms.KSK_REGIS_CNT) as animal_registrations,
	SUM(ms.SFS_RDMPTN_CNT) as sfs_redemptions,
	SUM(ms.BEAR_BOUTQ_RDMPTN_CNT) as boutique_transactions,
	SUM(ms.SFS_TRN_CNT) as SFS_transactions --This will need remapped!!!!!
	

from dw.dbo.[BVILLE_MTRC_SUM] MS
--FULL OUTER JOIN dwdev01.dw.dbo.BVILLE_ACTVN_SUM SM ON RS.STR_ID = SM.STR_ID AND RS.TRN_DT_ID = SM.TRN_DT_ID
GROUP BY ms.STR_ID, ms.TRN_DT_ID
```

