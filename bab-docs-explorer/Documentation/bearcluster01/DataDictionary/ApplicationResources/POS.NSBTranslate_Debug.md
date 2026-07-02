# POS.NSBTranslate_Debug

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 | YES |  |  |
| dTimeStamp | datetime | 8 | 0 |  |  |  |
| sOrderNumber | varchar | 50 | 1 |  |  |  |
| sNSBTransID | varchar | 50 | 1 |  |  |  |
| sStructure | varchar | 200 | 1 |  |  |  |
| iLineID | int | 4 | 1 |  |  |  |
| iLogLevel | int | 4 | 1 |  |  |  |
| iLogID | int | 4 | 1 |  |  |  |
| sMessage | varchar | 5000 | 1 |  |  |  |
| sMethod | varchar | 50 | 1 |  |  |  |
| sProduction | varchar | 50 | 1 |  |  |  |
| iStore | int | 4 | 1 |  |  |  |

