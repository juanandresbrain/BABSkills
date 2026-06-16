# TXT.PrdDates

**Database:** IntegrationStaging  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Fiscal_year_pd | varchar | 14 | 0 |  |  |  |
| fiscal_year | int | 4 | 1 |  |  |  |
| fiscal_period | int | 4 | 1 |  |  |  |
| BOPDate | datetime | 8 | 1 |  |  |  |
| EOPDate | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [IntegrationStaging: TXT.spOnHandFields](../../StoredProcedures/IntegrationStaging/TXT.spOnHandFields.md)
- [IntegrationStaging: TXT.spPeriodDates](../../StoredProcedures/IntegrationStaging/TXT.spPeriodDates.md)
- [IntegrationStaging: TXT.spWeeklyReportTable](../../StoredProcedures/IntegrationStaging/TXT.spWeeklyReportTable.md)

