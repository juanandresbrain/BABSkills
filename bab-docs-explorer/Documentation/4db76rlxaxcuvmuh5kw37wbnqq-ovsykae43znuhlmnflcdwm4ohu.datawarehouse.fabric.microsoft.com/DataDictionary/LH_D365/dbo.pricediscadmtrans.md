# dbo.pricediscadmtrans

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| accountcode | bigint | 8 | 1 |  |  |  |
| allocatemarkup | bigint | 8 | 1 |  |  |  |
| calendardays | bigint | 8 | 1 |  |  |  |
| differentfromposted | bigint | 8 | 1 |  |  |  |
| disregardleadtime | bigint | 8 | 1 |  |  |  |
| genericcurrency | bigint | 8 | 1 |  |  |  |
| itemcode | bigint | 8 | 1 |  |  |  |
| module | bigint | 8 | 1 |  |  |  |
| mustbedeleted | bigint | 8 | 1 |  |  |  |
| relation | bigint | 8 | 1 |  |  |  |
| searchagain | bigint | 8 | 1 |  |  |  |
| priceapplyadjustment | bigint | 8 | 1 |  |  |  |
| unitappliestoall | bigint | 8 | 1 |  |  |  |
| pricingattributesheaderarematched | bigint | 8 | 1 |  |  |  |
| pricingattributeslinearematched | bigint | 8 | 1 |  |  |  |
| isguptradeagreement | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| accountrelation | varchar | 8000 | 1 |  |  |  |
| agreement | varchar | 8000 | 1 |  |  |  |
| agreementheaderext_ru | bigint | 8 | 1 |  |  |  |
| amount | decimal | 17 | 1 |  |  |  |
| currency | varchar | 8000 | 1 |  |  |  |
| deliverytime | bigint | 8 | 1 |  |  |  |
| fromdate | datetime2 | 8 | 1 |  |  |  |
| inventbaileefreedays_ru | bigint | 8 | 1 |  |  |  |
| inventdimid | varchar | 8000 | 1 |  |  |  |
| itemrelation | varchar | 8000 | 1 |  |  |  |
| journalnum | varchar | 8000 | 1 |  |  |  |
| linenum | decimal | 17 | 1 |  |  |  |
| log | varchar | 8000 | 1 |  |  |  |
| markup | decimal | 17 | 1 |  |  |  |
| maximumretailprice_in | decimal | 17 | 1 |  |  |  |
| pdscalculationid | varchar | 8000 | 1 |  |  |  |
| percent1 | decimal | 17 | 1 |  |  |  |
| percent2 | decimal | 17 | 1 |  |  |  |
| pricedisctableref | bigint | 8 | 1 |  |  |  |
| priceunit | decimal | 17 | 1 |  |  |  |
| quantityamountfrom | decimal | 17 | 1 |  |  |  |
| quantityamountto | decimal | 17 | 1 |  |  |  |
| todate | datetime2 | 8 | 1 |  |  |  |
| unitid | varchar | 8000 | 1 |  |  |  |
| subbillflattierprice | decimal | 17 | 1 |  |  |  |
| pricingruleheader | bigint | 8 | 1 |  |  |  |
| pricingruleline | bigint | 8 | 1 |  |  |  |
| pricecomponentcombination | bigint | 8 | 1 |  |  |  |
| pricegroup | varchar | 8000 | 1 |  |  |  |
| modifieddatetime | datetime2 | 8 | 1 |  |  |  |
| modifiedby | varchar | 8000 | 1 |  |  |  |
| modifiedtransactionid | bigint | 8 | 1 |  |  |  |
| createddatetime | datetime2 | 8 | 1 |  |  |  |
| createdby | varchar | 8000 | 1 |  |  |  |
| createdtransactionid | bigint | 8 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| recversion | bigint | 8 | 1 |  |  |  |
| partition | bigint | 8 | 1 |  |  |  |
| sysrowversion | bigint | 8 | 1 |  |  |  |
| recid | bigint | 8 | 1 |  |  |  |
| tableid | bigint | 8 | 1 |  |  |  |
| versionnumber | bigint | 8 | 1 |  |  |  |
| createdon | datetime2 | 8 | 1 |  |  |  |
| modifiedon | datetime2 | 8 | 1 |  |  |  |
| IsDelete | bit | 1 | 1 |  |  |  |
| createdonpartition | varchar | 8000 | 1 |  |  |  |
| PartitionId | varchar | 2048 | 1 |  |  |  |
| pricepreventdiscount | bigint | 8 | 1 |  |  |  |
