# dbo.giftcard_header_international

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_header_international"]
    dbo_giftcard_header_international(["dbo.giftcard_header_international"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_header_international |

## View Code

```sql
;

CREATE VIEW dbo.giftcard_header_international AS SELECT FileID, GroupCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS GroupCode, file_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS file_name, dw_processed_date, version COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS version, processed_date, period_start_date, period_end_date, file_number, number_of_files, file_data_type COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS file_data_type, record_length, sequence_number, prev_sequence_number, rows_found, rows_expected, footer_found, InsertDate, UpdateDate FROM LH_Mart.dbo.giftcard_header_international;;
```

