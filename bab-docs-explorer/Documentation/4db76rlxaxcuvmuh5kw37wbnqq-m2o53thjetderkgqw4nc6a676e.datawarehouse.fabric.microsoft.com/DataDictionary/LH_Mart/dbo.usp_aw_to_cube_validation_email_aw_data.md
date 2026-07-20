# dbo.usp_aw_to_cube_validation_email_aw_data

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_no | int | 4 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| transaction_id_AW | decimal | 9 | 1 |  |  |  |
| voucher_adjustment | decimal | 17 | 1 |  |  |  |
| GAAPSales_AW | decimal | 17 | 1 |  |  |  |
