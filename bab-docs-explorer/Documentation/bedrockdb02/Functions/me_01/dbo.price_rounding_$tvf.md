# dbo.price_rounding_$tvf

**Database:** me_01  
**Server:** bedrockdb02  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.price_rounding_$tvf"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Price | float | 8 | NO |
| @Pricing_Rule_ID | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql




-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Create Function
--	History:
--	Date		By who		Bug number and description
--	Feb. 17		Feng		156574 when using a % off method the system is rounding up instead of down
-----------------------------------------------------------------------------------------------------------------------------

CREATE FUNCTION dbo.price_rounding_$tvf

	(
		 @Price AS FLOAT
		,@Pricing_Rule_ID AS INT
	)

RETURNS TABLE

AS

--	Object GUID: 149FDDAF-FE56-47A0-B7A2-EFD489339D23
--	Pricing GUID (General): EFB5A343-8978-4ACF-952C-37862704CBC8

RETURN

-----------------------------------------------------------------------------------------------------------------------------
--	Main Query: Final Display / Output
-----------------------------------------------------------------------------------------------------------------------------


SELECT
	(CASE
		-- Nearest
		WHEN sqRR.rounding_rule_type = 1 THEN
			(CASE
				WHEN sqRR.ending_rule = 1 AND ABS (@Price - caRLDD.value ) < ABS (@Price - caRHDD.value) THEN caRLDD.value
				WHEN sqRR.ending_rule = 1 THEN caRHDD.value
				WHEN sqRR.ending_rule = 2 AND ABS (@Price - caCALC.new_higher_price_RHEW) < ABS (@Price - caCALC.new_lower_price_RHEW) THEN caCALC.new_higher_price_RHEW
				WHEN sqRR.ending_rule = 2 THEN caCALC.new_lower_price_RHEW
				WHEN sqRR.ending_rule = 3 THEN caCALC.new_RMO
				END)
		-- Next Highest
		WHEN sqRR.rounding_rule_type = 2 THEN
			(CASE
				WHEN sqRR.ending_rule = 1 THEN caRHDD.value
				WHEN sqRR.ending_rule = 2 AND caRHEW.value1 - @Price < ISNULL (caRHEW.value2 - @Price, 9999) THEN caRHEW.value1
				WHEN sqRR.ending_rule = 2 THEN caRHEW.value2
				WHEN sqRR.ending_rule = 3 THEN caRHMO.value1
				END)
		-- Next Lowest
		WHEN sqRR.rounding_rule_type = 3 THEN
			(CASE
				WHEN sqRR.ending_rule = 1 THEN caRLDD.value
				WHEN sqRR.ending_rule = 2 AND @Price - caRLEW.value1 < ISNULL (@Price - caRLEW.value2,9999) THEN caRLEW.value1
				WHEN sqRR.ending_rule = 2 THEN caRLEW.value2
				WHEN sqRR.ending_rule = 3 THEN caRLMO.value1
				END)
		-- Return Exact Price If Nothing Else Is Available
		ELSE caRE.value
		END) AS price
FROM

	(
		SELECT
			SIGN (CAST ((@Price * 100 + 0.001) AS INT) % 10 - CAST ((@Price * 10 + 0.001) AS INT) % 10) AS sgn_value
	) sqSGN

	CROSS APPLY

		(
			SELECT
				 CAST ((@Price * 10 + 0.001) AS INT) % 10 -- Get tenths
					-- Add 1 to the tenths if hundreds are higher (0.56 -> 0.66, 0.54 -> 0.55), idea is add @x*(sign(@x + 1)) where @x indicates if hundreds are higher (1) or lower(-1) or equal(0) to the tents
					+ sqSGN.sgn_value * (SIGN (sqSGN.sgn_value + 1)) AS adjustedTenthsADD
				,CAST ((@Price * 10 + 0.001) AS INT) % 10 -- Get tenths
					-- Substract 1 from the tenths if hundreds are lower (0.56 -> 0.55, 0.54 -> 0.44), idea is substract @x*(sign(@x - 1)) where @x indicates if hundreds are higher (1) or lower(-1) or equal(0) to the tents
					- sqSGN.sgn_value * (SIGN (sqSGN.sgn_value - 1)) AS adjustedTenthsMINUS
		) sqTN

	OUTER APPLY

		( -- Get the rounding rule for the price
			SELECT -- top 1 with an order by as it is not unique?
				PRD.rounding_rule_id
			FROM
				dbo.pricing_rule_detail PRD
			WHERE
				@Price >= PRD.from_value
				AND
				(
					@Price <= PRD.to_value
					OR PRD.to_value is NULL
				)
				AND PRD.pricing_rule_id = @Pricing_Rule_ID
		) sqPRI

	OUTER APPLY

		(
			SELECT
				 RR.rounding_rule_type
				,RR.ending_rule
				,RR.value1
				,RR.value2
			FROM
				dbo.rounding_rule RR
			WHERE
				RR.rounding_rule_id = sqPRI.rounding_rule_id
		) sqRR

	CROSS APPLY

		(
			SELECT
				ROUND (CAST(@Price AS DECIMAL(12,5)),2) AS value
		) caRE -- Rounding Exact

	CROSS APPLY

		(
			SELECT
				FLOOR (@Price) + sqTN.adjustedTenthsADD * 0.1 + sqTN.adjustedTenthsADD * 0.01 AS value
		) caRHDD -- Rounding Higher Double Digits

	CROSS APPLY

		(
			SELECT
				FLOOR (@Price) + sqTN.adjustedTenthsMINUS * 0.1 + sqTN.adjustedTenthsMINUS * 0.01 AS value
		) caRLDD -- Rounding Lower Double Digits

	CROSS APPLY

		(
			SELECT
				 FLOOR (@Price - sqRR.value1) + sqRR.value1 AS value1
				,FLOOR (@Price - sqRR.value2) + sqRR.value2 AS value2
		) caRLEW -- Rounding Lower Ending With

	CROSS APPLY

		(
			SELECT
				 FLOOR (@Price + (0.99 - sqRR.value1)) + sqRR.value1 AS value1
				,FLOOR (@Price + (0.99 - sqRR.value2)) + sqRR.value2 AS value2
		) caRHEW -- Rounding Higher Ending With

	CROSS APPLY

		(
			SELECT
				 (FLOOR((@Price-COALESCE(sqRR.value2, 0))/sqRR.value1+0.00001)*sqRR.value1)+COALESCE(sqRR.value2, 0) AS value1   -- Float is an approximate data type. @Price looks like max 2 decimal places...adding just a little more to compensate.
		) caRLMO -- Rounding Lower Multiple Of

	CROSS APPLY

		(
			SELECT
				 CASE
					WHEN @Price = 0 THEN COALESCE(sqRR.value2, 0)
					WHEN CAST((CAST(@Price AS DECIMAL(12,5)) -COALESCE(sqRR.value2,0))/sqRR.value1 AS INT) = (CAST(@Price AS DECIMAL(12,5))-COALESCE(sqRR.value2,0))/sqRR.value1 THEN ROUND(@Price, 2)
						ELSE (FLOOR((@Price+sqRR.value1-COALESCE(sqRR.value2, 0))/sqRR.value1+0.00001)*sqRR.value1)+COALESCE(sqRR.value2, 0)
					END AS value1

		) caRHMO -- Rounding Higher Multiple Of

	CROSS APPLY

		(
			SELECT
				 (CASE -- Get Next Higher Price (Rounding Higher Ending With)
					WHEN caRHEW.value1 - @Price < ISNULL (caRHEW.value2 - @Price, 9999) THEN caRHEW.value1
					ELSE caRHEW.value2
					END) AS new_higher_price_RHEW
				,(CASE -- Get Next Lower Price (Rounding Lower Ending With)
					WHEN @Price - caRLEW.value1 < ISNULL (@Price - caRLEW.value2, 9999) THEN caRLEW.value1
					ELSE caRLEW.value2
					END) AS new_lower_price_RHEW

				,(CASE  -- Get Nearest Multiple Of
					WHEN ABS(@Price - caRLMO.value1) <= ABS(@Price - caRHMO.value1) THEN caRLMO.value1
					ELSE caRHMO.value1
					END) AS new_RMO
		) caCALC -- Calculations For "Nearest"
```
