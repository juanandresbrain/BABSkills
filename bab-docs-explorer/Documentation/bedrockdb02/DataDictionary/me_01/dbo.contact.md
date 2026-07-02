# dbo.contact

**Database:** me_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| contact_id | decimal | 9 | 0 | YES |  |  |
| parent_id | decimal | 9 | 0 |  |  |  |
| parent_type | smallint | 2 | 0 |  |  |  |
| contact_type | smallint | 2 | 0 |  |  |  |
| contact_description1 | nvarchar | 60 | 0 |  |  |  |
| contact_description2 | nvarchar | 60 | 1 |  |  |  |
| contact_number | nvarchar | 100 | 0 |  |  |  |
| main_flag | bit | 1 | 0 |  |  |  |

## Referenced By Stored Procedures

- [me_01: dbo.rpt_get_contacts_$sp](../../StoredProcedures/me_01/dbo.rpt_get_contacts_$sp.md)
- [me_01: dbo.spBABW_getGoogleStoreFeedData](../../StoredProcedures/me_01/dbo.spBABW_getGoogleStoreFeedData.md)

