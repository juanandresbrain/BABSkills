# dbo.retailtransactionpaymenttranshistory

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| changeline | bigint | 8 | 1 |  |  |  |
| isprepayment | bigint | 8 | 1 |  |  |  |
| managerkeylive | bigint | 8 | 1 |  |  |  |
| replicated | bigint | 8 | 1 |  |  |  |
| transactionstatus | bigint | 8 | 1 |  |  |  |
| iscapturefailed | bigint | 8 | 1 |  |  |  |
| ispaymentcaptured | bigint | 8 | 1 |  |  |  |
| voidstatus | bigint | 8 | 1 |  |  |  |
| creditcardprocessorstatus | bigint | 8 | 1 |  |  |  |
| iscustomeraccountfloorlimitused | bigint | 8 | 1 |  |  |  |
| islinkedrefund | bigint | 8 | 1 |  |  |  |
| ispaymentdataarchived | bigint | 8 | 1 |  |  |  |
| ispaymentdatacompressed | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| amountcur | decimal | 17 | 1 |  |  |  |
| amountmst | decimal | 17 | 1 |  |  |  |
| amounttendered | decimal | 17 | 1 |  |  |  |
| authenticationcode | varchar | 8000 | 1 |  |  |  |
| businessdate | datetime2 | 8 | 1 |  |  |  |
| cardoraccount | varchar | 8000 | 1 |  |  |  |
| cardtypeid | varchar | 8000 | 1 |  |  |  |
| cashdocid_ru | varchar | 8000 | 1 |  |  |  |
| channel | bigint | 8 | 1 |  |  |  |
| counter | bigint | 8 | 1 |  |  |  |
| creditvoucherid | varchar | 8000 | 1 |  |  |  |
| currency | varchar | 8000 | 1 |  |  |  |
| defaultdimension | bigint | 8 | 1 |  |  |  |
| exchrate | decimal | 17 | 1 |  |  |  |
| exchratemst | decimal | 17 | 1 |  |  |  |
| giftcardid | varchar | 8000 | 1 |  |  |  |
| linenum | decimal | 17 | 1 |  |  |  |
| loyaltycardid | varchar | 8000 | 1 |  |  |  |
| messagenum | bigint | 8 | 1 |  |  |  |
| origin | varchar | 8000 | 1 |  |  |  |
| paymentauthorization | varchar | 8000 | 1 |  |  |  |
| qty | decimal | 17 | 1 |  |  |  |
| receiptid | varchar | 8000 | 1 |  |  |  |
| replicationcounterfromorigin | bigint | 8 | 1 |  |  |  |
| shift | varchar | 8000 | 1 |  |  |  |
| shiftdate | datetime2 | 8 | 1 |  |  |  |
| sigcapdata | varchar | 8000 | 1 |  |  |  |
| staff | varchar | 8000 | 1 |  |  |  |
| statementcode | varchar | 8000 | 1 |  |  |  |
| statementid | varchar | 8000 | 1 |  |  |  |
| store | varchar | 8000 | 1 |  |  |  |
| tendertype | varchar | 8000 | 1 |  |  |  |
| terminal | varchar | 8000 | 1 |  |  |  |
| transactionid | varchar | 8000 | 1 |  |  |  |
| transdate | datetime2 | 8 | 1 |  |  |  |
| transtime | bigint | 8 | 1 |  |  |  |
| paymentcardtoken | varchar | 8000 | 1 |  |  |  |
| authorizedamount | decimal | 17 | 1 |  |  |  |
| paymentrefrecid | bigint | 8 | 1 |  |  |  |
| cardpaymentaccountid | varchar | 8000 | 1 |  |  |  |
| linkedpaymentstore | varchar | 8000 | 1 |  |  |  |
| linkedpaymentterminalid | varchar | 8000 | 1 |  |  |  |
| linkedpaymenttransactionid | varchar | 8000 | 1 |  |  |  |
| linkedpaymentlinenumber | decimal | 17 | 1 |  |  |  |
| linkedpaymentcurrency | varchar | 8000 | 1 |  |  |  |
| refundableamount | decimal | 17 | 1 |  |  |  |
| paymentcapturetoken | varchar | 8000 | 1 |  |  |  |
| linkedpaymentrefrecid | bigint | 8 | 1 |  |  |  |
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
