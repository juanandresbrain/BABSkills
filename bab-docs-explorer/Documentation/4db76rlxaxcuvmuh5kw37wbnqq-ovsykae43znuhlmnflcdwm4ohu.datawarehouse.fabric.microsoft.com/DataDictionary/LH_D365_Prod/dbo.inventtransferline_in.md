# dbo.inventtransferline_in

**Database:** LH_D365_Prod  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| pricetype | bigint | 8 | 1 |  |  |  |
| vatpricetype | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| inventtransferline | bigint | 8 | 1 |  |  |  |
| currencycode | varchar | 8000 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| invntcostprice | decimal | 17 | 1 |  |  |  |
| netamount | decimal | 17 | 1 |  |  |  |
| taxgroup | varchar | 8000 | 1 |  |  |  |
| taxitemgroup | varchar | 8000 | 1 |  |  |  |
| unitid | varchar | 8000 | 1 |  |  |  |
| unitprice | decimal | 17 | 1 |  |  |  |
| vatretentioncode | varchar | 8000 | 1 |  |  |  |
| retention | decimal | 17 | 1 |  |  |  |
| assessablevaluetransactioncurrency | decimal | 17 | 1 |  |  |  |
| maximumretailprice | decimal | 17 | 1 |  |  |  |
| fromtaxinformation | bigint | 8 | 1 |  |  |  |
| totaxinformation | bigint | 8 | 1 |  |  |  |
| assessablevalue | decimal | 17 | 1 |  |  |  |
| companylocation | bigint | 8 | 1 |  |  |  |
| inventcostpricecalculated | decimal | 17 | 1 |  |  |  |
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
