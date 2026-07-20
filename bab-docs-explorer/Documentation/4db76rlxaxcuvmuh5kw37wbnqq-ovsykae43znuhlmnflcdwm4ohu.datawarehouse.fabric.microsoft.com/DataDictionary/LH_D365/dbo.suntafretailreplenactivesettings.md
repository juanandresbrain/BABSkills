# dbo.suntafretailreplenactivesettings

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| replenishmentmethod | bigint | 8 | 1 |  |  |  |
| historymanualoverride | bigint | 8 | 1 |  |  |  |
| reverthistoryoverride | bigint | 8 | 1 |  |  |  |
| ordermanualoverride | bigint | 8 | 1 |  |  |  |
| revertorderoverride | bigint | 8 | 1 |  |  |  |
| stockmanualoverride | bigint | 8 | 1 |  |  |  |
| revertstockoverride | bigint | 8 | 1 |  |  |  |
| enabled | bigint | 8 | 1 |  |  |  |
| babstoreproducteligible | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| storenumber | varchar | 8000 | 1 |  |  |  |
| distinctproduct | bigint | 8 | 1 |  |  |  |
| weekshistory | bigint | 8 | 1 |  |  |  |
| seasonalitycurveid | varchar | 8000 | 1 |  |  |  |
| maximumsupply | decimal | 17 | 1 |  |  |  |
| minimumsupply | decimal | 17 | 1 |  |  |  |
| targetweekssupply | bigint | 8 | 1 |  |  |  |
| orderminimum | decimal | 17 | 1 |  |  |  |
| ordermultiple | decimal | 17 | 1 |  |  |  |
| historyreplenconfigsource | bigint | 8 | 1 |  |  |  |
| stockreplenconfigsource | bigint | 8 | 1 |  |  |  |
| orderreplenconfigsource | bigint | 8 | 1 |  |  |  |
| historystartdate | datetime2 | 8 | 1 |  |  |  |
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
