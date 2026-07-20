# MulesoftTest.DeckJsonRaw_OrderPayments

**Database:** IntegrationStaging_AZSFDBProd  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| _RowIndex | bigint | 8 | 0 |  |  |  |
| _ParentKeyField | bigint | 8 | 0 |  |  |  |
| ID | bigint | 8 | 1 |  |  |  |
| OrderID | bigint | 8 | 1 |  |  |  |
| PaymentProcessorID | bigint | 8 | 1 |  |  |  |
| PaymentProcessor | varchar | -1 | 1 |  |  |  |
| PaymentSubType | varchar | -1 | 1 |  |  |  |
| AuthorizedAmount | real | 4 | 1 |  |  |  |
| CapturedAmount | real | 4 | 1 |  |  |  |
| EarlyCaptureAmount | real | 4 | 1 |  |  |  |
| EarlyUsedAmount | real | 4 | 1 |  |  |  |
| EarlyCreditAmount | real | 4 | 1 |  |  |  |
| CreditedAmount | real | 4 | 1 |  |  |  |
| Generic1 | varchar | -1 | 1 |  |  |  |
| Generic2 | varchar | -1 | 1 |  |  |  |
| Generic3 | varchar | -1 | 1 |  |  |  |
| Generic4 | varchar | -1 | 1 |  |  |  |
| Generic5 | varchar | -1 | 1 |  |  |  |
| AmountAvailableForCapture | real | 4 | 1 |  |  |  |
| AmountAvaialbleForCredit | real | 4 | 1 |  |  |  |
| DateCreated | datetime2 | 8 | 1 |  |  |  |
| CardType | varchar | -1 | 1 |  |  |  |
| CardNumber | varchar | -1 | 1 |  |  |  |
| CardHolder | varchar | -1 | 1 |  |  |  |
| ExpirationMonth | bigint | 8 | 1 |  |  |  |
| ExpirationYear | bigint | 8 | 1 |  |  |  |
| PaymentToken | varchar | -1 | 1 |  |  |  |
| IsOriginalPayment | bit | 1 | 1 |  |  |  |
| IsEarlyCapture | bit | 1 | 1 |  |  |  |
| CreditCardIsChanged | bit | 1 | 1 |  |  |  |
| InsertDate | datetime2 | 8 | 1 |  |  |  |
| UpdateDate | datetime2 | 8 | 1 |  |  |  |
| JSONDate | datetime2 | 8 | 1 |  |  |  |
| MSSQL_System_Uniquifier_1785773419 | bigint | 8 | 0 |  |  |  |
