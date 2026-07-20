# dbo.tmpdynsalestotals

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| InventLocationId | varchar | 8000 | 1 |  |  |  |
| SalesBucket | varchar | 8000 | 1 |  |  |  |
| SumDynUnitGrossAmount | decimal | 17 | 1 |  |  |  |
| SumDynUnitDiscAmt | decimal | 17 | 1 |  |  |  |
| MinTransDate | date | 3 | 1 |  |  |  |
| MaxTransDate | date | 3 | 1 |  |  |  |
| SumDynSalesTotal | decimal | 17 | 1 |  |  |  |
