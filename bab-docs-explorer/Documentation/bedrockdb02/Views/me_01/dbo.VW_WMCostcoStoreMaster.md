# dbo.VW_WMCostcoStoreMaster

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.VW_WMCostcoStoreMaster"]
    dbo_tblCostcoLocations(["dbo.tblCostcoLocations"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblCostcoLocations |

## View Code

```sql
create view [dbo].[VW_WMCostcoStoreMaster]

as 

select 	'980' as WHSE,
	location_code as STORE_NBR,
	'Costco - ' + replace(location_name, 'costco', '') as NAME,
	address_line1 as ADDR_LINE_1,
	address_line2 as ADDR_LINE_2,
	NULL as ADDR_LINE_3,
	address_city as CITY,
	address_state as STATE,
	case when country_code in ('US', 'USA')
	then right('00000' + convert(varchar(5),left(address_zip_code,5)),5)
	else address_zip_code 
	end as ZIP,
	case when country_code = 'USA' then 'US' else country_code end as CNTRY,
	'Costco - ' + replace(location_name, 'costco', '') as CONTACT,
	isnull(max (substring (phone,1,15)),'000-000-0000') as PHONE,
	NULL as FAX,
	NULL as EMAIL,
	'001' as DFLT_CO,
	'001' AS DFLT_DIV,
	0 as STAT_CODE,
	NULL as OPEN_DATE,
	NULL as CLOSED_DATE,
	NULL as HOLD_DATE,
	NULL as GRP,
	NULL as CHAIN,
	NULL as ZONE,
	NULL as TERRITORY,
	NULL as REGION,
	NULL as DISTRICT,
	NULL as SHIP_MON,
	NULL as SHIP_TUE,
	NULL as SHIP_WED,
	NULL as SHIP_THU,
	NULL as SHIP_FRI,
	NULL as SHIP_SAT,
	NULL as SHIP_SU,
	NULL as ACCEPT_IRREG,
	NULL as WAVE_LABEL_TYPE,
	NULL as PKG_SLIP_TYPE,
	NULL as PRINT_CODE,
	'001' as CARTON_CNT_TYPE,
	NULL as STORE_TYPE,
	NULL as SHIP_VIA,
	NULL as RTE_NBR,
	NULL as RTE_ATTR,
	NULL as RTE_TO,
	NULL as RTE_TYPE_1,
	NULL as RTE_TYPE_2,
	NULL as RTE_ZIP,
	NULL as SPL_INSTR_CODE_1,
	NULL as SPL_INSTR_CODE_2,
	NULL as SPL_INSTR_CODE_3,
	NULL as SPL_INSTR_CODE_4,
	NULL as SPL_INSTR_CODE_5,
	NULL as SPL_INSTR_CODE_6,
	NULL as SPL_INSTR_CODE_7,
	NULL as SPL_INSTR_CODE_8,
	NULL as SPL_INSTR_CODE_9,
	NULL as SPL_INSTR_CODE_10,
	NULL as ASSIGN_MERCH_TYPE,
	NULL as ASSIGN_MERCH_GROUP,
	NULL as ASSIGN_STORE_DEPT,
	0 as PROC_STAT_CODE,
	0 as ERROR_SEQ_NBR,
	'' as CARTON_LABEL_TYPE,
	51 as CARTON_CUBNG_INDIC,
	' ' as MAX_CTN,
	' ' as MAX_PLT,
	NULL as BUSN_UNIT_CODE,
	'N' as USE_INBD_LPN_AS_OUT_BD_LPN	,
	getdate() as CREATE_DATE_TIME,
	getdate() as MOD_DATE_TIME,
	'COSTCO' as USER_ID	
from Kodiak.Beardata.dbo.tblCostcoLocations
group by location_code,location_name, address_line1,address_line2,address_city,address_state,address_zip_code,country_code
```

