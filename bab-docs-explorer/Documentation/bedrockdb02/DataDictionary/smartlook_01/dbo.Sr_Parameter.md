# dbo.Sr_Parameter

**Database:** smartlook_01  
**Server:** bedrockdb02  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tag | varchar | 30 | 0 | YES |  |  |
| tag_value | varchar | 255 | 1 |  |  |  |
| last_modified | datetime | 8 | 1 |  |  |  |

## Referenced By Stored Procedures

- [fn_01: dbo.Cs_TransmissionResults](../../StoredProcedures/fn_01/dbo.Cs_TransmissionResults.md)
- [fn_01: dbo.Sr_CompatibilityCheck](../../StoredProcedures/fn_01/dbo.Sr_CompatibilityCheck.md)
- [fn_01: dbo.Sr_HistoryCleanup](../../StoredProcedures/fn_01/dbo.Sr_HistoryCleanup.md)
- [fn_01: dbo.Sr_MachineStart](../../StoredProcedures/fn_01/dbo.Sr_MachineStart.md)
- [fn_01: dbo.Sr_ServerStart](../../StoredProcedures/fn_01/dbo.Sr_ServerStart.md)
- [smartlook_01: dbo.Cs_TransmissionResults](../../StoredProcedures/smartlook_01/dbo.Cs_TransmissionResults.md)
- [smartlook_01: dbo.Sr_CompatibilityCheck](../../StoredProcedures/smartlook_01/dbo.Sr_CompatibilityCheck.md)
- [smartlook_01: dbo.Sr_HistoryCleanup](../../StoredProcedures/smartlook_01/dbo.Sr_HistoryCleanup.md)
- [smartlook_01: dbo.Sr_MachineStart](../../StoredProcedures/smartlook_01/dbo.Sr_MachineStart.md)
- [smartlook_01: dbo.Sr_ServerStart](../../StoredProcedures/smartlook_01/dbo.Sr_ServerStart.md)

