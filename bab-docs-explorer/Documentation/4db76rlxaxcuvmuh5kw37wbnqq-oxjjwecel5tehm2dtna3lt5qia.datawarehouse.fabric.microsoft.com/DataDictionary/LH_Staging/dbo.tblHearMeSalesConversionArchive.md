# dbo.tblHearMeSalesConversionArchive

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ib_inventory_id | decimal | 9 | 1 |  |  |  |
| proc_date | datetime2 | 8 | 1 |  |  |  |
| sku_id | decimal | 9 | 1 |  |  |  |
| location_id | smallint | 2 | 1 |  |  |  |
| price_status_id | smallint | 2 | 1 |  |  |  |
| transaction_date | datetime2 | 8 | 1 |  |  |  |
| transaction_type_code | smallint | 2 | 1 |  |  |  |
| inventory_status_id | smallint | 2 | 1 |  |  |  |
| other_location_id | smallint | 2 | 1 |  |  |  |
| transaction_reason_id | smallint | 2 | 1 |  |  |  |
| document_number | varchar | 8000 | 1 |  |  |  |
| transaction_units | int | 4 | 1 |  |  |  |
| transaction_cost | decimal | 9 | 1 |  |  |  |
| transaction_valuation_retail | decimal | 9 | 1 |  |  |  |
| transaction_selling_retail | decimal | 9 | 1 |  |  |  |
| price_change_type | smallint | 2 | 1 |  |  |  |
| units_affected | int | 4 | 1 |  |  |  |
| style_code | varchar | 8000 | 1 |  |  |  |
| short_desc | varchar | 8000 | 1 |  |  |  |
| location_code | varchar | 8000 | 1 |  |  |  |
| transaction_cost_local | decimal | 9 | 1 |  |  |  |
| updated_flag | bit | 1 | 1 |  |  |  |
| transaction_no | int | 4 | 1 |  |  |  |
| batch_no | int | 4 | 1 |  |  |  |
| register_no | smallint | 2 | 1 |  |  |  |
