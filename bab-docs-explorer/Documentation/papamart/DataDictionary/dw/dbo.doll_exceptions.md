# dbo.doll_exceptions

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ID | int | 4 | 0 |  |  |  |
| iRLanguageID | smallint | 2 | 1 |  |  |  |
| iSLanguageID | smallint | 2 | 1 |  |  |  |
| sRBarCodeNumber | nvarchar | 26 | 1 |  |  |  |
| sRAnimalID | nvarchar | 26 | 1 |  |  |  |
| sRRecipientType | varchar | 20 | 1 |  |  |  |
| sRBookSchedule | nvarchar | 12 | 1 |  |  |  |
| sRDocumentType | nvarchar | 40 | 1 |  |  |  |
| iRStoryID | smallint | 2 | 1 |  |  |  |
| sRProcessFlow | varchar | 150 | 1 |  |  |  |
| sBearDollSelect | nvarchar | 20 | 1 |  |  |  |
| sCharmID | nvarchar | 20 | 1 |  |  |  |
| iRStore | smallint | 2 | 1 |  |  |  |
| dREndTime | datetime | 8 | 1 |  |  |  |
