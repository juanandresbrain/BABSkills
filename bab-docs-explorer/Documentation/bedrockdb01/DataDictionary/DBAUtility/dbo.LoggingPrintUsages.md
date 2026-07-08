# dbo.LoggingPrintUsages

**Database:** DBAUtility  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LogID | bigint | 8 | 0 | YES |  |  |
| SkinID | nvarchar | 36 | 0 |  |  |  |
| DateOfPrint | datetime | 8 | 0 |  |  |  |
| PrintJobType | nvarchar | 100 | 0 |  |  |  |
| ChosenBirthCertificate | nvarchar | 100 | 0 |  |  |  |
| PrintLanguage | nvarchar | 10 | 0 |  |  |  |
| FoundDataInNameMe | bit | 1 | 0 |  |  |  |
| IPPrintedFrom | nvarchar | 100 | 0 |  |  |  |
| StoreNumber | int | 4 | 0 |  |  |  |
