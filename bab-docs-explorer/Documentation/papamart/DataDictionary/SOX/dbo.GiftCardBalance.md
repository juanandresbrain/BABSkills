# dbo.GiftCardBalance

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditQuarterKey | smallint | 2 | 0 |  |  |  |
| CardNumber | varchar | 50 | 0 |  |  |  |
| ActivationMid | varchar | 50 | 1 |  |  |  |
| ActivationStore | varchar | 50 | 1 |  |  |  |
| ActivationAmount | money | 8 | 1 |  |  |  |
| RedemptionAmount | money | 8 | 1 |  |  |  |
| ReloadAmount | money | 8 | 1 |  |  |  |
| AdjustedAmount | money | 8 | 1 |  |  |  |
| ServiceFeeAmount | money | 8 | 1 |  |  |  |
| OutstandingBalance | money | 8 | 1 |  |  |  |
| ActivationDate | datetime | 8 | 1 |  |  |  |
