# dbo.ServiceDeskOpenStage

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Incident | int | 4 | 1 |  |  |  |
| Summary | nvarchar | 510 | 1 |  |  |  |
| Status | nvarchar | 510 | 1 |  |  |  |
| Priority | nvarchar | 510 | 1 |  |  |  |
| Customer | nvarchar | 510 | 1 |  |  |  |
| CustomerLocation | varchar | 4 | 1 |  |  |  |
| Owner | nvarchar | 510 | 1 |  |  |  |
| Created On | datetime | 8 | 1 |  |  |  |
| Source | nvarchar | 510 | 1 |  |  |  |
| Team | nvarchar | 510 | 1 |  |  |  |
| Area | nvarchar | 510 | 1 |  |  |  |
| Category | nvarchar | 510 | 1 |  |  |  |
| Subcategory | nvarchar | 510 | 1 |  |  |  |
| ResolvedDateTime | datetime | 8 | 1 |  |  |  |
| Description | nvarchar | -1 | 1 |  |  |  |
| Country | nvarchar | 510 | 1 |  |  |  |
| Owner Email | nvarchar | 510 | 1 |  |  |  |
| Problem | nvarchar | 510 | 1 |  |  |  |
| OpenWK | int | 4 | 1 |  |  |  |
| OpenMo | int | 4 | 1 |  |  |  |
| OpenYr | int | 4 | 1 |  |  |  |
