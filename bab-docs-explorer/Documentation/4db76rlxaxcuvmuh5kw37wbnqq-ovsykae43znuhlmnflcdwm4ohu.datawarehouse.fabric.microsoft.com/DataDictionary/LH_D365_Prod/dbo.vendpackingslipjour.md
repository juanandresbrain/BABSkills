# dbo.vendpackingslipjour

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| deliverytype | bigint | 8 | 1 |  |  |  |
| freightsliptype | bigint | 8 | 1 |  |  |  |
| intercompanyposted | bigint | 8 | 1 |  |  |  |
| inventprofiletype_ru | bigint | 8 | 1 |  |  |  |
| purchasetype | bigint | 8 | 1 |  |  |  |
| receiptlistdeviationtype_ru | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| orderaccount | varchar | 8000 | 1 |  |  |  |
| consigneeaccount_ru | varchar | 8000 | 1 |  |  |  |
| consignoraccount_ru | varchar | 8000 | 1 |  |  |  |
| countryregionid | varchar | 8000 | 1 |  |  |  |
| currencycode_w | varchar | 8000 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| deliverydate | datetime2 | 8 | 1 |  |  |  |
| deliveryname | varchar | 8000 | 1 |  |  |  |
| deliverypostaladdress | bigint | 8 | 1 |  |  |  |
| dlvmode | varchar | 8000 | 1 |  |  |  |
| dlvterm | varchar | 8000 | 1 |  |  |  |
| documentdate | datetime2 | 8 | 1 |  |  |  |
| enddisc_ru | decimal | 17 | 1 |  |  |  |
| freightslipnum | varchar | 8000 | 1 |  |  |  |
| grnnumber_in | varchar | 8000 | 1 |  |  |  |
| intercompanycompanyid | varchar | 8000 | 1 |  |  |  |
| intercompanysalesid | varchar | 8000 | 1 |  |  |  |
| intrastatdispatch | varchar | 8000 | 1 |  |  |  |
| intrastatfulfillmentdate_hu | datetime2 | 8 | 1 |  |  |  |
| invoiceaccount | varchar | 8000 | 1 |  |  |  |
| invoiceissueduedate_w | datetime2 | 8 | 1 |  |  |  |
| itembuyergroupid | varchar | 8000 | 1 |  |  |  |
| languageid | varchar | 8000 | 1 |  |  |  |
| numbersequencegroup | varchar | 8000 | 1 |  |  |  |
| offsessionid_ru | varchar | 8000 | 1 |  |  |  |
| orderbalance_ru | decimal | 17 | 1 |  |  |  |
| packingslipid | varchar | 8000 | 1 |  |  |  |
| packingslipnumberingcode_lt | varchar | 8000 | 1 |  |  |  |
| purchid | varchar | 8000 | 1 |  |  |  |
| reqattention | varchar | 8000 | 1 |  |  |  |
| requester | bigint | 8 | 1 |  |  |  |
| returnitemnum | varchar | 8000 | 1 |  |  |  |
| sourcedocumentheader | bigint | 8 | 1 |  |  |  |
| transportationdocument | bigint | 8 | 1 |  |  |  |
| taxid | bigint | 8 | 1 |  |  |  |
| partytaxid | bigint | 8 | 1 |  |  |  |
| fintag | bigint | 8 | 1 |  |  |  |
| banklcimportline | bigint | 8 | 1 |  |  |  |
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
