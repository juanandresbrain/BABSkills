# dbo.line_object_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| Line_Object_Key | int | 4 | 0 | YES |  | Surrogate key, IDENTITY column |
| Line_Object | int | 4 | 1 |  |  | Natural key:  from table auditworks.dbo.line_object.line_object:  from view auditworks.dbo.vwDW_LINE_OBJECT_Dim |
| Line_Object_Type | int | 4 | 1 |  |  |  |
| Line_Object_Description | varchar | 50 | 1 |  |  | LINE_OBJECT name/description:  from table auditworks.line_object.line_object_description:  from view auditworks.dbo.vwDW_LINE_OBJECT_Dim |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
