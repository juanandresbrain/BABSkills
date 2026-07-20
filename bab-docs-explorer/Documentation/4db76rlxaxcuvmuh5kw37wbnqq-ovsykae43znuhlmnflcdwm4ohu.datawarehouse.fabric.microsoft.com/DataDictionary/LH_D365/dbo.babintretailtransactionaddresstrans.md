# dbo.babintretailtransactionaddresstrans

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| babintretailprocessed | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| attentiontoaddressline | varchar | 8000 | 1 |  |  |  |
| channel | bigint | 8 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| countryregionid | varchar | 8000 | 1 |  |  |  |
| county | varchar | 8000 | 1 |  |  |  |
| deliveryname | varchar | 8000 | 1 |  |  |  |
| districtname | varchar | 8000 | 1 |  |  |  |
| email | varchar | 8000 | 1 |  |  |  |
| emailcontent | varchar | 8000 | 1 |  |  |  |
| origin | varchar | 8000 | 1 |  |  |  |
| phone | varchar | 8000 | 1 |  |  |  |
| replicationcounterfromorigin | bigint | 8 | 1 |  |  |  |
| salelinenum | decimal | 17 | 1 |  |  |  |
| salesname | varchar | 8000 | 1 |  |  |  |
| state | varchar | 8000 | 1 |  |  |  |
| store | varchar | 8000 | 1 |  |  |  |
| street | varchar | 8000 | 1 |  |  |  |
| streetnumber | varchar | 8000 | 1 |  |  |  |
| terminal | varchar | 8000 | 1 |  |  |  |
| retailtransactionid | varchar | 8000 | 1 |  |  |  |
| zipcode | varchar | 8000 | 1 |  |  |  |
| buildingcompliment | varchar | 8000 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
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
