# dbo.v_nonmerch_discounts_comp

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.v_nonmerch_discounts_comp"]
    dbo_exchange_rate_facts(["dbo.exchange_rate_facts"]) --> VIEW
    dbo_v_nonmerch_discounts_core(["dbo.v_nonmerch_discounts_core"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.exchange_rate_facts |
| dbo.v_nonmerch_discounts_core |

## View Code

```sql
CREATE   VIEW dbo.v_nonmerch_discounts_comp AS SELECT     c.business_unit_id,     c.business_date,     c.sequence_number,     c.description,      CASE         WHEN c.country_id = 'IE'             THEN ROUND(COALESCE(erf.bbw_rate, 1.0) * c.modification_total, 4)         ELSE c.modification_total     END AS modification_total,      c.item_type,     c.country_id,     c.create_time  FROM dbo.v_nonmerch_discounts_core AS c LEFT JOIN LH_MART.dbo.exchange_rate_facts AS erf   ON CAST(c.create_time AS date) = CAST(erf.actual_date AS date)  AND erf.from_currency_code = 'EUR'  AND erf.to_currency_code   = 'GBP';
```

