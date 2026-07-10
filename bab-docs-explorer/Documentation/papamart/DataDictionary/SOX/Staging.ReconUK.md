# Staging.ReconUK

**Database:** SOX  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| SourceFileName | nvarchar | -1 | 1 |  |  |  |
| ActivationMid | varchar | 50 | 1 |  |  |  |
| ActivationStore | varchar | 50 | 1 |  |  |  |
| CardNumber | varchar | 50 | 0 |  |  |  |
| ActivationAmount | money | 8 | 1 |  |  |  |
| redemptionAmount | money | 8 | 1 |  |  |  |
| ReloadAmount | money | 8 | 1 |  |  |  |
| AdjustedAmount | money | 8 | 1 |  |  |  |
| ServiceFeeAmount | money | 8 | 1 |  |  |  |
| OutstandingBalance | money | 8 | 1 |  |  |  |
| ActivationDate | datetime | 8 | 1 |  |  |  |
