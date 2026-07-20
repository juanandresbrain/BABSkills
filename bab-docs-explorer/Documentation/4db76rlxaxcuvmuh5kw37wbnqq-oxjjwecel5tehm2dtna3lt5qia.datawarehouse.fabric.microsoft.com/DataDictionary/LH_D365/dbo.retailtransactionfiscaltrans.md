# dbo.retailtransactionfiscaltrans

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| receiptcopy | bigint | 8 | 1 |  |  |  |
| registrationstatus | bigint | 8 | 1 |  |  |  |
| registrationtype | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| channel | bigint | 8 | 1 |  |  |  |
| controlcode | varchar | 8000 | 1 |  |  |  |
| linenum | decimal | 17 | 1 |  |  |  |
| origin | varchar | 8000 | 1 |  |  |  |
| registerid | varchar | 8000 | 1 |  |  |  |
| replicationcounterfromorigin | bigint | 8 | 1 |  |  |  |
| store | varchar | 8000 | 1 |  |  |  |
| terminal | varchar | 8000 | 1 |  |  |  |
| transactionid | varchar | 8000 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
| transtime | bigint | 8 | 1 |  |  |  |
| registerresponse | varchar | 8000 | 1 |  |  |  |
| staffid | varchar | 8000 | 1 |  |  |  |
| recordguid | varchar | 8000 | 1 |  |  |  |
| registerstore | varchar | 8000 | 1 |  |  |  |
| registerterminal | varchar | 8000 | 1 |  |  |  |
| registrationprocessid | varchar | 8000 | 1 |  |  |  |
| connectorgroup | varchar | 8000 | 1 |  |  |  |
| connectorname | varchar | 8000 | 1 |  |  |  |
| connectorfunctionalityprofileid | varchar | 8000 | 1 |  |  |  |
| registerinfo | varchar | 8000 | 1 |  |  |  |
| documentnumber | varchar | 8000 | 1 |  |  |  |
| servicename | varchar | 8000 | 1 |  |  |  |
| countryregionid | varchar | 8000 | 1 |  |  |  |
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
