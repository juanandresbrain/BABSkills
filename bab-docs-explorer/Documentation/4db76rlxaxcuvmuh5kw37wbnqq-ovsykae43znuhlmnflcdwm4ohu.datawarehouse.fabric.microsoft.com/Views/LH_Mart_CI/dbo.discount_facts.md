# dbo.discount_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.discount_facts"]
    dbo_discount_facts(["dbo.discount_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.discount_facts |

## View Code

```sql
CREATE  VIEW [dbo].[discount_facts] AS    SELECT [transaction_id]       ,[store_key]       ,[date_key]       ,[coupon_key]       ,[line_object_key]       ,[units]       ,[unit_gross_amount]       ,[reference_no]       ,[process_name]       ,[process_date]       ,[uid]       ,[transaction_no]       ,[INS_DT]       ,[UPDT_DT]       ,[ETL_LOG_ID]       ,[ETL_EVNT_ID]       ,[categoryTypeID]       ,[isExpired]       ,[lift_amount]       ,[line_action_key]   FROM LH_Mart.[dbo].[discount_facts]
```

