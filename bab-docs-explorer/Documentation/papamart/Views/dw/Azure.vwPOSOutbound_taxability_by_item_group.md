# Azure.vwPOSOutbound_taxability_by_item_group

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_taxability_by_item_group"]
    dbo_taxability_by_item_group(["dbo.taxability_by_item_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.taxability_by_item_group |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_taxability_by_item_group] AS

select * from bedrockdb01.auditworks.dbo.taxability_by_item_group 
union
select 'MO521' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MO521' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MO521' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2016-08-05 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'MO521' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2016-08-05 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'MO521' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MO534' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MO534' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MO534' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2016-08-05 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'MO534' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2016-08-05 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'MO534' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH539' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH539' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH539' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2016-08-08 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'OH539' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2016-08-08 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'OH539' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH558' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH558' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH558' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2016-08-08 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'OH558' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2016-08-08 17:15:00.000' as effective_from_date, null as effective_until_date
union
select 'OH558' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL530' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL530' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL530' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL530' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL530' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL530' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL529' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL529' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL529' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL529' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL529' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL529' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL527' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL527' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL527' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL527' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL527' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL527' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL532' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL532' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL532' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL532' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL532' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL532' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL533' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL533' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL533' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL533' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL533' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL533' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL538' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL538' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL538' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL538' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL538' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL538' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL555' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL555' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL555' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL555' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL555' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL555' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL804' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL804' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL804' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL804' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL804' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'FL804' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-07-20 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IN800' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IN800' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IN800' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IN800' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'AZ548' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'AZ548' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'AZ548' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'AZ548' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA546' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA546' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA546' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA546' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA546' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA556' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA556' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA556' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA556' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA556' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA397' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA397' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA397' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA397' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA397' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA367' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA367' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA367' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA367' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA367' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA398' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA398' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA5398' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA398' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA398' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA393' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA393' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA393' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA393' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA393' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA542' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA542' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA542' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA542' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA542' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA805' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA805' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA805' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA805' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA805' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA809' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA809' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA809' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA809' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'CA809' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA552' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA552' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA552' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA552' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA552' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA806' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA806' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA806' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA806' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'GA806' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA553' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA553' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA552' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA553' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA553' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2016-09-17 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IL407' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IL407' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IL407' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'IL407' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MD808' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MD808' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MD808' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MI364' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MI364' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MI364' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MI364' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MS535' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MS535' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MS535' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-07-31 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MS535' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC541' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC541' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC541' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC541' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC801' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC801' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC801' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NC801' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'ND554' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'ND554' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'ND554' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'ND554' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NH324' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NH324' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NH324' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NH324' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ361' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ361' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ361' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ361' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ361' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NV547' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-01-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NV547' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NV547' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-07-30 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NV547' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH536' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2015-08-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH536' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH536' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-08-08 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH536' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-08 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH536' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-08-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH810' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2015-08-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH810' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH810' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2016-08-08 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH810' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2015-08-08 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'OH810' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-08-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'SC543' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'SC543' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'SC543' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2019-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'SC543' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'SC543' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'SC543' as 'tax_jurisdiction', 53 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-08-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX545' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX545' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX545' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX545' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX545' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX537' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX537' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX537' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX537' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX537' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX525' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX525' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX525' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX525' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX525' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX802' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX802' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX802' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX802' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX802' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX803' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX803' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX803' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX803' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX803' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX551' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX551' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX525' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX551' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX551' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX807' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX807' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX807' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX807' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 2 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'TX807' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA528' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA528' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA528' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA528' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA528' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA458' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA458' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA458' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA458' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'VA458' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'WA382' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-03-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'WA382' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-03-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'WA382' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'WA330' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '1970-03-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'WA330' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '1970-03-01 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'WA330' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2015-07-05 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA549' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA549' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA549' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA549' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'MA549' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2018-09-12 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ550' as 'tax_jurisdiction', 10 as tax_item_group_id, 1 as  tax_level, 0 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ550' as 'tax_jurisdiction', 20 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ550' as 'tax_jurisdiction', 21 as tax_item_group_id, 1 as  tax_level, 7 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ550' as 'tax_jurisdiction', 22 as tax_item_group_id, 1 as  tax_level, 1 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
union
select 'NJ550' as 'tax_jurisdiction', 41 as tax_item_group_id, 1 as  tax_level, 4 as tax_rate_code, '2019-03-07 00:00:00.000' as effective_from_date, null as effective_until_date
```

