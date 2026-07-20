# dbo.dirperson

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| anniversarymonth | bigint | 8 | 1 |  |  |  |
| birthmonth | bigint | 8 | 1 |  |  |  |
| gender | bigint | 8 | 1 |  |  |  |
| maritalstatus | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| anniversaryday | bigint | 8 | 1 |  |  |  |
| anniversaryyear | bigint | 8 | 1 |  |  |  |
| birthday | bigint | 8 | 1 |  |  |  |
| birthyear | bigint | 8 | 1 |  |  |  |
| childrennames | varchar | 8000 | 1 |  |  |  |
| communicatorsignin | bigint | 8 | 1 |  |  |  |
| hobbies | varchar | 8000 | 1 |  |  |  |
| initials | varchar | 8000 | 1 |  |  |  |
| namesequence | bigint | 8 | 1 |  |  |  |
| personalsuffix | bigint | 8 | 1 |  |  |  |
| personaltitle | bigint | 8 | 1 |  |  |  |
| phoneticfirstname | varchar | 8000 | 1 |  |  |  |
| phoneticlastname | varchar | 8000 | 1 |  |  |  |
| phoneticmiddlename | varchar | 8000 | 1 |  |  |  |
| professionalsuffix | varchar | 8000 | 1 |  |  |  |
| professionaltitle | varchar | 8000 | 1 |  |  |  |
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
