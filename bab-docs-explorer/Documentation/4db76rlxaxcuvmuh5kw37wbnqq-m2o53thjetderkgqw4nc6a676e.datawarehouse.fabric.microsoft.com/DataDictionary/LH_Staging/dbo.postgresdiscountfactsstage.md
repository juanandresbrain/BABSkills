# dbo.postgresdiscountfactsstage

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transactionkey | varchar | 8000 | 1 |  |  |  |
| device_id | varchar | 8000 | 1 |  |  |  |
| storeid | int | 4 | 1 |  |  |  |
| business_date | datetime2 | 8 | 1 |  |  |  |
| transactionnumber | int | 4 | 1 |  |  |  |
| registernumber | int | 4 | 1 |  |  |  |
| barcode | varchar | 8000 | 1 |  |  |  |
| entity | varchar | 8000 | 1 |  |  |  |
| promotion_id | varchar | 8000 | 1 |  |  |  |
| campaignId | varchar | 8000 | 1 |  |  |  |
| description | varchar | 8000 | 1 |  |  |  |
| discountamount | decimal | 9 | 1 |  |  |  |
| loyaltycertificateid | varchar | 8000 | 1 |  |  |  |
