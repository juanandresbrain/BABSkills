# dbo.ReportGroup

**Database:** reportingservices_subscription  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| rptGroupID | int | 4 | 0 | YES |  |  |
| Description | varchar | 50 | 0 |  |  |  |
| rootDirectory | varchar | 255 | 1 |  |  | This is the Root Directory where the reports are written to. |
