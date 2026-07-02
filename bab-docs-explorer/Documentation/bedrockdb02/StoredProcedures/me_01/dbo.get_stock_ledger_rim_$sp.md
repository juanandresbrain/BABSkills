# dbo.get_stock_ledger_rim_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_stock_ledger_rim_$sp"]
    dbo_calendar_period(["dbo.calendar_period"]) --> SP
    dbo_calendar_year(["dbo.calendar_year"]) --> SP
    dbo_gl_period(["dbo.gl_period"]) --> SP
    dbo_hierarchy_group(["dbo.hierarchy_group"]) --> SP
    dbo_hierarchy_level(["dbo.hierarchy_level"]) --> SP
    dbo_history_period(["dbo.history_period"]) --> SP
    dbo_location(["dbo.location"]) --> SP
    dbo_location_parent(["dbo.location_parent"]) --> SP
    dbo_merch_group_parent(["dbo.merch_group_parent"]) --> SP
    dbo_parameter_sl_accum_dep(["dbo.parameter_sl_accum_dep"]) --> SP
    dbo_sl_history(["dbo.sl_history"]) --> SP
    dbo_thg(["dbo.thg"]) --> SP
    dbo_view_cumulative_values(["dbo.view_cumulative_values"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.calendar_period |
| dbo.calendar_year |
| dbo.gl_period |
| dbo.hierarchy_group |
| dbo.hierarchy_level |
| dbo.history_period |
| dbo.location |
| dbo.location_parent |
| dbo.merch_group_parent |
| dbo.parameter_sl_accum_dep |
| dbo.sl_history |
| dbo.thg |
| dbo.view_cumulative_values |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[get_stock_ledger_rim_$sp]
	(@detail_level_id int,
	 @1st_sum_level_id int,
	 @2nd_sum_level_id int,
	 @sl_period_type tinyint,
	 @gl_period_code nvarchar(20),
	 @merch_year_period nvarchar(6),
	 @report_currency tinyint)
AS

BEGIN

/*
History:
9/18/2015		Ivan Dimitrov		137279 - Incorrect CC% on SL Report (RIM method)
*/

DECLARE
   @hist_period_id_eoly decimal(12, 0),
   @hist_period_id_boy decimal(12, 0),
   @hist_period_id_eolp decimal(12, 0),
   @hist_period_id_bop decimal(12, 0),
   @hist_period_id_eop decimal(12, 0)

IF @sl_period_type = 0 -- @sl_period_type = GL period
BEGIN
   -- @hist_period_id_bop: beginning of current period (used for non on hand)
   -- @hist_period_id_eop: end of current period
   SELECT @hist_period_id_bop = MIN(hp.history_period_id), @hist_period_id_eop = MAX(hp.history_period_id)
   FROM gl_period gp WITH (NOLOCK)
   INNER JOIN history_period hp WITH (NOLOCK)
      ON gp.gl_period_id = hp.gl_period_id
      AND gp.gl_period_code = @gl_period_code
      AND hp.start_date <= GETDATE()

   -- @hist_period_id_eolp: end of last period (used for on hand)
   SELECT @hist_period_id_eolp = MAX(hp.history_period_id)
   FROM history_period hp
   WHERE hp.history_period_id < @hist_period_id_bop

   -- @hist_period_id_boy: beginning of current year (used for non on hand)
   SELECT @hist_period_id_boy = MIN(hp.history_period_id)
   FROM gl_period gp WITH (NOLOCK)
   INNER JOIN history_period hp WITH (NOLOCK)
      ON gp.gl_period_id = hp.gl_period_id
      AND FLOOR(gp.gl_period_code/100) = FLOOR(@gl_period_code/100)

   -- @hist_period_id_eoly: end of last year (used for on hand)
   SELECT @hist_period_id_eoly = MAX(hp.history_period_id)
   FROM history_period hp
   WHERE hp.history_period_id < @hist_period_id_boy
END
ELSE
BEGIN  -- @sl_period_type = merch period
   -- @hist_period_id_bop: beginning of current period (used for non on hand)
   -- @hist_period_id_eop: end of current period
   SELECT @hist_period_id_bop = MIN(hp.history_period_id), @hist_period_id_eop = MAX(hp.history_period_id)
   FROM calendar_period cp WITH (NOLOCK)
   INNER JOIN calendar_year cy WITH (NOLOCK)
      ON cp.calendar_year_id = cy.calendar_year_id
      AND cy.calendar_year_code * 100 + cp.calendar_period_code = CONVERT(int, @merch_year_period)
   INNER JOIN history_period hp WITH (NOLOCK)
      ON cp.calendar_period_id = hp.calendar_period_id
      AND hp.start_date <= GETDATE()

   -- @hist_period_id_eolp: end of last period (used for on hand)
   SELECT @hist_period_id_eolp = MAX(hp.history_period_id)
   FROM history_period hp
   WHERE hp.history_period_id < @hist_period_id_bop

   -- @hist_period_id_boy: beginning of current year (used for non on hand)
   SELECT @hist_period_id_boy = MIN(hp.history_period_id)
   FROM calendar_period cp WITH (NOLOCK)
   INNER JOIN calendar_year cy WITH (NOLOCK)
      ON cp.calendar_year_id = cy.calendar_year_id
      AND cy.calendar_year_code = FLOOR(@merch_year_period/100)
   INNER JOIN history_period hp WITH (NOLOCK)
      ON cp.calendar_period_id = hp.calendar_period_id

   -- @hist_period_id_eoly: end of last year (used for on hand)
   SELECT @hist_period_id_eoly = MAX(hp.history_period_id)
   FROM history_period hp
   WHERE hp.history_period_id < @hist_period_id_boy
END

IF NOT object_id(N'tempdb..#temp_hg_loc') IS NULL
   DROP TABLE #temp_hg_loc
BEGIN
   CREATE TABLE #temp_hg_loc(
      hierarchy_group_id int not null,
      location_id smallint not null,
      detail_level_id int null,
      detail_code nvarchar(20),
      detail_label nvarchar(120),
      detail_level_label nvarchar(60),
      first_sum_level_id int null,
      first_sum_code nvarchar(20) null,
      first_sum_label nvarchar(120) null,
      first_sum_level_label nvarchar(60) null,
      second_sum_level_id int null,
      second_sum_code nvarchar(20) null,
      second_sum_label nvarchar(120) null,
      second_sum_level_label nvarchar(60) null,
      cum_cost decimal(14, 2) null,
      cum_retail decimal(14, 2) null,
      cum_cost_local decimal(14, 2) null,
      cum_retail_local decimal(14, 2) null,
	  cum_val_merch_group_id int null,
	  cum_val_location_group_id int null,
	  jurisdiction_id smallint null
   )
END


INSERT INTO #temp_hg_loc
   (hierarchy_group_id, location_id)
SELECT DISTINCT lst.hierarchy_group_id, lst.location_id
FROM sl_history sl WITH (NOLOCK)
INNER JOIN #temp_hg_loc_list lst
   ON sl.merch_hierarchy_group_id = lst.hierarchy_group_id
   AND sl.history_period_id BETWEEN @hist_period_id_eoly AND @hist_period_id_eop


-- detail level is a merch hierchy level
UPDATE thg
SET detail_level_id = hg.hierarchy_level_id,
    detail_code = hg.hierarchy_group_code,
    detail_label = hg.hierarchy_group_label,
    detail_level_label = hl.hierarchy_level_label
FROM #temp_hg_loc thg
INNER JOIN merch_group_parent mgp WITH (NOLOCK)
   ON  thg.hierarchy_group_id = mgp.hierarchy_group_id
INNER JOIN hierarchy_level hl WITH (NOLOCK)
   ON mgp.hierarchy_level_id = hl.hierarchy_level_id
   AND mgp.hierarchy_level_id = @detail_level_id
   AND hl.hierarchy_level_id = @detail_level_id
   AND hl.hierarchy_id = 1
INNER JOIN hierarchy_group hg WITH (NOLOCK)
   ON mgp.hierarchy_level_id = hg.hierarchy_level_id
   AND hl.hierarchy_level_id = hg.hierarchy_level_id
   AND hg.hierarchy_level_id = @detail_level_id
   AND mgp.parent_hierarchy_group_id = hg.hierarchy_group_id

-- detail level is a location hierchy level
UPDATE thg
SET detail_level_id = hg.hierarchy_level_id,
    detail_code = hg.hierarchy_group_code,
    detail_label = hg.hierarchy_group_label,
    detail_level_label = hl.hierarchy_level_label
FROM #temp_hg_loc thg
INNER JOIN hierarchy_level hl WITH (NOLOCK)
   ON hl.hierarchy_level_id = @detail_level_id
   AND hl.hierarchy_id = 2
LEFT OUTER JOIN location_parent lp WITH (NOLOCK)
   ON  thg.location_id = lp.location_id
   AND lp.hierarchy_level_id = hl.hierarchy_level_id
   AND lp.hierarchy_level_id = @detail_level_id
LEFT OUTER JOIN hierarchy_group hg WITH (NOLOCK)
   ON lp.hierarchy_level_id = hg.hierarchy_level_id
   AND hl.hierarchy_level_id = hg.hierarchy_level_id
   AND hg.hierarchy_level_id = @detail_level_id
   AND lp.parent_hierarchy_group_id = hg.hierarchy_group_id

-- detail level is location
UPDATE thg
SET detail_code = l.location_code,
    detail_label = l.location_name
FROM #temp_hg_loc thg
INNER JOIN location l WITH (NOLOCK)
   ON  thg.location_id = l.location_id
   AND @detail_level_id = 0

-- first summary total level is a merch hierchy level
UPDATE thg
SET thg.first_sum_level_id = hg.hierarchy_level_id,
    thg.first_sum_code = hg.hierarchy_group_code,
    thg.first_sum_label = hg.hierarchy_group_label,
    thg.first_sum_level_label = hl.hierarchy_level_label
FROM #temp_hg_loc thg
INNER JOIN merch_group_parent mgp WITH (NOLOCK)
   ON  thg.hierarchy_group_id = mgp.hierarchy_group_id
INNER JOIN hierarchy_level hl WITH (NOLOCK)
   ON mgp.hierarchy_level_id = hl.hierarchy_level_id
   AND mgp.hierarchy_level_id = @1st_sum_level_id
   AND hl.hierarchy_level_id = @1st_sum_level_id
   AND hl.hierarchy_id = 1
INNER JOIN hierarchy_group hg WITH (NOLOCK)
   ON mgp.hierarchy_level_id = hg.hierarchy_level_id
   AND hl.hierarchy_level_id = hg.hierarchy_level_id
   AND hg.hierarchy_level_id = @1st_sum_level_id
   AND mgp.parent_hierarchy_group_id = hg.hierarchy_group_id

-- first summary total level is a location hierarchy level
UPDATE thg
SET thg.first_sum_level_id = hg.hierarchy_level_id,
    thg.first_sum_code = hg.hierarchy_group_code,
    thg.first_sum_label = hg.hierarchy_group_label,
    thg.first_sum_level_label = hl.hierarchy_level_label
FROM #temp_hg_loc thg
INNER JOIN hierarchy_level hl WITH (NOLOCK)
   ON hl.hierarchy_level_id = @1st_sum_level_id
   AND hl.hierarchy_id = 2
LEFT OUTER JOIN location_parent lp WITH (NOLOCK)
   ON  thg.location_id = lp.location_id
   AND lp.hierarchy_level_id = hl.hierarchy_level_id
   AND lp.hierarchy_level_id = @1st_sum_level_id
LEFT OUTER JOIN hierarchy_group hg WITH (NOLOCK)
   ON lp.hierarchy_level_id = hg.hierarchy_level_id
   AND hl.hierarchy_level_id = hg.hierarchy_level_id
   AND hg.hierarchy_level_id = @1st_sum_level_id
   AND lp.parent_hierarchy_group_id = hg.hierarchy_group_id

-- first summary total level is a location hierarchy level
UPDATE thg
SET first_sum_code = l.location_code,
    first_sum_label = l.location_name
FROM #temp_hg_loc thg
INNER JOIN location l WITH (NOLOCK)
   ON thg.location_id = l.location_id
   AND @1st_sum_level_id = 0

-- second summary total level is a merch hierchy level
UPDATE thg
SET thg.second_sum_level_id = hg.hierarchy_level_id,
    thg.second_sum_code = hg.hierarchy_group_code,
    thg.second_sum_label = hg.hierarchy_group_label,
    thg.second_sum_level_label = hl.hierarchy_level_label
FROM #temp_hg_loc thg
INNER JOIN merch_group_parent mgp WITH (NOLOCK)
   ON  thg.hierarchy_group_id = mgp.hierarchy_group_id
INNER JOIN hierarchy_level hl WITH (NOLOCK)
   ON mgp.hierarchy_level_id = hl.hierarchy_level_id
   AND mgp.hierarchy_level_id = @2nd_sum_level_id
   AND hl.hierarchy_level_id = @2nd_sum_level_id
   AND hl.hierarchy_id = 1
INNER JOIN hierarchy_group hg WITH (NOLOCK)
   ON mgp.hierarchy_level_id = hg.hierarchy_level_id
   AND hl.hierarchy_level_id = hg.hierarchy_level_id
   AND hg.hierarchy_level_id = @2nd_sum_level_id
   AND mgp.parent_hierarchy_group_id = hg.hierarchy_group_id

-- second summary total level is a location hierarchy level
UPDATE thg
SET thg.second_sum_level_id = hg.hierarchy_level_id,
    thg.second_sum_code = hg.hierarchy_group_code,
    thg.second_sum_label = hg.hierarchy_group_label,
    thg.second_sum_level_label = hl.hierarchy_level_label
FROM #temp_hg_loc thg
INNER JOIN hierarchy_level hl WITH (NOLOCK)
   ON hl.hierarchy_level_id = @2nd_sum_level_id
   AND hl.hierarchy_id = 2
LEFT OUTER JOIN location_parent lp WITH (NOLOCK)
   ON  thg.location_id = lp.location_id
   AND lp.hierarchy_level_id = hl.hierarchy_level_id
   AND lp.hierarchy_level_id = @2nd_sum_level_id
LEFT OUTER JOIN hierarchy_group hg WITH (NOLOCK)
   ON lp.hierarchy_level_id = hg.hierarchy_level_id
   AND hl.hierarchy_level_id = hg.hierarchy_level_id
   AND hg.hierarchy_level_id = @2nd_sum_level_id
   AND lp.parent_hierarchy_group_id = hg.hierarchy_group_id

-- second summary total level is a location hierarchy level
UPDATE thg
SET second_sum_code = l.location_code,
    second_sum_label = l.location_name
FROM #temp_hg_loc thg
INNER JOIN location l WITH (NOLOCK)
   ON thg.location_id = l.location_id
   AND @2nd_sum_level_id = 0


-- populate the merch group ids at the cum val level
UPDATE #temp_hg_loc
SET cum_val_merch_group_id = parent_hierarchy_group_id
FROM #temp_hg_loc thl, merch_group_parent mgp, parameter_sl_accum_dep ps
WHERE thl.hierarchy_group_id = mgp.hierarchy_group_id
AND mgp.hierarchy_level_id = ps.cum_val_merch_level_id


-- populate the location group ids at the cum val level
UPDATE #temp_hg_loc
SET cum_val_location_group_id = parent_hierarchy_group_id, jurisdiction_id = l.jurisdiction_id
FROM #temp_hg_loc thl, location_parent lp, parameter_sl_accum_dep ps, location l
WHERE thl.location_id = lp.location_id
AND thl.location_id = l.location_id
AND lp.hierarchy_level_id = ps.cum_val_loc_level_id

UPDATE thg
SET thg.cum_cost = sq.cumulative_cost,
    thg.cum_retail = sq.cumulative_retail,
    thg.cum_cost_local = sq.cumulative_cost_local,
    thg.cum_retail_local = sq.cumulative_retail_local
FROM #temp_hg_loc thg
INNER JOIN
    (SELECT tgl.detail_code, tgl.first_sum_code, tgl.second_sum_code,
     SUM(v.cumulative_cost) cumulative_cost, SUM(v.cumulative_retail) cumulative_retail,
     SUM(v.cumulative_cost_local) cumulative_cost_local, SUM(v.cumulative_retail_local) cumulative_retail_local
     FROM
         (SELECT DISTINCT detail_code, first_sum_code, second_sum_code, cum_val_merch_group_id, cum_val_location_group_id, jurisdiction_id
          FROM #temp_hg_loc) tgl
     INNER JOIN view_cumulative_values v
        ON tgl.cum_val_merch_group_id = v.hierarchy_group_id
		AND tgl.cum_val_location_group_id = v.location_hierarchy_group_id
		AND tgl.jurisdiction_id = v.jurisdiction_id
     INNER JOIN history_period hp
        ON hp.calendar_period_id = v.calendar_period_id
      AND hp.history_period_id = @hist_period_id_eop
      GROUP BY tgl.detail_code, tgl.first_sum_code, tgl.second_sum_code
) sq
   ON thg.detail_code = sq.detail_code
   AND thg.first_sum_code = sq.first_sum_code
   AND thg.second_sum_code = sq.second_sum_code

SELECT hgl.detail_code, hgl.detail_label,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 14))) * (1 - abs (sign (sh.history_period_id - @hist_period_id_eolp )))) as beg_inv_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 14))) * (1 - abs (sign (sh.history_period_id - @hist_period_id_eoly )))) as beg_inv_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 27 ))) * (1 - abs (sign (sh.history_period_id - @hist_period_id_eolp )))) as beg_inv_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 27 ))) * (1 - abs (sign (sh.history_period_id - @hist_period_id_eoly )))) as beg_inv_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 18))) * (sign (1 + sign (sh.history_period_id- @hist_period_id_bop ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as purchases_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 18))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as purchases_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 17))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as purchases_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 17))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as purchases_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 8 ))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as distro_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 8 ))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as distro_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 7 ))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as distro_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 7 ))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as distro_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 21))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as xfer_retail_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 21))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as xfer_retail_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 20))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as xfer_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 20))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as xfer_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 13))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as markups_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 13))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as markups_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 10))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as freights_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 10))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as freights_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 19))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as sales_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 19))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as sales_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 23))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as sales_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 23))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as sales_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 12))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as md_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 12))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as md_retail_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 26))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as md_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 26))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as md_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 16))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as pos_disc_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 16))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as pos_disc_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 29))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as pos_disc_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 29))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as pos_disc_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 9 ))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as emp_disc_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 9 ))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as emp_disc_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 24 ))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as emp_disc_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 24))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as emp_disc_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 1 ))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as shrink_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 1 ))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as shrink_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 22 ))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as shrink_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 22 ))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as shrink_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 31))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as exchange_diff_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 31))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as exchange_diff_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 15))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as other_reduct_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 15))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as other_reduct_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 28))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as other_reduct_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 28))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as other_reduct_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 11))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as total_reduct_ret_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 11))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as total_reduct_ret_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 25))) * (sign (1 + sign (sh.history_period_id - @hist_period_id_bop))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as total_reduct_cost_pd,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 25))) * (sign (1 + sign (sh.history_period_id -@hist_period_id_boy   ))) *  (sign (1 - sign  (sh.history_period_id -@hist_period_id_eop)))) as total_reduct_cost_yr,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 14))) * (1 - abs (sign  (sh.history_period_id - @hist_period_id_eop)))) as end_inv_ret,
   SUM(CASE @report_currency WHEN 0 THEN sh.history_value ELSE sh.history_value_local END * (1-abs(sign(sh.sl_component_id - 27))) * (1 - abs (sign  (sh.history_period_id - @hist_period_id_eop)))) as end_inv_cost,
   CASE @report_currency WHEN 0 THEN hgl.cum_cost ELSE hgl.cum_cost_local END cum_cost,
   CASE @report_currency WHEN 0 THEN hgl.cum_retail ELSE hgl.cum_retail_local END cum_retail,
   hgl.second_sum_code, hgl.second_sum_label, hgl.first_sum_code, hgl.first_sum_label,
   hgl.detail_level_label, hgl.first_sum_level_label, hgl.second_sum_level_label
FROM sl_history sh WITH (NOLOCK)
INNER JOIN #temp_hg_loc hgl
   ON sh.merch_hierarchy_group_id = hgl.hierarchy_group_id
   AND sh.location_id = hgl.location_id
   AND sh.history_period_id BETWEEN @hist_period_id_eoly AND @hist_period_id_eop
GROUP BY hgl.second_sum_code, hgl.second_sum_label, hgl.second_sum_level_label,
   hgl.first_sum_code, hgl.first_sum_label, hgl.first_sum_level_label,
   hgl.detail_code, hgl.detail_label, hgl.detail_level_label,
   hgl.cum_cost, hgl.cum_cost_local, hgl.cum_retail, hgl.cum_retail_local
ORDER BY hgl.second_sum_code, hgl.first_sum_code, hgl.detail_code

DROP TABLE #temp_hg_loc

END
```

