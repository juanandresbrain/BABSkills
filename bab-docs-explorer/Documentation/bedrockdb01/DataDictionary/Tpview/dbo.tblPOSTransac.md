# dbo.tblPOSTransac

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| POSTransacID | int | 4 | 0 | YES |  |  |
| MsgType | varchar | 16 | 0 |  |  |  |
| TimeReceived | datetime | 8 | 0 |  |  |  |
| StoreNumber | varchar | 6 | 0 |  |  |  |
| CurrentTime | datetime | 8 | 0 |  |  |  |
| Hdr_MsgType | varchar | 2 | 0 |  |  |  |
| Hdr_SubType | varchar | 2 | 0 |  |  |  |
| Hdr_Service | varchar | 2 | 0 |  |  |  |
| Hdr_Seq | int | 4 | 0 |  |  |  |
| Hdr_TimeOut | int | 4 | 0 |  |  |  |
| Hdr_LoopBack | varchar | 2 | 0 |  |  |  |
| Hdr_Hop | varchar | 2 | 0 |  |  |  |
| Hdr_State | varchar | 2 | 0 |  |  |  |
| Hdr_RegNo | varchar | 2 | 0 |  |  |  |
| Hdr_LoopBackCode | int | 4 | 0 |  |  |  |
| Hdr_ReqReplyFlag | varchar | 2 | 0 |  |  |  |
| Hdr_Len | int | 4 | 0 |  |  |  |
| Hdr_POSTime | datetime | 8 | 0 |  |  |  |
| Hdr_POSRegNo | varchar | 2 | 0 |  |  |  |
| Hdr_Filler | varchar | 22 | 0 |  |  |  |
| Account | varchar | 50 | 0 |  |  |  |
| ExpDate | varchar | 10 | 0 |  |  |  |
| Amount | varchar | 10 | 0 |  |  |  |
| Track1 | varchar | 255 | 0 |  |  |  |
| Track2 | varchar | 255 | 0 |  |  |  |
| Track3 | varchar | 255 | 0 |  |  |  |
| T2ExpDate | varchar | 10 | 0 |  |  |  |
| DrvLicence | varchar | 30 | 0 |  |  |  |
| BirthDate | varchar | 10 | 0 |  |  |  |
| TransNum | varchar | 20 | 0 |  |  |  |
| OrigTranCode | varchar | 20 | 0 |  |  |  |
| TranCode | varchar | 20 | 0 |  |  |  |
| Aba | varchar | 20 | 0 |  |  |  |
| CheckSeq | varchar | 5 | 0 |  |  |  |
| StateCode | varchar | 2 | 0 |  |  |  |
| CardId | varchar | 2 | 0 |  |  |  |
| RegNo | varchar | 5 | 0 |  |  |  |
| PurchaseCode | varchar | 20 | 0 |  |  |  |
| SwipedInd | varchar | 2 | 0 |  |  |  |
| StatusCode | varchar | 2 | 0 |  |  |  |
| AuthCode | varchar | 8 | 0 |  |  |  |
| Display | varchar | 112 | 0 |  |  |  |
| Receipt | varchar | 12 | 0 |  |  |  |
| BalanceFlag | varchar | 2 | 0 |  |  |  |
| Balance | varchar | 10 | 0 |  |  |  |
| RegNumber | varchar | 2 | 0 |  |  |  |
| CoNumber | varchar | 2 | 0 |  |  |  |
| RevSeqNum | varchar | 10 | 0 |  |  |  |
| Method | varchar | 1 | 0 |  |  |  |
| CardType | varchar | 5 | 0 |  |  |  |
| StoreNum | varchar | 5 | 0 |  |  |  |
| ExpiryDay | varchar | 2 | 0 |  |  |  |
| ExpiryMonth | varchar | 2 | 0 |  |  |  |
| ExpiryYear | varchar | 2 | 0 |  |  |  |
| FirstName | varchar | 50 | 0 |  |  |  |
| LastName | varchar | 50 | 0 |  |  |  |
