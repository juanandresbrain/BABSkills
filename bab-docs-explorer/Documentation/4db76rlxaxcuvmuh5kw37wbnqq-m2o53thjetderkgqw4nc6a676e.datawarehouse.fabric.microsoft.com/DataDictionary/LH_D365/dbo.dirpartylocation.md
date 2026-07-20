# dbo.dirpartylocation

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| islocationowner | bigint | 8 | 1 |  |  |  |
| ispostaladdress | bigint | 8 | 1 |  |  |  |
| isprimary | bigint | 8 | 1 |  |  |  |
| isprimarytaxregistration | bigint | 8 | 1 |  |  |  |
| isprivate | bigint | 8 | 1 |  |  |  |
| isrolebusiness | bigint | 8 | 1 |  |  |  |
| isroledelivery | bigint | 8 | 1 |  |  |  |
| isrolehome | bigint | 8 | 1 |  |  |  |
| isroleinvoice | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| attentiontoaddressline | varchar | 8000 | 1 |  |  |  |
| location | bigint | 8 | 1 |  |  |  |
| party | bigint | 8 | 1 |  |  |  |
| postaladdressroles | varchar | 8000 | 1 |  |  |  |
| assignmentdate | datetime2 | 8 | 1 |  |  |  |
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
