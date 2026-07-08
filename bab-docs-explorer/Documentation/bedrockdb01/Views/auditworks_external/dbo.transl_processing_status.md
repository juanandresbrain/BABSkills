# dbo.transl_processing_status

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transl_processing_status"]
    dbo_ext_processing_status(["dbo.ext_processing_status"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ext_processing_status |

## View Code

```sql
CREATE VIEW dbo.transl_processing_status AS
   SELECT input_id,
          process_start_datetime,
          process_no,
          processing_message 
     FROM auditworks_work.dbo.ext_processing_status
```

