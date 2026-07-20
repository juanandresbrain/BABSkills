# dbo.retailsalestable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| retailorder | bigint | 8 | 1 |  |  |  |
| retailprepaymentoverridden | bigint | 8 | 1 |  |  |  |
| retailretailstatustype | bigint | 8 | 1 |  |  |  |
| gsttransactionidfrompos_in | bigint | 8 | 1 |  |  |  |
| retailcfdidocumenttype_mx | bigint | 8 | 1 |  |  |  |
| istaxexemptedforpriceinclusive | bigint | 8 | 1 |  |  |  |
| paymentstype | bigint | 8 | 1 |  |  |  |
| ispriceanddiscountrecalculationrequired | bigint | 8 | 1 |  |  |  |
| shoulduseunifiedpricingengineonsalesorder | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| channelreferenceid | varchar | 8000 | 1 |  |  |  |
| ominternalorganization | bigint | 8 | 1 |  |  |  |
| originaltransactiontime | datetime2 | 8 | 1 |  |  |  |
| retailchannel | bigint | 8 | 1 |  |  |  |
| retailhourofday | bigint | 8 | 1 |  |  |  |
| retailloyaltycard | bigint | 8 | 1 |  |  |  |
| retailreplenishmentlocationid | varchar | 8000 | 1 |  |  |  |
| retailstoreid | varchar | 8000 | 1 |  |  |  |
| retailterminalid | varchar | 8000 | 1 |  |  |  |
| salestable | bigint | 8 | 1 |  |  |  |
| totalmanualdiscountamount | decimal | 17 | 1 |  |  |  |
| totalmanualdiscountpercentage | decimal | 17 | 1 |  |  |  |
| taxoverridecode | varchar | 8000 | 1 |  |  |  |
| gsttransactionid_in | varchar | 8000 | 1 |  |  |  |
| statementid | varchar | 8000 | 1 |  |  |  |
| creditcardtypeid | varchar | 8000 | 1 |  |  |  |
| creditcardtendertypeid | varchar | 8000 | 1 |  |  |  |
| retailproductlistupdatename | varchar | 8000 | 1 |  |  |  |
| retailproductlistupdateid | varchar | 8000 | 1 |  |  |  |
| initialreceiptid | varchar | 8000 | 1 |  |  |  |
| originchannel | bigint | 8 | 1 |  |  |  |
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
