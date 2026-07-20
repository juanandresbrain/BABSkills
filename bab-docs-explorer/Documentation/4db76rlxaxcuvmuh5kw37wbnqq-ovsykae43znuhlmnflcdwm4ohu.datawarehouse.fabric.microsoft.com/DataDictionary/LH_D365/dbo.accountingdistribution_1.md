# dbo.accountingdistribution_1

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| amountsource | bigint | 8 | 1 |  |  |  |
| monetaryamount | bigint | 8 | 1 |  |  |  |
| referencerole | bigint | 8 | 1 |  |  |  |
| type | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountingdate | datetime2 | 8 | 1 |  |  |  |
| accountingevent | bigint | 8 | 1 |  |  |  |
| accountinglegalentity | bigint | 8 | 1 |  |  |  |
| allocationfactor | decimal | 17 | 1 |  |  |  |
| finalizeaccountingevent | bigint | 8 | 1 |  |  |  |
| ledgerdimension | bigint | 8 | 1 |  |  |  |
| number | bigint | 8 | 1 |  |  |  |
| parentdistribution | bigint | 8 | 1 |  |  |  |
| referencedistribution | bigint | 8 | 1 |  |  |  |
| sourcedocumentheader | bigint | 8 | 1 |  |  |  |
| sourcedocumentline | bigint | 8 | 1 |  |  |  |
| transactioncurrency | varchar | 8000 | 1 |  |  |  |
| transactioncurrencyamount | decimal | 17 | 1 |  |  |  |
| fintag | bigint | 8 | 1 |  |  |  |
| accountingcurrencyamount | decimal | 17 | 1 |  |  |  |
| accountingcurrency | varchar | 8000 | 1 |  |  |  |
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
