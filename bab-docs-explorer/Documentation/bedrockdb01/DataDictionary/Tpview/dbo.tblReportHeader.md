# dbo.tblReportHeader

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReportHeaderID | int | 4 | 0 | YES |  |  |
| Name | varchar | 255 | 0 |  |  |  |
| Type | int | 4 | 0 |  |  |  |
| Missing | int | 4 | 0 |  |  |  |
| AutoPrint | int | 4 | 0 |  |  |  |
| Path | varchar | 255 | 0 |  |  |  |
| Prefix | varchar | 255 | 0 |  |  |  |
| AutoTime | datetime | 8 | 0 |  |  |  |
| Frequency | int | 4 | 0 |  |  |  |
| LastPrintTime | datetime | 8 | 0 |  |  |  |
