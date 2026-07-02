# Views: BABWPartyPlanner_Restore

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [vwCWMToStoreMDM](dbo.vwCWMToStoreMDM.md) | dbo.CNTCT_DIM, dbo.ROLES_DIM, dbo.Store, dbo.STR_CNTCT_DIM, dbo.STR_DIM, dbo.STR_INFO, dbo.STR_OPEN_DIM |
| dbo | [vwCWMToStoreMDM_1_1](dbo.vwCWMToStoreMDM_1_1.md) | dbo.CNTCT_DIM, dbo.ROLES_DIM, dbo.Store, dbo.STR_CNTCT_DIM, dbo.STR_DIM, dbo.STR_OPEN_DIM |
| dbo | [vwDistrictToStoreMDM](dbo.vwDistrictToStoreMDM.md) | dbo.BEARITORY_DIM, dbo.CNTCT_DIM |
| dbo | [vwDWPartyFacts](dbo.vwDWPartyFacts.md) | dbo.date_dim, dbo.Event, dbo.Occasion, dbo.Package, dbo.Party, dbo.Store, dbo.store_dim, dbo.theme, dbo.themePackageXref, dbo.time_dim |
| dbo | [vwHugsNHopeParties](dbo.vwHugsNHopeParties.md) | dbo.Country, dbo.Customer, dbo.Event, dbo.Package, dbo.Party, dbo.Store |
| dbo | [vwMissingStoreFromStoreMDM](dbo.vwMissingStoreFromStoreMDM.md) | dbo.BEAREA_CNTCT_DIM, dbo.BEAREA_DIM, dbo.BEARITORY_DIM, dbo.CNTCT_DIM, dbo.Store, dbo.STR_DIM, dbo.STR_INFO, dbo.STR_OPEN_DIM |
| dbo | [vwPackageStyleParties](dbo.vwPackageStyleParties.md) | dbo.Country, dbo.Customer, dbo.Event, dbo.Package, dbo.PackageStyle, dbo.Party, dbo.Store |
| dbo | [vwPartiesBookedEvery30Minutes](dbo.vwPartiesBookedEvery30Minutes.md) | dbo.Event, dbo.Party |
| dbo | [vwStoreToStoreMDM](dbo.vwStoreToStoreMDM.md) | dbo.BEAREA_CNTCT_DIM, dbo.BEAREA_DIM, dbo.BEARITORY_DIM, dbo.CNTCT_DIM, dbo.Store, dbo.STR_DIM, dbo.STR_INFO, dbo.STR_OPEN_DIM |
| dbo | [vwThemesPackages](dbo.vwThemesPackages.md) | dbo.Package, dbo.Theme, dbo.ThemePackageXref |
