# dbo.dim_employee_discount_reward

**Database:** DataflowsStagingLakehouse  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_employee_discount_reward"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW dbo.dim_employee_discount_reward AS /* STUB — returns zero rows until upstream replication lands. */ SELECT     CAST(NULL AS varchar(50))  AS reward_id,     CAST(NULL AS varchar(200)) AS reward_name,     CAST(NULL AS varchar(100)) AS promotion_id,     CAST(NULL AS varchar(100)) AS campaign_id,     CAST(NULL AS varchar(200)) AS discount_text,     CAST(NULL AS decimal(5,2)) AS markdown_percentage,     CAST(NULL AS bit)          AS is_employee_discount,     CAST(NULL AS date)         AS effective_from,     CAST(NULL AS date)         AS effective_to,     CAST(NULL AS bit)          AS is_active WHERE 1 = 0;
```

