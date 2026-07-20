# dbo.tmpdwsalestotals

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| store_id | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| Line_Object | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 8000 | 1 |  |  |  |
| SumUnitGrossAmt | decimal | 17 | 1 |  |  |  |
| SumUnitDiscAmt | decimal | 17 | 1 |  |  |  |
| SumUpsellDiscAllocated | decimal | 9 | 1 |  |  |  |
| MinTransDate | datetime2 | 8 | 1 |  |  |  |
| MaxTransDate | datetime2 | 8 | 1 |  |  |  |
| SumSalesTotal | decimal | 17 | 1 |  |  |  |
