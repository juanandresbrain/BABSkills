# esell.csaRoleLocationAttributes

**Database:** esell  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RETAILER_ID | int | 4 | 0 | YES |  |  |
| ROLE_ID | nvarchar | 40 | 0 | YES |  |  |
| LocationHierarchyID | nvarchar | 160 | 1 |  |  |  |
| LocationLvl | int | 4 | 1 |  |  |  |
| LocationGroupID | nvarchar | 160 | 1 |  |  |  |

