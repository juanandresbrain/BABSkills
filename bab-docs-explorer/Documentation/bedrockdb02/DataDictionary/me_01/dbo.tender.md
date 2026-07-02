# dbo.tender

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tender_id | smallint | 2 | 0 | YES |  |  |
| tender_code | nvarchar | 10 | 0 |  |  |  |
| tender_description | nvarchar | 100 | 0 |  |  |  |
| authorization_required_flag | bit | 1 | 0 |  |  |  |
| active_flag | bit | 1 | 0 |  |  |  |
| updatestamp | int | 4 | 0 |  |  |  |

## Referenced By Stored Procedures

- [USICOAL: dbo.NSB_SP_CUST_HIST1_TNDR](../../StoredProcedures/USICOAL/dbo.NSB_SP_CUST_HIST1_TNDR.md)
- [USICOAL: dbo.NSB_SP_LP_MAN_KEY_CARD1](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_MAN_KEY_CARD1.md)
- [USICOAL: dbo.NSB_SP_LP_VOID_TENDER](../../StoredProcedures/USICOAL/dbo.NSB_SP_LP_VOID_TENDER.md)
- [USICOAL: dbo.NSB_SP_MAN_KEY_CARD1](../../StoredProcedures/USICOAL/dbo.NSB_SP_MAN_KEY_CARD1.md)
- [USICOAL: dbo.NSB_SP_TILL_DEC_SUMM](../../StoredProcedures/USICOAL/dbo.NSB_SP_TILL_DEC_SUMM.md)

