# dbo.tblRemote

**Database:** Tpview  
**Server:** bedrockdb01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| RemoteID | int | 4 | 0 | YES |  |  |
| RemoteNumber | numeric | 9 | 0 |  |  |  |
| VersionID | int | 4 | 0 |  |  |  |
| RemoteName | varchar | 60 | 0 |  |  |  |
| SunTime | datetime | 8 | 1 |  |  |  |
| MonTime | datetime | 8 | 1 |  |  |  |
| TueTime | datetime | 8 | 1 |  |  |  |
| WedTime | datetime | 8 | 1 |  |  |  |
| ThuTime | datetime | 8 | 1 |  |  |  |
| FriTime | datetime | 8 | 1 |  |  |  |
| SatTime | datetime | 8 | 1 |  |  |  |
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
| ZipCode | varchar | 5 | 0 |  |  |  |
| IPAddress | int | 4 | 0 |  |  |  |
| LocationType | int | 4 | 0 |  |  |  |
| Country | int | 4 | 0 |  |  |  |
| CityName | varchar | 40 | 0 |  |  |  |
| EffectiveDate | datetime | 8 | 1 |  |  |  |
| EndDate | datetime | 8 | 1 |  |  |  |
