# dbo.FA_TDF_ReportModel

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.FA_TDF_ReportModel"]
    transaction_detail_facts(["transaction_detail_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| transaction_detail_facts |

## View Code

```sql
create view dbo.FA_TDF_ReportModel
as 
select * from transaction_detail_facts with (nolock) 
where date_key between 4229 and 4235
```

