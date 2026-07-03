# dbo.rounding_round_price_$fn

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Scalar Function  
**Returns:** float(8)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.rounding_round_price_$fn"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @price | float | 8 | NO |
| @pricing_rule_id | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql


CREATE FUNCTION rounding_round_price_$fn (@price float, @pricing_rule_id int)
RETURNS float
AS
BEGIN
	DECLARE @CExact int,
		@CNearest int,
		@CNextHighest int,
		@CNextLowest int,
		@CNull int,
		@CDoubleDigit int,
		@CPriceEndingIn int,
		@CMultipleOf int,
		@rounding_rule_id int,
		@rounding_rule_type int,
		@ending_rule int,
		@value1 float,
		@value2 float,
		@new_lower_price float,
		@new_higher_price float
		
	
	-- declare some constants
	SELECT 
		-- rounding rule types
		@CExact = 0,
		@CNearest = 1,
		@CNextHighest = 2,
		@CNextLowest = 3,
		-- ending rule types
		@CNull = 0,
		@CDoubleDigit = 1,
		@CPriceEndingIn = 2,
		@CMultipleOf = 3
		
	-- get the rounding rule for the price
	SELECT @rounding_rule_id = rounding_rule_id
	from pricing_rule_detail
	where @price >= from_value
	AND (@price <= to_value OR to_value is NULL)
	AND pricing_rule_id = @pricing_rule_id
	
	SELECT @rounding_rule_type = rounding_rule_type, @ending_rule = ending_rule, @value1 = value1, @value2 = value2
	FROM rounding_rule
	WHERE rounding_rule_id = @rounding_rule_id
	
	--next highest
	IF @rounding_rule_type = @CNextHighest
	BEGIN
		IF @ending_rule = @CDoubleDigit
			RETURN dbo.rounding_higher_double_digits_$fn (@price)
		
		IF @ending_rule = @CPriceEndingIn
		BEGIN
			IF dbo.rounding_higher_ending_with_$fn(@price,@value1) - @price < ISNULL(dbo.rounding_higher_ending_with_$fn(@price,@value2) - @price,9999)
				RETURN dbo.rounding_higher_ending_with_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				RETURN dbo.rounding_higher_ending_with_$fn(@price,@value2)
		END
		
		IF @ending_rule = @CMultipleOf
		BEGIN
			IF dbo.rounding_higher_multple_of_$fn(@price,@value1) - @price < ISNULL(dbo.rounding_higher_multple_of_$fn(@price,@value2) - @price,9999)
				RETURN dbo.rounding_higher_multple_of_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				RETURN dbo.rounding_higher_multple_of_$fn(@price,@value2)
		END		
	END
	
	--next lowest
	IF @rounding_rule_type = @CNextLowest
	BEGIN
		IF @ending_rule = @CDoubleDigit
			RETURN dbo.rounding_lower_double_digits_$fn (@price)
		
		IF @ending_rule = @CPriceEndingIn
		BEGIN
			IF @price - dbo.rounding_lower_ending_with_$fn(@price,@value1) < ISNULL( @price - dbo.rounding_lower_ending_with_$fn(@price,@value2),9999)
				RETURN dbo.rounding_lower_ending_with_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				RETURN dbo.rounding_lower_ending_with_$fn(@price,@value2)
		END
		
		IF @ending_rule = @CMultipleOf
		BEGIN
			IF @price - dbo.rounding_lower_multple_of_$fn(@price,@value1)  < ISNULL(@price - dbo.rounding_lower_multple_of_$fn(@price,@value2),9999)
				RETURN dbo.rounding_lower_multple_of_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				RETURN dbo.rounding_lower_multple_of_$fn(@price,@value2)
		END		
	END
	
	--nearest
	IF @rounding_rule_type = @CNearest
	BEGIN
		IF @ending_rule = @CDoubleDigit
			IF ABS(@price - dbo.rounding_lower_double_digits_$fn(@price)) < ABS(@price - dbo.rounding_higher_double_digits_$fn(@price))
				RETURN dbo.rounding_lower_double_digits_$fn(@price) -- rounding lower is nearer to the original price
			ELSE
				RETURN dbo.rounding_higher_double_digits_$fn(@price) 
		
		IF @ending_rule = @CPriceEndingIn
		BEGIN
			-- get next higher price
			IF dbo.rounding_higher_ending_with_$fn(@price,@value1) - @price < ISNULL(dbo.rounding_higher_ending_with_$fn(@price,@value2) - @price,9999)
				SET @new_higher_price = dbo.rounding_higher_ending_with_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				SET @new_higher_price = dbo.rounding_higher_ending_with_$fn(@price,@value2)
			
			-- get next lower price
			IF @price - dbo.rounding_lower_ending_with_$fn(@price,@value1) < ISNULL( @price - dbo.rounding_lower_ending_with_$fn(@price,@value2),9999)
				SET @new_lower_price = dbo.rounding_lower_ending_with_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				SET @new_lower_price = dbo.rounding_lower_ending_with_$fn(@price,@value2)
		
			-- return nearer one
			IF ABS(@price - @new_higher_price) < ABS(@price - @new_lower_price)
				RETURN @new_higher_price 
			ELSE 
				RETURN @new_lower_price
		END
		
		IF @ending_rule = @CMultipleOf
		BEGIN
			-- get next higher price
			IF dbo.rounding_higher_multple_of_$fn(@price,@value1) - @price < ISNULL(dbo.rounding_higher_multple_of_$fn(@price,@value2) - @price,9999)
				SET @new_higher_price = dbo.rounding_higher_multple_of_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				SET @new_higher_price = dbo.rounding_higher_multple_of_$fn(@price,@value2)
			
			-- get next lower price
			IF @price - dbo.rounding_lower_multple_of_$fn(@price,@value1)  < ISNULL(@price - dbo.rounding_lower_multple_of_$fn(@price,@value2),9999)
				SET @new_lower_price = dbo.rounding_lower_multple_of_$fn(@price,@value1) -- value1 rounding is closer to the price
			ELSE
				SET @new_lower_price = dbo.rounding_lower_multple_of_$fn(@price,@value2)
		
			-- return nearer one
			IF ABS(@price - @new_higher_price) < ABS(@price - @new_lower_price)
				RETURN @new_higher_price 
			ELSE 
				RETURN @new_lower_price
		END		
	END
	
	--return exact price if nothing else
	RETURN dbo.rounding_exact_$fn(@price)
END
```
