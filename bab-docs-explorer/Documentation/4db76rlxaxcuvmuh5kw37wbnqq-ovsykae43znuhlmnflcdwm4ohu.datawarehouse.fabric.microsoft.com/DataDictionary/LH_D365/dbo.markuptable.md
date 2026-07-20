# dbo.markuptable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| custompaymtype_ru | bigint | 8 | 1 |  |  |  |
| custposting | bigint | 8 | 1 |  |  |  |
| custtype | bigint | 8 | 1 |  |  |  |
| isletterofcredit_sa | bigint | 8 | 1 |  |  |  |
| markupclassification_br | bigint | 8 | 1 |  |  |  |
| mcrbrokercontractfee | bigint | 8 | 1 |  |  |  |
| mcrprorate | bigint | 8 | 1 |  |  |  |
| moduletype | bigint | 8 | 1 |  |  |  |
| usecustpostingtypetransit_ru | bigint | 8 | 1 |  |  |  |
| useinmatching | bigint | 8 | 1 |  |  |  |
| vendposting | bigint | 8 | 1 |  |  |  |
| vendtype | bigint | 8 | 1 |  |  |  |
| includeintointrastatinvoicevalue | bigint | 8 | 1 |  |  |  |
| includeintointrastatstatisticalvalue | bigint | 8 | 1 |  |  |  |
| isshipping | bigint | 8 | 1 |  |  |  |
| refundable | bigint | 8 | 1 |  |  |  |
| skipinfreeinvoices_it | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| customerledgerdimension | bigint | 8 | 1 |  |  |  |
| markupcode | varchar | 8000 | 1 |  |  |  |
| maxamount | decimal | 17 | 1 |  |  |  |
| taxitemgroup | varchar | 8000 | 1 |  |  |  |
| txt | varchar | 8000 | 1 |  |  |  |
| vendorledgerdimension | bigint | 8 | 1 |  |  |  |
| satproductcode_mx | varchar | 8000 | 1 |  |  |  |
| satunitcode_mx | varchar | 8000 | 1 |  |  |  |
| taxratetype | bigint | 8 | 1 |  |  |  |
| taxwithholditemgroup | bigint | 8 | 1 |  |  |  |
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
