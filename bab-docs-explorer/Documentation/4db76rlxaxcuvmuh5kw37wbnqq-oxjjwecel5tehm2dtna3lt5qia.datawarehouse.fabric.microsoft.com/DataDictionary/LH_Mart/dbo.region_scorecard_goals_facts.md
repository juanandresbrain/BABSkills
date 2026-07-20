# dbo.region_scorecard_goals_facts

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| region_key | varchar | 8000 | 1 |  |  |  |
| as_of_date_key | int | 4 | 1 |  |  |  |
| currency_key | int | 4 | 1 |  |  |  |
| hpg_goal | decimal | 9 | 1 |  |  |  |
| bags_goal | decimal | 5 | 1 |  |  |  |
| party_sales_percent_goal | decimal | 5 | 1 |  |  |  |
| skins_to_trans_goal | decimal | 5 | 1 |  |  |  |
| avg_skin_price_goal | decimal | 9 | 1 |  |  |  |
| sounds_to_skins_goal | decimal | 5 | 1 |  |  |  |
| shoes_to_skins_goal | decimal | 5 | 1 |  |  |  |
| FileLocation | varchar | 8000 | 1 |  |  |  |
| ModifiedDateTime | datetime2 | 8 | 1 |  |  |  |
