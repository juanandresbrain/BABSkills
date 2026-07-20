# dbo.dim_gl_account

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_gl_account"]
    dbo_ref_chart_of_accounts(["dbo.ref_chart_of_accounts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ref_chart_of_accounts |

## View Code

```sql
CREATE   VIEW dbo.dim_gl_account AS SELECT     LTRIM(RTRIM(coa.main_account))                          AS gl_account_code,     coa.name                                                AS gl_account_name,     coa.main_account_type                                   AS gl_account_type,     coa.main_account_category                               AS gl_account_category,     CASE WHEN coa.main_account_type IN ('Asset','Liability','Equity') THEN 1 ELSE 0 END AS is_balance_sheet,     CASE WHEN coa.main_account_type IN ('Revenue','Expense') THEN 1 ELSE 0 END           AS is_income_statement   FROM LH_Source.dbo.ref_chart_of_accounts AS coa;
```

