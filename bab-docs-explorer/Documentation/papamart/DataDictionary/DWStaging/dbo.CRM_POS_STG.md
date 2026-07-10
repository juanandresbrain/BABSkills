# dbo.CRM_POS_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRM_POS_STG_ID | int | 4 | 0 | YES |  | The unique identifier of a record within the CRM POS Staging table.  This is a surrogate key for the records in this table and will uniquely identify a record with the Staging environment.  It is not, however, connected to a record within the source system. |
| CRM_GST_NBR | varchar | 20 | 1 |  |  | The number identifying the guest within the CRM source system.  This is the surrogate key associated with the guest within CRM.  It can be used to match up guests with their transactions from the Point-of_Sale (POS) system. |
| STR_NBR | int | 4 | 1 |  |  | The unique identifier, in the source system, of the store in which this POS transaction took place.  This will also act as the natural key for the STORE_DIM table. |
| POS_TRN_DT | datetime | 8 | 1 |  |  | The date and time at which the POS transaction occurred.  This is the timestamp of the transaction set by the register. |
| POS_TRN_NBR | varchar | 20 | 1 |  |  | The number associated with this POS transaction within the source system.  This can be used as a natural key for the transaction when interacting with the source data. |
| SRC_TRN_REC_ID | int | 4 | 1 |  |  | The unique identifier of a transaction record within the source system.  This is the primary key for the source Transaction_Header table. |
| RGSTR_NBR | varchar | 20 | 1 |  |  | The number representing the register on which this POS transaction took place.  This is the number assigned to the register within the store.  The register numbers are not unique across stores.  In fact, they typically start at 1 and go up sequentially from there.  Therefore, it is likely that they will be duplicated across stores. |
| POS_TRN_PSTD_DT | datetime | 8 | 1 |  |  | The date of the day on which this POS Transaction was posted in the source system.  This is used when extracting data from the source system to make sure that only those records posted since the last run are extracted. |
| CRM_LYLTY_NBR | varchar | 20 | 1 |  |  | The number associated with the guest as a Loyalty (Stuff For Stuff - SFS) member.  This is the number found on the SFS card used by the guest. |
| CRM_MBRSHP_DT | datetime | 8 | 1 |  |  | The date on which the guest joined the CRM program.  This is used, among other things, to determine whether or not the guest can be opted out of email communications. |
| SFS_TRN_TYP_CD | varchar | 5 | 1 |  |  | The code identifying the type of Stuff for Stuff Transaction that this POS transaction represents.  Valid values include 1 (a POS transaction within the first 90 days of the guests membership in the SFS program) and 2 (a POS transaction beyond the first 90 days of the guests membership in the SFS program). |
| SLS_MDULE_TRN_NBR | varchar | 20 | 1 |  |  | The number representing the Sales Module Transaction. |
| TTL_NET_RTL_AMT | decimal | 9 | 1 |  |  | The total retail amount of this POS transaction.  The retail amount includes the net amount received by Build-A-Bear for this retail POS transaction, excluding the costs associated with the acquisition of the products on the transaction. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the INS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
