# dbo.mainaccount

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| adjustmentmethod_mx | bigint | 8 | 1 |  |  |  |
| closetype | bigint | 8 | 1 |  |  |  |
| closing | bigint | 8 | 1 |  |  |  |
| debitcreditbalancedemand | bigint | 8 | 1 |  |  |  |
| debitcreditcheck | bigint | 8 | 1 |  |  |  |
| debitcreditproposal | bigint | 8 | 1 |  |  |  |
| exchangeadjusted | bigint | 8 | 1 |  |  |  |
| financialreportingtranslationtype | bigint | 8 | 1 |  |  |  |
| inflationadjustment_mx | bigint | 8 | 1 |  |  |  |
| mandatorypaymentreference | bigint | 8 | 1 |  |  |  |
| monetary | bigint | 8 | 1 |  |  |  |
| postingtype | bigint | 8 | 1 |  |  |  |
| repomotype_mx | bigint | 8 | 1 |  |  |  |
| reportingaccounttype | bigint | 8 | 1 |  |  |  |
| type | bigint | 8 | 1 |  |  |  |
| validatecurrency | bigint | 8 | 1 |  |  |  |
| validateposting | bigint | 8 | 1 |  |  |  |
| validateuser | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountcategoryref | bigint | 8 | 1 |  |  |  |
| consolidationmainaccount | varchar | 8000 | 1 |  |  |  |
| currencycode | varchar | 8000 | 1 |  |  |  |
| exchangeadjustmentratetype | bigint | 8 | 1 |  |  |  |
| financialreportingexchangeratetype | bigint | 8 | 1 |  |  |  |
| ledgerchartofaccounts | bigint | 8 | 1 |  |  |  |
| mainaccountid | varchar | 8000 | 1 |  |  |  |
| mainaccounttemplate | bigint | 8 | 1 |  |  |  |
| name | varchar | 8000 | 1 |  |  |  |
| offsetledgerdimension | bigint | 8 | 1 |  |  |  |
| openingaccount | bigint | 8 | 1 |  |  |  |
| parentmainaccount | bigint | 8 | 1 |  |  |  |
| srucode | varchar | 8000 | 1 |  |  |  |
| transferyearendaccount_es | bigint | 8 | 1 |  |  |  |
| unitofmeasure | bigint | 8 | 1 |  |  |  |
| userinfoid | varchar | 8000 | 1 |  |  |  |
| parentmainaccount_br | bigint | 8 | 1 |  |  |  |
| reportingexchangeadjustmentratetype | bigint | 8 | 1 |  |  |  |
| standardmainaccount_w | bigint | 8 | 1 |  |  |  |
| naturecode_br | varchar | 8000 | 1 |  |  |  |
| modifieddatetime | datetime2 | 8 | 1 |  |  |  |
| modifiedby | varchar | 8000 | 1 |  |  |  |
| modifiedtransactionid | bigint | 8 | 1 |  |  |  |
| createddatetime | datetime2 | 8 | 1 |  |  |  |
| createdby | varchar | 8000 | 1 |  |  |  |
| createdtransactionid | bigint | 8 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| recversion | bigint | 8 | 1 |  |  |  |
| partition | bigint | 8 | 1 |  |  |  |
| sysrowversion | bigint | 8 | 1 |  |  |  |
| recid | bigint | 8 | 1 |  |  |  |
| tableid | bigint | 8 | 1 |  |  |  |
| versionnumber | bigint | 8 | 1 |  |  |  |
| createdon | datetime2 | 8 | 1 |  |  |  |
| modifiedon | datetime2 | 8 | 1 |  |  |  |
| IsDelete | bit | 1 | 1 |  |  |  |
| createdonpartition | varchar | 8000 | 1 |  |  |  |
| PartitionId | varchar | 2048 | 1 |  |  |  |
