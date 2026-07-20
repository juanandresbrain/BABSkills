# dbo.customertransactionetllog

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PackageStartTime | datetime2 | 8 | 1 |  |  |  |
| CRMCustomerDimStaged | int | 4 | 1 |  |  |  |
| CRMCustomerDimMergeInserted | int | 4 | 1 |  |  |  |
| CRMCustomerDimMergeUpdated | int | 4 | 1 |  |  |  |
| CRMTransactionFactStaged | int | 4 | 1 |  |  |  |
| CRMTransactionFactMergeInserted | int | 4 | 1 |  |  |  |
| CRMTransactionFactMergeUpdated | int | 4 | 1 |  |  |  |
| NameMeTransactionFactStaged | int | 4 | 1 |  |  |  |
| NameMeTransactionFactMergeInserted | int | 4 | 1 |  |  |  |
| NameMeTransactionFactMergeUpdated | int | 4 | 1 |  |  |  |
| ETLLogID | int | 4 | 1 |  |  |  |
| ValidationStatus | varchar | 8000 | 1 |  |  |  |
