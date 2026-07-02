# Views: esell

| Schema | View | Table Dependencies |
|---|---|---|
| dbo | [BIvw_enterprise_selling_facts](dbo.BIvw_enterprise_selling_facts.md) | esell.order_current_state_type, esell.order_fulfillment, esell.order_line_item, esell.order_state, esell.order_type, esell.orders, esell.outlet, esell.sku |
| dbo | [SV_ADDRESS](dbo.SV_ADDRESS.md) | dbo.GEOG_ADRS, dbo.PRTY_ADRS, dbo.PRTY_ADRS_FNCTN, dbo.PRTY_ADRS_FNCTN_LANG |
| dbo | [SV_FACILITY](dbo.SV_FACILITY.md) | dbo.FNDTN_LANG, dbo.ORG_CHN, dbo.ORG_CHN_TYPE |
| dbo | [SV_HEAD_OFFICE](dbo.SV_HEAD_OFFICE.md) | dbo.FNDTN_LANG, dbo.ORG_CHN, dbo.ORG_CHN_TYPE |
| dbo | [SV_ORG_CHN](dbo.SV_ORG_CHN.md) | dbo.FNDTN_LANG, dbo.ORG_CHN, dbo.ORG_CHN_TYPE |
| dbo | [SV_PRMY_ADDRESS](dbo.SV_PRMY_ADDRESS.md) | dbo.GEOG_ADRS, dbo.PRTY_ADRS |
| dbo | [SV_SERVER_WRKSTN](dbo.SV_SERVER_WRKSTN.md) | dbo.ORG_CHN_WRKSTN |
| dbo | [SV_STORE_BANK](dbo.SV_STORE_BANK.md) | dbo.ORG_BANK, dbo.ORG_BANK_ACNT, dbo.ORG_BANK_BRNCH, dbo.SV_STORES |
| dbo | [SV_STORES](dbo.SV_STORES.md) | dbo.FNDTN_LANG, dbo.ORG_CHN, dbo.ORG_CHN_TYPE |
| dbo | [vwInventory](dbo.vwInventory.md) | dbo.vwWebHierarchy, dbo.vwWebIncludedStyles, dbo.vwWebLocations, esell.outlet_sku_xref, esell.sku |
