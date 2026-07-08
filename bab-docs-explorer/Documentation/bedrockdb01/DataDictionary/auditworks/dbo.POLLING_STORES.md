# dbo.POLLING_STORES

**Database:** auditworks  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STORE_NUM | numeric | 5 | 0 |  |  |  |
| POLLING_VLDTN | bit | 1 | 0 |  |  |  |
| POLLING_VLDTN_DATE | smalldatetime | 4 | 1 |  |  |  |
| MODIFIED_BY | varchar | 20 | 1 |  |  |  |
| LAST_MODIFIED_DTTM | smalldatetime | 4 | 1 |  |  |  |
| OPEN_DATE | date | 3 | 1 |  |  |  |
| CLOSED_DATE | date | 3 | 1 |  |  |  |
| COUNTRY | varchar | 3 | 1 |  |  |  |
| STORE_TYPE | varchar | 20 | 1 |  |  |  |
| STORE_BRAND | varchar | 20 | 1 |  |  |  |
