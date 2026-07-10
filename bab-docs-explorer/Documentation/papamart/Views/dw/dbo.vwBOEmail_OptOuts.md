# dbo.vwBOEmail_OptOuts

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBOEmail_OptOuts"]
    dbo_prefctr_email_out(["dbo.prefctr_email_out"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.prefctr_email_out |

## View Code

```sql
create view dbo.vwBOEmail_OptOuts
as
select o.email_addr_lc PCOut_Email, max(o.date_optout) PCOut_date_optout, max(o.date_optbackin) PCOut_date_optbackin, max(o.final_optout) PCOut_final_optout
--into queries.dbo.Email_OptOuts
from dw.dbo.prefctr_email_out o with (nolock)
group by o.email_addr_lc
```

