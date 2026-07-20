# dbo.payroll_payrollmonthfacts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.payroll_payrollmonthfacts"]
    dbo_payroll_payrollmonthfacts(["dbo.payroll_payrollmonthfacts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.payroll_payrollmonthfacts |

## View Code

```sql
; CREATE   VIEW payroll_payrollmonthfacts AS SELECT * FROM LH_Mart.dbo.payroll_payrollmonthfacts;
```

