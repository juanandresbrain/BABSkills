# dbo.REPORT_PARAMETER

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| REPORT_ID | int | 4 | 0 | YES |  |  |
| PARAMETER_NAME | nvarchar | 100 | 0 | YES |  |  |
| SUBREPORT | nvarchar | 100 | 0 | YES |  |  |
| DESCRIPTION | nvarchar | 510 | 1 |  |  |  |
| DEFAULT_VALUE | nvarchar | 2000 | 1 |  |  |  |

