# WMS.RetailStoreTenderTypeStage

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AboveMinimumTenderId | nvarchar | 8000 | 1 |  |  |  |
| AccountType | nvarchar | 510 | 1 |  |  |  |
| AccountTypeGiftCardCompany | nvarchar | 510 | 1 |  |  |  |
| ActiveAccount | nvarchar | 510 | 1 |  |  |  |
| AllowFloat | nvarchar | 510 | 1 |  |  |  |
| AllowOvertender | nvarchar | 510 | 1 |  |  |  |
| AllowReturnNegative | nvarchar | 510 | 1 |  |  |  |
| AllowUndertender | nvarchar | 510 | 1 |  |  |  |
| AskForDate | nvarchar | 510 | 1 |  |  |  |
| BankBagAccountType | nvarchar | 510 | 1 |  |  |  |
| BankBagLedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| ChangeLineOnReceipt | nvarchar | 8000 | 1 |  |  |  |
| ChangeTenderId | nvarchar | 8000 | 1 |  |  |  |
| CheckPayee | nvarchar | 8000 | 1 |  |  |  |
| CompressPaymentEntries | nvarchar | 510 | 1 |  |  |  |
| ConnectorName | nvarchar | 8000 | 1 |  |  |  |
| CountingRequired | nvarchar | 510 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| DefaultDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| DiffAccBigDiffLedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| DifferenceAccLedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| EndorseCheck | nvarchar | 510 | 1 |  |  |  |
| EndorsmentLine1 | nvarchar | 8000 | 1 |  |  |  |
| EndorsmentLine2 | nvarchar | 8000 | 1 |  |  |  |
| FrontOfCheck | nvarchar | 510 | 1 |  |  |  |
| Function | nvarchar | 510 | 1 |  |  |  |
| GiftCardCashOutThreshold | float | 8 | 1 |  |  |  |
| GiftCardCompany | nvarchar | 8000 | 1 |  |  |  |
| GiftCardItemId | nvarchar | 8000 | 1 |  |  |  |
| HideCardInputDetailsInPOS | nvarchar | 510 | 1 |  |  |  |
| LedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| LedgerDimensionGiftCardCompanyDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| LineNumInTransaction | nvarchar | 8000 | 1 |  |  |  |
| MaxCountingDifference | float | 8 | 1 |  |  |  |
| MaximumAmountAllowed | float | 8 | 1 |  |  |  |
| MaximumAmountEntered | float | 8 | 1 |  |  |  |
| MaximumOvertenderAmount | float | 8 | 1 |  |  |  |
| MaxNormalDifferenceAmount | float | 8 | 1 |  |  |  |
| MaxRecount | int | 4 | 1 |  |  |  |
| MinimumAmountAllowed | float | 8 | 1 |  |  |  |
| MinimumAmountEntered | float | 8 | 1 |  |  |  |
| MinimumChangeAmount | float | 8 | 1 |  |  |  |
| MultiplyInTenderOperations | nvarchar | 510 | 1 |  |  |  |
| Name | nvarchar | 8000 | 1 |  |  |  |
| OpenDrawer | nvarchar | 510 | 1 |  |  |  |
| PayAccountBill | nvarchar | 510 | 1 |  |  |  |
| PaymentMethodNumber | nvarchar | 8000 | 1 |  |  |  |
| PaymTermId | nvarchar | 8000 | 1 |  |  |  |
| PosCountEntries | nvarchar | 510 | 1 |  |  |  |
| PosOperation | int | 4 | 1 |  |  |  |
| RetailChannelId | nvarchar | 8000 | 1 |  |  |  |
| Rounding | float | 8 | 1 |  |  |  |
| RoundingMethod | nvarchar | 510 | 1 |  |  |  |
| SafeAccLedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| SafeAccountType | nvarchar | 510 | 1 |  |  |  |
| SafeActiveAccount | nvarchar | 510 | 1 |  |  |  |
| SeekAuthorization | nvarchar | 510 | 1 |  |  |  |
| SigCapEnabled | nvarchar | 510 | 1 |  |  |  |
| SignatureCaptureMinAmount | float | 8 | 1 |  |  |  |
| SlipBackInPrinter | nvarchar | 8000 | 1 |  |  |  |
| SlipFrontInPrinter | nvarchar | 8000 | 1 |  |  |  |
| TakenToBank | nvarchar | 510 | 1 |  |  |  |
| TakenToSafe | nvarchar | 510 | 1 |  |  |  |
| TenderFlowLedgerDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| UndertenderAmount | float | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: WMS.spMergeRetailStoreTenderType](../../StoredProcedures/IntegrationStaging/WMS.spMergeRetailStoreTenderType.md)

