# dbo.LineObj_Store_Lookup

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| STS_line_object | int | 4 | 0 |  |  | from auditworks.line_object.line_object. |
| StoreNo | int | 4 | 0 |  |  | from auditworks.line_object.line_object_description.  Uses substring after "#" if present, if not, use 0 |
| Beehive_line_object | int | 4 | 0 |  |  | from auditworks.line_object.line_object.  ETL populates this with same value as STS_line_object, although 15 rows in prod are not = STS_line_object somehow. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
