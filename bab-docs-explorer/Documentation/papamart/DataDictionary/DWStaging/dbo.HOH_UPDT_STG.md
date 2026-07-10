# dbo.HOH_UPDT_STG

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| CLNSD_ADDR_ID | int | 4 | 0 |  |  |  |
| HOH_LYLTY_GST_NBR | varchar | 20 | 1 |  |  | This is the Loyalty Number (populated from the Customer_No field in the CRM source system) assigned to a Stuff for Stuff (SFS) Customer within the CRM source system for the head of household in which this guest resides.  This is equivalent to the number on the Rewards card that the Stuff for Stuff member uses when making purchases from Build-A-Bear for that head of household.  If this is the Head of Household record, this should be blank. |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
