# dbo.web_inventoryfact

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationCode | varchar | 8000 | 1 |  |  |  |
| GTIN | varchar | 8000 | 1 |  |  |  |
| PreviousGTIN | varchar | 8000 | 1 |  |  |  |
| StyleCode | varchar | 8000 | 1 |  |  |  |
| SKUDescription | varchar | 8000 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |
| PreviousQTY | int | 4 | 1 |  |  |  |
| SellingGeography | varchar | 8000 | 1 |  |  |  |
| UnbufferedQty | int | 4 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| CheckDate | datetime2 | 8 | 1 |  |  |  |
| SendData | int | 4 | 1 |  |  |  |
