# dbo.LOAD_REC_ID_CNTRL

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STG_ID | int | 4 | 0 |  |  | The identifier of the record in the CRM_STG or KSK_REGIS_STG table.  The STG_DTA_SET_CD field should be used in order to determine whether this represents a record from the CRM_STG table or the KSK_REGIS_STG table.  If this is from the CRM_STG table, the STG_DTA_SET_CD will be set to CRM.  If this is from the KSK_REGIS_STG table, the STG_DTA_SET_CD will be set to Kiosk.  This STG_ID is used to tie together all of the identifiers associated with a particular staging record so that it is easier to process records during the loads into the Data Warehouse. |
| STG_DTA_SET_CD | varchar | 20 | 0 |  |  | This field identifies from which staging table this record is sourced.  If this record comes from the CRM_STG table, this will be set to CRM.  If this record comes from the KSK_REGSI_STG Table, this will be set to Kiosk.  This is needed in order to help uniquely identify records in the table, since it is possible that each staging table may contain the same unique identifier (CRM_STG_ID and KSK_REGIS_STG_ID). |
| RAW_GST_ID | int | 4 | 0 |  |  |  |
| RAW_RCPNT_ID | int | 4 | 0 |  |  |  |
| DT_ID | int | 4 | 1 |  |  |  |
| TM_ID | int | 4 | 1 |  |  |  |
| PRDCT_ID | int | 4 | 1 |  |  |  |
| STR_ID | int | 4 | 1 |  |  |  |
| TRN_KSK_CNTXT_ID | int | 4 | 1 |  |  |  |
| TKF_ID | int | 4 | 1 |  |  |  |
| INS_DT | datetime | 8 | 1 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| ETL_LOG_ID | int | 4 | 1 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 1 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| NRST_STR_ID | int | 4 | 1 |  |  |  |
| EMAIL_ADDR_ID | int | 4 | 1 |  |  |  |
| TOR_CLNSD_ADDR_ID | int | 4 | 1 |  |  |  |
| CLNSD_GST_ID | int | 4 | 0 |  |  |  |
| CLNSD_ADDR_ID | int | 4 | 0 |  |  |  |
| RAW_ADDR_ID | int | 4 | 0 |  |  |  |
| MOBILE_TXT_ID | int | 4 | 1 |  |  |  |
