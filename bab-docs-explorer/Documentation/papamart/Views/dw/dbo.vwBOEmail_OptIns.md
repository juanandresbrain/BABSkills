# dbo.vwBOEmail_OptIns

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBOEmail_OptIns"]
    dbo_prefctr_email_in(["dbo.prefctr_email_in"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.prefctr_email_in |

## View Code

```sql
create view dbo.vwBOEmail_OptIns
as
select i.email_addr_lc PCIn_Email, max(i.date_optin) PCIn_date_optin, max(i.date_optout) PCIn_date_optout
--into queries.dbo.Email_OptIns
from dw.dbo.prefctr_email_in i with (nolock)
group by i.email_addr_lc
```

