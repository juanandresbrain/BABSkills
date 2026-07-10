# dbo.vwETL_store_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwETL_store_dim"]
    dbo_store_dim(["dbo.store_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_dim |

## View Code

```sql
CREATE VIEW vwETL_store_dim
as
SELECT 
	  [store_key]
      ,[store_id]
      ,[bearea]
      ,[store_name]
      ,[bearritory]
      ,[address1]
      ,[region]
      ,[zone]
      ,[address2]
      ,[state_province_name]
      ,[business_type]
      ,[city]
      ,[division]
      ,[state_province]
      ,[county]
      ,[business_unit]
      ,[country]
      ,[country_name]
      ,[postal_code]
      ,[phone]
      ,[fax]
      ,[email]
      ,[opening_date]
      ,[active]
      ,[latitude]
      ,[longitude]
      ,[volume_group]
      ,[store_mgr]
      ,[bearea_mgr]
      ,[bearitory_mgr]
      ,[region_mgr]
      ,[store_type]
      ,[closing_date]
      ,[comp_date]
      ,[store_group_id]
      ,[address3]
      ,[address4]
      ,[square_feet]
      ,[num_of_pos]
      ,[num_of_kiosks]
      ,[postal_plus4]
      ,[Abbreviation]
      ,[Legal_Description]
      ,[comp_week_id]
      ,[bearea_id]
      ,[bearitory_id]
      ,[region_id]
      ,[division_code]
      ,[language]
      ,[demographics_bg_key]
	  ,CASE WHEN division = 'US-Zone' THEN 'RZ'
		ELSE 'BABW' END as company_group
	  ,CASE WHEN store_id in (13, 136, 1513) THEN 'web'
		ELSE 'store' END as type_group
  FROM [dw].[dbo].[store_dim]
```

