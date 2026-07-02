# dbo.Sr_Host

**Database:** fn_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| machine_id | int | 4 | 0 |  |  |  |
| host_id | int | 4 | 0 |  |  |  |
| host_label | varchar | 30 | 1 |  |  |  |
| host_name | varchar | 30 | 1 |  |  |  |
| user_name | varchar | 60 | 1 |  |  |  |
| user_password | varchar | 60 | 1 |  |  |  |
| merge_directory | varchar | 255 | 1 |  |  |  |
| ftp_destination_directory | varchar | 255 | 1 |  |  |  |
| version | int | 4 | 1 |  |  |  |
| transfer_protocol | int | 4 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Sv_UpdateNextID](../../StoredProcedures/fn_01/dbo.Sv_UpdateNextID.md)
- [smartlook_01: dbo.Sv_UpdateNextID](../../StoredProcedures/smartlook_01/dbo.Sv_UpdateNextID.md)

