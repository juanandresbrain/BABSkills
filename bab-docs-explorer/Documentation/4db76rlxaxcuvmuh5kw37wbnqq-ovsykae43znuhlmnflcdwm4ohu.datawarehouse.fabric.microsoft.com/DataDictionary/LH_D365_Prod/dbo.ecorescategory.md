# dbo.ecorescategory

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| changestatus | bigint | 8 | 1 |  |  |  |
| isactive | bigint | 8 | 1 |  |  |  |
| iscategoryattributesinherited | bigint | 8 | 1 |  |  |  |
| istangible | bigint | 8 | 1 |  |  |  |
| exempt_in | bigint | 8 | 1 |  |  |  |
| nongst_in | bigint | 8 | 1 |  |  |  |
| forcefulllookupsync | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| categoryhierarchy | bigint | 8 | 1 |  |  |  |
| code | varchar | 8000 | 1 |  |  |  |
| defaultprojectglobalcategory | bigint | 8 | 1 |  |  |  |
| defaultthreshold_psn | decimal | 17 | 1 |  |  |  |
| instancerelationtype | bigint | 8 | 1 |  |  |  |
| level | bigint | 8 | 1 |  |  |  |
| name | varchar | 8000 | 1 |  |  |  |
| nestedsetleft | bigint | 8 | 1 |  |  |  |
| nestedsetright | bigint | 8 | 1 |  |  |  |
| parentcategory | bigint | 8 | 1 |  |  |  |
| pkwiucode | varchar | 8000 | 1 |  |  |  |
| hsncodetable_in | bigint | 8 | 1 |  |  |  |
| serviceaccountingcodetable_in | bigint | 8 | 1 |  |  |  |
| displayorder | decimal | 17 | 1 |  |  |  |
| externalid | varchar | 8000 | 1 |  |  |  |
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
| salescategory | bigint | 8 | 1 |  |  |  |
