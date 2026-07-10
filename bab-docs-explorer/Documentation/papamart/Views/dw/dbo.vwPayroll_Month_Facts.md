# dbo.vwPayroll_Month_Facts

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPayroll_Month_Facts"]
    dbo_payroll_month_facts(["dbo.payroll_month_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.payroll_month_facts |

## View Code

```sql
CREATE   VIEW dbo.vwPayroll_Month_Facts
AS

SELECT *
FROM payroll.dbo.payroll_month_facts
```

