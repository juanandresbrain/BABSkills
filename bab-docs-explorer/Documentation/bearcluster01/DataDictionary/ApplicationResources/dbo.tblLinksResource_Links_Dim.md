# dbo.tblLinksResource_Links_Dim

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LinkID | int | 4 | 0 | YES |  |  |
| Link | varchar | 255 | 0 |  |  |  |
| Name | varchar | 50 | 0 |  |  |  |
| Description | varchar | 250 | 1 |  |  |  |
| ScreenID | int | 4 | 0 |  | YES |  |
| TypeID | int | 4 | 0 |  | YES |  |

