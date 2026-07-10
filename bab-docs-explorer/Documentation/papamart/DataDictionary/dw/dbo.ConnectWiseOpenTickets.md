# dbo.ConnectWiseOpenTickets

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ticket_number | float | 8 | 0 |  |  |  |
| company_id | nvarchar | 100 | 0 |  |  |  |
| summary | nvarchar | 200 | 0 |  |  |  |
| status | nvarchar | 100 | 0 |  |  |  |
| date_entered | datetime2 | 8 | 0 |  |  |  |
| last_update | datetime2 | 8 | 0 |  |  |  |
| team_name | nvarchar | 100 | 0 |  |  |  |
| ticket_owner | nvarchar | 100 | 1 |  |  |  |
| age | float | 8 | 0 |  |  |  |
| board_name | nvarchar | 100 | 0 |  |  |  |
