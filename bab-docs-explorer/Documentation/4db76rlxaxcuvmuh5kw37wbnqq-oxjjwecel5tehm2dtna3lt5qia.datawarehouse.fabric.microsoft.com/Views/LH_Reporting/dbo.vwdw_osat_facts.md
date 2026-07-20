# dbo.vwdw_osat_facts

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_osat_facts"]
    dbo_osat_mo_facts(["dbo.osat_mo_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.osat_mo_facts |

## View Code

```sql
CREATE VIEW vwdw_osat_facts AS
SELECT        osat_mo_facts_key, store_key, last_dom_date_key, mo_score, mo_responses, roll_score, roll_responses, ytd_score, ytd_responses, CAST(1 AS smallint) 
                         AS calc
FROM            LH_Mart.dbo.osat_mo_facts
```

