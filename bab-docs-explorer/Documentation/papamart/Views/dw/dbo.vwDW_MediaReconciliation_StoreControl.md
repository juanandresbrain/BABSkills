# dbo.vwDW_MediaReconciliation_StoreControl

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_MediaReconciliation_StoreControl"]
    store_dim(["store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| store_dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_MediaReconciliation_StoreControl]
AS
-- History
SELECT store_id, store_name 
FROM store_dim 
WHERE store_key NOT IN (SELECT store_key 
						FROM store_dim	
						WHERE (opening_date < GETDATE() AND closing_date < GETDATE()) OR opening_date > GETDATE()) -- Closed stores or stores yet to open
	AND store_id NOT IN (-991, 10056, 10063, 950, 960, 975)
	--AND store_id NOT BETWEEN 2000 AND 2999





dbo,vwADDR_SUM_FACT,/***********************************************************************************************
Object Name:			dbo.vwADDR_SUM_FACT
Description/Purpose:	View used for reporting.  Primarily used by BO universes to 
						conveniently access all relevant pieces of Address Summary data.
						Sourced from kiosk registrations only.
						Joins ADDR_SUM_FACT to CLNSD_ADDR_DIM, NRST_PSTL_CD_STR_DIM, DMA_MSA and MAPINFO_PSYTE_CLUSTER

-- Dependencies: 
--
-- Revision History
--		Name:					Date:			Comments:
--		Funmi Agbebi			3/6/2009		Original Creation
--		Funmi Agbebi			1/12/2010		Added Cluster Information
--		dave rice				01/18/2011		store keys from NRST_PSTL_CD_STR_DIM were being used instead of store_ids from store_dim

**********************************************************************************************/
CREATE VIEW [dbo].[vwADDR_SUM_FACT]
as
SELECT
n.PSTL_CD NrstStrDim_PstlCd,
ns.store_id NearestStoreID,ns.store_name NearestStore,
fs.store_id FutureNearestStoreID, 
fs.store_name FutureNearestStore,
f.actual_date HHFrstStrVstDt, s.actual_date HHScndStrVstDt, 
t.actual_date HHThrdStrVstDt,l.actual_date HHLastStrVstDt,
i.actual_date HHSumFactUpdtDt, a.*
,c.[ADDR_LN_1_TXT],c.[ADDR_LN_2_TXT],c.[ADDR_LN_3_TXT]
,c.[ADDR_LN_4_TXT],c.[ADDR_LN_5_TXT],c.[APT_UNIT_NBR]
,c.[CTY_NM],c.[VNTY_CTY_NM],c.[CNTY_NM],c.[ST_PRVNC_ABBRV]
,c.[ST_PRVNC_NM],c.[PSTL_CD],c.[PSTL_PLS_4_CD],c.[NRST_STR_PSTL_CD]
,c.[CNTRY_ABBRV],c.[CNTRY_NM]

/*  Cluster Information addition starts (FA 1/12/2010) */
,c.[BLKGRP_CD],c.[CLUS_ID]
,m.CLUS_CD, m.CLUS_GRP, M.CLUS_NM
/*  Cluster Information addition ends */

,dma.DMA, dma.DMA_NM, dma.MSA, dma.MSA_NM
,c.[ORIG_SRC_SYS_CD]
,c.[LAT_NBR],c.[LONG_NBR],c.[APT_UNIT_IND]
,c.[MAIL_STAT_CD],c.[OPT_IN_SRC_SYS_CD],c.[GLBL_OPT_IN_DT]
,c.[ADDR_TYP_CD],c.[ADDR_TYP_DESCR],c.[ADDR_ACTV_STAT_CD]
FROM [dbo].[ADDR_SUM_FACT] a WITH (NOLOCK) LEFT JOIN  
[dbo].[CLNSD_ADDR_DIM] c WITH (NOLOCK) on
a.CLNSD_ADDR_ID = c.CLNSD_ADDR_ID LEFT JOIN  
dbo.NRST_PSTL_CD_STR_DIM n WITH (NOLOCK) ON 
a.NRST_PSTL_CD_STR_ID = n.NRST_PSTL_CD_STR_ID LEFT JOIN  
dbo.DMA_MSA dma WITH (NOLOCK) ON 
c.cntry_abbrv = dma.cntry_abbrv and
c.pstl_cd = dma.pstl_cd LEFT JOIN  
dbo.store_dim ns WITH (NOLOCK) ON 
n.str_id = ns.store_key LEFT JOIN   
dbo.store_dim fs on n.futr_str_id = fs.store_key LEFT JOIN  
dbo.date_dim f WITH (NOLOCK) ON 
a.[FRST_STR_VST_DT_ID] = f.date_key LEFT JOIN  
dbo.date_dim s WITH (NOLOCK) ON 
a.[SCND_STR_VST_DT_ID] = s.date_key LEFT JOIN  
dbo.date_dim t WITH (NOLOCK) ON 
a.[THRD_STR_VST_DT_ID] = t.date_key LEFT JOIN  
dbo.date_dim l WITH (NOLOCK) ON 
a.[LAST_STR_VST_DT_ID] = l.date_key LEFT JOIN  
dbo.date_dim i WITH (NOLOCK) ON 
a.[ADDR_SUM_FACT_UPDT_DT_ID] = i.date_key
LEFT JOIN dbo.MAPINFO_PSYTE_CLUSTER m ON 
c.clus_id = m.clus_id
```

