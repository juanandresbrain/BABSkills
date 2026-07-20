# dbo.whsworkline

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| askfornewlicenseplate | bigint | 8 | 1 |  |  |  |
| isanchored | bigint | 8 | 1 |  |  |  |
| mandatory | bigint | 8 | 1 |  |  |  |
| replendemand | bigint | 8 | 1 |  |  |  |
| skipped | bigint | 8 | 1 |  |  |  |
| workstatus | bigint | 8 | 1 |  |  |  |
| workstop | bigint | 8 | 1 |  |  |  |
| worktype | bigint | 8 | 1 |  |  |  |
| workcreationfailedonreservation | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| actualtime | decimal | 17 | 1 |  |  |  |
| availphysical | decimal | 17 | 1 |  |  |  |
| containerid | varchar | 8000 | 1 |  |  |  |
| estimatedtime | decimal | 17 | 1 |  |  |  |
| fefobatchid | varchar | 8000 | 1 |  |  |  |
| inventdimid | varchar | 8000 | 1 |  |  |  |
| inventqtyremain | decimal | 17 | 1 |  |  |  |
| inventqtywork | decimal | 17 | 1 |  |  |  |
| inventtransid | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| linenum | decimal | 17 | 1 |  |  |  |
| loadid | varchar | 8000 | 1 |  |  |  |
| loadlinerefrecid | bigint | 8 | 1 |  |  |  |
| locatedlpid | varchar | 8000 | 1 |  |  |  |
| ordernum | varchar | 8000 | 1 |  |  |  |
| qtyremain | decimal | 17 | 1 |  |  |  |
| qtywork | decimal | 17 | 1 |  |  |  |
| shipmentid | varchar | 8000 | 1 |  |  |  |
| sortcode | bigint | 8 | 1 |  |  |  |
| unitid | varchar | 8000 | 1 |  |  |  |
| userid | varchar | 8000 | 1 |  |  |  |
| wmslocationid | varchar | 8000 | 1 |  |  |  |
| workclassid | varchar | 8000 | 1 |  |  |  |
| workclosedutcdatetime | datetime2 | 8 | 1 |  |  |  |
| workid | varchar | 8000 | 1 |  |  |  |
| workinprocessutcdatetime | datetime2 | 8 | 1 |  |  |  |
| worktemplatelinerecid | bigint | 8 | 1 |  |  |  |
| worktypecustomcode | varchar | 8000 | 1 |  |  |  |
| zoneid | varchar | 8000 | 1 |  |  |  |
| extrainventhandlingqty | decimal | 17 | 1 |  |  |  |
| capturedweight | decimal | 17 | 1 |  |  |  |
| outboundsortposition | bigint | 8 | 1 |  |  |  |
| inventtransoriginidsupply | bigint | 8 | 1 |  |  |  |
| ordercommittedinventdimid | varchar | 8000 | 1 |  |  |  |
| allocatedwmslocationid | varchar | 8000 | 1 |  |  |  |
| origpackingworktargetlicenseplateid | varchar | 8000 | 1 |  |  |  |
| mhxworklinepairid | varchar | 8000 | 1 |  |  |  |
| wmheworklinepairid | varchar | 8000 | 1 |  |  |  |
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
| inventorytransactionoriginid | varchar | 8000 | 1 |  |  |  |
| itemsetid | varchar | 8000 | 1 |  |  |  |
| itemsetidnobelowlocdim | varchar | 8000 | 1 |  |  |  |
