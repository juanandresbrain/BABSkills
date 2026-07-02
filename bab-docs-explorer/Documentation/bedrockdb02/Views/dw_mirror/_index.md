# Views: dw_mirror

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [vwDW_Store](dbo.vwDW_Store.md) |  |
| 08-31-06 TMK added unique keys for Bear Range | [Region](08-31-06_TMK_added_unique_keys_for_Bear_Range.Region.md) |  |
| -- | [s.bearritory](--_s.bearritory.md) |  |
| --					when s.store_id in ('2007' | ['2008'](--_when_s_store_id_in_'2007'.'2008'.md) |  |
| --					when s.store_id in ('2005' | ['2009'](--_when_s_store_id_in_'2005'.'2009'.md) |  |
| when s.bearritory in ('Midlands' | ['Scotland & North') then 'North UK'](when_s_bearritory_in_'Midlands'.'Scotland_&_North'_then_'North_UK'.md) |  |
| when s.bearritory in ('Southeast-UK' | ['Southern'](when_s_bearritory_in_'Southeast-UK'.'Southern'.md) |  |
| -- | [Country = case](--.Country_=_case.md) |  |
| -- | [CASE WHEN s.state_province IS NULL OR s.state_province = '' THEN 'Other' ELSE s.state_province END AS state_province](--_CASE_WHEN_s_state_province_IS_NULL_OR_s_state_province_=_''_THEN_'Other'_ELSE_s.state_province_END_AS_state_province.md) |  |
| -- | [CASE WHEN s.city IS NULL OR s.city = '' THEN 'Other' ELSE s.city END AS city](--_CASE_WHEN_s_city_IS_NULL_OR_s_city_=_''_THEN_'Other'_ELSE_s.city_END_AS_city.md) |  |
| -- | [CASE WHEN s.postal_code IS NULL OR s.postal_code = '' THEN 'Other' ELSE s.postal_code END AS postal_code](--_CASE_WHEN_s_postal_code_IS_NULL_OR_s_postal_code_=_''_THEN_'Other'_ELSE_s.postal_code_END_AS_postal_code.md) |  |
| -- | [d.date_key AS comp_date_key](--_d.date_key_AS_comp_date_key.md) |  |
| -- | [(SELECT date_key FROM date_dim WHERE actual_date = store_table.comp_date) AS comp_date_key](--_SELECT_date_key_FROM_date_dim_WHERE_actual_date_=_store_table.comp_date_AS_comp_date_key.md) |  |
| -- | [CASE](--.CASE.md) |  |
| --	WHEN s.store_id in (480 | [482](--_WHEN_s_store_id_in_480.482.md) |  |
| --	WHEN s.region IN ('North US' | ['South US'](--_WHEN_s_region_IN_'North_US'.'South_US'.md) |  |
| --	WHEN s.region IN ('US-Corporate' | ['Web Stores') THEN 2](--_WHEN_s_region_IN_'US-Corporate'.'Web_Stores'_THEN_2.md) |  |
| -- | [CASE](--.CASE.md) |  |
| WHEN s.store_id in (480 | [482](WHEN_s_store_id_in_480.482.md) |  |
| WHEN s.region IN ('North US' | ['South US'](WHEN_s_region_IN_'North_US'.'South_US'.md) |  |
| WHEN s.region IN ('US-Corporate' | ['Web Stores') THEN 2](WHEN_s_region_IN_'US-Corporate'.'Web_Stores'_THEN_2.md) |  |
| WHEN s.region IN ('East US' | ['Central US'](WHEN_s_region_IN_'East_US'.'Central_US'.md) |  |
| when s.region in ('Web Stores' | ['US-Corporate'](when_s_region_in_'Web_Stores'.'US-Corporate'.md) |  |
| WHEN s.store_id in (480 | [482](WHEN_s_store_id_in_480.482.md) |  |
| WHEN s.region IN ('East US' | ['Central US'](WHEN_s_region_IN_'East_US'.'Central_US'.md) |  |
| dbo | [vwDW_product_dim](dbo.vwDW_product_dim.md) |  |
| CAST(product_key AS varchar) AS product_key | [sku](CAST_product_key_AS_varchar_AS_product_key.sku.md) |  |
| SUBSTRING(subclass_code | [1](SUBSTRING_subclass_code.1.md) |  |
| -- | [SUBSTRING(subclass_code](--.SUBSTRING_subclass_code.md) |  |
| -- | [department_code + ' - ' + department AS color_desc](--.department_code_+_'_-_'_+_department_AS_color_desc.md) |  |
| SUBSTRING(subclass_code | [1](SUBSTRING_subclass_code.1.md) |  |
| -- | [SUBSTRING(subclass_code](--.SUBSTRING_subclass_code.md) |  |
| -- | [subclass_code + ' - ' + subclass AS color_desc](--.subclass_code_+_'_-_'_+_subclass_AS_color_desc.md) |  |
| -- | [style_code + ' - ' + style_desc AS color_desc](--.style_code_+_'_-_'_+_style_desc_AS_color_desc.md) |  |
| dbo | [vwStore_dim_ForCube](dbo.vwStore_dim_ForCube.md) |  |
| SELECT sd.store_key | [sd.store_id](SELECT_sd_store_key_sd.store_id.md) |  |
| when country = 'UK' then RIGHT('000' + CAST(sd.store_id AS varchar) | [4) + ' ' + sd.store_name](when_country_=_'UK'_then_RIGHT_'000'_+_CAST_sd_store_id_AS_varchar_4_+_'_'_+_sd.store_name.md) |  |
| when region = 'Ridemakerz' then RIGHT('000' + CAST(sd.store_id AS varchar) | [4) + ' ' + sd.store_name](when_region_=_'Ridemakerz'_then_RIGHT_'000'_+_CAST_sd_store_id_AS_varchar_4_+_'_'_+_sd.store_name.md) |  |
| else RIGHT('000' + CAST(sd.store_id AS varchar) | [3) + ' ' + sd.store_name](else_RIGHT_'000'_+_CAST_sd_store_id_AS_varchar_3_+_'_'_+_sd.store_name.md) |  |
| CASE WHEN sd.store_id IN (130 | [174](CASE_WHEN_sd_store_id_IN_130.174.md) |  |
| WHEN sd.store_id IN (119 | [124](WHEN_sd_store_id_IN_119.124.md) |  |
| WHEN sd.store_id IN (13 | [136](WHEN_sd_store_id_IN_13.136.md) |  |
| WHEN sd.store_id IN (130 | [174](WHEN_sd_store_id_IN_130.174.md) |  |
| WHEN sd.store_id IN (119 | [124](WHEN_sd_store_id_IN_119.124.md) |  |
| WHEN sd.store_id IN (13 | [136](WHEN_sd_store_id_IN_13.136.md) |  |
| WHEN sd.bearritory IN ('Southwest' | ['Southeast') AND sd.country = 'GB' THEN sd.bearritory + '-UK'](WHEN_sd_bearritory_IN_'Southwest'_'Southeast'_AND_sd_country_=_'GB'_THEN_sd.bearritory_+_'-UK'.md) |  |
| WHEN sd.store_id IN (130 | [174](WHEN_sd_store_id_IN_130.174.md) |  |
| WHEN sd.store_id IN (119 | [124](WHEN_sd_store_id_IN_119.124.md) |  |
| WHEN sd.store_id IN (13 | [136](WHEN_sd_store_id_IN_13.136.md) |  |
| END AS region | [sd.country](END_AS_region_sd.country.md) |  |
| --WHERE (sd.store_id < 990 or sd.store_id > 1999 ) and sd.store_id not in (489 | [471)](--WHERE_sd_store_id_990_or_sd_store_id_1999_and_sd_store_id_not_in_489.471.md) |  |
