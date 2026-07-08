# dbo.SV_STORES

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.SV_STORES"]
    FNDTN_LANG(["FNDTN_LANG"]) --> VIEW
    ORG_CHN(["ORG_CHN"]) --> VIEW
    ORG_CHN_TYPE(["ORG_CHN_TYPE"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| FNDTN_LANG |
| ORG_CHN |
| ORG_CHN_TYPE |

## View Code

```sql
create view [dbo].[SV_STORES] 
AS
SELECT o.ORG_CHN_NUM ,
       o.ORG_CHN_NAME,
       o.ORG_CHN_SHRT_NAME ,
       o.ORG_CHN_TYPE_CODE,
       ISNULL(f.LANG_DESC, CONVERT(VARCHAR,o.PRMRY_LANG_ID)) AS PRMRY_LANG,
       o.PRMRY_LANG_ID,
       o.PRTY_ID,
       o.AUTO_ACPT,
       o.GMT_OFST,
       o.GL_CMPNY_NUM,
       o.GL_LOC_NUM,
       o.USE_AS_TMPLT,
       o.TMPLT_DESC,
       o.COMP_DATE,
       o.OPEN_TO_RCV_DATE,
       o.OPEN_DATE,
       o.CLS_DATE,
       o.ACTV,
       o.STLMNT_BLNG_NAME,
       o.MD_PRMTR_TBL_NUM,
       o.VCHR_CNFG_TYPE,
       o.TAX_JRSDCTN_CODE,
       o.PRMRY_BANK_ACNT_ID,
       o.OPEN_HOUR_ID,
       t.SYS_CODE,
       t.ORG_CHN_TYPE_SHRT_DESC,
       o.DFLT_CRNCY_CODE, 
       o.REOPEN_DATE, 
       o.ORG_CHN_STS, 
       o.SLNG_FLAG, 
       o.CLS_RSN, 
       o.SLNG_SPC, 
       o.NON_SLNG_SPC, 
       o.TRGT_SALES, 
       o.WH_SYSTM, 
       o.ALLW_CSTM_ODR, 
       o.SND_INV_MVMNT_TO_OMS,
       o.ALLW_CSTM_PKP_ODR, 
       o.RTNG_PRRTY, 
       t.ORG_CHN_TYPE_DESC, 
       o.RPLNSHBL, 
       o.SHRNKG_FCTR, 
       o.OCPNCY_COST_FXD   
FROM ORG_CHN o
     INNER JOIN ORG_CHN_TYPE t ON (o.ORG_CHN_TYPE_CODE = t.ORG_CHN_TYPE_CODE)
     LEFT JOIN FNDTN_LANG f ON (o.PRMRY_LANG_ID = f.LANG_ID)
WHERE  (o.LOC_CTGRY_CODE = 'STR')
```

