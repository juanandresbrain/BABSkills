# dbo.WCAUDIT_ExportVsSalesDate

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| iStoreID | int | 4 | 0 |  |  |  |
| orders | int | 4 | 1 |  |  |  |
| AWSalesDate | smalldatetime | 4 | 1 |  |  |  |
| ExportDate | smalldatetime | 4 | 1 |  |  |  |
| Amount | money | 8 | 1 |  |  |  |
| Amount_CC | money | 8 | 1 |  |  |  |
| Amount_GC | money | 8 | 1 |  |  |  |
| Amount_SFS | money | 8 | 1 |  |  |  |
| Units | int | 4 | 1 |  |  |  |
