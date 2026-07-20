# dbo.whsworktable_prod_sc

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| autoexecute | bigint | 8 | 1 |  |  |  |
| frozen | bigint | 8 | 1 |  |  |  |
| usermanuallyassigned | bigint | 8 | 1 |  |  |  |
| useworkforwavereplen | bigint | 8 | 1 |  |  |  |
| workismultisku | bigint | 8 | 1 |  |  |  |
| workstatus | bigint | 8 | 1 |  |  |  |
| worktranstype | bigint | 8 | 1 |  |  |  |
| cancelreplenwhendemandcanceled | bigint | 8 | 1 |  |  |  |
| hasworklineloadlinedetails | bigint | 8 | 1 |  |  |  |
| replenishmentdependentworkblockingpolicy | bigint | 8 | 1 |  |  |  |
| ispartialcyclecountwork | bigint | 8 | 1 |  |  |  |
| workcreationfailedonreservation | bigint | 8 | 1 |  |  |  |
| inventorytransactionmechanism | bigint | 8 | 1 |  |  |  |
| executedwithoutuserlocation | bigint | 8 | 1 |  |  |  |
| isgtdissuesupport_ru | bigint | 8 | 1 |  |  |  |
| babparentlppicked | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| actualtime | decimal | 17 | 1 |  |  |  |
| combinedworkid | varchar | 8000 | 1 |  |  |  |
| containerid | varchar | 8000 | 1 |  |  |  |
| cyclecountplanoverview | bigint | 8 | 1 |  |  |  |
| dispositioncode | varchar | 8000 | 1 |  |  |  |
| estimatedtime | decimal | 17 | 1 |  |  |  |
| inventjournalid | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
| loadid | varchar | 8000 | 1 |  |  |  |
| lockeduser | varchar | 8000 | 1 |  |  |  |
| ordernum | varchar | 8000 | 1 |  |  |  |
| shipmentid | varchar | 8000 | 1 |  |  |  |
| targetlicenseplateid | varchar | 8000 | 1 |  |  |  |
| transtxt | varchar | 8000 | 1 |  |  |  |
| waveid | varchar | 8000 | 1 |  |  |  |
| workbuildid | varchar | 8000 | 1 |  |  |  |
| workcancelledbyuser | varchar | 8000 | 1 |  |  |  |
| workcancelledutcdatetime | datetime2 | 8 | 1 |  |  |  |
| workclosedutcdatetime | datetime2 | 8 | 1 |  |  |  |
| workcounterror | varchar | 8000 | 1 |  |  |  |
| workcreatedby | varchar | 8000 | 1 |  |  |  |
| workid | varchar | 8000 | 1 |  |  |  |
| workinprocessutcdatetime | datetime2 | 8 | 1 |  |  |  |
| workmanuallycompletedby | varchar | 8000 | 1 |  |  |  |
| workpoolid | varchar | 8000 | 1 |  |  |  |
| workpriority | bigint | 8 | 1 |  |  |  |
| worktemplatecode | varchar | 8000 | 1 |  |  |  |
| immediatereplenishmentunitid | varchar | 8000 | 1 |  |  |  |
| inventqualityorderid | varchar | 8000 | 1 |  |  |  |
| clusterprofileid | varchar | 8000 | 1 |  |  |  |
| itmgoodsintransitid | varchar | 8000 | 1 |  |  |  |
| itmregisteredlicenseplateid | varchar | 8000 | 1 |  |  |  |
| inventoryadjustmentjournalid | varchar | 8000 | 1 |  |  |  |
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
| packingworkremainingqtycalculationmechanism | bigint | 8 | 1 |  |  |  |
| warehouseinventorytransactiongroupingmechanism | bigint | 8 | 1 |  |  |  |
