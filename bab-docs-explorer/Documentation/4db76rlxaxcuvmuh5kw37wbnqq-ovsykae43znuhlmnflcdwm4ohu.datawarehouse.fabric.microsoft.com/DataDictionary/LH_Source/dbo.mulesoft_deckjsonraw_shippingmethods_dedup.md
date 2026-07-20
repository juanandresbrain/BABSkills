# dbo.mulesoft_deckjsonraw_shippingmethods_dedup

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 1 |  |  |  |
| _ParentKeyField | bigint | 8 | 1 |  |  |  |
| OrderShippingID | bigint | 8 | 1 |  |  |  |
| ReferenceID | bigint | 8 | 1 |  |  |  |
| ShippingMethodID | bigint | 8 | 1 |  |  |  |
| OrderID | bigint | 8 | 1 |  |  |  |
| NetTotal | real | 4 | 1 |  |  |  |
| GrossTotal | real | 4 | 1 |  |  |  |
| AdjustedNetTotal | real | 4 | 1 |  |  |  |
| AdjustedGrossTotal | real | 4 | 1 |  |  |  |
| IsChanged | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
