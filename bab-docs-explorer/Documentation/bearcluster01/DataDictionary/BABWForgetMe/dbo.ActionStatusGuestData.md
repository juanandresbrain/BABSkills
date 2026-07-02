# dbo.ActionStatusGuestData

**Database:** BABWForgetMe  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ActionStatusGuestDataID | int | 4 | 0 | YES |  |  |
| RecordKey | varchar | 26 | 0 |  | YES |  |
| GuestDataTypeID | int | 4 | 0 |  | YES |  |
| FirstName | nvarchar | 128 | 1 |  |  |  |
| LastName | nvarchar | 128 | 1 |  |  |  |
| Address1 | nvarchar | 200 | 1 |  |  |  |
| Address2 | nvarchar | 200 | 1 |  |  |  |
| City | nvarchar | 100 | 1 |  |  |  |
| State | nvarchar | 100 | 1 |  |  |  |
| PostalCode | nvarchar | 100 | 1 |  |  |  |
| Country | nvarchar | 100 | 1 |  |  |  |
| Phone | nvarchar | 100 | 1 |  |  |  |

