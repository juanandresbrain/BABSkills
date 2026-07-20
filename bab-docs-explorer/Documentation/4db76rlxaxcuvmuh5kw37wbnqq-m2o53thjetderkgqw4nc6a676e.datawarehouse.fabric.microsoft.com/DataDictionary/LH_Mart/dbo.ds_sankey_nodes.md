# dbo.ds_sankey_nodes

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| source | varchar | 8000 | 1 |  |  |  |
| target | varchar | 8000 | 1 |  |  |  |
| num_customers | bigint | 8 | 1 |  |  |  |
| gross_amount | decimal | 13 | 1 |  |  |  |
| net_amount | decimal | 17 | 1 |  |  |  |
