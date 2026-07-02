# WMS.vwDistributionRecTypeByCountryForLookup

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["WMS.vwDistributionRecTypeByCountryForLookup"]
    erp_DistributionRecType(["erp.DistributionRecType"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| erp.DistributionRecType |

## View Code

```sql
create view [WMS].[vwDistributionRecTypeByCountryForLookup]

as

with 
ModeOfDeliveryUnpivot as
	(
			select
				RecType,
				Modes,
				ModeValue
			from 
				(
					select 
						RecType, 
						ModeOfDelivery,
						isnull(ModeOfDeliveryCA,ModeOfDelivery) ModeOfDeliveryCA,
						isnull(ModeOfDeliveryUK,ModeOfDelivery) ModeOfDeliveryUK,
						isnull(ModeOfDeliveryCN,ModeOfDelivery) ModeOfDeliveryCN
					from erp.DistributionRecType with (nolock)
				) as rt
			UNPIVOT
				(
					ModeValue FOR Modes in 
						(ModeOfDelivery,ModeOfDeliveryCA, ModeOfDeliveryUK, ModeOfDeliveryCN)
				) as unpvt
	)
select 
	RecType,
	case Modes 
		when 'ModeOfDelivery'	then 'US'
		when 'ModeOfDeliveryCA' then 'CA'
		when 'ModeOfDeliveryUK' then 'UK'
		when 'ModeOfDeliveryCN' then 'CN'
	end as Country,
	ModeValue as ModeOfDelivery
from ModeOfDeliveryUnpivot
```

