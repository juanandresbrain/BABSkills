# dbo.ReportParameter_SnapshotBeforeHierarchyChange_DoNotDelete

**Database:** reportingservices_subscription  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ReportParameterId | int | 4 | 0 | YES |  |  |
| ReportId | int | 4 | 0 |  |  |  |
| ParameterName | varchar | 50 | 0 |  |  |  |
| ParameterLabel | varchar | 50 | 0 |  |  |  |
| ParameterValue | varchar | 512 | 1 |  |  |  |
| Enabled | bit | 1 | 0 |  |  |  |
