# Views: DBAUtility

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [BlitzFirst_FileStats_Deltas](dbo.BlitzFirst_FileStats_Deltas.md) | dbo.BlitzFirst_FileStats |
| ROW_NUMBER() OVER (ORDER BY [ServerName] | [[CheckDate]) ID](ROW_NUMBER_OVER_ORDER_BY_ServerName_._CheckDate_ID.md) |  |
| GROUP BY [ServerName] | [[CheckDate]](GROUP_BY_ServerName_._CheckDate.md) |  |
| DATEDIFF(ss | [fPrior.CheckDate](DATEDIFF_ss_fPrior.CheckDate.md) |  |
| AND DATEDIFF(MI | [fPrior.CheckDate](AND_DATEDIFF_MI_fPrior.CheckDate.md) |  |
| dbo | [BlitzFirst_PerfmonStats_Actuals](dbo.BlitzFirst_PerfmonStats_Actuals.md) | dbo.BlitzFirst_PerfmonStats_Deltas |
| CASE WHEN CHARINDEX('(' | [counter_name) = 0 THEN counter_name ELSE LEFT (counter_name](CASE_WHEN_CHARINDEX_'_'.counter_name_=_0_THEN_counter_name_ELSE_LEFT_counter_name.md) |  |
| LEFT(counter_name | [CHARINDEX('BASE'](LEFT_counter_name.CHARINDEX_'BASE'.md) |  |
| WHERE  cntr_type IN(272696576 | [272696320)](WHERE_cntr_type_IN_272696576.272696320.md) |  |
| WHERE  cntr_type IN(65792 | [65536)](WHERE_cntr_type_IN_65792.65536.md) |  |
| CAST((CAST(NUM.cntr_delta as DECIMAL(19)) / DEN.cntr_delta) as decimal(23 | [3))  AS cntr_value](CAST_CAST_NUM_cntr_delta_as_DECIMAL_19_DEN_cntr_delta_as_decimal_23.3_AS_cntr_value.md) |  |
| dbo | [BlitzFirst_PerfmonStats_Deltas](dbo.BlitzFirst_PerfmonStats_Deltas.md) | dbo.BlitzFirst_PerfmonStats |
| ROW_NUMBER() OVER (ORDER BY [ServerName] | [[CheckDate]) ID](ROW_NUMBER_OVER_ORDER_BY_ServerName_._CheckDate_ID.md) |  |
| GROUP BY [ServerName] | [[CheckDate]](GROUP_BY_ServerName_._CheckDate.md) |  |
| WHERE DATEDIFF(MI | [pMonPrior.CheckDate](WHERE_DATEDIFF_MI_pMonPrior.CheckDate.md) |  |
| dbo | [BlitzFirst_WaitStats_Deltas](dbo.BlitzFirst_WaitStats_Deltas.md) | dbo.BlitzFirst_WaitStats, dbo.BlitzFirst_WaitStats_Categories |
| ROW_NUMBER() OVER (ORDER BY [ServerName] | [[CheckDate]) ID](ROW_NUMBER_OVER_ORDER_BY_ServerName_._CheckDate_ID.md) |  |
| GROUP BY [ServerName] | [[CheckDate]](GROUP_BY_ServerName_._CheckDate.md) |  |
| SELECT w.ServerName | [w.CheckDate](SELECT_w_ServerName_w.CheckDate.md) |  |
| WHERE DATEDIFF(MI | [wPrior.CheckDate](WHERE_DATEDIFF_MI_wPrior.CheckDate.md) |  |
