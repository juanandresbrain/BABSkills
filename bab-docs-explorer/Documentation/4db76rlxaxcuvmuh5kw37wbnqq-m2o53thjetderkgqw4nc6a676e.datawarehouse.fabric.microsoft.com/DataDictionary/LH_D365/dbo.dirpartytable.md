# dbo.dirpartytable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| instancerelationtype | bigint | 8 | 1 |  |  |  |
| knownas | varchar | 8000 | 1 |  |  |  |
| languageid | varchar | 8000 | 1 |  |  |  |
| name | varchar | 8000 | 1 |  |  |  |
| namealias | varchar | 8000 | 1 |  |  |  |
| partynumber | varchar | 8000 | 1 |  |  |  |
| primaryaddresslocation | bigint | 8 | 1 |  |  |  |
| primarycontactemail | bigint | 8 | 1 |  |  |  |
| primarycontactfax | bigint | 8 | 1 |  |  |  |
| primarycontactphone | bigint | 8 | 1 |  |  |  |
| primarycontacttelex | bigint | 8 | 1 |  |  |  |
| primarycontacturl | bigint | 8 | 1 |  |  |  |
| primarycontactfacebook | bigint | 8 | 1 |  |  |  |
| primarycontacttwitter | bigint | 8 | 1 |  |  |  |
| primarycontactlinkedin | bigint | 8 | 1 |  |  |  |
| addressbooknames | varchar | 8000 | 1 |  |  |  |
| legacyinstancerelationtype | bigint | 8 | 1 |  |  |  |
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
