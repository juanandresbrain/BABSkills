# dbo.ecommerce_nsbtranslate_logtrans

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| iAWTransID | int | 4 | 1 |  |  |  |
| sBatchID | varchar | 8000 | 1 |  |  |  |
| sOrderNumber | varchar | 8000 | 1 |  |  |  |
| dTimeStamp | datetime2 | 8 | 1 |  |  |  |
| mAmount | decimal | 9 | 1 |  |  |  |
| iUnits | int | 4 | 1 |  |  |  |
| sStore | varchar | 8000 | 1 |  |  |  |
| iStoreID | int | 4 | 1 |  |  |  |
| mCcAmount | decimal | 9 | 1 |  |  |  |
| mGcTenderAmount | decimal | 9 | 1 |  |  |  |
| mVoucherAmount | decimal | 9 | 1 |  |  |  |
| sSiteCode | varchar | 8000 | 1 |  |  |  |
| mGAAP | decimal | 9 | 1 |  |  |  |
