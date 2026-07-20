# dbo.demographics_bg_dim

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| demographics_bg_key | int | 4 | 1 |  |  |  |
| block_group_full | varchar | 8000 | 1 |  |  |  |
| demographic_year | int | 4 | 1 |  |  |  |
| msa | int | 4 | 1 |  |  |  |
| msa_name | varchar | 8000 | 1 |  |  |  |
| dma | int | 4 | 1 |  |  |  |
| dma_name | varchar | 8000 | 1 |  |  |  |
| nielson_county_size | int | 4 | 1 |  |  |  |
| cur_population | int | 4 | 1 |  |  |  |
| cur_num_of_households | int | 4 | 1 |  |  |  |
| prism_cluster | int | 4 | 1 |  |  |  |
| prizm_cluster_name | varchar | 8000 | 1 |  |  |  |
| hh_income_median_2002 | decimal | 9 | 1 |  |  |  |
| hh_total_2007 | int | 4 | 1 |  |  |  |
| hh_totoal_2002 | int | 4 | 1 |  |  |  |
| hh_with_5_persons_2002 | int | 4 | 1 |  |  |  |
| hh_size_avg_1990 | int | 4 | 1 |  |  |  |
| hh_size_avg_2002 | int | 4 | 1 |  |  |  |
| pop_total_2007 | int | 4 | 1 |  |  |  |
| pop_total_2002 | int | 4 | 1 |  |  |  |
| pop_white_2002 | int | 4 | 1 |  |  |  |
| pop_black_2002 | int | 4 | 1 |  |  |  |
| pop_hispanic_2002 | int | 4 | 1 |  |  |  |
| pop_total_hispanic_2002 | int | 4 | 1 |  |  |  |
| pop_hispanic_white_2002 | int | 4 | 1 |  |  |  |
| pop_asian_pacific_islander_2002 | int | 4 | 1 |  |  |  |
| pop_american_indian_eskimo_aleut_2002 | int | 4 | 1 |  |  |  |
| pop_age0_5_2002 | int | 4 | 1 |  |  |  |
| pop_age0_5_1990 | int | 4 | 1 |  |  |  |
| pop_age6_13_1990 | int | 4 | 1 |  |  |  |
| pop_age6_13_2002 | int | 4 | 1 |  |  |  |
| pop_age6_13_2007 | int | 4 | 1 |  |  |  |
| childrens_infants_clothing_stores_2002 | decimal | 9 | 1 |  |  |  |
| childrens_infants_clothing_stores_2007 | decimal | 9 | 1 |  |  |  |
