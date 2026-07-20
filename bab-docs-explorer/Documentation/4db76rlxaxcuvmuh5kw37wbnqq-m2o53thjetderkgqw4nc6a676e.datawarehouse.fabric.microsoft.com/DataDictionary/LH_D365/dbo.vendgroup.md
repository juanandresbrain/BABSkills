# dbo.vendgroup

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| excludefromsignup_psn | bigint | 8 | 1 |  |  |  |
| ispublicsector_it | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| clearingperiod | varchar | 8000 | 1 |  |  |  |
| name | varchar | 8000 | 1 |  |  |  |
| paymtermid | varchar | 8000 | 1 |  |  |  |
| taxgroupid | varchar | 8000 | 1 |  |  |  |
| taxperiodpaymentcode_pl | varchar | 8000 | 1 |  |  |  |
| vendgroup | varchar | 8000 | 1 |  |  |  |
| vendaccountnumseq | bigint | 8 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| accountingcurrencyexchangeratetype | bigint | 8 | 1 |  |  |  |
| reportingcurrencyexchangeratetype | bigint | 8 | 1 |  |  |  |
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
