# dbo.stg_paypal_oms_refs_per_order

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.stg_paypal_oms_refs_per_order"]
    dbo_stg_paypal_oms_refs(["dbo.stg_paypal_oms_refs"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.stg_paypal_oms_refs |

## View Code

```sql
/* =============================================================================    stg_paypal_oms_refs_per_order.sql, per-order MIN reference fallback    =============================================================================    Domain:   Reconciliation (Sales Audit)    Audience: rpt_sp_paypal_auth     PURPOSE      Final fallback ref when amount-and-sign matching fails to bind a leg      to a specific Adyen reference (e.g., a leg amount that does not equal      any capture amount on the OMS order). Returns the deterministic      MIN(reference_no) per (oms_order_number, sign_cohort).     SHAPE        oms_order_number   varchar    OMS OrderNumber.        sign_cohort        char(1)    'R' refund / 'S' sale.        min_reference_no   varchar    MIN(reference_no) under that cohort.     USAGE      The report does:          COALESCE(              CASE WHEN leg_amt < 0                   THEN COALESCE(par.reference_no, refr.min_reference_no)                   WHEN leg_amt > 0                   THEN COALESCE(pas.reference_no, refs.min_reference_no)              END,              refr.min_reference_no, refs.min_reference_no          )      where par/pas = stg_paypal_oms_refs filtered to R/S, and refr/refs =      this view filtered to R/S. Matches the prior in-line CTE behaviour      bit-for-bit.    ============================================================================= */  CREATE   VIEW dbo.stg_paypal_oms_refs_per_order AS SELECT     oms_order_number,     sign_cohort,     MIN(reference_no) AS min_reference_no   FROM dbo.stg_paypal_oms_refs  GROUP BY oms_order_number, sign_cohort;
```

