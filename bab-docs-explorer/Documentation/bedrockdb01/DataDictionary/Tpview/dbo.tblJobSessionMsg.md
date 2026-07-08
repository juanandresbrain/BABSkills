# dbo.tblJobSessionMsg

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobSessionMsgID | int | 4 | 0 | YES |  |  |
| MsgType | int | 4 | 0 |  |  |  |
| DTSMSessionNo | int | 4 | 0 |  |  |  |
| TimeSent | datetime | 8 | 0 |  |  |  |
| ResponseType | int | 4 | 0 |  |  |  |
| ErrorNumber | int | 4 | 0 |  |  |  |
| ErrorDesc | varchar | 255 | 0 |  |  |  |
