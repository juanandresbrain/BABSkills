# Stored Procedures: EJ

| Schema | Name | Table Dependencies |
|---|---|---|
| dbo | [spMDB_backup_for_WebEJ](dbo.spMDB_backup_for_WebEJ.md) | dbo.sp_send_dbmail |
| -- Description: | [Backs up MDB files used for importing into the EJ database for WebEJ.  Creates or adds to ZIP](--_Description_Backs_up_MDB_files_used_for_importing_into_the_EJ_database_for_WebEJ._Creates_or_adds_to_ZIP.md) |  |
| dbo | [spNewStoreSetupCheckWebEJ](dbo.spNewStoreSetupCheckWebEJ.md) | dbo.notification_history, dbo.POLLING_STORES, dbo.sp_send_dbmail, dbo.STORES |
| -- Description: | [Performs some checks on store setup and reports to the user responsible for](--_Description_.Performs_some_checks_on_store_setup_and_reports_to_the_user_responsible_for.md) |  |
| dbo | [spTruncateEJHistory](dbo.spTruncateEJHistory.md) | dbo.IMPORT_AUDIT, dbo.SIGNATURES, dbo.Tenders, dbo.Transactions |
| -- Description: | [Truncates history data to conserve space.](--_Description_Truncates_history_data_to_conserve_space..md) |  |
| dbo | [usi_GetModifiers](dbo.usi_GetModifiers.md) | dbo.Modifier_Types |
| dbo | [usi_GetReceipt](dbo.usi_GetReceipt.md) | dbo.TRANSACTIONS |
| and TILLNO | [= @Till](and_TILLNO.=_@Till.md) |  |
| and | [STORENO](and.STORENO.md) |  |
| and | [[DATETIME]](and._DATETIME.md) |  |
| dbo | [usi_GetStores](dbo.usi_GetStores.md) | dbo.STORES |
| dbo | [usi_GetTenderTypes](dbo.usi_GetTenderTypes.md) | dbo.TENDER_TYPES |
| dbo | [usi_GetTransactionTypes](dbo.usi_GetTransactionTypes.md) | dbo.TRANSACTION_TYPES |
