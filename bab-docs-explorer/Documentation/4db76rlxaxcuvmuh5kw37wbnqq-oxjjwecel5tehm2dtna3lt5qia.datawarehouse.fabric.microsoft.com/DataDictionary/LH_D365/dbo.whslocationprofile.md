# dbo.whslocationprofile

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| allowmixedbatches | bigint | 8 | 1 |  |  |  |
| allowmixeditems | bigint | 8 | 1 |  |  |  |
| allowmixedstatus | bigint | 8 | 1 |  |  |  |
| allownegative | bigint | 8 | 1 |  |  |  |
| cyclecountable | bigint | 8 | 1 |  |  |  |
| dimensionfillpct | bigint | 8 | 1 |  |  |  |
| gencheckdigit | bigint | 8 | 1 |  |  |  |
| ignorebatchdates | bigint | 8 | 1 |  |  |  |
| lpcontrolled | bigint | 8 | 1 |  |  |  |
| enablelocationactivitydatetimeupdate | bigint | 8 | 1 |  |  |  |
| enableiteminlocationupdate | bigint | 8 | 1 |  |  |  |
| enablelocationstatusupdate | bigint | 8 | 1 |  |  |  |
| workavailabilitythresholdtype | bigint | 8 | 1 |  |  |  |
| replenishmentexceedlocationcapacity | bigint | 8 | 1 |  |  |  |
| enablelocationlicenseplatepositioning | bigint | 8 | 1 |  |  |  |
| displaymobiledevicelocationlicenseplatepositioning | bigint | 8 | 1 |  |  |  |
| enablelocationproductdimensionspecificmixing | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| depth | decimal | 17 | 1 |  |  |  |
| dockmgmtprofileid | varchar | 8000 | 1 |  |  |  |
| fillpercentage | decimal | 17 | 1 |  |  |  |
| height | decimal | 17 | 1 |  |  |  |
| locformatid | varchar | 8000 | 1 |  |  |  |
| locprofileid | varchar | 8000 | 1 |  |  |  |
| locprofilename | varchar | 8000 | 1 |  |  |  |
| loctype | varchar | 8000 | 1 |  |  |  |
| maxweight | decimal | 17 | 1 |  |  |  |
| storageunit | varchar | 8000 | 1 |  |  |  |
| totalvolume | decimal | 17 | 1 |  |  |  |
| usabledepth | decimal | 17 | 1 |  |  |  |
| usableheight | decimal | 17 | 1 |  |  |  |
| usablevolume | decimal | 17 | 1 |  |  |  |
| usablewidth | decimal | 17 | 1 |  |  |  |
| width | decimal | 17 | 1 |  |  |  |
| allowedcontainertypegroup | bigint | 8 | 1 |  |  |  |
| replenishmentoverflowcapacitypercent | decimal | 17 | 1 |  |  |  |
| replenishmentoverflowcapacityqty | decimal | 17 | 1 |  |  |  |
| replenishmentoverflowcapacityunit | varchar | 8000 | 1 |  |  |  |
| productdimfixed | bigint | 8 | 1 |  |  |  |
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
