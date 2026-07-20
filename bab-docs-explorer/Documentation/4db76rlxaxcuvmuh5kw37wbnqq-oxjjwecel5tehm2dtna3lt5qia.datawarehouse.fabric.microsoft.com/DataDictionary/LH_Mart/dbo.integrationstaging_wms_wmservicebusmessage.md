# dbo.integrationstaging_wms_wmservicebusmessage

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ServiceBusMessageId | bigint | 8 | 1 |  |  |  |
| MessageId | varchar | 8000 | 1 |  |  |  |
| Message | varchar | 8000 | 1 |  |  |  |
| Sequence | bigint | 8 | 1 |  |  |  |
| MessageTypeId | int | 4 | 1 |  |  |  |
| EnqueuedTimeUTC | datetime2 | 8 | 1 |  |  |  |
