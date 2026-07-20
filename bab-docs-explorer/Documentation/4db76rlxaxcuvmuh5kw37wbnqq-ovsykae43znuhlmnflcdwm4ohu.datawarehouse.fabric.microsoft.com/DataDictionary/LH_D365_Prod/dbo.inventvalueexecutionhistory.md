# dbo.inventvalueexecutionhistory

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| calcavgunitcost | bigint | 8 | 1 |  |  |  |
| detaillevel | bigint | 8 | 1 |  |  |  |
| includebeginningbalance | bigint | 8 | 1 |  |  |  |
| includenotpostedvalue | bigint | 8 | 1 |  |  |  |
| printtotalqtyvalue | bigint | 8 | 1 |  |  |  |
| summarizephysfinvalues | bigint | 8 | 1 |  |  |  |
| viewcogs | bigint | 8 | 1 |  |  |  |
| viewdeferredcogs | bigint | 8 | 1 |  |  |  |
| viewdirectoutsourcing | bigint | 8 | 1 |  |  |  |
| viewindirect | bigint | 8 | 1 |  |  |  |
| viewinventory | bigint | 8 | 1 |  |  |  |
| viewlabor | bigint | 8 | 1 |  |  |  |
| viewmaterial | bigint | 8 | 1 |  |  |  |
| viewprofitloss | bigint | 8 | 1 |  |  |  |
| viewresourcegroup | bigint | 8 | 1 |  |  |  |
| viewresourcegrouptotal | bigint | 8 | 1 |  |  |  |
| viewresourceid | bigint | 8 | 1 |  |  |  |
| viewresourceidtotal | bigint | 8 | 1 |  |  |  |
| viewwip | bigint | 8 | 1 |  |  |  |
| viewconfigid | bigint | 8 | 1 |  |  |  |
| viewinventbatchid | bigint | 8 | 1 |  |  |  |
| viewinventcolorid | bigint | 8 | 1 |  |  |  |
| viewinventgtdid_ru | bigint | 8 | 1 |  |  |  |
| viewinventownerid_ru | bigint | 8 | 1 |  |  |  |
| viewinventprofileid_ru | bigint | 8 | 1 |  |  |  |
| viewinventlocationid | bigint | 8 | 1 |  |  |  |
| viewinventserialid | bigint | 8 | 1 |  |  |  |
| viewinventsiteid | bigint | 8 | 1 |  |  |  |
| viewinventsizeid | bigint | 8 | 1 |  |  |  |
| viewinventstatus | bigint | 8 | 1 |  |  |  |
| viewinventstyleid | bigint | 8 | 1 |  |  |  |
| viewinventversionid | bigint | 8 | 1 |  |  |  |
| viewlicenseplate | bigint | 8 | 1 |  |  |  |
| viewwmslocationid | bigint | 8 | 1 |  |  |  |
| viewinventdimension1 | bigint | 8 | 1 |  |  |  |
| viewinventdimension2 | bigint | 8 | 1 |  |  |  |
| viewinventdimension3 | bigint | 8 | 1 |  |  |  |
| viewinventdimension4 | bigint | 8 | 1 |  |  |  |
| viewinventdimension5 | bigint | 8 | 1 |  |  |  |
| viewinventdimension6 | bigint | 8 | 1 |  |  |  |
| viewinventdimension7 | bigint | 8 | 1 |  |  |  |
| viewinventdimension8 | bigint | 8 | 1 |  |  |  |
| viewinventdimension9 | bigint | 8 | 1 |  |  |  |
| viewinventdimension10 | bigint | 8 | 1 |  |  |  |
| viewinventdimension11 | bigint | 8 | 1 |  |  |  |
| viewinventdimension12 | bigint | 8 | 1 |  |  |  |
| stoprunning | bigint | 8 | 1 |  |  |  |
| stoponerror | bigint | 8 | 1 |  |  |  |
| executionstatus | bigint | 8 | 1 |  |  |  |
| runinbundle | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| transactionid | bigint | 8 | 1 |  |  |  |
| executionname | varchar | 8000 | 1 |  |  |  |
| executiontime | datetime2 | 8 | 1 |  |  |  |
| fromdate | datetime2 | 8 | 1 |  |  |  |
| todate | datetime2 | 8 | 1 |  |  |  |
| dimensionfocus | bigint | 8 | 1 |  |  |  |
| reportid | varchar | 8000 | 1 |  |  |  |
| dateinterval | varchar | 8000 | 1 |  |  |  |
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
