# dbo.fn_DistroMultipleBreakout

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_DistroMultipleBreakout"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @transaction_id | int | 4 | NO |
| @sku | varchar | 20 | NO |
| @quant_wanted | int | 4 | NO |
| @distro_mult | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE function dbo.fn_DistroMultipleBreakout (@transaction_id int, @sku varchar(20), @quant_wanted int, @distro_mult int) 
returns @tempTable table
	(transaction_id 	int,
	sku	varchar(20),
	quant_breakout	int
)
as 
begin

-- 	insert into @tempTable values(1, 1,1)

	while @quant_wanted > 0
	begin
		insert into @tempTable values(@transaction_id, @sku, @distro_mult)
		set @quant_wanted = @quant_wanted - @distro_mult
	end
	
return
end
```
