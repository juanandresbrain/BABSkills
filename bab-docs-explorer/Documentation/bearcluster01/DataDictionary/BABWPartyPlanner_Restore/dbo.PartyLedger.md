# dbo.PartyLedger

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| PartyLedgerID | int | 4 | 0 | YES |  |  |
| PartyLedgerTypeID | int | 4 | 1 |  | YES |  |
| PartyLedgerAmount | decimal | 5 | 1 |  |  |  |
| PartyLedgerDate | datetime | 8 | 1 |  |  |  |
| PartyID | int | 4 | 1 |  | YES |  |

