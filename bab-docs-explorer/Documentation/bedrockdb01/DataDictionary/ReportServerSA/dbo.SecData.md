# dbo.SecData

**Database:** ReportServerSA  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SecDataID | uniqueidentifier | 16 | 0 |  |  |  |
| PolicyID | uniqueidentifier | 16 | 0 |  |  |  |
| AuthType | int | 4 | 0 |  |  |  |
| XmlDescription | ntext | 256 | 0 |  |  |  |
| NtSecDescPrimary | image | 256 | 0 |  |  |  |
| NtSecDescSecondary | ntext | 256 | 1 |  |  |  |
