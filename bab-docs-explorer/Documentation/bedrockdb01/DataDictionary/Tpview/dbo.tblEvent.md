# dbo.tblEvent

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| EventID | int | 4 | 0 | YES |  |  |
| EventType | int | 4 | 0 |  |  |  |
| EventTime | datetime | 8 | 0 |  |  |  |
| RemoteNumber | int | 4 | 0 |  |  |  |
| RegisterNumber | int | 4 | 0 |  |  |  |
| LocationType | int | 4 | 0 |  |  |  |
| ConnectType | int | 4 | 0 |  |  |  |
| BusySignalPrim | int | 4 | 0 |  |  |  |
| BusySignalBack | int | 4 | 0 |  |  |  |
| ConnectDuration | int | 4 | 0 |  |  |  |
| DisconnDuration | int | 4 | 0 |  |  |  |
| NbrLocNotPrim | int | 4 | 0 |  |  |  |
| HostRespTime | int | 4 | 0 |  |  |  |
| LocRespTime | int | 4 | 0 |  |  |  |
| MsgType | varchar | 2 | 0 |  |  |  |
| Card | varchar | 2 | 0 |  |  |  |
| Service | varchar | 2 | 0 |  |  |  |
| POSRequestTime | datetime | 8 | 0 |  |  |  |
| DrvLicence | varchar | 30 | 0 |  |  |  |
| BirthDate | varchar | 10 | 0 |  |  |  |
| Aba | varchar | 20 | 0 |  |  |  |
| CheckSeq | varchar | 5 | 0 |  |  |  |
| StateCode | varchar | 2 | 0 |  |  |  |
| Account | varchar | 20 | 0 |  |  |  |
| Amount | varchar | 10 | 0 |  |  |  |
| StatusCode | varchar | 2 | 0 |  |  |  |
| AuthCode | varchar | 8 | 0 |  |  |  |
| PDConnTime | int | 4 | 0 |  |  |  |
| PDTransTime | int | 4 | 0 |  |  |  |
| PDSendTime | int | 4 | 0 |  |  |  |
| LocServHoldTime | int | 4 | 0 |  |  |  |
| ServLocHoldTime | int | 4 | 0 |  |  |  |
| ServRespTime | int | 4 | 0 |  |  |  |
| ExpDate | varchar | 10 | 0 |  |  |  |
| ConnRegNo | int | 4 | 0 |  |  |  |
| POSRequestTZDesc | varchar | 50 | 0 |  |  |  |
| POSRequestTZSec | int | 4 | 0 |  |  |  |
| NbrRegNotPrim | int | 4 | 0 |  |  |  |
| NbrRegNotPrimLoc | int | 4 | 0 |  |  |  |
| VoucherFirstName | varchar | 20 | 0 |  |  |  |
| VoucherLastName | varchar | 20 | 0 |  |  |  |
| VoucherPhoneNo | varchar | 16 | 0 |  |  |  |
| VoucherCustomerNo | numeric | 13 | 0 |  |  |  |
| VoucherNo | varchar | 20 | 0 |  |  |  |
| VoucherResult | int | 4 | 0 |  |  |  |
| LocationID | int | 4 | 0 |  |  |  |
| DeviceID | int | 4 | 0 |  |  |  |
| ApplicationID | int | 4 | 0 |  |  |  |
| CoNumber | varchar | 2 | 0 |  |  |  |
| RevSeqNum | varchar | 10 | 0 |  |  |  |
| Method | varchar | 1 | 0 |  |  |  |
| TransNum | varchar | 20 | 0 |  |  |  |
| ExpiryDay | varchar | 2 | 0 |  |  |  |
| ExpiryMonth | varchar | 2 | 0 |  |  |  |
| ExpiryYear | varchar | 2 | 0 |  |  |  |
| FirstName | varchar | 50 | 0 |  |  |  |
| LastName | varchar | 50 | 0 |  |  |  |
| Receipt | varchar | 12 | 0 |  |  |  |
| ReversalStateCode | int | 4 | 0 |  |  |  |
| LoopbackCode | int | 4 | 0 |  |  |  |
| LoopbackMessage | varchar | 255 | 0 |  |  |  |
| HostReceivedTime | datetime | 8 | 0 |  |  |  |
| HostSentTime | datetime | 8 | 0 |  |  |  |
| HostReplyAckTime | datetime | 8 | 0 |  |  |  |
| HostReplyAckStatus | int | 4 | 0 |  |  |  |
| ServiceSentTime | datetime | 8 | 0 |  |  |  |
| ServiceReceivedTime | datetime | 8 | 0 |  |  |  |
| CallerIPAddress | varchar | 15 | 0 |  |  |  |
| CallerIPPort | int | 4 | 0 |  |  |  |
| ListenerIPAddress | varchar | 15 | 0 |  |  |  |
| ListenerIPPort | int | 4 | 0 |  |  |  |
| ConnFailedCode | int | 4 | 0 |  |  |  |
