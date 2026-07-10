# dbo.NRST_PSTL_CD_STR_DIM

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| NRST_PSTL_CD_STR_ID | int | 4 | 0 | YES |  | The unique identifier of a Nearest Store record.  Calculation of a nearest store is based on postal code.  Distances for each store are calculated based on the postal code of the store and all postal codes closer to that store than any other. |
| CNTRY_ABBRV | varchar | 5 | 1 |  |  | The abbreviation for the country in which this postal code resides.  Most of these values are two character country codes, however, there are some that are three characters or more.  This is needed to distinguish between postal codes that are duplicated across countries.  For example, some of the postal codes in the US and France match. |
| PSTL_CD | varchar | 10 | 1 |  |  | A postal code for which the nearest store is being calculated.  Postal Codes are used by the postal service to group address together for mail routing and delivery.  In the United States, there is usually a relationship between a postal code and a post office.  Cities and Counties are grouped into Postal Codes, which are grouped into States/Provinces. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
| FUTR_STR_ID | int | 4 | 0 |  |  |  |
| STR_ID | int | 4 | 0 |  |  |  |
