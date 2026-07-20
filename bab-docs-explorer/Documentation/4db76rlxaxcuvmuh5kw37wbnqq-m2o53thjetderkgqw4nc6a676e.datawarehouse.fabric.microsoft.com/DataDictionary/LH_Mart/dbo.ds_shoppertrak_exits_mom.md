# dbo.ds_shoppertrak_exits_mom

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| StoreKey | int | 4 | 1 |  |  |  |
| month_cohort | date | 3 | 1 |  |  |  |
| total_exits | bigint | 8 | 1 |  |  |  |
| prev_month_exits | bigint | 8 | 1 |  |  |  |
| mom_pct_change | float | 8 | 1 |  |  |  |
