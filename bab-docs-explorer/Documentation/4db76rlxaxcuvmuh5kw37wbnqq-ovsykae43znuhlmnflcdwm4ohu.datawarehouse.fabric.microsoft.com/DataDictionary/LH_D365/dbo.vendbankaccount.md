# dbo.vendbankaccount

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| bankaccounttype | bigint | 8 | 1 |  |  |  |
| bankcodetype | bigint | 8 | 1 |  |  |  |
| lvdefaultbank | bigint | 8 | 1 |  |  |  |
| transtype_jp | bigint | 8 | 1 |  |  |  |
| reviewed | bigint | 8 | 1 |  |  |  |
| bankinformationorigin | bigint | 8 | 1 |  |  |  |
| workflowstate | bigint | 8 | 1 |  |  |  |
| versioningstate | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountid | varchar | 8000 | 1 |  |  |  |
| accountnum | varchar | 8000 | 1 |  |  |  |
| activedate | datetime2 | 8 | 1 |  |  |  |
| bankaccountnamekana_jp | varchar | 8000 | 1 |  |  |  |
| bankcin | varchar | 8000 | 1 |  |  |  |
| bankconstantsymbol | bigint | 8 | 1 |  |  |  |
| bankcontractaccount | varchar | 8000 | 1 |  |  |  |
| bankgroupid | varchar | 8000 | 1 |  |  |  |
| bankiban | varchar | 8000 | 1 |  |  |  |
| cellularphone | varchar | 8000 | 1 |  |  |  |
| contactperson | varchar | 8000 | 1 |  |  |  |
| corraccount_w | varchar | 8000 | 1 |  |  |  |
| correspbank_ee | varchar | 8000 | 1 |  |  |  |
| currencycode | varchar | 8000 | 1 |  |  |  |
| dirdunsnumber | bigint | 8 | 1 |  |  |  |
| email | varchar | 8000 | 1 |  |  |  |
| exchrate | decimal | 17 | 1 |  |  |  |
| exchrateref | varchar | 8000 | 1 |  |  |  |
| expirydate | datetime2 | 8 | 1 |  |  |  |
| foreignaccount_ru | varchar | 8000 | 1 |  |  |  |
| foreignbank_ru | varchar | 8000 | 1 |  |  |  |
| foreignswift_ru | varchar | 8000 | 1 |  |  |  |
| intermaccount_ee | varchar | 8000 | 1 |  |  |  |
| intermbank_ee | varchar | 8000 | 1 |  |  |  |
| intermbankaccountid | varchar | 8000 | 1 |  |  |  |
| location | bigint | 8 | 1 |  |  |  |
| logisticslocation | bigint | 8 | 1 |  |  |  |
| msgtobank | varchar | 8000 | 1 |  |  |  |
| name | varchar | 8000 | 1 |  |  |  |
| pager | varchar | 8000 | 1 |  |  |  |
| phone | varchar | 8000 | 1 |  |  |  |
| phonelocal | varchar | 8000 | 1 |  |  |  |
| registrationnum | varchar | 8000 | 1 |  |  |  |
| sms | varchar | 8000 | 1 |  |  |  |
| specificsymbol | varchar | 8000 | 1 |  |  |  |
| swiftno | varchar | 8000 | 1 |  |  |  |
| telefax | varchar | 8000 | 1 |  |  |  |
| telex | varchar | 8000 | 1 |  |  |  |
| url | varchar | 8000 | 1 |  |  |  |
| vendaccount | varchar | 8000 | 1 |  |  |  |
| vendduns4number | varchar | 8000 | 1 |  |  |  |
| vendpaymenttextcode | varchar | 8000 | 1 |  |  |  |
| ficreditorid_dk | varchar | 8000 | 1 |  |  |  |
| correspondentbankaccount_lt | varchar | 8000 | 1 |  |  |  |
| correspondentbankaddress_lt | varchar | 8000 | 1 |  |  |  |
| correspondentbankname_lt | varchar | 8000 | 1 |  |  |  |
| correspondentbankswift_lt | varchar | 8000 | 1 |  |  |  |
| intermediatebankaccount_lt | varchar | 8000 | 1 |  |  |  |
| intermediatebankaddress_lt | varchar | 8000 | 1 |  |  |  |
| intermediatebankname_lt | varchar | 8000 | 1 |  |  |  |
| intermediatebankswift_lt | varchar | 8000 | 1 |  |  |  |
| comments | varchar | 8000 | 1 |  |  |  |
| qriban_ch | varchar | 8000 | 1 |  |  |  |
| specparameters_ch | varchar | 8000 | 1 |  |  |  |
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
| payeename | varchar | 8000 | 1 |  |  |  |
