# Stored Procedures: BABWPartyPlanner

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [sp_AddPackageStyleData](dbo.sp_AddPackageStyleData.md) | dbo.PackageStyle |
| dbo | [sp_AddPackageThemeXref](dbo.sp_AddPackageThemeXref.md) | dbo.ThemePackageXref |
| dbo | [sp_alterdiagram](dbo.sp_alterdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_creatediagram](dbo.sp_creatediagram.md) | dbo.sysdiagrams |
| dbo | [sp_DeletePackageThemeXref](dbo.sp_DeletePackageThemeXref.md) | dbo.ThemePackageXref |
| dbo | [sp_DisableTheme](dbo.sp_DisableTheme.md) | dbo.Theme |
| dbo | [sp_dropdiagram](dbo.sp_dropdiagram.md) | dbo.sysdiagrams |
| dbo | [sp_GetAllStyles](dbo.sp_GetAllStyles.md) | dbo.PackageStyle, dbo.PackageStyleXref, dbo.Style |
| dbo | [sp_GetAllStylesData](dbo.sp_GetAllStylesData.md) | dbo.PackageStyle, dbo.PackageStyleXref, dbo.Style |
| dbo | [sp_GetBookedDatesAndTimesByStore_SS20170725](dbo.sp_GetBookedDatesAndTimesByStore_SS20170725.md) | dbo.Event, dbo.Store |
| dbo | [sp_GetBookedPartiesByCustomer_BJB](dbo.sp_GetBookedPartiesByCustomer_BJB.md) |  |
| dbo | [sp_GetBookedPartiesByCustomer_SS20170725](dbo.sp_GetBookedPartiesByCustomer_SS20170725.md) | dbo.Comment, dbo.Customer, dbo.Event, dbo.OptionPartyXref, dbo.Party |
| dbo | [sp_GetBookedPartiesByEventID](dbo.sp_GetBookedPartiesByEventID.md) | dbo.Comment, dbo.Customer, dbo.Event, dbo.OptionPartyXref, dbo.Party |
| dbo | [sp_GetBookedPartiesByEventIDS](dbo.sp_GetBookedPartiesByEventIDS.md) | dbo.Comment, dbo.Customer, dbo.Event, dbo.OptionPartyXref, dbo.Party, Item.value |
| dbo | [sp_GetBookedPartiesByPartyID_BJB20190228](dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md) | dbo.Comment, dbo.Customer, dbo.Event, dbo.OptionPartyXref, dbo.Party, dbo.PartyEnterpriseSellingXRef, dbo.PurchaseOrder, WM.ItemStatus, WM.ItemStatus_Archive, WM.OrderItems, WM.Orders |
| dbo | [sp_GetBookedPartiesByPartyID_BJB20240611](dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md) | dbo.Comment, dbo.Customer, dbo.Event, dbo.OptionPartyXref, dbo.Party, dbo.PartyEnterpriseSellingXRef, dbo.PurchaseOrder, WM.ItemStatus, WM.ItemStatus_Archive, WM.OrderItems, WM.Orders |
| dbo | [sp_GetLargestPackageStyleID](dbo.sp_GetLargestPackageStyleID.md) | dbo.PackageStyle |
| dbo | [sp_GetNewStylesData](dbo.sp_GetNewStylesData.md) | dbo.PackageStyle |
| dbo | [sp_GetPartyChoicesByStore_V2](dbo.sp_GetPartyChoicesByStore_V2.md) | dbo.ATTR_VALUE_DIM, dbo.DepositLevel, dbo.Occasion, dbo.Option, dbo.OptionStoreXref, dbo.Package, dbo.Store, dbo.StorePackageXref, dbo.STR_ATTR_DIM, dbo.STR_DIM, dbo.ThemePackageXref |
| dbo | [sp_GetStyleCodeIdData](dbo.sp_GetStyleCodeIdData.md) | dbo.Style |
| dbo | [sp_GetTheme](dbo.sp_GetTheme.md) | dbo.Theme |
| dbo | [sp_GetThemes](dbo.sp_GetThemes.md) | dbo.Theme |
| dbo | [sp_GetThemesByPackageID](dbo.sp_GetThemesByPackageID.md) | dbo.vwThemesPackages |
| dbo | [sp_helpdiagramdefinition](dbo.sp_helpdiagramdefinition.md) | dbo.sysdiagrams |
| dbo | [sp_helpdiagrams](dbo.sp_helpdiagrams.md) | dbo.sysdiagrams |
| dbo | [sp_InsertCommentFromPartyID](dbo.sp_InsertCommentFromPartyID.md) | dbo.Party, dbo.sp_InsertNewComment |
| dbo | [sp_InsertNewParty_V2](dbo.sp_InsertNewParty_V2.md) | dbo.Party |
| dbo | [sp_InsertNewPrivacyProtection](dbo.sp_InsertNewPrivacyProtection.md) | dbo.PrivacyProtection, dbo.PrivacyRegulation |
| dbo | [sp_InsertTheme](dbo.sp_InsertTheme.md) | dbo.Theme |
| dbo | [sp_renamediagram](dbo.sp_renamediagram.md) | dbo.sysdiagrams |
| dbo | [sp_SubmitBooking_V4](dbo.sp_SubmitBooking_V4.md) | dbo.Comment, dbo.OptionPartyXref, dbo.sp_FindExistingCustomerID, dbo.sp_InsertNewCustomer, dbo.sp_InsertNewEvent, dbo.sp_InsertNewParty_V2, dbo.sp_InsertNewPurchaseOrder, dbo.sp_UpdateCustomer, Item.value |
| dbo | [sp_SubmitBooking_V5](dbo.sp_SubmitBooking_V5.md) | dbo.Comment, dbo.OptionPartyXref, dbo.sp_FindExistingCustomerID, dbo.sp_InsertNewCustomer, dbo.sp_InsertNewEvent, dbo.sp_InsertNewParty_V2, dbo.sp_InsertNewPrivacyProtection, dbo.sp_InsertNewPurchaseOrder, dbo.sp_UpdateCustomer, Item.value |
| dbo | [sp_UpdateBooking_V3](dbo.sp_UpdateBooking_V3.md) | dbo.Comment, dbo.Customer, dbo.Event, dbo.Party, dbo.PurchaseOrder, dbo.sp_UpdateCustomer, Item.value |
| dbo | [sp_UpdateTheme](dbo.sp_UpdateTheme.md) | dbo.Theme |
| dbo | [sp_upgraddiagrams](dbo.sp_upgraddiagrams.md) | dbo.dtproperties, dbo.sysdiagrams |
| dbo | [spGetStoreMDMPositionByUserName](dbo.spGetStoreMDMPositionByUserName.md) | dbo.CNTCT_DIM, dbo.ROLES_DIM |
| dbo | [spGetStoreMDMStoresByUserName](dbo.spGetStoreMDMStoresByUserName.md) | dbo.BEARITORY_DIM, dbo.CNTCT_DIM, dbo.STR_DIM, dbo.STR_OPEN_DIM |
| dbo | [spLoadOrderIdForPartyESOrder](dbo.spLoadOrderIdForPartyESOrder.md) | dbo.PartyEnterpriseSellingXRef, WM.Orders |
| dbo | [spMaintainStyle](dbo.spMaintainStyle.md) | dbo.hierarchy_group, dbo.style, dbo.style_group |
| dbo | [spRPT_GSPartyBookingsReportDaily](dbo.spRPT_GSPartyBookingsReportDaily.md) | dbo.Country, dbo.Customer, dbo.Event, dbo.Occasion, dbo.Package, dbo.Party, dbo.sp_send_dbmail, dbo.Store, WMS.PartyHeader |
| dbo | [spRPT_GSPartyBookingsReportDaily_BAK20240729](dbo.spRPT_GSPartyBookingsReportDaily_BAK20240729.md) | dbo.Country, dbo.Customer, dbo.Event, dbo.Occasion, dbo.Package, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
| dbo | [spRPT_GSPartyBookingsReportDaily_BAK20260512](dbo.spRPT_GSPartyBookingsReportDaily_BAK20260512.md) | dbo.Country, dbo.Customer, dbo.Event, dbo.Occasion, dbo.Package, dbo.Party, dbo.sp_send_dbmail, dbo.Store, WMS.PartyHeader |
| dbo | [spRPT_PartyBookingSummaryDailyUK](dbo.spRPT_PartyBookingSummaryDailyUK.md) | dbo.Event, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
| dbo | [spRPT_PartyBookingSummaryDailyUK_BAK20220419](dbo.spRPT_PartyBookingSummaryDailyUK_BAK20220419.md) | dbo.Event, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
| dbo | [spRPT_PartyBookingSummaryDailyUK_WIP20220419](dbo.spRPT_PartyBookingSummaryDailyUK_WIP20220419.md) | dbo.Event, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
| dbo | [spRPT_PartyBookingSummaryDailyUS](dbo.spRPT_PartyBookingSummaryDailyUS.md) | dbo.Event, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
| dbo | [spRPT_PartyBookingSummaryDailyUS_BAK20220419](dbo.spRPT_PartyBookingSummaryDailyUS_BAK20220419.md) | dbo.Event, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
| dbo | [spRPT_PartyBookingSummaryDailyUS_WIP20220419](dbo.spRPT_PartyBookingSummaryDailyUS_WIP20220419.md) | dbo.Event, dbo.Party, dbo.sp_send_dbmail, dbo.Store |
