# dbo.vwBO_Coupon_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwBO_Coupon_Dim"]
    dbo_Coupon_dim(["dbo.Coupon_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Coupon_dim |

## View Code

```sql
CREATE view [dbo].[vwBO_Coupon_Dim] as
select case when qty_distributed is not null and qty_distributed > 0 then 
cast(Retail_Pro as varchar(50)) + ' (' + cast(qty_distributed as varchar(50)) + ' Distributed)'
else cast(Retail_Pro as varchar(50)) end as Retail_Pro_Display , 
* from dbo.Coupon_dim
```

