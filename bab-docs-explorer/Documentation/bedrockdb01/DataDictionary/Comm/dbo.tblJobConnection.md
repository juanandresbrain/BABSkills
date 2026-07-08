# dbo.tblJobConnection

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| JobConnectionID | int | 4 | 0 | YES |  |  |
| RegisterType | int | 4 | 0 |  |  |  |
| Phone | varchar | 24 | 0 |  |  |  |
| HostName | nvarchar | 30 | 0 |  |  |  |
| BSCLineID | int | 4 | 0 |  |  |  |
| BaudRate | int | 4 | 0 |  |  |  |
| CallTermDelay | int | 4 | 0 |  |  |  |
| NbrColRegPrinter | int | 4 | 0 |  |  |  |
| SignOnID | varchar | 4 | 0 |  |  |  |
| FileOrQueue | int | 4 | 0 |  |  |  |
| ListAndPunch | int | 4 | 0 |  |  |  |
| EBCDICOrASCII | int | 4 | 0 |  |  |  |
| PToPOrMultiDrop | int | 4 | 0 |  |  |  |
| PrimaryOrSecondary | int | 4 | 0 |  |  |  |
| ControlOrTributary | int | 4 | 0 |  |  |  |
| LRCOrCRC | int | 4 | 0 |  |  |  |
| Transparency | int | 4 | 0 |  |  |  |
| Compression | int | 4 | 0 |  |  |  |
| TwoOrThree780 | int | 4 | 0 |  |  |  |
| BinaryOrText | int | 4 | 0 |  |  |  |
| NbrBytesPerRecord | int | 4 | 0 |  |  |  |
| NbrRecordsPerBlock | int | 4 | 0 |  |  |  |
| ReceiveConv | int | 4 | 0 |  |  |  |
| TransmitConv | int | 4 | 0 |  |  |  |
| Transmit | int | 4 | 0 |  |  |  |
| DelayFirstFile | int | 4 | 0 |  |  |  |
| DelayOtherFile | int | 4 | 0 |  |  |  |
| InitFromRegNumber | int | 4 | 0 |  |  |  |
| InitToRegNumber | int | 4 | 0 |  |  |  |
| ConnTransMethod | int | 4 | 0 |  |  |  |
| PhoneBookEntry | varchar | 255 | 0 |  |  |  |
| FTPPortNumber | int | 4 | 0 |  |  |  |
| FTPUserAccount | nvarchar | 128 | 0 |  |  |  |
| FTPPassword | nvarchar | 322 | 0 |  |  |  |
| FTPSendCommand | varchar | 20 | 0 |  |  |  |
| FTPReceivedCommand | varchar | 20 | 0 |  |  |  |
| ChangeDirBefTrans | int | 4 | 0 |  |  |  |
| SingleQuoteRemotePath | int | 4 | 0 |  |  |  |
| FTPFileNamePosition | int | 4 | 0 |  |  |  |
| LocalHost | nvarchar | 30 | 0 |  |  |  |
