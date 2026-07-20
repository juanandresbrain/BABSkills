# dbo.discountmstr_discountresults

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| recID | int | 4 | 1 |  |  |  |
| ChannelYearID | int | 4 | 1 |  |  |  |
| budgetMonthID | int | 4 | 1 |  |  |  |
| countryID | int | 4 | 1 |  |  |  |
| discountID | int | 4 | 1 |  |  |  |
| categoryTypeID | int | 4 | 1 |  |  |  |
| isExpired | bit | 1 | 1 |  |  |  |
| resultTypeID | int | 4 | 1 |  |  |  |
| numRedemptions | int | 4 | 1 |  |  |  |
| amtRedemptions | decimal | 9 | 1 |  |  |  |
| numGAAPTransactions | int | 4 | 1 |  |  |  |
| amtGAAPSales | decimal | 9 | 1 |  |  |  |
