# dbo.azure_newdatedim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Date_Key | date | 3 | 1 |  |  |  |
| Date_Name | varchar | 8000 | 1 |  |  |  |
| Fiscal_Year_key | date | 3 | 1 |  |  |  |
| Fiscal_Year | varchar | 8000 | 1 |  |  |  |
| Fiscal_Quarter_key | date | 3 | 1 |  |  |  |
| Fiscal_Quarter | varchar | 8000 | 1 |  |  |  |
| Fiscal_Month_Key | date | 3 | 1 |  |  |  |
| Fiscal_Month | varchar | 8000 | 1 |  |  |  |
| Fiscal_Week_Key | date | 3 | 1 |  |  |  |
| Fiscal_Week | varchar | 8000 | 1 |  |  |  |
| Fiscal_Day_of_year_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Day_Of_Year | varchar | 8000 | 1 |  |  |  |
| Fiscal_Day_Of_Quarter_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Day_Of_Quarter | varchar | 8000 | 1 |  |  |  |
| Fiscal_Day_Of_Month_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Day_Of_Month | varchar | 8000 | 1 |  |  |  |
| Fiscal_Day_Of_Week_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Day_Of_Week | varchar | 8000 | 1 |  |  |  |
| Fiscal_Week_Of_Year_key | bigint | 8 | 1 |  |  |  |
| Fiscal_Week_of_Year | varchar | 8000 | 1 |  |  |  |
| Fiscal_Week_Of_Quarter_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Week_Of_Quarter | varchar | 8000 | 1 |  |  |  |
| Fiscal_Week_Of_Month_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Week_Of_Month | varchar | 8000 | 1 |  |  |  |
| Fiscal_Month_Of_Year_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Month_Of_Year | varchar | 8000 | 1 |  |  |  |
| Fiscal_Month_Of_Quarter_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Month_Of_Quarter | varchar | 8000 | 1 |  |  |  |
| Fiscal_Quarter_Of_Year_Key | bigint | 8 | 1 |  |  |  |
| Fiscal_Quarter_Of_Year | varchar | 8000 | 1 |  |  |  |
| FiscalYearNumber | bigint | 8 | 1 |  |  |  |
| FiscalPeriodSequenceKey | bigint | 8 | 1 |  |  |  |
| DailyInvFilter | int | 4 | 1 |  |  |  |
| SlicerWeek | varchar | 8000 | 1 |  |  |  |
| OffSetWeek | bigint | 8 | 1 |  |  |  |
| AlternateFiscalWeek | date | 3 | 1 |  |  |  |
| DescDate | date | 3 | 1 |  |  |  |
| DescSort | int | 4 | 1 |  |  |  |
| SlicerMonth | varchar | 8000 | 1 |  |  |  |
| DayName | varchar | 8000 | 1 |  |  |  |
| MonthKey | float | 8 | 1 |  |  |  |
| LastFiscalWeek | date | 3 | 1 |  |  |  |
| Fiscal_YTD_Include | varchar | 8000 | 1 |  |  |  |
| MonthOffSet | bigint | 8 | 1 |  |  |  |
| CnyExchangeRate | decimal | 9 | 1 |  |  |  |
| GbpExchangeRate | decimal | 9 | 1 |  |  |  |
| IsLatestWeek | int | 4 | 1 |  |  |  |
