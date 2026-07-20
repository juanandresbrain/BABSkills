# dbo.giftcard_header

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_header"]
    dbo_giftcard_header(["dbo.giftcard_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_header |

## View Code

```sql
; CREATE   VIEW [dbo].[giftcard_header] AS     SELECT [FileID], [file_name] COLLATE Latin1_General_CI_AS AS [file_name], [dw_processed_date], [version] COLLATE Latin1_General_CI_AS AS [version], [processed_date], [period_start_date], [period_end_date], [file_number], [number_of_files], [file_data_type] COLLATE Latin1_General_CI_AS AS [file_data_type], [record_length], [sequence_number], [prev_sequence_number], [rows_found], [rows_expected], [footer_found], [InsertDate], [UpdateDate]     FROM [dbo].[giftcard_header]
```

