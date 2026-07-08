# dbo.dw_input_line_note

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dw_input_line_note"]
    dbo_input_line_note(["dbo.input_line_note"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.input_line_note |

## View Code

```sql
CREATE VIEW dbo.dw_input_line_note AS
SELECT input_id,
       store_no,
       register_no,
       entry_date_time,
       transaction_series,
       transaction_no,
       line_id,
       note_type,
       line_note,
       lookup_pos_code,
       pos_description,
       row_sequence_no FROM dbo.input_line_note
```

