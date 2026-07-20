# dbo.retailvendtable

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| createbarcodeifneeded | bigint | 8 | 1 |  |  |  |
| fixedexchrate | bigint | 8 | 1 |  |  |  |
| pricepointroundingtype | bigint | 8 | 1 |  |  |  |
| salespricerounding | bigint | 8 | 1 |  |  |  |
| useprefixforitemnumber | bigint | 8 | 1 |  |  |  |
| usevendorsitemnumberseq | bigint | 8 | 1 |  |  |  |
| vendtype | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| itemnumberseq | varchar | 8000 | 1 |  |  |  |
| accountnum | varchar | 8000 | 1 |  |  |  |
| barcodenumberseq | varchar | 8000 | 1 |  |  |  |
| coloridprefix | varchar | 8000 | 1 |  |  |  |
| defaultshelflifeperiod_ath | bigint | 8 | 1 |  |  |  |
| exchrate | decimal | 17 | 1 |  |  |  |
| fileexportprefix | varchar | 8000 | 1 |  |  |  |
| foreignvendpricegroup_ath | varchar | 8000 | 1 |  |  |  |
| franchiseeid | varchar | 8000 | 1 |  |  |  |
| itemnumberprefix | varchar | 8000 | 1 |  |  |  |
| itemsalesexportpath | varchar | 8000 | 1 |  |  |  |
| pricepointgroupid | varchar | 8000 | 1 |  |  |  |
| purchunit | varchar | 8000 | 1 |  |  |  |
| roundingmethod | varchar | 8000 | 1 |  |  |  |
| salesunit | varchar | 8000 | 1 |  |  |  |
| servicecategory | varchar | 8000 | 1 |  |  |  |
| sizeidprefix | varchar | 8000 | 1 |  |  |  |
| styleidprefix | varchar | 8000 | 1 |  |  |  |
| vendorproducthierarchyid | bigint | 8 | 1 |  |  |  |
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
