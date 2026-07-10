# dbo.vwUltiProStageFromAD

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwUltiProStageFromAD"]
    vwUltiProValidationVsADStageVsAD(["vwUltiProValidationVsADStageVsAD"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| vwUltiProValidationVsADStageVsAD |

## View Code

```sql
CREATE view [dbo].[vwUltiProStageFromAD]
as 
select 
	EmployeeID,
	CompanyCode,
	Location,
	LastHireDate,
	UltiProSamAccountName,
	UltiProEmail,
	UltiProStatus,
	FullName,
	UltiProInsertDate,
	UltiProUpdateDate,
	ADStageDate,
	ADSamAccountName,
	ADEmail,
	ADInsertDate,
	ADUpdateDate,
	SSOInsertDate,
	SSOActivatedDate
from vwUltiProValidationVsADStageVsAD
where 1=1
--and not (Location = 'UKBQ' or left(Location,1) = '2')
and UltiProStatus <> 'Terminated'
and 
	(
		(ADStageDate is NOT NULL and isnull(ADUpdateDate, ADInsertDate) is NULL)
		OR
		datediff(dd, LastHireDate, getdate()) <= 7
		OR
		ADStageDate is NOT NULL and ADSamAccountName is NULL
		or
		datediff(dd, ADStageDate, getdate()) = 0
	)
```

