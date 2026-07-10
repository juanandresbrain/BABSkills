# dbo.CRM_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CRM_STG_ID | int | 4 | 0 |  |  | The unique identifier of a CRM Staging record.  This acts as the primary key on the Staging table for CRM data. |
| SRC_REC_CRTE_DT | datetime | 8 | 1 |  |  | The date on which the record was inserted into the source system.  This, along with the SRC_REC_UPDT_DT are used to extract newly inserted and updated records. |
| STR_NBR | varchar | 20 | 1 |  |  | The number identifying the store in which the guest was entered into the CRM system.  This should correspond to a valid record in the STR_DIM table. |
| CRM_GST_NBR | varchar | 20 | 1 |  |  | The number identifying the guest within the CRM source system.  This is the surrogate key associated with the guest within CRM. |
| CRM_LYLTY_NBR | varchar | 20 | 1 |  |  | The number associated with the guest as a Loyalty (Stuff For Stuff - SFS) member.  This is the number found on the SFS card used by the guest. |
| CRM_HSHLD_NBR | varchar | 20 | 1 |  |  | The number associated with the household to which this guest belongs.  This groups similar guest listed at the same address together into a single unit. |
| CRM_ADDR_NBR | int | 4 | 1 |  |  | The identifier of an address within the CRM system.  This can be used to trace a CRM_STG record back to the source system. |
| FRST_NM | varchar | 20 | 1 |  |  | The first name of the guest, as entered into the CRM system. |
| LAST_NM | varchar | 50 | 1 |  |  | The last name (surname) of the guest, as entered into the CRM system. |
| GNDR_CD | varchar | 5 | 1 |  |  | The gender of the guest.  This is typically entered into the kiosk at the time of animal registration, loaded into the Data Warehouse for that guest and then sent on to the CRM system via a data update from the Data Warehouse.  Valid values include Male (M), Female (F) and Unknown (U). |
| BRTH_DT | datetime | 8 | 1 |  |  | The date on which the CRM guest was born, as entered into the CRM system. |
| ADDR_LN_1_TXT | varchar | 60 | 1 |  |  | The first line of the address for the customer within the CRM system. |
| ADDR_LN_2_TXT | varchar | 60 | 1 |  |  | The second line of the address for the customer within the CRM system. |
| CTY_NM | varchar | 50 | 1 |  |  | The name of the city in which the guest resides, as entered into the CRM system. |
| ST_PRVNC_TXT | varchar | 50 | 1 |  |  | The name of the state or province in which the guest resides, as entered into the CRM system. |
| PSTL_CD | varchar | 20 | 1 |  |  | The postal code in which the guest address resides, as entered into the CRM system. |
| CNTRY_ABBRV | varchar | 5 | 1 |  |  | The abbreviation of the country in which the guest address resides, as entered into the CRM system. |
| PHN_NBR | varchar | 20 | 1 |  |  | The phone number of the guest, as entered into the CRM system.  Phone numbers are only collected within the CRM system.  Therefore, a guest record entered only from the Kiosk will have a blank value in this field, unless it has been updated by a corresponding record from the CRM system. |
| PHN_EXTNS_NBR | varchar | 20 | 1 |  |  | The extension on the phone number of the guest, as entered into the CRM system.  Very few records have a value in this field. |
| EMAIL_ADDR_TXT | varchar | 100 | 1 |  |  | email address values - one in CRM and one on a kiosk record, the CRM value should be the one stored on the guest record within the Data Warehouse. |
| SND_MAIL_CD | varchar | 5 | 1 |  |  | The code identifying whether or not the guest living at a particular address wishes to receive mailings from Build-A-Bear.  This is the mailing opt-in. |
| SND_EMAIL_CD | varchar | 5 | 1 |  |  | The code identifying whether or not the guest using a particular email address wishes to receive emails from Build-A-Bear.  This is the email opt-in. |
| EMAIL_OPT_IN_CD | varchar | 5 | 1 |  |  | A second code identifying whether the guest wishes to receive email from Build-A-Bear.  This field, along with another field are used together to identify whether or not email can be sent to guest. |
| LANG_CD | varchar | 5 | 1 |  |  | The code identifying the language in which the guest communicates. |
| SRC_REC_UPDT_DT | datetime | 8 | 1 |  |  | The date on which this CRM guest record was updated within the CRM system. |
| CRM_MBRSHP_DT | datetime | 8 | 1 |  |  | The date on which the guest joined the CRM program.  This is used, among other things, to determine whether or not the guest can be opted out of email communications. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| GST_CHKSUM | int | 4 | 1 |  |  |  |
| ADDR_CHKSUM | int | 4 | 1 |  |  |  |
| MAIL_OPT_IN_CD | varchar | 5 | 1 |  |  | A second code identifying whether the guest wishes to receive mail from Build-A-Bear.  This field, along with another field are used together to identify whether or not mail can be sent to guest. |
| MOBILE_TXT_NBR | varchar | 20 | 1 |  |  |  |
| MOBILE_TXT_STAT_CD | varchar | 5 | 1 |  |  |  |
| MOBILE_UPDT_DT | datetime | 8 | 1 |  |  |  |
| MAIL_UPDT_DT | datetime | 8 | 1 |  |  |  |
| EMAIL_UPDT_DT | datetime | 8 | 1 |  |  |  |
| DM_ATTR_STAT_CD | varchar | 1 | 1 |  |  |  |
| EMAIL_ATTR_STAT_CD | varchar | 1 | 1 |  |  |  |
| EMAILCERT_STAT_CD | varchar | 1 | 1 |  |  |  |
| EMAILCERT_UPDT_DT | datetime | 8 | 1 |  |  |  |
| SFSPOINTS_STAT_CD | varchar | 1 | 1 |  |  |  |
| SFSPOINTS_UPDT_DT | datetime | 8 | 1 |  |  |  |
