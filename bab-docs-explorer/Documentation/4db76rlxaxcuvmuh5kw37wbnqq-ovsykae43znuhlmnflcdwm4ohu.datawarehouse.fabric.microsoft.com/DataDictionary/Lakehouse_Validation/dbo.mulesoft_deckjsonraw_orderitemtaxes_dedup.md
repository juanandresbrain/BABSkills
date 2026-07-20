# dbo.mulesoft_deckjsonraw_orderitemtaxes_dedup

**Database:** Lakehouse_Validation  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| TaxType | bigint | 8 | 1 |  |  |  |
| IsVAT | bit | 1 | 1 |  |  |  |
| Amount | real | 4 | 1 |  |  |  |
| Rate | real | 4 | 1 |  |  |  |
| Description | varchar | 8000 | 1 |  |  |  |
| TaxExempt | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
