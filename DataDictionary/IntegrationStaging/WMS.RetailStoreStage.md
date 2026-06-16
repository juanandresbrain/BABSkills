# WMS.RetailStoreStage

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| BankDropCalculation | nvarchar | 510 | 1 |  |  |  |
| ChannelProfileName | nvarchar | 8000 | 1 |  |  |  |
| ChannelTimeZone | nvarchar | 510 | 1 |  |  |  |
| ChannelTimeZoneInfoId | nvarchar | 8000 | 1 |  |  |  |
| ClosingMethod | nvarchar | 510 | 1 |  |  |  |
| CreateLabelsForZeroPrice | nvarchar | 510 | 1 |  |  |  |
| CultureName | nvarchar | 8000 | 1 |  |  |  |
| Currency | nvarchar | 8000 | 1 |  |  |  |
| DatabaseName | nvarchar | 8000 | 1 |  |  |  |
| DefaultCustomerAccount | nvarchar | 8000 | 1 |  |  |  |
| DefaultCustomerLegalEntity | nvarchar | 8000 | 1 |  |  |  |
| DefaultDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| DisplayTaxPerTaxComponent | nvarchar | 510 | 1 |  |  |  |
| ElectronicFundsTransferStoreNumber | nvarchar | 8000 | 1 |  |  |  |
| EndOfBusinessDay | int | 4 | 1 |  |  |  |
| EventNotificationProfileId | nvarchar | 8000 | 1 |  |  |  |
| FunctionalityProfile | nvarchar | 8000 | 1 |  |  |  |
| GeneratesItemLabels | nvarchar | 510 | 1 |  |  |  |
| GeneratesShelfLabels | nvarchar | 510 | 1 |  |  |  |
| HideTrainingMode | nvarchar | 510 | 1 |  |  |  |
| InventoryLookup | nvarchar | 510 | 1 |  |  |  |
| LayoutId | nvarchar | 8000 | 1 |  |  |  |
| LiveDatabaseConnectionProfileName | nvarchar | 8000 | 1 |  |  |  |
| MaximumPostingDifference | float | 8 | 1 |  |  |  |
| MaximumTextLengthOnReceipt | int | 4 | 1 |  |  |  |
| MaxRoundingAmount | float | 8 | 1 |  |  |  |
| MaxRoundingTaxAmount | float | 8 | 1 |  |  |  |
| MaxShiftDifferenceAmount | float | 8 | 1 |  |  |  |
| MaxTransactionDifferenceAmount | float | 8 | 1 |  |  |  |
| NumberOfTopOrBottomLines | int | 4 | 1 |  |  |  |
| OfflineProfileName | nvarchar | 8000 | 1 |  |  |  |
| OneStatementPerDay | nvarchar | 510 | 1 |  |  |  |
| OpenFrom | int | 4 | 1 |  |  |  |
| OpenTo | int | 4 | 1 |  |  |  |
| OperatingUnitNumber | nvarchar | 8000 | 1 |  |  |  |
| OperatingUnitPartyNumber | nvarchar | 8000 | 1 |  |  |  |
| PaymentMethodName | nvarchar | 8000 | 1 |  |  |  |
| PaymentMethodToRemoveOrAdd | nvarchar | 8000 | 1 |  |  |  |
| Phone | nvarchar | 8000 | 1 |  |  |  |
| PriceIncludesSalesTax | nvarchar | 510 | 1 |  |  |  |
| ProductCategoryHierarchyName | nvarchar | 8000 | 1 |  |  |  |
| ProductNumberOnReceipt | nvarchar | 510 | 1 |  |  |  |
| PurchaseOrderItemFilter | nvarchar | 510 | 1 |  |  |  |
| RetailChannelId | nvarchar | 8000 | 1 |  |  |  |
| RetailChannelPriceGroup | nvarchar | -1 | 1 |  |  |  |
| RetailStoreHardwareStation | nvarchar | -1 | 1 |  |  |  |
| RetailStoreLocatorGroupOwner | nvarchar | -1 | 1 |  |  |  |
| RetailStoreTenderType | nvarchar | -1 | 1 |  |  |  |
| RetailTerminal | nvarchar | -1 | 1 |  |  |  |
| RoundingAccountLedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| RoundingTaxAccount | nvarchar | 8000 | 1 |  |  |  |
| SeparateStatementPerStaffTerminal | nvarchar | 510 | 1 |  |  |  |
| ServiceChargePercentage | float | 8 | 1 |  |  |  |
| ServiceChargePrompt | nvarchar | 8000 | 1 |  |  |  |
| SQLServerName | nvarchar | 8000 | 1 |  |  |  |
| StartAmountCalculation | nvarchar | 510 | 1 |  |  |  |
| StatementMethod | nvarchar | 510 | 1 |  |  |  |
| StatementPostAsBusinessDay | nvarchar | 510 | 1 |  |  |  |
| StoreArea | float | 8 | 1 |  |  |  |
| StoreNumber | nvarchar | 8000 | 1 |  |  |  |
| TaxGroupCode | nvarchar | 8000 | 1 |  |  |  |
| TaxGroupLegalEntity | nvarchar | 8000 | 1 |  |  |  |
| TaxIdentificationNumber | nvarchar | 8000 | 1 |  |  |  |
| TaxOverrideGroupCode | nvarchar | 8000 | 1 |  |  |  |
| TaxOverrideGroupCodeLegalEntity | nvarchar | 8000 | 1 |  |  |  |
| TenderDeclarationCalculation | nvarchar | 510 | 1 |  |  |  |
| TermsOfPayment | nvarchar | 8000 | 1 |  |  |  |
| TransactionServiceProfile | nvarchar | 8000 | 1 |  |  |  |
| UseCustomerBasedTax | nvarchar | 510 | 1 |  |  |  |
| UseCustomerBasedTaxExemption | nvarchar | 510 | 1 |  |  |  |
| UseDefaultCustomerAccount | nvarchar | 510 | 1 |  |  |  |
| UseDestinationBasedTax | nvarchar | 510 | 1 |  |  |  |
| WarehouseId | nvarchar | 8000 | 1 |  |  |  |
| WarehouseIdForCustomerOrder | nvarchar | 8000 | 1 |  |  |  |
| WarehouseLegalEntity | nvarchar | 8000 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeRetailStore](../../StoredProcedures/IntegrationStaging/WMS.spMergeRetailStore.md)

