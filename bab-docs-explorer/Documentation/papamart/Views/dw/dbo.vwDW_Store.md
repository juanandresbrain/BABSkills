# dbo.vwDW_Store

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Store"]
    vwDW_Store_biapp01(["vwDW_Store_biapp01"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| vwDW_Store_biapp01 |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Store] 
-- =============================================================================================================
-- Name: [dbo].[vwDW_Store]
--
-- Description: 
--
-- Dependencies: 
--
-- Revision History

--		Name:			Date:			Comments:
--		Gary Murrish	4/5/2013		Changed to run off of the new logic in vwdw_Store_biapp01

-- =============================================================================================================

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
			dsb.MerchBearritory,
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
			FROM vwDW_Store_biapp01 dsb WITH (NOLOCK)
```

