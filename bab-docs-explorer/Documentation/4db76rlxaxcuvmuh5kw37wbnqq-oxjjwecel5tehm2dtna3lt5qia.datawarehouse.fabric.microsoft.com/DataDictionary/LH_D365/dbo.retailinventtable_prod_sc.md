# dbo.retailinventtable_prod_sc

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Id | varchar | 8000 | 1 |  |  |  |
| SinkCreatedOn | datetime2 | 8 | 1 |  |  |  |
| SinkModifiedOn | datetime2 | 8 | 1 |  |  |  |
| blockedonpos | bigint | 8 | 1 |  |  |  |
| blockedonselfcheckout | bigint | 8 | 1 |  |  |  |
| keyinginprice | bigint | 8 | 1 |  |  |  |
| keyinginqty | bigint | 8 | 1 |  |  |  |
| mustkeyincomment | bigint | 8 | 1 |  |  |  |
| nodiscountallowed | bigint | 8 | 1 |  |  |  |
| printvariantsshelflabels | bigint | 8 | 1 |  |  |  |
| prohibitreturn_ru | bigint | 8 | 1 |  |  |  |
| qtybecomesnegative | bigint | 8 | 1 |  |  |  |
| scaleitem | bigint | 8 | 1 |  |  |  |
| useeanstandardbarcode | bigint | 8 | 1 |  |  |  |
| zeropricevalid | bigint | 8 | 1 |  |  |  |
| nomanualdiscountallowed | bigint | 8 | 1 |  |  |  |
| noperiodicdiscountallowed | bigint | 8 | 1 |  |  |  |
| notenderdiscountsallowed | bigint | 8 | 1 |  |  |  |
| sysdatastatecode | bigint | 8 | 1 |  |  |  |
| barcodesetupid | varchar | 8000 | 1 |  |  |  |
| basecomparisonunitcode | varchar | 8000 | 1 |  |  |  |
| dateblocked | datetime2 | 8 | 1 |  |  |  |
| datetoactivateitem | datetime2 | 8 | 1 |  |  |  |
| datetobeblocked | datetime2 | 8 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| lifefrom | datetime2 | 8 | 1 |  |  |  |
| lifeto | datetime2 | 8 | 1 |  |  |  |
| seasoncode | varchar | 8000 | 1 |  |  |  |
| labelattribute1 | bigint | 8 | 1 |  |  |  |
| labelattribute2 | bigint | 8 | 1 |  |  |  |
| labelattribute3 | bigint | 8 | 1 |  |  |  |
| labelattribute4 | bigint | 8 | 1 |  |  |  |
| labelattribute5 | bigint | 8 | 1 |  |  |  |
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
