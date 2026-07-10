# Job: zRetired_store_dim_snapshot_uk

**Enabled:** No  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_store_dim_snapshot_uk"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
DELETE
FROM
	dw.dbo.store_dim_snapshot_uk
WHERE
	datestamp < dateadd(dd, -21, getdate())

INSERT
INTO
	dw.dbo.store_dim_snapshot_uk
SELECT getdate() datestamp
	 , store_key
      ,store_id
      ,bearea
      ,store_name
      ,store_name_abbrv
      ,bearritory
      ,address1
      ,region
      ,[zone]
      ,address2
      ,state_province_name
      ,business_type
      ,city
      ,division
      ,state_province
      ,county
      ,business_unit
      ,country
      ,country_name
      ,postal_code
      ,phone
      ,fax
      ,email
      ,opening_date
      ,active
      ,latitude
      ,longitude
      ,volume_group
      ,store_mgr
      ,bearea_mgr
      ,bearitory_mgr
      ,region_mgr
      ,store_type
      ,closing_date
      ,comp_date
      ,store_group_id
      ,address3
      ,address4
      ,square_feet
      ,num_of_pos
      ,num_of_kiosks
      ,postal_plus4
      ,Abbreviation
      ,Legal_Description
      ,comp_week_id
      ,bearea_id
      ,bearitory_id
      ,region_id
      ,division_code
      ,[language]
      ,demographics_bg_key
FROM
	dw.dbo.store_dim
```

