# Azure.vwPOSOutbound_taxability_by_item_group_v2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_taxability_by_item_group_v2"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_taxability_by_item_group_v2] AS

--select * from bedrockdb01.auditworks.dbo.taxability_by_item_group -- where tax_jurisdiction in ('GBP','EIRE','*IE')

select '*IE' as 'tax_jurisdiction', 10 as tax_item_group_id, 11 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
union
select '*IE' as 'tax_jurisdiction', 20 as tax_item_group_id, 11 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
union
select 'EIRE' as 'tax_jurisdiction', 10 as tax_item_group_id, 11 as  tax_level, 9 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
union
select 'EIRE' as 'tax_jurisdiction', 20 as tax_item_group_id, 11 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
union
select 'GBP' as 'tax_jurisdiction', 10 as tax_item_group_id, 11 as  tax_level, 9 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
union
select 'GBP' as 'tax_jurisdiction', 20 as tax_item_group_id, 11 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
union
select 'GBP' as 'tax_jurisdiction', 21 as tax_item_group_id, 11 as  tax_level, 9 as tax_rate_code, '2016-07-21 08:27:00.000' as effective_from_date, cast(null as datetime) as effective_until_date
```

