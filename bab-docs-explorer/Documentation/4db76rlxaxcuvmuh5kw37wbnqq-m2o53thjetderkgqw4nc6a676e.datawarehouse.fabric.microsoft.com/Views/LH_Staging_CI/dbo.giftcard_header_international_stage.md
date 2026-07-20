# dbo.giftcard_header_international_stage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_header_international_stage"]
    dbo_giftcard_header_international_stage(["dbo.giftcard_header_international_stage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_header_international_stage |

## View Code

```sql
;
CREATE   VIEW [dbo].[giftcard_header_international_stage]
AS
    SELECT [GroupCode] COLLATE Latin1_General_CI_AS AS [GroupCode], [file_name] COLLATE Latin1_General_CI_AS AS [file_name], [dw_processed_date], [version] COLLATE Latin1_General_CI_AS AS [version], [processed_date], [period_start_date], [period_end_date], [file_number], [number_of_files], [file_data_type] COLLATE Latin1_General_CI_AS AS [file_data_type], [record_length], [sequence_number], [prev_sequence_number], [rows_found], [rows_expected], [footer_found]
    FROM LH_Staging.[dbo].[giftcard_header_international_stage]
```

