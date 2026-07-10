# dbo.Report_Snapshot20160320_DeleteIfMoreRecentOneCreated

**Database:** reportingservices_subscription  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReportId | int | 4 | 0 | YES |  |  |
| Name | varchar | 200 | 0 |  |  |  |
| Path | varchar | 100 | 0 |  |  |  |
| FileExtension | varchar | 3 | 0 |  |  |  |
| ReportingServiceReportName | varchar | 200 | 0 |  |  |  |
| Enabled | bit | 1 | 0 |  |  |  |
| rptGroupID | int | 4 | 0 |  |  |  |
| rptFreq | varchar | 1 | 0 |  |  |  |
