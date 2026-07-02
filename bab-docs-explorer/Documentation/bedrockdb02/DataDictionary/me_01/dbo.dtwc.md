# dbo.dtwc

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| DOCUMENT_NBR | varchar | 10 | 1 |  |  |  |
| CREATE_DATE | varchar | 10 | 1 |  |  |  |
| FROM_LOCATION | varchar | 4 | 1 |  |  |  |
| TO_LOCATION | varchar | 4 | 1 |  |  |  |
| QTY | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.dant_DamageTransfersWithoutCartonNumbers](../../StoredProcedures/me_01/dbo.dant_DamageTransfersWithoutCartonNumbers.md)

