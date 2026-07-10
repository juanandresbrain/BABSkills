# dbo.tender_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| tender_key | int | 4 | 0 | YES |  | Surrogate key, IDENTITY column |
| tender_code | varchar | 5 | 0 |  |  | Natural key:  from table auditworks.dbo.line_object.line_object:  from view auditworks.dbo.vwDW_Tender_Dim |
| tender_desc | varchar | 50 | 1 |  |  | Tender name/description:  from table auditworks.line_object.line_object_description:  from view auditworks.dbo.vwDW_Tender_Dim |
| process_name | varchar | 50 | 1 |  |  | Audit column for the ETL package that last touched the data, may be elimintated with new ETL audit columns being added:  from SSIS.PackageName |
| process_date | datetime | 8 | 1 |  |  | Audit column for the time that the ETL last touched the data, may be elimintated with new ETL audit columns being added:  from SSIS.StartTime |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
