# dbo.giftcardbalancebackup20170105

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| AuditQuarterKey | int | 4 | 1 |  |  |  |
| CardNumber | varchar | 8000 | 1 |  |  |  |
| ActivationMid | varchar | 8000 | 1 |  |  |  |
| ActivationStore | varchar | 8000 | 1 |  |  |  |
| ActivationAmount | decimal | 9 | 1 |  |  |  |
| RedemptionAmount | decimal | 9 | 1 |  |  |  |
| ReloadAmount | decimal | 9 | 1 |  |  |  |
| AdjustedAmount | decimal | 9 | 1 |  |  |  |
| ServiceFeeAmount | decimal | 9 | 1 |  |  |  |
| OutstandingBalance | decimal | 9 | 1 |  |  |  |
| ActivationDate | datetime2 | 8 | 1 |  |  |  |
