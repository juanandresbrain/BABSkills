# dbo.retailstatementtable

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| closingmethod | bigint | 8 | 1 |  |  |  |
| debugmode | bigint | 8 | 1 |  |  |  |
| recalculate | bigint | 8 | 1 |  |  |  |
| skipconfirmation | bigint | 8 | 1 |  |  |  |
| statementmethod | bigint | 8 | 1 |  |  |  |
| postingstatus | bigint | 8 | 1 |  |  |  |
| postingerrorcode | bigint | 8 | 1 |  |  |  |
| postingerrorstatus | bigint | 8 | 1 |  |  |  |
| eodcodeversion | bigint | 8 | 1 |  |  |  |
| paymentstatus | bigint | 8 | 1 |  |  |  |
| ignorereturnlink | bigint | 8 | 1 |  |  |  |
| statementtype | bigint | 8 | 1 |  |  |  |
| aggregatebeforeposting | bigint | 8 | 1 |  |  |  |
| creationversionindicator | bigint | 8 | 1 |  |  |  |
| startamountcalculation | bigint | 8 | 1 |  |  |  |
| onestatementperday | bigint | 8 | 1 |  |  |  |
| bankdropcalculation | bigint | 8 | 1 |  |  |  |
| tenderdeclarationcalculation | bigint | 8 | 1 |  |  |  |
| disablecountingrequired | bigint | 8 | 1 |  |  |  |
| reserveinventoryduringstatementcalculation | bigint | 8 | 1 |  |  |  |
| skipaggregationforreturns | bigint | 8 | 1 |  |  |  |
| updategsttransactionid_in | bigint | 8 | 1 |  |  |  |
| disabletransactionconsistencychecker | bigint | 8 | 1 |  |  |  |
| recalculatedimensionsonpostingerror | bigint | 8 | 1 |  |  |  |
| autosettle | bigint | 8 | 1 |  |  |  |
| processgiftcardsasprepayments_ru | bigint | 8 | 1 |  |  |  |
| taxongiftcards | bigint | 8 | 1 |  |  |  |
| usefinancialdimensionfromreturnstore | bigint | 8 | 1 |  |  |  |
| stmtautosettlecustomerdeposit | bigint | 8 | 1 |  |  |  |
| usechannelcashmanagementreconciliation | bigint | 8 | 1 |  |  |  |
| enableparallelpaymentpostingforsales | bigint | 8 | 1 |  |  |  |
| prioritizedimensionsfrompaymentmethod | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| calculateddate | datetime2 | 8 | 1 |  |  |  |
| calculatedlines | bigint | 8 | 1 |  |  |  |
| calculatedtime | bigint | 8 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| posteddate | datetime2 | 8 | 1 |  |  |  |
| postedtime | bigint | 8 | 1 |  |  |  |
| postingdate | datetime2 | 8 | 1 |  |  |  |
| replicationcounter | bigint | 8 | 1 |  |  |  |
| shiftdate | datetime2 | 8 | 1 |  |  |  |
| shiftid | varchar | 8000 | 1 |  |  |  |
| stafforterminal | varchar | 8000 | 1 |  |  |  |
| statementdate | datetime2 | 8 | 1 |  |  |  |
| statementid | varchar | 8000 | 1 |  |  |  |
| storeid | varchar | 8000 | 1 |  |  |  |
| transfromdate | datetime2 | 8 | 1 |  |  |  |
| transfromtime | bigint | 8 | 1 |  |  |  |
| transtodate | datetime2 | 8 | 1 |  |  |  |
| transtotime | bigint | 8 | 1 |  |  |  |
| postingerrormessage | varchar | 8000 | 1 |  |  |  |
| postingbatchjobid | bigint | 8 | 1 |  |  |  |
| stmtcalcbatchendtime | bigint | 8 | 1 |  |  |  |
| maxnumberofthreadscustomerorder | bigint | 8 | 1 |  |  |  |
| offerledgerdimension | bigint | 8 | 1 |  |  |  |
| mixmatchledgerdimension | bigint | 8 | 1 |  |  |  |
| multibuyledgerdimension | bigint | 8 | 1 |  |  |  |
| thresholdledgerdimension | bigint | 8 | 1 |  |  |  |
| prepaymentledgerdimension | bigint | 8 | 1 |  |  |  |
| prepaymentledgerjournalname | varchar | 8000 | 1 |  |  |  |
| giftcarditem | varchar | 8000 | 1 |  |  |  |
| aggregatedtransactionsbundlesize | bigint | 8 | 1 |  |  |  |
| lastattempttoclear | datetime2 | 8 | 1 |  |  |  |
| calculateddatetime | datetime2 | 8 | 1 |  |  |  |
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
