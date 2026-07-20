# dbo.retailchanneltable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| channeltimezone | bigint | 8 | 1 |  |  |  |
| channeltype | bigint | 8 | 1 |  |  |  |
| priceincludessalestax | bigint | 8 | 1 |  |  |  |
| displaytaxpertaxcomponent | bigint | 8 | 1 |  |  |  |
| manualaccept | bigint | 8 | 1 |  |  |  |
| calcexempttaxesforpriceinclusive | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| cashoffice_ru | varchar | 8000 | 1 |  |  |  |
| categoryhierarchy | bigint | 8 | 1 |  |  |  |
| channeltimezoneinfoid | varchar | 8000 | 1 |  |  |  |
| currency | varchar | 8000 | 1 |  |  |  |
| defaultcustaccount | varchar | 8000 | 1 |  |  |  |
| defaultcustdataareaid | varchar | 8000 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| eventnotificationprofileid | varchar | 8000 | 1 |  |  |  |
| instancerelationtype | bigint | 8 | 1 |  |  |  |
| inventlocation | varchar | 8000 | 1 |  |  |  |
| inventlocationdataareaid | varchar | 8000 | 1 |  |  |  |
| omoperatingunitid | bigint | 8 | 1 |  |  |  |
| payment | varchar | 8000 | 1 |  |  |  |
| paymmode | varchar | 8000 | 1 |  |  |  |
| storearea | decimal | 17 | 1 |  |  |  |
| transactionserviceprofile | varchar | 8000 | 1 |  |  |  |
| retailchannelid | varchar | 8000 | 1 |  |  |  |
| retailreturnpolicychannel | bigint | 8 | 1 |  |  |  |
| cardtypeid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
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
| sunecommintegrationtype | bigint | 8 | 1 |  |  |  |
| sunecommsalesoriginid | varchar | 8000 | 1 |  |  |  |
