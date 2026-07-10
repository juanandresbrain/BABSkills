# Azure.vwPOSOutbound_tax_rate_v2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_tax_rate_v2"]
    dbo_ReportingCombinations(["dbo.ReportingCombinations"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ReportingCombinations |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_tax_rate_v2] AS

--select * from bedrockdb01.auditworks.dbo.tax_rate -- where tax_jurisdiction in ('EIRE', 'GBP')

select 'EIRE' as tax_jurisdiction, 11 as tax_level, 1 as tax_rate_code, '2021-03-01 00:00:00' as effective_from_date, cast(null as datetime) as effective_until_date, 'Taxable' as tax_rate_code_description, 
23.0000 as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, 600 as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code

union

select 'EIRE' as tax_jurisdiction, 11 as tax_level, 9 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, cast(null as datetime) as effective_until_date, 'Non-Taxable' as tax_rate_code_description, 
0.0000 as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, 1277 as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code

union

--select 'GBP' as tax_jurisdiction, 11 as tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, null as effective_until_date, 'Taxable' as tax_rate_code_description, 
--20.0000 as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
--0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
--0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, 493 as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code

---- (select VATRate from [stl-avaldb-p-01].[VATReportingProd].[dbo].[ReportingCombinations] where VATCode = 'UK-STDS' and Country = 'GB' and UserID = 1)

--union

--select 'GBP' as tax_jurisdiction, 11 as tax_level, 9 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, null as effective_until_date, 'Non-Taxable' as tax_rate_code_description, 
--0.0000 as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
--0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
--0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, 1275 as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code


select 'GBP' as tax_jurisdiction, 11 as tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, cast(null as datetime) as effective_until_date, 'Taxable' as tax_rate_code_description, 
cast(VATRate as decimal(6,4)) as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, iVATTransactionID as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code
from [stl-avaldb-p-01].[VATReportingProd].[dbo].[ReportingCombinations] 
where VATCode = 'UK-STDS' and Country = 'GB' and UserID = 1 and EndDate = '1900-01-01 00:00:00.000'

union

select 'GBP' as tax_jurisdiction, 11 as tax_level, 2 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, cast(null as datetime) as effective_until_date, 'Reduced VT Rate' as tax_rate_code_description, 
cast(VATRate as decimal(6,4))  as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, iVATTransactionID as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code
from [stl-avaldb-p-01].[VATReportingProd].[dbo].[ReportingCombinations] 
where VATCode =  'UK-REDUCEDS'  and Country = 'GB' and UserID = 1 and EndDate = '1900-01-01 00:00:00.000'

union

select 'GBP' as tax_jurisdiction, 11 as tax_level, 9 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, cast(null as datetime) as effective_until_date, 'Non-Taxable' as tax_rate_code_description, 
cast(VATRate as decimal(6,4))  as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, iVATTransactionID as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code
from [stl-avaldb-p-01].[VATReportingProd].[dbo].[ReportingCombinations] 
where VATCode = 'UK-EXEMPTS' and Country = 'GB' and UserID = 1 and EndDate = '1900-01-01 00:00:00.000'

union

select 'GBP' as tax_jurisdiction, 11 as tax_level, 3 as tax_rate_code, '1970-01-01 00:00:00' as effective_from_date, cast(null as datetime) as effective_until_date, 'UK Sales VAT Rate to EU' as tax_rate_code_description, 
cast(VATRate as decimal(6,4))  as combined_rate, 0.0000 as federal_rate,0.0000 as state_rate, 0.0000 as county_rate, 0.0000 as city_rate, 	0.0000 as district_rate, 0.00 as threshold_amount, 1 as tax_on_threshold_excess,
0 as tax_on_tax_level, 0.0000 as below_threshold_combined_rate, 0.0000 as below_federal_rate, 0.0000 as below_state_rate, 0.0000 as below_county_rate, 0.0000 as below_city_rate, 
0.0000 as below_district_rate, null as resource_id, 1 as item_tax_strip_flag, iVATTransactionID as tax_rate_id, null as tax_schedule_id, 0 as transaction_level_tax_calc, 0 as compound_order, null as exemption_tax_rate_code
from [stl-avaldb-p-01].[VATReportingProd].[dbo].[ReportingCombinations] 
where VATCode = 'EU-ZEROS'  and Country = 'GB' and UserID = 1 and EndDate = '1900-01-01 00:00:00.000'
```

