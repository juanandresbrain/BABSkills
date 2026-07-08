# dbo.aw_gl_interface_vw

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.aw_gl_interface_vw"]
    aw_gl_interface(["aw_gl_interface"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| aw_gl_interface |

## View Code

```sql
create view dbo.aw_gl_interface_vw  AS
SELECT
  record_type,
  journal_entry_description,
  detail_type_indicator,
  gl_account_no,
  amount,
  gl_period_no,
  period_ending_date,
  gl_company_no
FROM aw_gl_interface
```

