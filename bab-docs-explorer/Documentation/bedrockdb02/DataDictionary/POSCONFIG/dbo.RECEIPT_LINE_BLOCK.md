# dbo.RECEIPT_LINE_BLOCK

**Database:** POSCONFIG  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| FLOW_ID | int | 4 | 0 | YES |  |  |
| PRN_LINE_TYPE_CODE | varchar | 10 | 0 | YES |  |  |
| SEQ_NO | smallint | 2 | 0 | YES |  |  |
| LINE_NAME | varchar | 50 | 0 | YES |  |  |
| SCRIPT | ntext | 16 | 1 |  |  |  |
| PRN_LINE_SUBTYPE | varchar | 20 | 1 |  |  |  |
| LINE_LAYOUT | ntext | 16 | 1 |  |  |  |

## Referenced By Stored Procedures

- [POSCONFIG: dbo.CLONE_FLOW](../../StoredProcedures/POSCONFIG/dbo.CLONE_FLOW.md)
- [POSCONFIG: dbo.DELETE_FLOW](../../StoredProcedures/POSCONFIG/dbo.DELETE_FLOW.md)

