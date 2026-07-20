# dbo.vwDW_Store

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Store"]
    dbo_vwdw_store_biapp01(["dbo.vwdw_store_biapp01"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwdw_store_biapp01 |

## View Code

```sql
CREATE   VIEW [dbo].[vwDW_Store] 
AS
	SELECT dsb.store_key,
			dsb.store_id,
			dsb.StoreRanking,
			dsb.store_name,
			dsb.storeNameNum,
			dsb.bearea,
			dsb.bearritory,
			dsb.region,
			dsb.GeographyRegion,
			dsb.ParentCountry,
			dsb.ChildCountry,
			dsb.country,
			dsb.country_name,
			dsb.country_display,
			dsb.state_province,
			dsb.state_province_key,
			dsb.city,
			dsb.postal_code,
			dsb.latitude,
			dsb.longitude,
			dsb.dma_name,
			dsb.opening_date,
			dsb.opening_date_id,
			dsb.comp_week_id,
			dsb.open_fp_id,
			dsb.open_week_id,
			dsb.comp_date_key,
			dsb.ReportFlag,
			dsb.ClubMaxFlag,
			dsb.BearRange,
			dsb.CompanyLevel,
			dsb.IsClosed,
			dsb.closing_date_key,
			dsb.closing_date,
			dsb.closing_max_comp_date_key,
			dsb.closing_max_comp_date,
			dsb.closing_max_ly_comp_date_key,
			dsb.closing_max_ly_comp_date,
			dsb.MerchCompanyLevel,
			dsb.MerchBearRange,
			dsb.MerchCountry,
			dsb.MerchRegion,
			dsb.Merchbearritory,
			dsb.isHispanicStore,
			dsb.HispanicStoreGroup,
			--dsb.LocationType,
			--dsb.JurisdictionCode,
			dsb.MerchBearRangeKey,
			dsb.MerchCountryKey,
			dsb.MerchRegionKey,
			dsb.MerchBearitoryKey,
			dsb.CountryKey,
			dsb.RankedCompanyLevelKey,
			dsb.RankedBearRangeKey,
			dsb.RankedRegionKey,
			dsb.RankedBearitoryKey,
			dsb.BearRangeKey,
			dsb.RegionKey,
			dsb.BearitoryKey,
			dsb.city_key,
			dsb.city_display,
			dsb.postal_code_key,
			dsb.postal_code_display,
			dsb.GeographyParentCountryKey,
			dsb.GeographyRegionKey
			--dsb.isWebStore 
			FROM dbo.vwdw_store_biapp01 dsb
```

