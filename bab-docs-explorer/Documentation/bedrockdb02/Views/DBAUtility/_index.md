# Views: DBAUtility

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [AVAIL_980_SUPPLY](dbo.AVAIL_980_SUPPLY.md) | dbo.AVAIL_980_SUPPLY |
| dbo | [AVAIL_980_SUPPLY_V2](dbo.AVAIL_980_SUPPLY_V2.md) | dbo.AVAIL_980_SUPPLY, ERP.vwAvailableSupplies |
| dbo | [AVAIL_980_SUPPLY_V3](dbo.AVAIL_980_SUPPLY_V3.md) | dbo.AVAIL_980_SUPPLY, WMS.vwAvailableSupplies |
| dbo | [vwDBA_Failed_Jobs](dbo.vwDBA_Failed_Jobs.md) | dbo.sysjobhistory, dbo.sysjobs, dbo.sysjobsteps |
| dbo | [vwEsell__pickpack](dbo.vwEsell_pickpack.md) | esell.orders |
