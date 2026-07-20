# dbo.ds_customers

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CustomerNumber | varchar | 8000 | 1 |  |  |  |
| first_txn_date | datetime2 | 8 | 1 |  |  |  |
| acquisition_month_cohort | datetime2 | 8 | 1 |  |  |  |
| last_txn_date | datetime2 | 8 | 1 |  |  |  |
| num_txns | bigint | 8 | 1 |  |  |  |
| gross_amount | decimal | 13 | 1 |  |  |  |
| net_amount | decimal | 17 | 1 |  |  |  |
| CalculatedBirthDate | date | 3 | 1 |  |  |  |
| has_birthday_bear | bit | 1 | 1 |  |  |  |
| num_partys | bigint | 8 | 1 |  |  |  |
| countrycode | varchar | 8000 | 1 |  |  |  |
| total_population | int | 4 | 1 |  |  |  |
| population_by_age_sex | int | 4 | 1 |  |  |  |
| total_race_population | int | 4 | 1 |  |  |  |
| white_population | int | 4 | 1 |  |  |  |
| black_population | int | 4 | 1 |  |  |  |
| asian_population | int | 4 | 1 |  |  |  |
| total_ethnicity_population | int | 4 | 1 |  |  |  |
| hispanic_population | int | 4 | 1 |  |  |  |
| housing_units | int | 4 | 1 |  |  |  |
| total_occupancy | int | 4 | 1 |  |  |  |
| occupied_units | int | 4 | 1 |  |  |  |
| vacant_units | int | 4 | 1 |  |  |  |
| total_tenure | int | 4 | 1 |  |  |  |
| owner_occupied | int | 4 | 1 |  |  |  |
| renter_occupied | int | 4 | 1 |  |  |  |
| median_home_value | int | 4 | 1 |  |  |  |
| median_rent | int | 4 | 1 |  |  |  |
| median_household_income | int | 4 | 1 |  |  |  |
| median_household_income_bucket | varchar | 8000 | 1 |  |  |  |
| per_capita_income | int | 4 | 1 |  |  |  |
| total_poverty_status | int | 4 | 1 |  |  |  |
| below_poverty | int | 4 | 1 |  |  |  |
| total_income_distribution | int | 4 | 1 |  |  |  |
| income_under_10k | int | 4 | 1 |  |  |  |
| income_10k_to_15k | int | 4 | 1 |  |  |  |
| total_education_attainment | int | 4 | 1 |  |  |  |
| high_school_graduate | int | 4 | 1 |  |  |  |
| bachelor_degree | int | 4 | 1 |  |  |  |
| total_school_enrollment | int | 4 | 1 |  |  |  |
| enrolled_in_school | int | 4 | 1 |  |  |  |
| total_employment_status | int | 4 | 1 |  |  |  |
| employed | int | 4 | 1 |  |  |  |
| unemployed | int | 4 | 1 |  |  |  |
| industry_distribution | int | 4 | 1 |  |  |  |
| occupation_distribution | int | 4 | 1 |  |  |  |
| total_commuting | int | 4 | 1 |  |  |  |
| public_transport_commute | int | 4 | 1 |  |  |  |
| total_language_spoken | int | 4 | 1 |  |  |  |
| english_only | int | 4 | 1 |  |  |  |
| total_nativity | int | 4 | 1 |  |  |  |
| us_citizens | int | 4 | 1 |  |  |  |
| total_health_insurance | int | 4 | 1 |  |  |  |
| coverage_by_age_type | int | 4 | 1 |  |  |  |
| marital_status | int | 4 | 1 |  |  |  |
| household_type | int | 4 | 1 |  |  |  |
| group_quarters_population | int | 4 | 1 |  |  |  |
| zip_code_tabulation_area | varchar | 8000 | 1 |  |  |  |
| net_margin | decimal | 17 | 1 |  |  |  |
