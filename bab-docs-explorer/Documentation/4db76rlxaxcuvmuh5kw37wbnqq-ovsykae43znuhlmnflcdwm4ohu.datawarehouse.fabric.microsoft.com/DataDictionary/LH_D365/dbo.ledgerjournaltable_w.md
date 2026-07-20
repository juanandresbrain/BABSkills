# dbo.ledgerjournaltable_w

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| approvalstatus_cn | bigint | 8 | 1 |  |  |  |
| informbyphone_lt | bigint | 8 | 1 |  |  |  |
| informbytelex_lt | bigint | 8 | 1 |  |  |  |
| prepayment_w | bigint | 8 | 1 |  |  |  |
| reverse_ru | bigint | 8 | 1 |  |  |  |
| reversetype_ru | bigint | 8 | 1 |  |  |  |
| taxtype_br | bigint | 8 | 1 |  |  |  |
| foreignbankfee_lt | bigint | 8 | 1 |  |  |  |
| paymentpriority_lt | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| cashaccount_w | varchar | 8000 | 1 |  |  |  |
| debitcurrencycode_lt | varchar | 8000 | 1 |  |  |  |
| fiscalestablishment_br | bigint | 8 | 1 |  |  |  |
| ledgerjournaltable | bigint | 8 | 1 |  |  |  |
| reportperiod_ru | datetime2 | 8 | 1 |  |  |  |
| reportingdate_ru | datetime2 | 8 | 1 |  |  |  |
| rtax25regversion | bigint | 8 | 1 |  |  |  |
| reversejournaltable_lt | bigint | 8 | 1 |  |  |  |
| categorypurpose_w | bigint | 8 | 1 |  |  |  |
| chargebearer_w | bigint | 8 | 1 |  |  |  |
| localinstrument_w | bigint | 8 | 1 |  |  |  |
| servicelevel_w | bigint | 8 | 1 |  |  |  |
| businessdocumentsubmissionid_w | varchar | 8000 | 1 |  |  |  |
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
