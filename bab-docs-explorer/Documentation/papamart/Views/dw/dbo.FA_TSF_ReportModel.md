# dbo.FA_TSF_ReportModel

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.FA_TSF_ReportModel"]
    transaction_summary_facts(["transaction_summary_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| transaction_summary_facts |

## View Code

```sql
create view dbo.FA_TSF_ReportModel
as 
select * from transaction_summary_facts with (nolock) 
where date_key between 4229 and 4235
```

