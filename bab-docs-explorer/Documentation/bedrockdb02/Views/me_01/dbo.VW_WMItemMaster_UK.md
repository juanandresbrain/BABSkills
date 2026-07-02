# dbo.VW_WMItemMaster_UK

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.VW_WMItemMaster_UK"]
    dbo_attribute_set(["dbo.attribute_set"]) --> VIEW
    dbo_entity_attribute_set(["dbo.entity_attribute_set"]) --> VIEW
    dbo_entity_custom_property(["dbo.entity_custom_property"]) --> VIEW
    dbo_factory_address(["dbo.factory_address"]) --> VIEW
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> VIEW
    dbo_keith_average_cost(["dbo.keith_average_cost"]) --> VIEW
    dbo_style(["dbo.style"]) --> VIEW
    dbo_style_group(["dbo.style_group"]) --> VIEW
    dbo_style_retail(["dbo.style_retail"]) --> VIEW
    WMS_vwUKItemMasterWarehouse(["WMS.vwUKItemMasterWarehouse"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.attribute_set |
| dbo.entity_attribute_set |
| dbo.entity_custom_property |
| dbo.factory_address |
| dbo.hierarchy_group |
| dbo.keith_average_cost |
| dbo.style |
| dbo.style_group |
| dbo.style_retail |
| WMS.vwUKItemMasterWarehouse |

## View Code

```sql
CREATE view [dbo].[VW_WMItemMaster_UK]
as
select m.*
from

	(
	select 	'001' as CO,
		'001' as DIV,
		s.style_code as STYLE,
		replace(replace(replace(s.short_desc,'"',' ') ,'[',' '), ',', '') as SKU_DESC,
		'' as CARTON_TYPE,
		'0.00' as UNIT_PRICE,
		'0.00' as RETAIL_PRICE,  -- changed to avg cost from sr.current_selling_retail 6/16/2009
		case when substring(hg.hierarchy_group_code,7,2)='60'
		then
			isnull(ecp2.custom_property_value,1)
		else	s.distribution_multiple 
		end as STD_PACK_QTY,
		case when substring(hg.hierarchy_group_code,7,2)='60'
		then	1
		else 	s.order_multiple 
		end as STD_CASE_QTY,	
		0 as MAX_CASE_QTY,
		0 as STD_CASE_LEN,
		0 as STD_CASE_WIDTH,
		0 as STD_CASE_HT,
		1 as UNIT_WT,
		1 as UNIT_VOL,
		0 as STD_PACK_WT,
		0 as STD_PACK_VOL,
		0 as STD_CASE_WT,
		0 as STD_CASE_VOL,
		0 as CRITCL_DIM_1,
		0 as CRITCL_DIM_2,
		0 as CRITCL_DIM_3,
		0 as STAT_CODE,
		s.style_code as SKU_BRCD,
		0 as STD_PACK_WIDTH,
		0 as STD_PACK_LEN,
		0 as STD_PACK_HT,
		0 as UNIT_WIDTH,
		0 as UNIT_LEN,
		0 as UNIT_HT,
		'999' as SKU_PROFILE_ID,
		'EAR99' as ECCN_NBR,
		'NLR' as EXP_LICN_NBR,
		case when substring(hg.hierarchy_group_code,7,2)='60'
		then substring(isnull(ecp3.custom_property_value,'NONE ASSIGN'),1,12)
		else substring(isnull(att.attribute_set_label,'NONE ASSIGN'),1,12)
		end as COMMODITY_CODE,
				--case when substring(hg.hierarchy_group_code,7,2)='60'
			--then	'SUPPLIES'
			--else	isnull(att.attribute_set_code, 'NONE ASSIGN') 
			--end as COMMODITY_LEVEL_DESC,
		im.nmfc_code,
		im.frt_class,
		isnull(im.commodity_level_desc, 'NONE ASSIGN') as COMMODITY_LEVEL_DESC,
		'2970' as WHSE,
		upper(replace(replace(replace(hg_dept.hierarchy_group_label,' ',''),'UK',''),'-','')) as STORE_DEPT,
		case when fa.country = 'P.R. of China'
			then 'CN'
		when fa.country = 'Vietnam'
			then 'VN'
		when fa.country = 'Indonesia'
			then 'ID'
		else fa.country	
		end as ORGN_CERT_CODE,
			im.wm_sku_desc WM_SKU_DESC,
			'0.00' WM_UNIT_PRICE,
			'0.00' WM_RETAIL_PRICE,
			im.wm_std_pack_qty WM_STD_PACK_QTY,
			im.wm_std_case_qty WM_STD_CASE_QTY,
			im.wm_COMMODITY_CODE WM_COMMODITY_CODE,
			im.wm_store_dept WM_STORE_DEPT,
			im.wm_ORGN_CERT_CODE WM_ORGN_CERT_CODE
	from	style s with (nolock) 
	join	style_retail sr with (nolock) on s.style_id = sr.style_id
	join	style_group sg with (nolock) on s.style_id = sg.style_id
	join	hierarchy_group hg with (nolock) on sg.hierarchy_group_id = hg.hierarchy_group_id
	join	hierarchy_group hg_dept with (nolock) on left(hg.hierarchy_group_code, 8) = hg_dept.hierarchy_group_code
	left outer join entity_custom_property ecp2 with (nolock) on s.style_id = ecp2.parent_id
		and		ecp2.custom_property_id = 2 -- FRCSTM
		and		ecp2.parent_type = 1
	left outer join entity_attribute_set eas with (nolock) on s.style_id = eas.parent_id
		and		eas.attribute_id = 156
	left join attribute_set att with (nolock) on eas.attribute_set_id = att.attribute_set_id
	left join keith_average_cost kac with (nolock) on s.style_code = kac.style_code
	left join entity_attribute_set eas_FACTRY with (nolock) on s.style_id = eas_FACTRY.parent_id
		and		eas_FACTRY.attribute_id = 122
	left join attribute_set att_FACTRY with (nolock) on eas_FACTRY.attribute_set_id = att_FACTRY.attribute_set_id
	left join factory_address fa with (nolock) on att_FACTRY.attribute_set_code = fa.attribute_set_code
	left outer join entity_custom_property ecp3 with (nolock) on s.style_id = ecp3.parent_id
		and		ecp3.custom_property_id = 24 -- UKHTS
		and		ecp3.parent_type = 1
	--left join wmdb01.wmprod.dbo.item_master im on s.style_code = im.style -- Replaced Jun 25 2020
	left join [stl-ssis-p-01].IntegrationStaging.[WMS].[vwUKItemMasterWarehouse] im on im.productnumber=s.style_code -- Replacement for MA-WMS table join above on  6/25/2020

	where sr.jurisdiction_id = 1 --HOME
	and substring(hg.hierarchy_group_code,7,2) not in ('40','45','46','47','48','49','50','51','53','54','55','57','65','70','75')
	and s.active_flag = 1
	and left(s.style_code, 1) = '4'
	AND substring(hg.hierarchy_group_code,7,2)<>'60' --excludes supplies, these are now sent from Dynamics
	) as M
```

