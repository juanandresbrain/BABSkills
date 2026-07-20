# dbo.transportationdocument

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| carriertype | bigint | 8 | 1 |  |  |  |
| doprinttransportationdocument | bigint | 8 | 1 |  |  |  |
| economicactivitytype | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| carriercode | varchar | 8000 | 1 |  |  |  |
| documentdatetime | datetime2 | 8 | 1 |  |  |  |
| issuedby | bigint | 8 | 1 |  |  |  |
| loadedaddressname | varchar | 8000 | 1 |  |  |  |
| loadeddatetime | datetime2 | 8 | 1 |  |  |  |
| loadedpostaladdress | bigint | 8 | 1 |  |  |  |
| packagedangerdegree | varchar | 8000 | 1 |  |  |  |
| packagedescription | varchar | 8000 | 1 |  |  |  |
| unloadedaddressname | varchar | 8000 | 1 |  |  |  |
| unloadeddatetime | datetime2 | 8 | 1 |  |  |  |
| unloadedpostaladdress | bigint | 8 | 1 |  |  |  |
| lineid | varchar | 8000 | 1 |  |  |  |
| satpermissiontype_mx | varchar | 8000 | 1 |  |  |  |
| satpermissionid_mx | varchar | 8000 | 1 |  |  |  |
| traveltime_mx | decimal | 17 | 1 |  |  |  |
| traveldistance_mx | decimal | 17 | 1 |  |  |  |
| pickupspot_mx | varchar | 8000 | 1 |  |  |  |
| dropoffspot_mx | varchar | 8000 | 1 |  |  |  |
| pickupmode_mx | varchar | 8000 | 1 |  |  |  |
| dropoffmode_mx | varchar | 8000 | 1 |  |  |  |
| weightunit_mx | varchar | 8000 | 1 |  |  |  |
| environmentaldamageinsurancevendor_mx | varchar | 8000 | 1 |  |  |  |
| environmentaldamageinsurancepolicynum_mx | varchar | 8000 | 1 |  |  |  |
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
