# dbo.coupon_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.coupon_dim"]
    dbo_coupon_dim(["dbo.coupon_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.coupon_dim |

## View Code

```sql
; CREATE   VIEW [dbo].[coupon_dim] AS     SELECT [coupon_key], [Retail_Pro], [coupon_desc] COLLATE Latin1_General_CI_AS AS [coupon_desc], [start_date], [stop_date], [qty_distributed], [event_id], [event_name] COLLATE Latin1_General_CI_AS AS [event_name], [category_id], [category] COLLATE Latin1_General_CI_AS AS [category], [INS_DT], [UPDT_DT], [ETL_LOG_ID], [ETL_EVNT_ID], [dmDiscountID], [categoryTypeID]     FROM LH_Mart.[dbo].[coupon_dim]
```

