# dbo.logisticspostaladdress

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| isprivate | bigint | 8 | 1 |  |  |  |
| timezone | bigint | 8 | 1 |  |  |  |
| issimplifiedaddress_ru | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| address | varchar | 8000 | 1 |  |  |  |
| apartment_ru | varchar | 8000 | 1 |  |  |  |
| building_ru | varchar | 8000 | 1 |  |  |  |
| buildingcompliment | varchar | 8000 | 1 |  |  |  |
| city | varchar | 8000 | 1 |  |  |  |
| cityrecid | bigint | 8 | 1 |  |  |  |
| countryregionid | varchar | 8000 | 1 |  |  |  |
| county | varchar | 8000 | 1 |  |  |  |
| district | bigint | 8 | 1 |  |  |  |
| districtname | varchar | 8000 | 1 |  |  |  |
| flatid_ru | bigint | 8 | 1 |  |  |  |
| houseid_ru | bigint | 8 | 1 |  |  |  |
| latitude | decimal | 17 | 1 |  |  |  |
| location | bigint | 8 | 1 |  |  |  |
| longitude | decimal | 17 | 1 |  |  |  |
| postbox | varchar | 8000 | 1 |  |  |  |
| privateforparty | bigint | 8 | 1 |  |  |  |
| state | varchar | 8000 | 1 |  |  |  |
| street | varchar | 8000 | 1 |  |  |  |
| streetid_ru | bigint | 8 | 1 |  |  |  |
| streetnumber | varchar | 8000 | 1 |  |  |  |
| validfrom | datetime2 | 8 | 1 |  |  |  |
| validto | datetime2 | 8 | 1 |  |  |  |
| zipcode | varchar | 8000 | 1 |  |  |  |
| zipcoderecid | bigint | 8 | 1 |  |  |  |
| citykana_jp | varchar | 8000 | 1 |  |  |  |
| streetkana_jp | varchar | 8000 | 1 |  |  |  |
| steadid_ru | bigint | 8 | 1 |  |  |  |
| channelreferenceid | varchar | 8000 | 1 |  |  |  |
| settlementrecid | bigint | 8 | 1 |  |  |  |
| localityrecid | bigint | 8 | 1 |  |  |  |
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
