# dbo.salestable_w

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| constarget_jp | bigint | 8 | 1 |  |  |  |
| customsexportorder_in | bigint | 8 | 1 |  |  |  |
| customsshippingbill_in | bigint | 8 | 1 |  |  |  |
| entrycertificaterequired_w | bigint | 8 | 1 |  |  |  |
| fiscaldoctype_pl | bigint | 8 | 1 |  |  |  |
| issueownentrycertificate_w | bigint | 8 | 1 |  |  |  |
| natureofassessee_in | bigint | 8 | 1 |  |  |  |
| unitedvatinvoice_lt | bigint | 8 | 1 |  |  |  |
| invoicetype_my | bigint | 8 | 1 |  |  |  |
| provisionalassessment_in | bigint | 8 | 1 |  |  |  |
| ecommercesale_in | bigint | 8 | 1 |  |  |  |
| withigstpayment_in | bigint | 8 | 1 |  |  |  |
| wouldyouclaimrefund_in | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| bankaccount_lv | varchar | 8000 | 1 |  |  |  |
| creditnotereasoncode | bigint | 8 | 1 |  |  |  |
| curbankaccount_lv | varchar | 8000 | 1 |  |  |  |
| custbankaccount_lv | varchar | 8000 | 1 |  |  |  |
| intrastataddvalue_lv | decimal | 17 | 1 |  |  |  |
| salestable | bigint | 8 | 1 |  |  |  |
| taxperiodpaymentcode_pl | varchar | 8000 | 1 |  |  |  |
| tcsgroup_in | varchar | 8000 | 1 |  |  |  |
| tdsgroup_in | varchar | 8000 | 1 |  |  |  |
| transportationdocument | bigint | 8 | 1 |  |  |  |
| merchantid_in | varchar | 8000 | 1 |  |  |  |
| ecommerceoperatorgstin_in | bigint | 8 | 1 |  |  |  |
| ecommerceoperator_in | varchar | 8000 | 1 |  |  |  |
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
