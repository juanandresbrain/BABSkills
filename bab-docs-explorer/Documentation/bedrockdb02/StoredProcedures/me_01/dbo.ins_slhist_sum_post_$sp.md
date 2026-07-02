# dbo.ins_slhist_sum_post_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ins_slhist_sum_post_$sp"]
    dbo_sl_history_sum_post(["dbo.sl_history_sum_post"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sl_history_sum_post |

## Stored Procedure Code

```sql
CREATE proc [dbo].[ins_slhist_sum_post_$sp] 

(@MerchGroupId decimal(12,0), 
@LocationId decimal(12,0), 
@HistPerId decimal(12,0), 
@SLCompId decimal(12,0), 
@HistVal decimal(14,2),
@HistValLocal decimal(14,2))
AS BEGIN

insert into sl_history_sum_post
(merch_hierarchy_group_id, location_id, 
history_period_id, sl_component_id,history_value,history_value_local) 
values (@MerchGroupId, @LocationId, @HistPerId, @SLCompId, @HistVal, @HistValLocal);
END;
```

