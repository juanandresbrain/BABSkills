# dbo.plu_price_change

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| plu_price_change_id | decimal | 9 | 0 | YES |  |  |
| document_number | nvarchar | 40 | 0 |  |  |  |
| start_date | smalldatetime | 4 | 0 |  |  |  |
| end_date | smalldatetime | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.pcm_issue_pc_$sp](../../StoredProcedures/me_01/dbo.pcm_issue_pc_$sp.md)

