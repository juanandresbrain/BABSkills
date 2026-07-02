# dbo.ins_cum_val_lowlevel_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.ins_cum_val_lowlevel_$sp"]
    dbo_cum_val_low_level_post(["dbo.cum_val_low_level_post"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cum_val_low_level_post |

## Stored Procedure Code

```sql
CREATE proc [dbo].[ins_cum_val_lowlevel_$sp] 
(@CalPerId decimal(12,0), 
@LocationId decimal(12,0), 
@MerchGroupId decimal(12,0), 
@Cost decimal(14,2), 
@CostLocal decimal(14,2), 
@Retail decimal(14,2),
@RetailLocal decimal(14,2))
AS BEGIN

INSERT INTO cum_val_low_level_post
(calendar_period_id, location_id, 
merch_hierarchy_group_id, cost, retail, cost_local, retail_local)
VALUES (@CalPerId, @LocationId, @MerchGroupId, @Cost, @Retail, @CostLocal, @RetailLocal);

END;
```

