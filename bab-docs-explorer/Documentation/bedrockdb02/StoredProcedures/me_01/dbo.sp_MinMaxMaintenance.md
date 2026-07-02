# dbo.sp_MinMaxMaintenance

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_MinMaxMaintenance"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_MinMaxMaintenance
AS
-- =====================================================================================================
-- Name: sp_MinMaxMaintenance
--
-- Description:	Update statistics for table used in the Min/Max Job to reduce job run time.
--		Called from the SQL Server Agent Job MERCHANDISING - Maintenance - Update Stats MinMax Job.
--
-- Dependencies: na
--
-- Revision History
-- Date				User			Description
-- 08/19/2019		Lizzy T			Creation
--
-- =====================================================================================================

Update statistics ma_01.dbo.hist_cmp_group_chn_li
Update statistics ma_01.dbo.hist_cmp_group_chn_pd
Update statistics ma_01.dbo.hist_cmp_group_chn_wk
Update statistics ma_01.dbo.hist_cmp_group_chn_yr
Update statistics ma_01.dbo.hist_cmp_group_loc_li
Update statistics ma_01.dbo.hist_cmp_group_loc_pd
Update statistics ma_01.dbo.hist_cmp_group_loc_wk
Update statistics ma_01.dbo.hist_cmp_group_loc_yr
Update statistics ma_01.dbo.hist_cmp_sku_chn_li
Update statistics ma_01.dbo.hist_cmp_sku_chn_pd
Update statistics ma_01.dbo.hist_cmp_sku_chn_wk
Update statistics ma_01.dbo.hist_cmp_sku_chn_yr
Update statistics ma_01.dbo.hist_cmp_sku_loc_li
Update statistics ma_01.dbo.hist_cmp_sku_loc_pd
Update statistics ma_01.dbo.hist_cmp_sku_loc_wk
Update statistics ma_01.dbo.hist_cmp_sku_loc_yr
Update statistics ma_01.dbo.hist_cmp_style_chn_li
Update statistics ma_01.dbo.hist_cmp_style_chn_pd
Update statistics ma_01.dbo.hist_cmp_style_chn_wk
Update statistics ma_01.dbo.hist_cmp_style_chn_yr
Update statistics ma_01.dbo.hist_cmp_style_loc_li
Update statistics ma_01.dbo.hist_cmp_style_loc_pd
Update statistics ma_01.dbo.hist_cmp_style_loc_wk
Update statistics ma_01.dbo.hist_cmp_style_loc_yr
Update statistics ma_01.dbo.hist_cmp_styleclr_chn_li
Update statistics ma_01.dbo.hist_cmp_styleclr_chn_pd
Update statistics ma_01.dbo.hist_cmp_styleclr_chn_wk
Update statistics ma_01.dbo.hist_cmp_styleclr_chn_yr
Update statistics ma_01.dbo.hist_cmp_styleclr_loc_li
Update statistics ma_01.dbo.hist_cmp_styleclr_loc_pd
Update statistics ma_01.dbo.hist_cmp_styleclr_loc_wk
Update statistics ma_01.dbo.hist_cmp_styleclr_loc_yr
Update statistics ma_01.dbo.hist_flsh_chn_da
Update statistics ma_01.dbo.hist_flsh_group_chn_da
Update statistics ma_01.dbo.hist_flsh_group_loc_da
Update statistics ma_01.dbo.hist_flsh_loc_da
Update statistics ma_01.dbo.hist_flsh_style_chn_da
Update statistics ma_01.dbo.hist_flsh_style_loc_da
Update statistics ma_01.dbo.hist_group_chn_li
Update statistics ma_01.dbo.hist_group_chn_pd
Update statistics ma_01.dbo.hist_group_chn_wk
Update statistics ma_01.dbo.hist_group_chn_yr
Update statistics ma_01.dbo.hist_group_loc_li
Update statistics ma_01.dbo.hist_group_loc_pd
Update statistics ma_01.dbo.hist_group_loc_wk
Update statistics ma_01.dbo.hist_group_loc_yr
Update statistics ma_01.dbo.hist_le_group_chn_li
Update statistics ma_01.dbo.hist_le_group_chn_pd
Update statistics ma_01.dbo.hist_le_group_chn_wk
Update statistics ma_01.dbo.hist_le_group_chn_yr
Update statistics ma_01.dbo.hist_le_group_loc_li
Update statistics ma_01.dbo.hist_le_group_loc_pd
Update statistics ma_01.dbo.hist_le_group_loc_wk
Update statistics ma_01.dbo.hist_le_group_loc_yr
Update statistics ma_01.dbo.hist_le_sku_chn_li
Update statistics ma_01.dbo.hist_le_sku_chn_pd
Update statistics ma_01.dbo.hist_le_sku_chn_wk
Update statistics ma_01.dbo.hist_le_sku_chn_yr
Update statistics ma_01.dbo.hist_le_sku_loc_li
Update statistics ma_01.dbo.hist_le_sku_loc_pd
Update statistics ma_01.dbo.hist_le_sku_loc_wk
Update statistics ma_01.dbo.hist_le_sku_loc_yr
Update statistics ma_01.dbo.hist_le_style_chn_li
Update statistics ma_01.dbo.hist_le_style_chn_pd
Update statistics ma_01.dbo.hist_le_style_chn_wk
Update statistics ma_01.dbo.hist_le_style_chn_yr
Update statistics ma_01.dbo.hist_le_style_loc_li
Update statistics ma_01.dbo.hist_le_style_loc_pd
Update statistics ma_01.dbo.hist_le_style_loc_wk
Update statistics ma_01.dbo.hist_le_style_loc_yr
Update statistics ma_01.dbo.hist_le_styleclr_chn_li
Update statistics ma_01.dbo.hist_le_styleclr_chn_pd
Update statistics ma_01.dbo.hist_le_styleclr_chn_wk
Update statistics ma_01.dbo.hist_le_styleclr_chn_yr
Update statistics ma_01.dbo.hist_le_styleclr_loc_li
Update statistics ma_01.dbo.hist_le_styleclr_loc_pd
Update statistics ma_01.dbo.hist_le_styleclr_loc_wk
Update statistics ma_01.dbo.hist_le_styleclr_loc_yr
Update statistics ma_01.dbo.hist_oh_group_chn_li
Update statistics ma_01.dbo.hist_oh_group_chn_pd
Update statistics ma_01.dbo.hist_oh_group_chn_wk
Update statistics ma_01.dbo.hist_oh_group_chn_yr
Update statistics ma_01.dbo.hist_oh_group_loc_li
Update statistics ma_01.dbo.hist_oh_group_loc_pd
Update statistics ma_01.dbo.hist_oh_group_loc_wk
Update statistics ma_01.dbo.hist_oh_group_loc_yr
Update statistics ma_01.dbo.hist_oh_sku_chn_li
Update statistics ma_01.dbo.hist_oh_sku_chn_pd
Update statistics ma_01.dbo.hist_oh_sku_chn_wk
Update statistics ma_01.dbo.hist_oh_sku_chn_yr
Update statistics ma_01.dbo.hist_oh_sku_loc_li
Update statistics ma_01.dbo.hist_oh_sku_loc_pd
Update statistics ma_01.dbo.hist_oh_sku_loc_wk
Update statistics ma_01.dbo.hist_oh_sku_loc_yr
Update statistics ma_01.dbo.hist_oh_style_chn_li
Update statistics ma_01.dbo.hist_oh_style_chn_pd
Update statistics ma_01.dbo.hist_oh_style_chn_wk
Update statistics ma_01.dbo.hist_oh_style_chn_yr
Update statistics ma_01.dbo.hist_oh_style_loc_li
Update statistics ma_01.dbo.hist_oh_style_loc_pd
Update statistics ma_01.dbo.hist_oh_style_loc_wk
Update statistics ma_01.dbo.hist_oh_style_loc_yr
Update statistics ma_01.dbo.hist_oh_styleclr_chn_li
Update statistics ma_01.dbo.hist_oh_styleclr_chn_pd
Update statistics ma_01.dbo.hist_oh_styleclr_chn_wk
Update statistics ma_01.dbo.hist_oh_styleclr_chn_yr
Update statistics ma_01.dbo.hist_oh_styleclr_loc_li
Update statistics ma_01.dbo.hist_oh_styleclr_loc_pd
Update statistics ma_01.dbo.hist_oh_styleclr_loc_wk
Update statistics ma_01.dbo.hist_oh_styleclr_loc_yr
Update statistics ma_01.dbo.hist_rim_oh_group_chn_li
Update statistics ma_01.dbo.hist_rim_oh_group_chn_pd
Update statistics ma_01.dbo.hist_rim_oh_group_chn_yr
Update statistics ma_01.dbo.hist_rim_oh_group_loc_li
Update statistics ma_01.dbo.hist_rim_oh_group_loc_pd
Update statistics ma_01.dbo.hist_rim_oh_group_loc_yr
Update statistics ma_01.dbo.hist_sku_chn_li
Update statistics ma_01.dbo.hist_sku_chn_pd
Update statistics ma_01.dbo.hist_sku_chn_wk
Update statistics ma_01.dbo.hist_sku_chn_yr
Update statistics ma_01.dbo.hist_sku_loc_li
Update statistics ma_01.dbo.hist_sku_loc_pd
Update statistics ma_01.dbo.hist_sku_loc_wk
Update statistics ma_01.dbo.hist_sku_loc_yr
Update statistics ma_01.dbo.hist_style_chn_li
Update statistics ma_01.dbo.hist_style_chn_pd
Update statistics ma_01.dbo.hist_style_chn_wk
Update statistics ma_01.dbo.hist_style_chn_yr
Update statistics ma_01.dbo.hist_style_loc_li
Update statistics ma_01.dbo.hist_style_loc_pd
Update statistics ma_01.dbo.hist_style_loc_wk
Update statistics ma_01.dbo.hist_style_loc_yr
Update statistics ma_01.dbo.hist_styleclr_chn_li
Update statistics ma_01.dbo.hist_styleclr_chn_pd
Update statistics ma_01.dbo.hist_styleclr_chn_wk
Update statistics ma_01.dbo.hist_styleclr_chn_yr
Update statistics ma_01.dbo.hist_styleclr_loc_li
Update statistics ma_01.dbo.hist_styleclr_loc_pd
Update statistics ma_01.dbo.hist_styleclr_loc_wk
Update statistics ma_01.dbo.hist_styleclr_loc_yr
Update statistics ma_01.dbo.history_component
Update statistics me_01.dbo.min_max_lead_time
Update statistics me_01.dbo.min_max_profile
Update statistics me_01.dbo.min_max_profile_archive
Update statistics me_01.dbo.min_max_profile_configuration_archive
Update statistics me_01.dbo.min_max_wos_param
Update statistics me_01.dbo.min_max_wos_param_id
Update statistics me_01.dbo.min_max_wos_param_loc
Update statistics me_01.dbo.min_max_wos_param_week
Update statistics me_01.dbo.style
Update statistics me_01.dbo.sku
Update statistics me_01.dbo.location
Update statistics me_01.dbo.seasonal_index
```

