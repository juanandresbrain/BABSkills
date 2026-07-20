# dbo.retailstatementtrans

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| addedtodrawer | decimal | 17 | 1 |  |  |  |
| bankedamount | decimal | 17 | 1 |  |  |  |
| bankedamountmst | decimal | 17 | 1 |  |  |  |
| bankedamountstore | decimal | 17 | 1 |  |  |  |
| cardfeeamount | decimal | 17 | 1 |  |  |  |
| cardtypeid | varchar | 8000 | 1 |  |  |  |
| cashlaterreturnedamountcur_ru | decimal | 17 | 1 |  |  |  |
| changetender | decimal | 17 | 1 |  |  |  |
| countedamount | decimal | 17 | 1 |  |  |  |
| countedamountmst | decimal | 17 | 1 |  |  |  |
| countedamountstore | decimal | 17 | 1 |  |  |  |
| currency | varchar | 8000 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| differenceamount | decimal | 17 | 1 |  |  |  |
| differenceamountmst | decimal | 17 | 1 |  |  |  |
| differenceamountstore | decimal | 17 | 1 |  |  |  |
| indraweratendofday | decimal | 17 | 1 |  |  |  |
| linenum | decimal | 17 | 1 |  |  |  |
| orderinvoiceamount | decimal | 17 | 1 |  |  |  |
| orderinvoiceamountmst | decimal | 17 | 1 |  |  |  |
| posteddate | datetime2 | 8 | 1 |  |  |  |
| realexchrate | decimal | 17 | 1 |  |  |  |
| removedfromdrawer | decimal | 17 | 1 |  |  |  |
| replicationcounter | bigint | 8 | 1 |  |  |  |
| safeamount | decimal | 17 | 1 |  |  |  |
| safeamountmst | decimal | 17 | 1 |  |  |  |
| safeamountstore | decimal | 17 | 1 |  |  |  |
| staffid | varchar | 8000 | 1 |  |  |  |
| statementcode | varchar | 8000 | 1 |  |  |  |
| statementid | varchar | 8000 | 1 |  |  |  |
| storeexchrate | decimal | 17 | 1 |  |  |  |
| storeid | varchar | 8000 | 1 |  |  |  |
| tendertypeid | varchar | 8000 | 1 |  |  |  |
| terminalid | varchar | 8000 | 1 |  |  |  |
| transamount | decimal | 17 | 1 |  |  |  |
| transamountinmst | decimal | 17 | 1 |  |  |  |
| transamountstore | decimal | 17 | 1 |  |  |  |
| uniqueshiftid | varchar | 8000 | 1 |  |  |  |
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
