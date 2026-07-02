# dbo.min_max_profile_configuration_archive

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ArchiveDate | datetime | 8 | 1 |  |  |  |
| MerchandiseLevel | varchar | 20 | 1 |  |  |  |
| MerchandiseCode | varchar | 20 | 1 |  |  |  |
| MerchandiseDescription | varchar | 100 | 1 |  |  |  |
| CyclePeriod | varchar | 10 | 1 |  |  |  |
| CycleFrequency | int | 4 | 1 |  |  |  |
| Sun | int | 4 | 1 |  |  |  |
| Mon | int | 4 | 1 |  |  |  |
| Tue | int | 4 | 1 |  |  |  |
| Wed | int | 4 | 1 |  |  |  |
| Thurs | int | 4 | 1 |  |  |  |
| Fri | int | 4 | 1 |  |  |  |
| Sat | int | 4 | 1 |  |  |  |
| NextRunDate | varchar | 10 | 1 |  |  |  |
| LastRunDate | varchar | 10 | 1 |  |  |  |
| Application_server | varchar | 20 | 1 |  |  |  |
| LastXWeeks | int | 4 | 1 |  |  |  |
| MinimumWeeksOfSupply | int | 4 | 1 |  |  |  |
| MaximumWeeksOfSupply | int | 4 | 1 |  |  |  |
| ProcessLevel | varchar | 100 | 1 |  |  |  |
| UseSeasonality | varchar | 3 | 1 |  |  |  |
| XWeeksAgo | int | 4 | 1 |  |  |  |
| Weight | decimal | 5 | 1 |  |  |  |
| LocationCode | varchar | 4 | 1 |  |  |  |
| LocationName | varchar | 100 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.spMerchandisingInsertMinMaxProfileArchive](../../StoredProcedures/me_01/dbo.spMerchandisingInsertMinMaxProfileArchive.md)

