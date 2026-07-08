# dbo.sv_store

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_store"]
    GEOG_ADRS(["GEOG_ADRS"]) --> VIEW
    GEOG_CNTRY(["GEOG_CNTRY"]) --> VIEW
    ORG_CHN(["ORG_CHN"]) --> VIEW
    ORG_CHN_LOC(["ORG_CHN_LOC"]) --> VIEW
    ORG_CHN_TYPE(["ORG_CHN_TYPE"]) --> VIEW
    PRTY_ADRS(["PRTY_ADRS"]) --> VIEW
    PRTY_CNTCT(["PRTY_CNTCT"]) --> VIEW
    country(["country"]) --> VIEW
    currency(["currency"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| GEOG_ADRS |
| GEOG_CNTRY |
| ORG_CHN |
| ORG_CHN_LOC |
| ORG_CHN_TYPE |
| PRTY_ADRS |
| PRTY_CNTCT |
| country |
| currency |

## View Code

```sql
create view dbo.sv_store 
AS
SELECT 
	store_no = OC.ORG_CHN_NUM, 
	store_name = OC.ORG_CHN_NAME, 
	store_short_name = OC.ORG_CHN_SHRT_NAME,  
	store_manager = NULL, 
	selling_space = SUM(OCL.AREA_SIZE), 
	open_period = NULL,  --no longer in use
	comp_period = NULL,  --no longer in use
	closed_date = OC.CLS_DATE, 
	selling_nonselling_flag = OCT.SYS_CODE, 
 	division_code = NULL, -- no longer supported
	region_code = NULL, -- no longer supported 
	district_code = NULL, -- no longer supported 
 	phone_no = PH.CNTCT,--NULL, 
	tax_jurisdiction = OC.TAX_JRSDCTN_CODE,
	balancing_method = NULL, --no longer in use
	deposit_balancing_method = NULL, --no longer in use
	autoaccept_flag = OC.AUTO_ACPT,
	tax_strip_flag = NULL, --no longer in use
	outlet_store_flag = OC.ORG_CHN_TYPE_CODE,
	settlement_billing_name = OC.STLMNT_BLNG_NAME,
	store_deposit_destination = OC.PRMRY_BANK_ACNT_ID,
	gl_company = OC.GL_CMPNY_NUM,
	gl_store = OC.GL_LOC_NUM,
	currency_id = cu.currency_id,
	country_id = c.country_id,  --note must remain numeric to support existing user-defined exception/rejection rules
	comp_date = OC.COMP_DATE,
	open_date = OC.OPEN_DATE,
	city = GA.CITY,
	state_code = GA.TRTRY_CODE,
	zip_code = GA.POST_CODE,
	country_code = GA.CNTRY_CODE_ISO3,
        media_parameter_table_no = OC.MD_PRMTR_TBL_NUM,
	location_id = OC.EXTRNL_RFRNC_NUM,  
	store_status_code = NULL,   ---- no longer in use
	interstore_export_region = OC.VCHR_CNFG_TYPE,
	timezone_offset_hours = OC.GMT_OFST,
	store_export_code = OC.ORG_CHN_TYPE_CODE,
	petty_cash_line_object = NULL  -- no longer in use
 FROM ORG_CHN OC
 JOIN ORG_CHN_LOC OCL
      ON OC.ORG_CHN_NUM = OCL.ORG_CHN_NUM
 JOIN ORG_CHN_TYPE OCT 
      ON OC.ORG_CHN_TYPE_CODE = OCT.ORG_CHN_TYPE_CODE
 JOIN currency cu
      ON OC.DFLT_CRNCY_CODE = cu.currency_code
 LEFT OUTER JOIN PRTY_ADRS PA
      ON OC.PRTY_ID = PA.PRTY_ID
      AND OC.DFLT_ADRS_SEQ = PA.PRTY_ADRS_SEQ
      AND PA.EFCTV_STRT_DATE <= GETDATE()
      AND (PA.EFCTV_END_DATE >= GETDATE() OR PA.EFCTV_END_DATE IS NULL)      
 LEFT OUTER JOIN GEOG_ADRS GA 
      ON PA.ADRS_ID = GA.ADRS_ID     
 LEFT OUTER JOIN PRTY_CNTCT PH
      ON OC.PRTY_ID = PH.PRTY_ID
      AND PH.CNTCT_TYPE_CODE = 'TLPH' 
      AND SEQ_NUM = 1  --- primary
 LEFT OUTER JOIN GEOG_CNTRY GC
   ON GA.CNTRY_CODE_ISO3 = GC.CNTRY_CODE_ISO3
 LEFT OUTER JOIN country c
      ON GC.CNTRY_CODE_ISO2 = c.country_code
GROUP BY OC.ORG_CHN_NUM, OC.ORG_CHN_NAME, OC.ORG_CHN_SHRT_NAME,
         OC.CLS_DATE, OCT.SYS_CODE, OC.TAX_JRSDCTN_CODE, 
         OC.AUTO_ACPT, OC.ORG_CHN_TYPE_CODE, 
         OC.STLMNT_BLNG_NAME, PH.CNTCT,
         OC.PRMRY_BANK_ACNT_ID, OC.GL_CMPNY_NUM, OC.GL_LOC_NUM, 
         cu.currency_id, GA.CNTRY_CODE_ISO3, OC.COMP_DATE, 
         OC.OPEN_DATE, GA.CITY, GA.TRTRY_CODE, GA.POST_CODE, GA.CNTRY_CODE_ISO3,
         OC.MD_PRMTR_TBL_NUM, OC.EXTRNL_RFRNC_NUM, OC.VCHR_CNFG_TYPE, OC.GMT_OFST,
         OC.ORG_CHN_TYPE_CODE, c.country_id
```

