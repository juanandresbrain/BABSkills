# dbo.vwBO_Product_Dim2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBO_Product_Dim2"]
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |

## View Code

```sql
CREATE view [dbo].[vwBO_Product_Dim2]
as
select Product_Group + ' ' + Division as division_key
	,department + ' ' + department_code as department_display 
	, department_code + ' ' + class as class_display
	, subclass + ' ' + subclass_code as subclass_display
	, cast(sku as varchar(50)) + ' - ' + [product_desc] as sku_display

/*
,CASE WHEN Department like 'Sp%rts%' then product_group + ' ' + department + ' ' + department_code-- as department_key 
	 ELSE department + ' ' + department_code  END as department_key 
,CASE WHEN Department like 'Sp%rts%' then product_group + ' ' + department_code + ' ' + class 
	ELSE  department_code + ' ' + class END as class_key
,CASE WHEN Department like 'Sp%rts%' then product_group + ' ' + subclass + ' ' + subclass_code
	ELSE subclass + ' ' + subclass_code END as subclass_key
,CASE WHEN Department like 'Sp%rts%' then product_group + ' ' + cast(sku as varchar(50)) + ' - ' + [product_desc]
ELSE cast(sku as varchar(50)) + ' - ' + [product_desc] END as sku_key
*/

,CASE WHEN Department like 'Sp%rts%' then product_group + ' ' + department + ' ' + department_code-- as department_key 
	 ELSE department + ' ' + department_code  END as department_key 
,CASE WHEN Department like 'Sp%rts%' then 'Sprts Lic ' + product_group + ' - ' + department_code + ' ' + class 
	ELSE  department_code + ' ' + class END as class_key
,CASE WHEN Department like 'Sp%rts%' then 'Sprts Lic ' + product_group + ' - ' + subclass + ' ' + subclass_code
	ELSE subclass + ' ' + subclass_code END as subclass_key
,CASE WHEN Department like 'Sp%rts%' then 'Sprts Lic ' + product_group + ' - ' + cast(sku as varchar(50)) + ' - ' + [product_desc]
ELSE cast(sku as varchar(50)) + ' - ' + [product_desc] END as sku_key

	, *
	from (

select 
  [product_key]
,CASE WHEN Department is null then 'N/A'
 WHEN division = 'Ridemakerz' THEN 'Ridemakerz-' + Department 
 WHEN right(department_code,2)='25' or (department = 'Sports Licensing' and subclass = 'Skins') 
	THEN 'Skins'
 WHEN right(department_code,2)='30'  or (department = 'Sports Licensing' and subclass like 'Prestuffed%') 
	THEN 'Prestuffed'
 WHEN right(department_code,2)='15'  or (department = 'Sports Licensing' and subclass = 'Footwear') 
	THEN 'Footwear' 
 WHEN right(department_code,2)='05'  or department = 'Accessories' or 
	(department = 'Sports Licensing' and subclass in 
	('Accessories','Caps','Motor Sports Access','Motor Sports Hats')) 
	THEN 'Accessories'
 WHEN right(department_code,2)='10' or department in ('clothes', 'Clothing') or (department in ('Sports Licensing','Sprts Lic') and 
	 (subclass not in ('Skins','Footwear') or subclass not like 'Prestuffed%')) 
	THEN 'Clothing'
	 WHEN right(department_code,2)='06' THEN 'Furniture'
	 WHEN right(department_code,2)='07' or department = 'Pets' THEN 'Pets'
	 WHEN right(department_code,2) in ('12','33','38') THEN 'Licensing'
	 WHEN right(department_code,2)='20' THEN 'Sounds'
	 WHEN right(department_code,2)='35' or department = 'Human' THEN 'Human'
	 WHEN right(department_code,2) in ('40','48') THEN 'Parties'
	 WHEN right(department_code,2)='45' THEN 'Bearbucks/Coupons'
	 WHEN right(department_code,2)='46' THEN 'Donations/Discounts'
	 WHEN right(department_code,2)='47' or department = 'Transaction Flags' THEN 'Transaction Flags'
	 WHEN right(department_code,2)='50' THEN 'Web'
	 WHEN right(department_code,2)='51' THEN 'Kits'
	 WHEN right(department_code,2)='55' THEN 'Corporate'
	 WHEN right(department_code,2)='60' or department = 'Supplies' THEN 'Supplies'
	 WHEN right(department_code,2)='65' THEN 'Embroidery'
	 WHEN right(department_code,2)='70' THEN 'Former Businesses'
	 WHEN right(department_code,2)='75' THEN 'Promotions'
	 WHEN right(department_code,2)='80' THEN 'Gift Cards'
	 WHEN right(department_code,2)='85' THEN 'Blanks'
	 WHEN right(department_code,2)='99' THEN 'Test'
	 WHEN Department = 'Misc POS' then 'N/A'
 ELSE department
 END  as Product_Group

	   ,CASE WHEN right(department_code,2) = 25 OR right(subclass_code,2) = 25 
            THEN 'Animals'
			WHEN right(department_code,2) = 05 THEN 'Accessories'
			WHEN right(department_code,2) = 15 THEN 'Footwear'
			WHEN right(department_code,2) = 20 THEN 'Sounds'
			WHEN right(department_code,2) = 10 THEN 'Clothing'
			WHEN right(department_code,2) NOT IN (25,10,15,20,05,30,35,12) or department_code is null  
				THEN 'Other'
			ELSE 'N/A'
		END AS KeyMetrics_ProductGroup
 
	   ,CASE WHEN right(department_code,2) = 25 OR right(subclass_code,2) = 25 
            OR right(department_code,2) = '02'--RZ added
			THEN 'AnimalsAndRZVehicles'
			WHEN right(department_code,2) = 05 THEN 'Accessories'
			WHEN right(department_code,2) = 15 THEN 'Footwear'
			WHEN right(department_code,2) = 20 THEN 'Sounds'
			WHEN right(department_code,2) = 10 THEN 'Clothing'
			WHEN right(department_code,2) NOT IN (25,10,15,20,05,30,35,12) or department_code is null  
				THEN 'Other'
			ELSE 'N/A'
		END AS KeyMetrics_ProductGroupWithRZ
      ,CASE WHEN [chain] is null THEN 'N/A'
	   ELSE [chain] END as [chain]
      ,CASE WHEN [division] is null THEN 'N/A'
	   ELSE [division] END as [division]
      ,CASE WHEN [department_code] is null THEN 'Unspecified'
	   ELSE department_code END as department_code
      ,CASE WHEN [department] is null THEN 'N/A'
	   ELSE [department] END as [department]
      ,CASE WHEN [class] is null THEN 'N/A'
	   ELSE [class] END as [class]
      ,CASE WHEN [subclass_code] is null and [subclass] is null THEN 'N/A'
			WHEN [subclass_code] is null and [subclass] is not null then [subclass] 
	   ELSE [subclass_code] END as [subclass_code]
      ,CASE WHEN [subclass] is null THEN 'N/A'
	   ELSE [subclass] END as [subclass]
     ,CASE WHEN [sku] is null THEN 0
	   ELSE [sku] END as [sku]
     ,CASE WHEN [style_desc] is null THEN 'N/A'
	   ELSE [style_desc] END as [style_desc]
     ,CASE WHEN [product_desc] is null THEN 'N/A'
	   ELSE [product_desc] END as [product_desc]
      ,[activation_date]
      ,[style_code]
      ,[color_code]
      ,[color_desc]
      ,[concept]
      ,[priceline_code]
      ,[class_code]
      ,[primary_vendor_code]
      ,[primary_vendor_name]
      ,[alt_primary_vendor_code]
      ,[current_retail]
      ,[original_retail]
      ,[price_with_vat]
      ,[reorder_flag]
      ,[euro_value]
      ,[merch_status]
      ,[wss_reportable]
      ,[style_id]
      ,[color_id]
      ,[current_selling_retail_home]
  FROM [dw].[dbo].[product_dim]) p
```

