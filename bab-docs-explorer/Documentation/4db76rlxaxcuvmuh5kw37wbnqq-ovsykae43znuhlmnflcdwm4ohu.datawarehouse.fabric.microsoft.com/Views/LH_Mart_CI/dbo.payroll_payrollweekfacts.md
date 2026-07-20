# dbo.payroll_payrollweekfacts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.payroll_payrollweekfacts"]
    dbo_payroll_payrollweekfacts(["dbo.payroll_payrollweekfacts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.payroll_payrollweekfacts |

## View Code

```sql
; CREATE   VIEW payroll_payrollweekfacts AS SELECT * FROM LH_Mart.dbo.payroll_payrollweekfacts;
```

