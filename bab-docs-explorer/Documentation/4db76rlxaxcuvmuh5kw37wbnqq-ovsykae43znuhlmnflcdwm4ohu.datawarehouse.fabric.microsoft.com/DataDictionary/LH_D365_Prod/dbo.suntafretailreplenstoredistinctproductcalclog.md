# dbo.suntafretailreplenstoredistinctproductcalclog

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| replenishmentmethod | bigint | 8 | 1 |  |  |  |
| replenqtymethod | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| parmid | varchar | 8000 | 1 |  |  |  |
| storenumber | varchar | 8000 | 1 |  |  |  |
| distinctproduct | bigint | 8 | 1 |  |  |  |
| weekshistory | bigint | 8 | 1 |  |  |  |
| seasonalitycurveid | varchar | 8000 | 1 |  |  |  |
| avgweeklysales | decimal | 17 | 1 |  |  |  |
| nonseasonalavgweeklysales | decimal | 17 | 1 |  |  |  |
| minimumsupply | decimal | 17 | 1 |  |  |  |
| targetweekssupply | bigint | 8 | 1 |  |  |  |
| targetweeksforecast | decimal | 17 | 1 |  |  |  |
| maximumsupply | decimal | 17 | 1 |  |  |  |
| storeonhand | decimal | 17 | 1 |  |  |  |
| storeopenreplenishment | decimal | 17 | 1 |  |  |  |
| suggestedreplenishment | decimal | 17 | 1 |  |  |  |
| actualreplenishment | decimal | 17 | 1 |  |  |  |
| orderminimum | decimal | 17 | 1 |  |  |  |
| ordermultiple | decimal | 17 | 1 |  |  |  |
| firmedreplenishment | decimal | 17 | 1 |  |  |  |
| historystartdate | datetime2 | 8 | 1 |  |  |  |
| suntafretailreplenproductcopyfrom | bigint | 8 | 1 |  |  |  |
| babinitialcartoncount | bigint | 8 | 1 |  |  |  |
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
