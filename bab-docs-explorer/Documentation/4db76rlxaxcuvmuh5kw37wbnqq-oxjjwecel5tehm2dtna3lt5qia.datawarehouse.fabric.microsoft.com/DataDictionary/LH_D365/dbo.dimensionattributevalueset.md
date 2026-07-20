# dbo.dimensionattributevalueset

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| hashversion | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| implieddataareaid | varchar | 8000 | 1 |  |  |  |
| mainaccount | bigint | 8 | 1 |  |  |  |
| mainaccountvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributebankaccount | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributebankaccountvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributecustomer | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributecustomervalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributeemployee | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributeemployeevalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributefixedasset | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributefixedassetvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributeitem | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributeitemvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributeproject | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributeprojectvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributevendor | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributevendorvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributefixedassets_ru | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributefixedassets_ruvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributerdeferrals | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributerdeferralsvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributercash | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributercashvalue | varchar | 8000 | 1 |  |  |  |
| systemgeneratedattributeemployee_ru | bigint | 8 | 1 |  |  |  |
| systemgeneratedattributeemployee_ruvalue | varchar | 8000 | 1 |  |  |  |
| costcenter | bigint | 8 | 1 |  |  |  |
| costcentervalue | varchar | 8000 | 1 |  |  |  |
| store | bigint | 8 | 1 |  |  |  |
| storevalue | varchar | 8000 | 1 |  |  |  |
| businessstream | bigint | 8 | 1 |  |  |  |
| businessstreamvalue | varchar | 8000 | 1 |  |  |  |
| projectid | bigint | 8 | 1 |  |  |  |
| projectidvalue | varchar | 8000 | 1 |  |  |  |
| projectcategory | bigint | 8 | 1 |  |  |  |
| projectcategoryvalue | varchar | 8000 | 1 |  |  |  |
| legalentity | bigint | 8 | 1 |  |  |  |
| legalentityvalue | varchar | 8000 | 1 |  |  |  |
| country | bigint | 8 | 1 |  |  |  |
| countryvalue | varchar | 8000 | 1 |  |  |  |
| fund | bigint | 8 | 1 |  |  |  |
| fundvalue | varchar | 8000 | 1 |  |  |  |
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
