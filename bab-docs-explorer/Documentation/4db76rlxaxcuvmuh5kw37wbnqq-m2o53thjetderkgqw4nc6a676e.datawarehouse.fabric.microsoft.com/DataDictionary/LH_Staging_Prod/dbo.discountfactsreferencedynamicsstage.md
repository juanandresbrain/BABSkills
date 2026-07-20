# dbo.discountfactsreferencedynamicsstage

**Database:** LH_Staging_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| transaction_id | decimal | 9 | 1 |  |  |  |
| line_id | decimal | 5 | 1 |  |  |  |
| line_sequence | decimal | 5 | 1 |  |  |  |
| SumDiscAmount | decimal | 17 | 1 |  |  |  |
| line_object | int | 4 | 1 |  |  |  |
| line_object_description | varchar | 8000 | 1 |  |  |  |
| line_object_type | int | 4 | 1 |  |  |  |
| object_type_display_descr | varchar | 8000 | 1 |  |  |  |
| DiscountType | varchar | 8000 | 1 |  |  |  |
| LineAction | int | 4 | 1 |  |  |  |
