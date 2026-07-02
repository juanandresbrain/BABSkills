# dbo.Sl_Md_Period

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_Period"]
    dbo_Md_Period(["dbo.Md_Period"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_Period |

## View Code

```sql
create view [dbo].[Sl_Md_Period] 
(period_id, topic_id, table_id, period_group_id, period_label_1, period_label_2, period_description_1, period_description_2, period_start_exp, all_dimensions, have_sub_periods, resource_id)
AS SELECT period_id, topic_id, table_id, period_group_id, period_label_1, period_label_2, period_description_1, period_description_2, period_start_exp, all_dimensions, have_sub_periods, resource_id
FROM fn_01.dbo.Md_Period
```

