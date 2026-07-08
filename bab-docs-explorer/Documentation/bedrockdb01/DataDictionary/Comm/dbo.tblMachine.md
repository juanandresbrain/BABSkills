# dbo.tblMachine

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| MachineID | int | 4 | 0 | YES |  |  |
| Name | varchar | 20 | 0 |  |  |  |
| MachineType | int | 4 | 0 |  |  |  |
| Host | nvarchar | 60 | 0 |  |  |  |
| Login | nvarchar | 128 | 0 |  |  |  |
| Password | nvarchar | 242 | 0 |  |  |  |
| DefaultMachine | int | 4 | 0 |  |  |  |
| UnixBSCVersion | int | 4 | 0 |  |  |  |
| PortNumber | int | 4 | 0 |  |  |  |
