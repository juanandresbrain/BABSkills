# dbo.transformedretailsalestransactions

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| transactionid | varchar | 8000 | 1 |  |  |  |
| store | varchar | 8000 | 1 |  |  |  |
| businessdate | date | 3 | 1 |  |  |  |
| currency | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| linenum | int | 4 | 1 |  |  |  |
| netamount | decimal | 17 | 1 |  |  |  |
| netprice | decimal | 17 | 1 |  |  |  |
| price | decimal | 17 | 1 |  |  |  |
| qty | decimal | 17 | 1 |  |  |  |
| taxamount | decimal | 17 | 1 |  |  |  |
| netamountincltax | decimal | 17 | 1 |  |  |  |
| costamount | decimal | 17 | 1 |  |  |  |
| discamount | decimal | 17 | 1 |  |  |  |
| discamountwithouttax | decimal | 17 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| subclass | varchar | 8000 | 1 |  |  |  |
| execution_timestamp | datetime2 | 8 | 1 |  |  |  |
