# dbo.tblRemote

**Database:** Comm  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RemoteID | int | 4 | 0 | YES |  |  |
| RemoteNumber | decimal | 9 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| RemoteName | nvarchar | 120 | 0 |  |  |  |
| GroupingIntervalID | int | 4 | 1 |  |  |  |
| RegisterType | int | 4 | 0 |  |  |  |
| PollID | varchar | 2 | 0 |  |  |  |
| CodeString | varchar | 30 | 0 |  |  |  |
| MerchantID1 | varchar | 11 | 0 |  |  |  |
| MerchantID2 | varchar | 11 | 0 |  |  |  |
| MerchantID3 | varchar | 11 | 0 |  |  |  |
| MerchantID4 | varchar | 11 | 0 |  |  |  |
| MerchantID5 | varchar | 11 | 0 |  |  |  |
| MerchantID6 | varchar | 11 | 0 |  |  |  |
| MerchantCode | varchar | 4 | 0 |  |  |  |
| StateCode | varchar | 2 | 0 |  |  |  |
| ZipCode | varchar | 9 | 0 |  |  |  |
| IPAddress | int | 4 | 0 |  |  |  |
| LocationType | int | 4 | 0 |  |  |  |
| Country | int | 4 | 0 |  |  |  |
| CityName | varchar | 40 | 0 |  |  |  |
| EffectiveDate | datetime | 8 | 1 |  |  |  |
| EndDate | datetime | 8 | 1 |  |  |  |
| OPNG_HOUR_GRP_ID | smallint | 2 | 0 |  |  |  |
| TIME_ZONE | bigint | 8 | 0 |  |  |  |
| RGN | int | 4 | 0 |  |  |  |
