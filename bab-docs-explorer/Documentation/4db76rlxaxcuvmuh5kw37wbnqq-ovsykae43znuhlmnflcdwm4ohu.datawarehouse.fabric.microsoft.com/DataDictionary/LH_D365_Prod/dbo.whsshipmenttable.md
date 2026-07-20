# dbo.whsshipmenttable

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| loaddirection | bigint | 8 | 1 |  |  |  |
| shipmentstatus | bigint | 8 | 1 |  |  |  |
| worktranstype | bigint | 8 | 1 |  |  |  |
| wavelabelsprinted | bigint | 8 | 1 |  |  |  |
| orderlineinventtranslinktype | bigint | 8 | 1 |  |  |  |
| babdayoftheweek | bigint | 8 | 1 |  |  |  |
| babshipmentfailedvalidation | bigint | 8 | 1 |  |  |  |
| babwhsshipmentaddressvalidationstatus | bigint | 8 | 1 |  |  |  |
| shipmentprocessingownership | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| carriercode | varchar | 8000 | 1 |  |  |  |
| accountnum | varchar | 8000 | 1 |  |  |  |
| address | varchar | 8000 | 1 |  |  |  |
| billofladingid | varchar | 8000 | 1 |  |  |  |
| brokercode | varchar | 8000 | 1 |  |  |  |
| carriergroupcode | varchar | 8000 | 1 |  |  |  |
| carrierservicecode | varchar | 8000 | 1 |  |  |  |
| countryregionisocode | varchar | 8000 | 1 |  |  |  |
| customerref | varchar | 8000 | 1 |  |  |  |
| customerreq | varchar | 8000 | 1 |  |  |  |
| deliveryname | varchar | 8000 | 1 |  |  |  |
| deliverypostaladdress | bigint | 8 | 1 |  |  |  |
| dlvtermid | varchar | 8000 | 1 |  |  |  |
| dropoffutcdatetime | datetime2 | 8 | 1 |  |  |  |
| freighttermcode | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
| loadid | varchar | 8000 | 1 |  |  |  |
| modecode | varchar | 8000 | 1 |  |  |  |
| ordernum | varchar | 8000 | 1 |  |  |  |
| pronum | varchar | 8000 | 1 |  |  |  |
| reference | varchar | 8000 | 1 |  |  |  |
| routecode | varchar | 8000 | 1 |  |  |  |
| scac | varchar | 8000 | 1 |  |  |  |
| shipcarrieraccount | varchar | 8000 | 1 |  |  |  |
| shipconfirmutcdatetime | datetime2 | 8 | 1 |  |  |  |
| shipmentarrivalutcdatetime | datetime2 | 8 | 1 |  |  |  |
| shipmentid | varchar | 8000 | 1 |  |  |  |
| stopnum | bigint | 8 | 1 |  |  |  |
| waveid | varchar | 8000 | 1 |  |  |  |
| waybill | varchar | 8000 | 1 |  |  |  |
| manifestedweight | decimal | 17 | 1 |  |  |  |
| manifestedweightuom | varchar | 8000 | 1 |  |  |  |
| wavelabelsprinteddatetime | datetime2 | 8 | 1 |  |  |  |
| wavelabelsprintedby | varchar | 8000 | 1 |  |  |  |
| shipconsolidationpolicy | bigint | 8 | 1 |  |  |  |
| hmimmultimodaldgid | varchar | 8000 | 1 |  |  |  |
| hmimcarrofmerchbyroadid | varchar | 8000 | 1 |  |  |  |
| hmimairwaybillnum | varchar | 8000 | 1 |  |  |  |
| shipmentcreatedutcdatetime | datetime2 | 8 | 1 |  |  |  |
| receivingcompletedpackingslipid | varchar | 8000 | 1 |  |  |  |
| receivingcompleteddocumentdate | datetime2 | 8 | 1 |  |  |  |
| preallocatedpackingslipid | varchar | 8000 | 1 |  |  |  |
| preallocatedpackingslipdocumentdate | datetime2 | 8 | 1 |  |  |  |
| outboundshipmentprocessingpolicy | bigint | 8 | 1 |  |  |  |
| babshipmentlines | bigint | 8 | 1 |  |  |  |
| babconveyorlane | bigint | 8 | 1 |  |  |  |
| babstorenumber | varchar | 8000 | 1 |  |  |  |
| babcontainercount | bigint | 8 | 1 |  |  |  |
| babaptosshipmentnum | varchar | 8000 | 1 |  |  |  |
| babexternalorderdate | datetime2 | 8 | 1 |  |  |  |
| babexternalbillofladingid | varchar | 8000 | 1 |  |  |  |
| sourcesystem | bigint | 8 | 1 |  |  |  |
| inventownerid | varchar | 8000 | 1 |  |  |  |
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
| babgs1128palletid | varchar | 8000 | 1 |  |  |  |
