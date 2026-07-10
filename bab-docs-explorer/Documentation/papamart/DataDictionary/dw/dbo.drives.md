# dbo.drives

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| server | varchar | 20 | 1 |  |  |  |
| drive | char | 1 | 1 |  |  |  |
| FreeSpace | int | 4 | 1 |  |  |  |
| TotalSize | bigint | 8 | 1 |  |  |  |
| PercentFree | int | 4 | 1 |  |  |  |
| DateStamp | datetime | 8 | 1 |  |  |  |
| emailsent | bit | 1 | 1 |  |  |  |
