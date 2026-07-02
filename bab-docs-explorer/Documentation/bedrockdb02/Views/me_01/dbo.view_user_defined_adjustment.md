# dbo.view_user_defined_adjustment

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_user_defined_adjustment"]
    dbo_user_defined_adjustment(["dbo.user_defined_adjustment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.user_defined_adjustment |

## View Code

```sql
create view dbo.view_user_defined_adjustment 
         (doc_type,
          doc_no,
          create_date,
          status,
          doc_id,
          grouping_label,
          transaction_reason_id,
          performed_by)
AS
   SELECT N'User-defined adjustment',
          document_no,
	  convert(smalldatetime,convert(char(12),create_date,109)),
          document_status,
          user_defined_adjustment_id,
          grouping_label,
          transaction_reason_id,
          performed_by
     FROM dbo.user_defined_adjustment
```

