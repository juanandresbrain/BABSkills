# WMS.VendInvoiceJournalLine

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AccountDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| AccountType | nvarchar | 510 | 1 |  |  |  |
| Approved | nvarchar | 510 | 1 |  |  |  |
| ApproverNumber | nvarchar | 8000 | 1 |  |  |  |
| AssetId | nvarchar | 8000 | 1 |  |  |  |
| AssetTransType | nvarchar | 510 | 1 |  |  |  |
| BankAccountId | nvarchar | 8000 | 1 |  |  |  |
| BookId | nvarchar | 8000 | 1 |  |  |  |
| CashDiscount | nvarchar | 8000 | 1 |  |  |  |
| CashDiscountAmount | float | 8 | 1 |  |  |  |
| CashDiscountDate | datetime | 8 | 1 |  |  |  |
| ChineseVoucher | nvarchar | 8000 | 1 |  |  |  |
| ChineseVoucherType | nvarchar | 8000 | 1 |  |  |  |
| Company | nvarchar | 8000 | 1 |  |  |  |
| Credit | float | 8 | 1 |  |  |  |
| Currency | nvarchar | 8000 | 1 |  |  |  |
| CustVendBankAccountId | nvarchar | 8000 | 1 |  |  |  |
| dataAreaId | nvarchar | 8000 | 1 |  |  |  |
| Date | datetime | 8 | 1 |  |  |  |
| Debit | float | 8 | 1 |  |  |  |
| DefaultDimensionDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| DeliveryDate | datetime | 8 | 1 |  |  |  |
| Description | nvarchar | 8000 | 1 |  |  |  |
| Document | nvarchar | 8000 | 1 |  |  |  |
| DueDate | datetime | 8 | 1 |  |  |  |
| ExchRate | float | 8 | 1 |  |  |  |
| ExchRateSecond | float | 8 | 1 |  |  |  |
| FullPrimaryRemittanceAddress | nvarchar | 8000 | 1 |  |  |  |
| GSTHSTTaxType | nvarchar | 510 | 1 |  |  |  |
| Invoice | nvarchar | 8000 | 1 |  |  |  |
| InvoiceDate | datetime | 8 | 1 |  |  |  |
| InvoiceDeclarationId | nvarchar | 8000 | 1 |  |  |  |
| IsWithholdingTaxCalculate | nvarchar | 510 | 1 |  |  |  |
| ItemSalesTaxGroup | nvarchar | 8000 | 1 |  |  |  |
| ItemWithholdingTaxGroupCode | nvarchar | 8000 | 1 |  |  |  |
| ITMCostArea | nvarchar | 510 | 1 |  |  |  |
| ITMCostTypeId | nvarchar | 8000 | 1 |  |  |  |
| JournalBatchNumber | nvarchar | 8000 | 1 |  |  |  |
| LineNumber | float | 8 | 1 |  |  |  |
| Listcode | nvarchar | 510 | 1 |  |  |  |
| MethodOfPayment | nvarchar | 8000 | 1 |  |  |  |
| OffsetAccountDisplayValue | nvarchar | 8000 | 1 |  |  |  |
| OffsetAccountType | nvarchar | 510 | 1 |  |  |  |
| OffsetCompany | nvarchar | 8000 | 1 |  |  |  |
| OffsetTransactionText | nvarchar | 8000 | 1 |  |  |  |
| OverrideSalesTax | nvarchar | 510 | 1 |  |  |  |
| PaymentSpecification | nvarchar | 8000 | 1 |  |  |  |
| PaymId | nvarchar | 8000 | 1 |  |  |  |
| PostingProfile | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressCity | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressCountry | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressCountryISOCode | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressCounty | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressDescription | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressDistrictName | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressLatitude | float | 8 | 1 |  |  |  |
| RemittanceAddressLocationId | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressLongitude | float | 8 | 1 |  |  |  |
| RemittanceAddressState | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressStreet | nvarchar | 8000 | 1 |  |  |  |
| RemittanceAddressTimeZone | nvarchar | 510 | 1 |  |  |  |
| RemittanceAddressValidFrom | datetime | 8 | 1 |  |  |  |
| RemittanceAddressValidTo | datetime | 8 | 1 |  |  |  |
| RemittanceAddressZipCode | nvarchar | 8000 | 1 |  |  |  |
| ReportingCurrencyExchRate | float | 8 | 1 |  |  |  |
| rsmActualSalesTaxAmount | float | 8 | 1 |  |  |  |
| rsmCalcSalesTaxAmount | float | 8 | 1 |  |  |  |
| SalesTaxCode | nvarchar | 8000 | 1 |  |  |  |
| SalesTaxGroup | nvarchar | 8000 | 1 |  |  |  |
| Tax1099Amount | float | 8 | 1 |  |  |  |
| Tax1099Fields | bigint | 8 | 1 |  |  |  |
| TaxExemptNumber | nvarchar | 8000 | 1 |  |  |  |
| TermsOfPayment | nvarchar | 8000 | 1 |  |  |  |
| TransactionType | nvarchar | 510 | 1 |  |  |  |
| TypeOfOperation | nvarchar | 510 | 1 |  |  |  |
| UUID | nvarchar | 8000 | 1 |  |  |  |
| Voucher | nvarchar | 8000 | 1 |  |  |  |

