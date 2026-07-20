# dbo.whsworkuser

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| allowlocoverridepick | bigint | 8 | 1 |  |  |  |
| allowlocoverrideput | bigint | 8 | 1 |  |  |  |
| disabled | bigint | 8 | 1 |  |  |  |
| workcountissupervisor | bigint | 8 | 1 |  |  |  |
| allowoverpicksales | bigint | 8 | 1 |  |  |  |
| allowoverpicktransfer | bigint | 8 | 1 |  |  |  |
| allowoverpickproduction | bigint | 8 | 1 |  |  |  |
| allowinventorymovementwithassociatedwork | bigint | 8 | 1 |  |  |  |
| allowmanualitemreallocation | bigint | 8 | 1 |  |  |  |
| allowadjustmentsfromuserlocation | bigint | 8 | 1 |  |  |  |
| isdefaultworkuser | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| menuname | varchar | 8000 | 1 |  |  |  |
| userdefaultwarehouse | varchar | 8000 | 1 |  |  |  |
| userid | varchar | 8000 | 1 |  |  |  |
| username | varchar | 8000 | 1 |  |  |  |
| userpasswordhash | varchar | 8000 | 1 |  |  |  |
| userpassworditerations | bigint | 8 | 1 |  |  |  |
| userpasswordsalt | varchar | 8000 | 1 |  |  |  |
| workcountmaxpercent | decimal | 17 | 1 |  |  |  |
| workcountmaxqty | decimal | 17 | 1 |  |  |  |
| workcountmaxvalue | decimal | 17 | 1 |  |  |  |
| worker | bigint | 8 | 1 |  |  |  |
| authenticationfailures | bigint | 8 | 1 |  |  |  |
| userguid | varchar | 8000 | 1 |  |  |  |
| workadjustmentmaxqty | decimal | 17 | 1 |  |  |  |
| workuseraccesspolicyid | varchar | 8000 | 1 |  |  |  |
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
