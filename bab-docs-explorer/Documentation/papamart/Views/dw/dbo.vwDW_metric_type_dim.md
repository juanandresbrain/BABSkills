# dbo.vwDW_metric_type_dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_metric_type_dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE view [dbo].[vwDW_metric_type_dim]
as

select 1 as metric_type_key
	, 'Merchandise' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 2 as metric_type_key
	, 'Gift Card Discount' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 3 as metric_type_key
	, 'Cub Cash UGA' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 4 as metric_type_key
	, 'Shipping UGA' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 5 as metric_type_key
	, 'Other Fees UGA' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 6 as metric_type_key
	, 'Stuffing And Supplies UGA' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 7 as metric_type_key
	, 'Reward Certificate Amt' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 8 as metric_type_key
	, 'Buy Stuff Amt' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 9 as metric_type_key
	, 'Coupon Discount' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 10 as metric_type_key
	, 'Total Discount' as metric_name
	, 1 as is_gaap
	, 0 as is_net
union all
select 11 as metric_type_key
	, 'Tax' as metric_name
	, 0 as is_gaap
	, 0 as is_net
union all
select 12 as metric_type_key
	, 'NA' as metric_name
	, 0 as is_gaap
	, 0 as is_net
```

