# dbo.currency_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| currency_key | int | 4 | 0 | YES |  | Surrogate key, IDENTITY column |
| currency_code | char | 3 | 1 |  |  | Natural key:  from table auditworks.dbo.CRNCY.CRNCY_CODE:  from view auditworks.dbo.vwDW_CURRENCY_DIM |
| currency_desc | varchar | 50 | 1 |  |  | Currnecy name/description:  from table auditworks.CRNCY.CRNCY_DESC:  from view auditworks.dbo.vwDW_CURRENCY_DIM |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
