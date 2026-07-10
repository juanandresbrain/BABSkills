# dbo.store_dim

**Database:** dw  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| store_key | int | 4 | 0 | YES |  | Surrogate key, IDENTITY column |
| store_id | int | 4 | 1 |  |  | Natural Key:  from table oursmerchdb01.me01.dbo.location.location_code and KODIAK.Bearhouse.dbo.tblStore.iStoreID :  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| bearea | varchar | 100 | 1 |  |  | from table oursmerchdb01.me01.dbo.hierarchy_group.short_label:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| store_name | varchar | 255 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.location.location_name:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| store_name_abbrv | varchar | 100 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.location.location_short_name:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| bearritory | varchar | 100 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.hierarchy_group.short_label:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| address1 | varchar | 255 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.address.  when loaction_code=132, address_line2, else address_line1:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| region | varchar | 100 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.hierarchy_group.short_label:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| zone | varchar | 50 | 1 |  |  | :Always null.  Determine if this column can be dropped |
| address2 | varchar | 255 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.address.  from address_line1 or 2 depending on location_code:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| state_province_name | varchar | 255 | 1 |  |  | :  from lookup on tblState by Abrev=address.state_province |
| business_type | varchar | 50 | 1 |  |  | :Always null.  Consider dropping. |
| city | varchar | 50 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.address.address_city - using custom InitCap function:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| division | varchar | 50 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.hierarchy_group.short_label:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| state_province | varchar | 10 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.address.address_state:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| county | varchar | 50 | 1 |  |  | Always null.  Consider Dropping |
| business_unit | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| country | varchar | 50 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.country.country_code:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| country_name | varchar | 50 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.country.country_description - uses custom InitCap function:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| postal_code | varchar | 50 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.address.address_zip_code:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| phone | varchar | 100 | 1 |  |  | :  from table kodiak.bearhouse.dbo.tblStore.sPhone:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| fax | varchar | 255 | 1 |  |  | :  from table kodiak.bearhouse.dbo.tblStore.sFax:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| email | varchar | 255 | 1 |  |  | :  from table kodiak.bearhouse.dbo.tblStore.Email - cast as varchar(50):  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| opening_date | datetime | 8 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.location.  coalesce(reopen_date, open_date):  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| active | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| latitude | numeric | 9 | 1 |  |  | spStoreLoad_Update_Override |
| longitude | numeric | 9 | 1 |  |  | spStoreLoad_Update_Override |
| volume_group | varchar | 1 | 1 |  |  | :  from table kodiak.bearhouse.dbo.tblStore.iGroup - cast as varchar(1):  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| store_mgr | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| bearea_mgr | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| bearitory_mgr | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| region_mgr | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| store_type | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| closing_date | datetime | 8 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.location.closed_date - overridden with spStoreLoad_Update_Override:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| comp_date | datetime | 8 | 1 |  |  | :  from table oursmerchdb01.me01.dbo.location.comparative_date - overridden with spStoreLoad_Update_Override:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| store_group_id | int | 4 | 1 |  |  | Always null.  Consider dropping |
| address3 | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| address4 | varchar | 50 | 1 |  |  | Always null.  Consider dropping |
| square_feet | int | 4 | 1 |  |  | Always null.  Consider dropping |
| num_of_pos | int | 4 | 1 |  |  | Always null.  Consider dropping |
| num_of_kiosks | int | 4 | 1 |  |  | Always null.  Consider dropping |
| postal_plus4 | char | 4 | 1 |  |  | Always null.  Consider dropping |
| Abbreviation | varchar | 3 | 1 |  |  | 3 digit abbreviation.  Not sure where this is populated from |
| Legal_Description | varchar | 50 | 1 |  |  | :  from table kodiak.bearhouse.dbo.tblStore.sStoreName1:  from view oursmerchdb01.me_01.dbo.vwDW_Store_Dim |
| comp_week_id | int | 4 | 1 |  |  | Always null.  Consider dropping |
| bearea_id | int | 4 | 1 |  |  | Always null.  Consider dropping |
| bearitory_id | int | 4 | 1 |  |  | Always null.  Consider dropping |
| region_id | int | 4 | 1 |  |  | Always null.  Consider dropping |
| division_code | char | 5 | 1 |  |  | Always null.  Consider dropping |
| language | varchar | 20 | 1 |  |  | Always null.  Consider dropping |
| demographics_bg_key | varchar | 20 | 1 |  |  | Populated from spStoreLoad_Update_Override |
| INS_DT | datetime | 8 | 0 |  |  | The date on which this record was originally inserted into the table.  Upon intial insert, this date will be the same as the UPDT_DT. |
| UPDT_DT | datetime | 8 | 0 |  |  | The date on which this record was last updated by an ETL process in the Data Warehouse.  For the initial record insert, this will equal the iNS_DT.  For all other updates to the record, this will differ from the INS_DT. |
| ETL_LOG_ID | int | 4 | 0 |  |  | The unique identifier of an ETL Log record.  This is used to track the execution of an entire set of ETL jobs within a particular batch, including the date and time on which they executed. |
| ETL_EVNT_ID | int | 4 | 0 |  |  | The unique identifier of an ETL event.  This tracks, at the lowest level, the execution of a particular ETL job, including the date and time on which the ETL job was executed. |
