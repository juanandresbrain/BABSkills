# azure.vw_crm_email_fact_rollup_summary

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["azure.vw_crm_email_fact_rollup_summary"]
    dbo_emailfactrollup(["dbo.emailfactrollup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailfactrollup |

## View Code

```sql
CREATE view [azure].[vw_crm_email_fact_rollup_summary]

AS



select 
count(distinct efr.EmailAddress) as [distinct_email_sent_last365]
from LH_Mart.dbo.emailfactrollup efr
where efr.LastSendDate between getdate()-366 and getdate()
```

