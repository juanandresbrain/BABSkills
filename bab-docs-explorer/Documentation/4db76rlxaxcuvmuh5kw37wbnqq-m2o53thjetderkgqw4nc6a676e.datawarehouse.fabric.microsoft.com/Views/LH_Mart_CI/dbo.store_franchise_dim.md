# dbo.store_franchise_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.store_franchise_dim"]
    dbo_store_franchise_dim(["dbo.store_franchise_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_franchise_dim |

## View Code

```sql
;

CREATE VIEW dbo.store_franchise_dim AS SELECT store_key, store_id COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS store_id, bearea COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS bearea, store_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS store_name, bearritory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS bearritory, address1 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS address1, region COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS region, zone COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS zone, address2 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS address2, state_province_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS state_province_name, business_type COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS business_type, city COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS city, division COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS division, state_province COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS state_province, county COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS county, business_unit COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS business_unit, country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS country, country_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS country_name, postal_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS postal_code, phone COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS phone, fax COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS fax, email COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS email, opening_date, active COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS active, latitude, longitude, volume_group COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS volume_group, store_mgr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS store_mgr, bearea_mgr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS bearea_mgr, bearitory_mgr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS bearitory_mgr, region_mgr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS region_mgr, store_type COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS store_type, closing_date, comp_date, store_group_id, address3 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS address3, address4 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS address4, square_feet, num_of_pos, num_of_kiosks, postal_plus4 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS postal_plus4, Abbreviation COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Abbreviation, Legal_Description COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Legal_Description, comp_week_id, bearea_id, bearitory_id, region_id, division_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS division_code, language COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS language, demographics_bg_key COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS demographics_bg_key, BearRange COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS BearRange FROM LH_Mart.dbo.store_franchise_dim;
```

