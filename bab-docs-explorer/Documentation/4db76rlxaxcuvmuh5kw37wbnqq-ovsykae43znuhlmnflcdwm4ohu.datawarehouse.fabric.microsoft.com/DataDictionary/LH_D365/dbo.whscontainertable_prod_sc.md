# dbo.whscontainertable_prod_sc

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| containerstatus | bigint | 8 | 1 |  |  |  |
| errorcontainer | bigint | 8 | 1 |  |  |  |
| containerreleased | bigint | 8 | 1 |  |  |  |
| inventorytransactionmechanism | bigint | 8 | 1 |  |  |  |
| baballowcontainerclose | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| closecontainerutcdatetime | datetime2 | 8 | 1 |  |  |  |
| containerattributecode1_ | varchar | 8000 | 1 |  |  |  |
| containerattributecode2_ | varchar | 8000 | 1 |  |  |  |
| containerattributecode3_ | varchar | 8000 | 1 |  |  |  |
| containerattributecode4_ | varchar | 8000 | 1 |  |  |  |
| containerbuildid | varchar | 8000 | 1 |  |  |  |
| containergroupid | varchar | 8000 | 1 |  |  |  |
| containerid | varchar | 8000 | 1 |  |  |  |
| containerlevel | bigint | 8 | 1 |  |  |  |
| containernum | bigint | 8 | 1 |  |  |  |
| containertypecode | varchar | 8000 | 1 |  |  |  |
| height | decimal | 17 | 1 |  |  |  |
| inventdimid | varchar | 8000 | 1 |  |  |  |
| length | decimal | 17 | 1 |  |  |  |
| mastertrackingnum | varchar | 8000 | 1 |  |  |  |
| nmfccode | varchar | 8000 | 1 |  |  |  |
| parentcontainerid | varchar | 8000 | 1 |  |  |  |
| shipcarriertrackingnum | varchar | 8000 | 1 |  |  |  |
| shipmentid | varchar | 8000 | 1 |  |  |  |
| stcccode | varchar | 8000 | 1 |  |  |  |
| waveexecutionid | varchar | 8000 | 1 |  |  |  |
| weight | decimal | 17 | 1 |  |  |  |
| weightuom | varchar | 8000 | 1 |  |  |  |
| width | decimal | 17 | 1 |  |  |  |
| closecontainerprofileid | varchar | 8000 | 1 |  |  |  |
| containergroupinglicenseplateid | varchar | 8000 | 1 |  |  |  |
| containerizationtable | bigint | 8 | 1 |  |  |  |
| babcaseid | varchar | 8000 | 1 |  |  |  |
| babcontainercount | bigint | 8 | 1 |  |  |  |
| babintercompcontainercompanyid | varchar | 8000 | 1 |  |  |  |
| babintercompcontainerid | varchar | 8000 | 1 |  |  |  |
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
| containercreatedbyworkuserid | varchar | 8000 | 1 |  |  |  |
| containerclosedbyworkuserid | varchar | 8000 | 1 |  |  |  |
