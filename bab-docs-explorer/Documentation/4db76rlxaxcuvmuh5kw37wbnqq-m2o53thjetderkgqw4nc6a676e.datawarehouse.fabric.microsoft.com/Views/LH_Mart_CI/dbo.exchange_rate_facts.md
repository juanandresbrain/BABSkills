# dbo.exchange_rate_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.exchange_rate_facts"]
    dbo_exchange_rate_facts(["dbo.exchange_rate_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.exchange_rate_facts |

## View Code

```sql
;

CREATE VIEW dbo.exchange_rate_facts AS SELECT exchange_rate_facts_key, date_key, from_currency_key, to_currency_key, actual_date, from_currency_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS from_currency_code, to_currency_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS to_currency_code, bbw_rate, actual_rate, fiscal_month_ave_rate, fiscal_month_end_rate, calendar_month_ave_rate, calendar_month_end_rate FROM LH_Mart.dbo.exchange_rate_facts;;
```

