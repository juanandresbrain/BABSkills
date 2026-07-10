# dbo.spDWBuildTransactionFactsDynamics_Bak20240506

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDWBuildTransactionFactsDynamics_Bak20240506"]
    dbo_aw_Transaction_Header(["dbo.aw_Transaction_Header"]) --> SP
    dbo_DiscountFactsDynamics(["dbo.DiscountFactsDynamics"]) --> SP
    dbo_line_action_dim(["dbo.line_action_dim"]) --> SP
    dbo_line_object_dim(["dbo.line_object_dim"]) --> SP
    dbo_product_dim(["dbo.product_dim"]) --> SP
    dbo_tender_dim(["dbo.tender_dim"]) --> SP
    dbo_TenderFactsDynamics(["dbo.TenderFactsDynamics"]) --> SP
    tmpESRef(["tmpESRef"]) --> SP
    Transaction_Type_Dim(["Transaction_Type_Dim"]) --> SP
    dbo_TransactionDetailFactsDynamics(["dbo.TransactionDetailFactsDynamics"]) --> SP
    dbo_WebToStoreLookup(["dbo.WebToStoreLookup"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.aw_Transaction_Header |
| dbo.DiscountFactsDynamics |
| dbo.line_action_dim |
| dbo.line_object_dim |
| dbo.product_dim |
| dbo.tender_dim |
| dbo.TenderFactsDynamics |
| tmpESRef |
| Transaction_Type_Dim |
| dbo.TransactionDetailFactsDynamics |
| dbo.WebToStoreLookup |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: [dbo].[spDWBuildTransactionFactsDynamics]
--
-- =============================================================================================================

CREATE PROC [dbo].[spDWBuildTransactionFactsDynamics_Bak20240506]
AS
	SET NOCOUNT ON;


		SELECT
			transaction_id
		INTO #tmpTrans
		FROM
			DWStaging.dbo.aw_Transaction_Header WITH (NOLOCK)
	--	WHERE 
	--		batchNumber = @batchNumber

--===========================================================================================
--== STAGE DISCOUNTS - SEPARATING ENTERPRISE SELLING ORDER VS NON ENTERPRISE SELLING ORDER ==
--===========================================================================================
/*  
	ES LINE_ACTIONS
	91	deducted on order -- ORDER
	92	reversed on order cancellation --CANCEL
	93	deducted on order delivery -- FULFILLMENT 
	160	deducted on order pickup --FULFILLMENT 
	94	reversed on delivery return --RETURN
*/
		IF OBJECT_ID('tempdb..#tmpDiscounts') IS NOT NULL
		BEGIN
			DROP TABLE #tmpDiscounts
		END
		
		SELECT
			df.transaction_id,
			SUM(ISNULL(df.unit_gross_amount, 0)) AS discount_amount,
			
	
			--EXCLUDES ES
			SUM(CASE
				WHEN lo.Line_Object IN (-1617, 640) THEN 0
				WHEN 
					( 
						lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --coupons
						and (lad.line_action NOT in (91,92,93,94,160) or lad.line_action is null) --null is because we recently added line_action to table, not updating old records.
					)
					THEN ISNULL(df.unit_gross_amount, 0) 
				ELSE 0
			END) AS coupon_discount_amount,
				
					-- INCLUDES ES ORDER / CANCEL
						SUM(CASE
						WHEN lo.Line_Object IN (-1617, 640) THEN 0
						WHEN 
							(
								lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --coupons
								and lad.line_action in (91,92) 
							)
							THEN ISNULL(df.unit_gross_amount, 0) 
						ELSE 0
					END) AS StoreOrder_coupon_discount_amount,

					--INCLUDES ES FULFILLMENT 
					SUM(CASE
						WHEN lo.Line_Object IN (-1617, 640) THEN 0
						WHEN 
							(
								lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --coupons
								and lad.line_action in (93,160) 
							)
							THEN ISNULL(df.unit_gross_amount, 0) 
						ELSE 0
					END) AS StoreFulfillment_coupon_discount_amount,

					--INCLUDES ES RETURN
					SUM(CASE
						WHEN lo.Line_Object IN (-1617, 640) THEN 0
						WHEN 
							(
								lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --coupons
								and lad.line_action in (94) 
							)
							THEN ISNULL(df.unit_gross_amount, 0) 
						ELSE 0
					END) AS StoreReturn_coupon_discount_amount,

			--EXCLUDES ES
			SUM(CASE
				WHEN lo.Line_Object IN (-1617, 640) THEN 0
				WHEN 
					(
						lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199)
						and (lad.line_action NOT in (91,92,93,94,160) or lad.line_action is null) 
					)
					THEN ISNULL(df.units, 0)
				ELSE 0
			END) AS coupon_discount_units,
						
						-- INCLUDES ES ORDER, CANCEL
						SUM(CASE
							WHEN lo.Line_Object IN (-1617, 640) THEN 0
							WHEN 
								(
									lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199)
									and lad.line_action in (91,92) 
								)
								THEN ISNULL(df.units, 0)
							ELSE 0
						END) AS StoreOrder_coupon_discount_units,

						--INCLUDES ES FULFILLMENT 
						SUM(CASE
							WHEN lo.Line_Object IN (-1617, 640) THEN 0
							WHEN 
								(
									lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199)
									and lad.line_action in (93,160) 
								)
								THEN ISNULL(df.units, 0)
							ELSE 0
						END) AS StoreFulfillment_coupon_discount_units,

						--INCLUDES ES RETURN 
						SUM(CASE
							WHEN lo.Line_Object IN (-1617, 640) THEN 0
							WHEN 
								(
									lo.Line_Object IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199)
									and lad.line_action in (94) 
								)
								THEN ISNULL(df.units, 0)
							ELSE 0
						END) AS StoreReturn_coupon_discount_units,
			
			--EXCLUDES ES
			SUM(CASE
				WHEN lo.Line_Object IN (-1617, 640) THEN 0
				WHEN 
					(
						lo.Line_Object NOT IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --excludes coupons
						and (lad.line_action NOT in (91,92,93,94,160) or lad.line_action is null) 
					)
					THEN ISNULL(df.unit_gross_amount, 0)
				ELSE 0
			END) AS total_discount_amount,

						-- INCLUDES ES ORDER, CANCEL
						SUM(CASE
							WHEN lo.Line_Object IN (-1617, 640) THEN 0
							WHEN 
								(
									lo.Line_Object NOT IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --excludes coupons
									and lad.line_action  in (91,92) 
								)
								THEN ISNULL(df.unit_gross_amount, 0)
							ELSE 0
						END) AS StoreOrder_total_discount_amount,

						--INCLUDES ES FULFILLMENT
						SUM(CASE
							WHEN lo.Line_Object IN (-1617, 640) THEN 0
							WHEN 
								(
									lo.Line_Object NOT IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --excludes coupons
									and lad.line_action in (93,160)  
								)
								THEN ISNULL(df.unit_gross_amount, 0)
							ELSE 0
						END) AS StoreFulfillment_total_discount_amount,

						--INCLUDES ES RETURN
						SUM(CASE
							WHEN lo.Line_Object IN (-1617, 640) THEN 0
							WHEN 
								(
									lo.Line_Object NOT IN (290, 295, 1841, 1842, 1843, 1846, 1849, 1860, 1600, 1610, 1611, 1615, 1618, 1630, 1636, 1641, 1642, 1643, 1646, 1649, 1802, 1803, 1806, 1809, 1830, 1187, 1199) --excludes coupons
									and lad.line_action in (94)  
								)
								THEN ISNULL(df.unit_gross_amount, 0)
							ELSE 0
						END) AS StoreReturn_total_discount_amount,
			
			--EXCLUDES ES
			SUM(CASE
				WHEN 
					(
						lo.Line_Object = -1617 --no ES equivalent found 
						AND (lad.line_action NOT in (91,92,93,94,160) or lad.line_action is null) 
					)
				THEN ISNULL(df.unit_gross_amount, 0) 
				ELSE 0
			END) AS upsell_discount_amount,
				
						-- INCLUDES ES ORDER, CANCEL
						SUM(CASE
							WHEN 
								(
									lo.Line_Object = -1617 --no ES equivalent found 
									AND lad.line_action in (91,92) -- INCLUDES ES ORDER DEDUCTED / REVERSED  
								)
							THEN ISNULL(df.unit_gross_amount, 0) 
							ELSE 0
						END) AS StoreOrder_upsell_discount_amount,
				
						--INCLUDES ES FULFILLMENT
						SUM(CASE
							WHEN 
								(
									lo.Line_Object = -1617 --no ES equivalent found 
									AND lad.line_action in (93,160)
								)
							THEN ISNULL(df.unit_gross_amount, 0) 
							ELSE 0
						END) AS StoreFulfillment_upsell_discount_amount,

						--INCLUDES ES RETURN
						SUM(CASE
							WHEN 
								(
									lo.Line_Object = -1617 --no ES equivalent found 
									AND lad.line_action in (94)
								)
							THEN ISNULL(df.unit_gross_amount, 0) 
							ELSE 0
						END) AS StoreReturn_upsell_discount_amount,

			--EXCLUDES ES
			SUM(CASE
				WHEN 
					(
						lo.Line_Object = 640 --no ES equivalent found
						and (lad.line_action NOT in (91,92,93,94,160) or lad.line_action is null) 
					)
				THEN ISNULL(df.unit_gross_amount, 0) 
				ELSE 0
			END) AS reward_certificate_amount,

						-- INCLUDES ES ORDER, CANCEL
						SUM(CASE
							WHEN 
								(
									lo.Line_Object = 640 --no ES equivalent found
									and lad.line_action in (91,92) 
								)
							THEN ISNULL(df.unit_gross_amount, 0) 
							ELSE 0
						END) AS StoreOrder_reward_certificate_amount,

						--INCLUDES ES FULFILLMENT
						SUM(CASE
							WHEN 
								(
									lo.Line_Object = 640 --no ES equivalent found
									and lad.line_action in (93,160)  
								)
							THEN ISNULL(df.unit_gross_amount, 0) 
							ELSE 0
						END) AS StoreFulfillment_reward_certificate_amount,

						--INCLUDES ES RETURN
						SUM(CASE
							WHEN 
								(
									lo.Line_Object = 640 --no ES equivalent found
									and lad.line_action in (94) 
								)
							THEN ISNULL(df.unit_gross_amount, 0) 
							ELSE 0
						END) AS StoreReturn_reward_certificate_amount,
			---	EMPLOYEE DISCOUNTS --
		SUM(CASE
					WHEN 
						(
							lo.Line_Object IN (1700,1740,1750,1900)
						)
					THEN ISNULL(df.unit_gross_amount, 0) 
					ELSE 0
				END) AS EmployeeDiscount
		INTO #tmpDiscounts
		FROM
			dbo.DiscountFactsDynamics df WITH (NOLOCK)
			INNER JOIN dbo.line_object_dim lo
				ON df.Line_Object_Key = lo.Line_Object_Key
			INNER JOIN #tmpTrans t
				ON df.transaction_id = t.transaction_id
			INNER JOIN dbo.line_action_dim lad 
				ON df.line_action_key = lad.line_action_key
		GROUP BY df.transaction_id



--===========================================================================================
--== END STAGE DISCOUNTS ====================================================================
--===========================================================================================

--------> keep going

--===========================================================================================
--== STAGE TENDER - no special handling for Non-ES vs ES == IF we do end up circling back to break out tender, there's other procs to consider, will need to review job.
--===========================================================================================	

		IF OBJECT_ID('tempdb..#tmpTender') IS NOT NULL
		BEGIN
			DROP TABLE #tmpTender
		END

		SELECT
			tf.transaction_id,
			SUM(CASE
				WHEN t.tender_code = 690 THEN ISNULL(tf.tender_amt, 0)
				ELSE 0
			END) AS buy_stuff_amount,
			SUM(CASE
				WHEN t.tender_code = -1 THEN ISNULL(tf.tender_amt, 0)
				ELSE 0
			END) AS tax_amount,
			SUM(CASE
				WHEN t.tender_code IN (621, 633, 690) THEN ISNULL(tf.tender_amt, 0)
				ELSE 0
			END) AS redemption_amount
		INTO #tmpTender
		FROM
			dbo.TenderFactsDynamics tf WITH (NOLOCK)
			INNER JOIN dbo.tender_dim t WITH (NOLOCK)
				ON t.tender_key = tf.tender_key
			INNER JOIN #tmpTrans t1
				ON tf.transaction_id = t1.transaction_id
		WHERE
			t.tender_code IN (-1, 621, 633, 690)
		GROUP BY tf.transaction_id

--===========================================================================================
--== END STAGE TENDER ====================================================================
--===========================================================================================

--------> keep going

--========================================================================--
--===STAGE TRANSACTION_DETAIL_FACTS=======================================--
--========================================================================--


		IF OBJECT_ID('tempdb..#tmpTDF') IS NOT NULL
		BEGIN
			DROP TABLE #tmpTDF
		END

		SELECT
			tdf.transaction_id,
			COUNT(*) AS line_count,
			------------------------------------------------------------------------------------
			--these columns are from 'store sale' perspective (gaap + es order/cancel + es return) --EXCLUDES ES FULFILLMENTS
			--these columns are not used to create other measures beyond themselves
			Sum(Case
					when (lo.line_object = 106 and lad.line_action in (90,142)) 
						then 0
					else ISNULL(tdf.units, 0)
				end) as total_units,
			Sum(Case
					when (lo.line_object = 106 and lad.line_action in (90,142))
						then 0
					else ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				end) as  unit_net_amount, 

			Sum(Case
					when (lo.line_object = 106 and lad.line_action in (90,142))
						then 0
					else ISNULL(tdf.unit_disc_amount, 0)
				end) as unit_discount_amount,
						
			Sum(Case
					when (lo.line_object = 106 and lad.line_action in (90,142))
						then 0
					else ISNULL(tdf.unit_gross_amount, 0)
				end) as unit_gross_amount, 

			SUM(CASE
				WHEN 
					(lo.Line_Object IN (202, 204, 205, 206, 296) AND lad.line_action in (97,147))
					 then 0 
				ELSE ISNULL(tdf.units, 0)
				END) AS other_fees_units,

			------------------------------------------------------------------------------------
			--THESE LINE OBJECTS DO NOT HAVE ES VS NON-ES LINE ACTIONS, SO NO WAY TO BREAK OUT
			SUM(CASE
				WHEN lo.Line_Object IN (101, 294, 400, 401, 402, 403, 404, 410) THEN ISNULL(tdf.unit_disc_amount, 0) * CASE
					WHEN ISNULL(tdf.unit_gross_amount, 0) >= 0 THEN -1
					ELSE -1
				END
				ELSE 0
			END) AS giftcard_discount_amount,

			SUM(CASE
				WHEN lo.Line_Object IN (101, 294, 400, 401, 402, 403, 404, 410) THEN (ISNULL(tdf.unit_disc_amount, 0) - ISNULL(tdf.upsell_disc_allocated, 0)) * CASE
					WHEN ISNULL(tdf.unit_gross_amount, 0) >= 0 THEN -1
					ELSE -1
				END
				ELSE 0
			END) AS giftcard_discount_amount_Less_Upsell,

			SUM(CASE
				WHEN lo.Line_Object IN (101, 292) THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS donations_UGA,
			SUM(CASE
				WHEN lo.Line_Object IN (101, 292) THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS donations_units,
			SUM(CASE
				WHEN tdf.product_key = -18 THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS party_deposit_UGA,
			SUM(CASE
				WHEN tdf.product_key = -18 THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS party_deposit_units,
			SUM(CASE
				WHEN lo.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS giftcard_UGA,
			SUM(CASE
				WHEN lo.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) giftcard_units,

			SUM(CASE
				WHEN lo.Line_Object = 291 THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS cub_cash_UGA,
			SUM(CASE
				WHEN lo.Line_Object = 291 THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS cub_cash_units,
			SUM(CASE
				WHEN lo.Line_Object IN (700, 701, 710, 711, 712, 713, 714) THEN ISNULL(tdf.unit_gross_amount, 0) * -1
				ELSE 0
			END) AS paid_outs_UGA,
			SUM(CASE
				WHEN lo.Line_Object IN (700, 701, 710, 711, 712, 713, 714) THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) * -1 AS paid_outs_units,
			SUM(CASE
				WHEN lo.Line_Object IN (210, 250) THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS stuffing_supplies_UGA,
			SUM(CASE
				WHEN lo.Line_Object IN (210, 250) THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS stuffing_supplies_units,

			------------------------------------------------------------------------------------


----NEXT BATCH OF MEASURES ARE ALL GAAP / STORE SALES RELATED
/*
		ES LINE_ACTIONS:
		7	ordered -- ORDER
		8	order cancelled -- CANCEL
		90	order delivered -- FULFILLMENT
		142	order picked up -- FULFILLMENT
		99	delivery returned -- RETURN
*/

--======== BEGIN NON ES --=================
			SUM(CASE
				WHEN lo.Line_Object IN (100, 102, 103, 104, 115) AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS merchandise_UGA,
			SUM(CASE
				WHEN lo.Line_Object IN (100, 102, 103, 104, 115) AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS merchandise_NetAmount,
			SUM(CASE
				WHEN lo.Line_Object IN (100, 102, 103, 104, 115) AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS merchandise_units,
			SUM(CASE
				WHEN lo.Line_Object IN (100, 102, 103, 104, 115) AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.ext_cost, 0)
				ELSE 0
			END) AS merchandise_cost,
			SUM(CASE
				WHEN lo.Line_Object IN (100, 102, 103, 104, 115) AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') AND
				ISNULL(tdf.units, 0) <> 0 THEN 1
				ELSE 0
			END) AS hasGAAPUnits,
--======== END NON ES =================--

--======== BEGIN ES ORDERS / CANCELS --=================
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (7,8))) 
					 )	
						AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS ES_Order_UGA,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (7,8)))
					 )	
						AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS ES_Order_NetAmount,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (7,8)))
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS ES_Order_units,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (7,8)))
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.ext_cost, 0)
				ELSE 0
			END) AS ES_Order_cost,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (7,8)))
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01')
				then 1
				else 0
			END) AS hasESOrderUnits,

--======== END ES ORDERS / CANCELS --=================

--======== BEGIN ES FULFILLMENTS --=================

		SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (90,142))) 
					 )	
						AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS ES_Fulfillment_UGA,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (90,142))) 
					 )	
						AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS ES_Fulfillment_NetAmount,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (90,142))) 
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS ES_Fulfillment_units,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (90,142))) 
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.ext_cost, 0)
				ELSE 0
			END) AS ES_Fulfillment_cost,
			SUM(CASE
				WHEN (
						(lo.line_object = 106 and (lad.line_action in (90,142))) 
					 )
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') AND
				ISNULL(tdf.units, 0) <> 0 THEN 1
				ELSE 0
			END) AS hasESFulfillmentUnits,

--======== END ES FULFILLMENT --=================

--======== BEGIN ES RETURNS --===========

		SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (99))) 
					 )	
						AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS ES_Return_UGA,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (99))) 
					 )	
						AND
				RIGHT(p.subclass_code, 8) NOT IN ('57-01-01') THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
				ELSE 0
			END) AS ES_Return_NetAmount,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (99))) 
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS ES_Return_units,
			SUM(CASE
				WHEN (
						 (lo.line_object = 106 and (lad.line_action in (99))) 
					 )	
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') THEN ISNULL(tdf.ext_cost, 0)
				ELSE 0
			END) AS ES_Return_cost,
			SUM(CASE
				WHEN (
						(lo.line_object = 106 and (lad.line_action in (99))) 
					 )
						AND
				RIGHT(p.department_code, 2) NOT IN ('45', '46', '47', '49', '50', '51', '55', '60', '70', '75', '80', '85') AND
				RIGHT(p.subclass_code, 8) NOT IN ('48-06-01', '57-01-01') AND
				ISNULL(tdf.units, 0) <> 0 THEN 1
				ELSE 0
			END) AS hasESReturnUnits,
--======== END ES RETURNS ===========--
			
			------------------------------------------------------------------------------------------------------------------------
			--these columns are from 'store sale' perspective (gaap + es order/cancel + es return) (---EXCLUDES ES FULFILLMENT---)
			------------------------------------------------------------------------------------------------------------------------
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Animal' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
								THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
						ELSE 0
						END, 0)) AS animal_UGA,
			SUM(CASE WHEN p.ScorecardCategory = 'Animal' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.units, 0)
					ELSE 0
					END) AS animal_units,
			SUM(CASE WHEN p.ScorecardCategory = 'Animal' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) ) 
						THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END) AS animal_cost,
			SUM(ISNULL(CASE WHEN  p.ScorecardCategory = 'Footwear' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
								THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS footwear_UGA,
			SUM(CASE WHEN p.ScorecardCategory = 'Footwear' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) ) 
						THEN ISNULL(tdf.units, 0)
					ELSE 0
					END) AS footwear_units,
			SUM(CASE WHEN p.ScorecardCategory = 'Footwear' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) ) 
						THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END) AS footwear_cost,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Accessories' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
								THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS accessories_UGA,
			SUM(CASE WHEN p.ScorecardCategory = 'Accessories' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) ) 
						THEN ISNULL(tdf.units, 0)
					ELSE 0
					END) AS accessories_units,
			SUM(CASE WHEN p.ScorecardCategory = 'Accessories' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) ) 
							THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END) AS accessories_cost,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Sounds' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS sounds_UGA,
			SUM(CASE WHEN p.ScorecardCategory = 'Sounds' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.units, 0)
					ELSE 0
					END) AS sounds_units,
			SUM(CASE WHEN p.ScorecardCategory = 'Sounds' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END) AS sounds_cost,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Scents' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS Scents_UGA,
			SUM(CASE WHEN p.ScorecardCategory = 'Scents' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.units, 0)
					ELSE 0
					END) AS Scents_units,
			SUM(CASE WHEN p.ScorecardCategory = 'Scents' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END) AS Scents_cost,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Clothing' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
								THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS clothing_UGA,
			SUM(CASE WHEN p.ScorecardCategory = 'Clothing' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.units, 0)
					ELSE 0
					END) AS clothing_units,
			SUM(CASE WHEN p.ScorecardCategory = 'Clothing' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END) AS clothing_cost,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Sports' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS sports_UGA,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Sports' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.units, 0)
					ELSE 0
					END, 0)) AS sports_units,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Sports' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
							THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END, 0)) AS sports_cost,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Prestuffed' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.unit_gross_amount - tdf.unit_disc_amount, 0)
					ELSE 0
					END, 0)) AS prestuffed_UGA,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Prestuffed' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.units, 0)
					ELSE 0
					END, 0)) AS prestuffed_units,
			SUM(ISNULL(CASE WHEN p.ScorecardCategory = 'Prestuffed' and (lo.line_object <> 106 and lad.line_action NOT in (90,142) )
						THEN ISNULL(tdf.ext_cost, 0)
					ELSE 0
					END, 0)) AS prestuffed_cost,

			------------------------------------------------------------------------------------------------------------------------
			-- OTHER UGA and Units are computed below
/*
	LINE_ACTIONS
	95	charged on order --ORDER
	96	refunded on order cancellation --CANCEL
	97	recognized on order delivery --FULFILLMENT
	147	recognized on order pickup --FULFILLMENT
	98	refunded on delivery return --RETURN

*/

			--EXCLUDES ES 
			SUM(CASE
				WHEN 
					(
						lo.Line_Object IN (200, 203, 215) 
					and lad.line_action NOT in (95,96,97,98,147)
					) THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0
			END) AS shipping_UGA,
					
					-- INCLUDES ES ORDER, CANCEL
					SUM(CASE
						WHEN 
							(
								lo.Line_Object IN (200, 203, 215) 
							and lad.line_action in (95,96)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS StoreOrder_shipping_UGA,

					--INCLUDES ES FULFILLMENT
					SUM(CASE
						WHEN 
							(
								lo.Line_Object IN (200, 203, 215) 
							and lad.line_action in (97,147)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS StoreFulfillment_shipping_UGA,

					--INCLUDES ES RETURN
					SUM(CASE
						WHEN 
							(
								lo.Line_Object IN (200, 203, 215) 
							and lad.line_action in (98)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS StoreReturn_shipping_UGA,

			--EXCLUDES ES
			SUM(CASE
				WHEN 
					(
						lo.Line_Object IN (200, 203, 215) 
					and lad.line_action NOT in (95,96,97,98,147)
					) THEN ISNULL(tdf.units, 0)
				ELSE 0
			END) AS shipping_units,
					
					-- INCLUDES ES ORDER, CANCEL
					SUM(CASE
						WHEN 
							(
								lo.Line_Object IN (200, 203, 215) 
							and lad.line_action in (95,96)
							) THEN ISNULL(tdf.units, 0)
						ELSE 0
					END) AS StoreOrder_shipping_units,

					--INCLUDES ES FULFILLMENT
					SUM(CASE
						WHEN 
							(
								lo.Line_Object IN (200, 203, 215) 
							and lad.line_action in (97,147)
							) THEN ISNULL(tdf.units, 0)
						ELSE 0
					END) AS StoreFulfillment_shipping_units,
					
					--INCLUDES ES RETURN 
					SUM(CASE
						WHEN 
							(
								lo.Line_Object IN (200, 203, 215) 
							and lad.line_action in (98)
							) THEN ISNULL(tdf.units, 0)
						ELSE 0
					END) AS StoreReturn_shipping_units,

			--EXCLUDES ES
			SUM(CASE
				WHEN 
					(
						lo.Line_Object IN (202, 204, 205, 206, 296) 
					and lad.line_action NOT in (95,96,97,98,147)
					) THEN ISNULL(tdf.unit_gross_amount, 0)
				ELSE 0 
			END) AS other_fees_UGA,
					
					-- INCLUDES ES ORDER, CANCEL
					SUM(CASE	
						WHEN 
							(
								lo.Line_Object IN (202, 204, 205, 206, 296) 
							and lad.line_action in (95,96)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS StoreOrder_other_fees_UGA,

					--INCLUDES ES FULFILLMENT
					SUM(CASE	
						WHEN 
							(
								lo.Line_Object IN (202, 204, 205, 206, 296) 
							and lad.line_action in (97,147)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS StoreFulfillment_other_fees_UGA,

					--INCLUDES ES RETURN
					SUM(CASE	
						WHEN 
							(
								lo.Line_Object IN (202, 204, 205, 206, 296) 
							and lad.line_action in (98)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS StoreReturn_other_fees_UGA,
				------------------
				--ALL RETURNS - SIMPLY LOOKING AT LINE ACTION 2 AND 99
				SUM(CASE	
						WHEN 
							(
								lad.line_action in (2,99)
							) THEN ISNULL(tdf.unit_gross_amount, 0)
						ELSE 0
					END) AS ReturnUGA,
				SUM(CASE
						WHEN 
							(
								lad.line_action in (2,99)
							) THEN ISNULL(tdf.units, 0)
						ELSE 0
					END) AS ReturnUnits

		INTO #tmpTDF
		FROM
			dbo.TransactionDetailFactsDynamics tdf WITH (NOLOCK)
			INNER JOIN #tmpTrans stg ON	tdf.transaction_id = stg.transaction_id  --load only transactions added or updated in tdf
			LEFT OUTER JOIN dbo.line_object_dim lo WITH (NOLOCK) ON lo.Line_Object_Key = tdf.Line_Object_Key
			LEFT OUTER JOIN dbo.product_dim p WITH (NOLOCK) ON p.product_key = tdf.product_key
			LEFT OUTER JOIN dbo.line_action_dim lad with (nolock) on tdf.line_action_key = lad.line_action_key
		WHERE
			tdf.transaction_line_seq > 0
		GROUP BY tdf.transaction_id

--========================================================--
--====BUILD TRANSACTION FACTS======================--
--========================================================--

IF OBJECT_ID('dwstaging..TransactionFactsDynamicsStage') IS NOT NULL DROP TABLE dwstaging.dbo.TransactionFactsDynamicsStage
SELECT
		t.transaction_id,
		isnull(es.store_key, ath.store_key) as store_key,
		ath.date_key,
		ath.time_key,
		ISNULL(ttd.transaction_key, 0) AS transaction_type_key,
		ath.currency_key,
		CAST(ath.transaction_id AS varchar) + '-' + CAST(ath.store_key AS varchar) + '-' + CAST(ath.date_key AS varchar) AS transaction_key,
		ath.transaction_no,
		ath.register_no,
		ISNULL(cte.line_count, 0) as line_count,
		CASE
			WHEN ath.party_y_n = 'y' THEN 1
			ELSE 0
		END AS party_flag,

		CASE
			WHEN cte.hasGAAPUnits > 0 or cte.hasESFulfillmentUnits > 0 or cte.hasESReturnUnits > 0 
				THEN 1
			ELSE 0
		END AS GAAP_transaction_flag,

		CASE
			WHEN cte.hasGAAPUnits > 0 or cte.hasESOrderUnits > 0 or cte.hasESReturnUnits > 0 
				THEN 1
			ELSE 0
		END AS Store_transaction_flag,

		CASE
			WHEN cte.hasGAAPUnits = 0 and (cte.hasESOrderUnits > 0 or cte.hasESReturnUnits > 0) 
				THEN 1
			ELSE 0
		END AS Enterprise_selling_only_flag,

		CASE
			WHEN cte.Merchandise_UGA = 0 AND
			cte.Donations_UGA <> 0 AND
			cte.giftcard_UGA = 0 AND
			cte.Party_Deposit_UGA = 0 THEN 1
			ELSE 0
		END AS donation_only_flag,
		CASE
			WHEN cte.Merchandise_UGA = 0 AND
			cte.Donations_UGA = 0 AND
			cte.giftcard_UGA <> 0 AND
			cte.Party_Deposit_UGA = 0 THEN 1
			ELSE 0
		END AS giftcard_only_flag,
		CASE
			WHEN cte.Merchandise_UGA = 0 AND
			cte.Donations_UGA = 0 AND
			cte.giftcard_UGA = 0 AND
			cte.Party_Deposit_UGA <> 0 THEN 1
			ELSE 0
		END AS party_deposit_only_flag,

		--GAAP INCLUDES ES FULFILLMENTS AND RETURNS
		ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Fulfillment_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreFulfillment_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreFulfillment_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			- ISNULL(cte.giftcard_discount_amount_Less_Upsell, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Cub_Cash_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreFulfillment_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			+ ISNULL(tender.buy_stuff_amount, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreFulfillment_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreFulfillment_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)
			+ ISNULL(cte.stuffing_supplies_UGA, 0) --no es vs non-es line action breakout possible
		AS GAAP_sales_amount,

		ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Order_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreOrder_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreOrder_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			- ISNULL(cte.giftcard_discount_amount_Less_Upsell, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Cub_Cash_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			+ ISNULL(tender.buy_stuff_amount, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreOrder_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreOrder_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)
			+ ISNULL(cte.stuffing_supplies_UGA, 0) --no es vs non-es line action breakout possible
		AS Store_sales_amount,

		ISNULL(cte.ES_Order_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(df.StoreOrder_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.StoreOrder_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			--- ISNULL(cte.giftcard_discount_amount_Less_Upsell, 0) --no es vs non-es line action breakout possible
			--+ ISNULL(cte.Cub_Cash_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			--+ ISNULL(tender.buy_stuff_amount, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.StoreOrder_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.StoreOrder_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)
			--+ ISNULL(cte.stuffing_supplies_UGA, 0) --no es vs non-es line action breakout possible
		AS Enterprise_selling_amount,

		--HANDLED AS STORE SALE, SO WILL INCLUDE ES ORDER, CANCELS AND RETURN
		ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Order_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreOrder_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreOrder_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			+ ISNULL(tender.redemption_amount, 0) --no tender breakout
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			+ ISNULL(cte.giftcard_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Cub_Cash_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Party_Deposit_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreOrder_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreOrder_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)
			+ ISNULL(cte.stuffing_supplies_UGA, 0) --no es vs non-es line action breakout possible
		AS net_sales_amount,

		ISNULL(cte.total_units, 0) as total_units,
		ISNULL(cte.unit_net_amount, 0) as unit_net_amount,
		ISNULL(cte.unit_gross_amount, 0) as unit_gross_amount,
		ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0) as reward_certificate_amount,
		ISNULL(tender.buy_stuff_amount, 0) as buy_stuff_amount ,
		ISNULL(tender.tax_amount, 0) as tax_amount,

		ISNULL(tender.redemption_amount, 0) 
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0) as redemption_amount,

		ISNULL(cte.unit_discount_amount, 0) as unit_discount_amount,
		ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreOrder_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0) as coupon_discount_amount,
		ISNULL(df.coupon_discount_units, 0) + ISNULL(df.StoreOrder_coupon_discount_units, 0) + ISNULL(df.StoreReturn_coupon_discount_units, 0) as coupon_discount_units,
		ISNULL(cte.giftcard_discount_amount, 0) as giftcard_discount_amount,
		ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreOrder_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0) as total_discount_amount,
		 
		(ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Order_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(cte.giftcard_UGA, 0) 
			+ ISNULL(cte.Donations_UGA, 0) 
			+ ISNULL(cte.stuffing_supplies_UGA, 0) 
			+ ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreOrder_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreOrder_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			+ ISNULL(cte.Party_Deposit_UGA, 0) 
			+ ISNULL(tender.tax_amount, 0) 
			+ ISNULL(tender.redemption_amount, 0) 
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			+ ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreOrder_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreOrder_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)) 
		AS receipt_total_amount,

		ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Order_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0) as merchandise_uga,

		ISNULL(cte.merchandise_units, 0) + ISNULL(cte.ES_Order_units, 0) + ISNULL(cte.ES_Return_units, 0) as merchandise_units,
		ISNULL(cte.merchandise_units, 0) + ISNULL(cte.ES_Order_units, 0) + ISNULL(cte.ES_Return_units, 0) as Store_units,
		ISNULL(cte.merchandise_units, 0) + ISNULL(cte.ES_Fulfillment_units, 0) + ISNULL(cte.ES_Return_units, 0) as Gaap_units,
		ISNULL(cte.ES_Order_units, 0) as Enterprise_selling_units,

		ISNULL(cte.Donations_UGA, 0) as Donations_UGA,
		ISNULL(cte.donations_units, 0) as donations_units,
		ISNULL(cte.Party_Deposit_UGA, 0) as Party_Deposit_UGA,
		ISNULL(cte.party_deposit_units, 0) as party_deposit_units,
		ISNULL(cte.giftcard_UGA, 0) as giftcard_UGA,
		ISNULL(cte.giftcard_units, 0) as giftcard_units,
		ISNULL(cte.animal_UGA, 0) as animal_UGA,
		ISNULL(cte.animal_units, 0) as animal_units,

		ISNULL(cte.merchandise_NetAmount, 0) + ISNULL(cte.ES_Order_NetAmount, 0) + ISNULL(cte.ES_Return_NetAmount, 0)
			- ISNULL(cte.animal_UGA, 0) 
		AS non_animal_UGA,

		ISNULL(cte.merchandise_units, 0) + ISNULL(cte.ES_Order_units, 0) + ISNULL(cte.ES_Return_units, 0)
			- ISNULL(cte.animal_units, 0) 
		AS non_animal_units,

		ISNULL(cte.Footwear_UGA, 0) as Footwear_UGA,
		ISNULL(cte.footwear_units, 0) as footwear_units,
		ISNULL(cte.accessories_UGA, 0) as accessories_UGA,
		ISNULL(cte.accessories_units, 0) as accessories_units,
		ISNULL(cte.sounds_UGA, 0) as sounds_UGA,
		ISNULL(cte.sounds_units, 0) as sounds_units,
		ISNULL(cte.Scents_UGA, 0) as Scents_UGA,
		ISNULL(cte.Scents_units, 0) as Scents_units,
		ISNULL(cte.Clothing_UGA, 0) as Clothing_UGA,
		ISNULL(cte.clothing_units, 0) as clothing_units,

		(ISNULL(merchandise_NetAmount, 0) + ISNULL(cte.ES_Order_NetAmount, 0) + ISNULL(cte.ES_Return_NetAmount, 0)
			- ISNULL(cte.animal_UGA, 0) 
			- ISNULL(accessories_UGA, 0)
			- ISNULL(Clothing_UGA, 0) 
			- ISNULL(Footwear_UGA, 0) 
			- ISNULL(sounds_UGA, 0) 
			- ISNULL(sports_UGA, 0)) 
		AS other_UGA,

		(ISNULL(merchandise_units, 0) + ISNULL(cte.ES_Order_units, 0) + ISNULL(cte.ES_Return_units, 0)
			- ISNULL(animal_units, 0) 
			- ISNULL(accessories_units, 0)
			- ISNULL(clothing_units, 0) 
			- ISNULL(footwear_units, 0) 
			- ISNULL(sounds_units, 0) 
			- ISNULL(sports_units, 0)) 
		AS other_units,

		ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreFulfillment_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0) as Shipping_UGA,
		ISNULL(cte.shipping_units, 0) + ISNULL(cte.StoreOrder_shipping_units, 0) + ISNULL(cte.StoreReturn_shipping_units, 0) as shipping_units,
		ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreFulfillment_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0) as Other_Fees_UGA,
		ISNULL(cte.other_fees_units, 0) as other_fees_units,
		ISNULL(cte.Cub_Cash_UGA, 0) as Cub_Cash_UGA,
		ISNULL(cte.cub_cash_units, 0) as cub_cash_units,
		ISNULL(cte.paid_outs_UGA, 0) as paid_outs_UGA,
		ISNULL(cte.paid_outs_units, 0) as paid_outs_units,
		ISNULL(cte.stuffing_supplies_UGA, 0) as stuffing_supplies_UGA,
		ISNULL(cte.stuffing_supplies_units, 0) as stuffing_supplies_units,
		ISNULL(cte.sports_UGA, 0) as sports_UGA,
		ISNULL(cte.sports_units, 0) as sports_units,
		ISNULL(cte.Prestuffed_UGA, 0) as Prestuffed_UGA,
		ISNULL(cte.prestuffed_units, 0) as prestuffed_units,
		ISNULL(df.upsell_discount_amount, 0) + ISNULL(df.StoreOrder_upsell_discount_amount, 0) + ISNULL(df.StoreReturn_upsell_discount_amount, 0) as upsell_discount_amount,

		ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Fulfillment_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreFulfillment_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreFulfillment_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			- ISNULL(cte.giftcard_discount_amount_Less_Upsell, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Cub_Cash_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreFulfillment_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			+ ISNULL(tender.buy_stuff_amount, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreFulfillment_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreFulfillment_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)
			+ ISNULL(cte.stuffing_supplies_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.upsell_discount_amount, 0) + ISNULL(df.StoreFulfillment_upsell_discount_amount, 0) + ISNULL(df.StoreReturn_upsell_discount_amount, 0)
		AS fin_GAAP_sales_amount,

		ISNULL(cte.Merchandise_UGA, 0) + ISNULL(cte.ES_Order_UGA, 0) + ISNULL(cte.ES_Return_UGA, 0)
			+ ISNULL(df.coupon_discount_amount, 0) + ISNULL(df.StoreOrder_coupon_discount_amount, 0) + ISNULL(df.StoreReturn_coupon_discount_amount, 0)
			+ ISNULL(df.total_discount_amount, 0) + ISNULL(df.StoreOrder_total_discount_amount, 0) + ISNULL(df.StoreReturn_total_discount_amount, 0)
			- ISNULL(cte.giftcard_discount_amount_Less_Upsell, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Cub_Cash_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.reward_certificate_amount, 0) + ISNULL(df.StoreOrder_reward_certificate_amount, 0) + ISNULL(df.StoreReturn_reward_certificate_amount, 0)
			+ ISNULL(tender.buy_stuff_amount, 0) --no es vs non-es line action breakout possible
			+ ISNULL(cte.Shipping_UGA, 0) + ISNULL(cte.StoreOrder_shipping_UGA, 0) + ISNULL(cte.StoreReturn_shipping_UGA, 0)
			+ ISNULL(cte.Other_Fees_UGA, 0) + ISNULL(cte.StoreOrder_other_fees_UGA, 0) + ISNULL(cte.StoreReturn_other_fees_UGA, 0)
			+ ISNULL(cte.stuffing_supplies_UGA, 0) --no es vs non-es line action breakout possible
			+ ISNULL(df.upsell_discount_amount, 0) + ISNULL(df.StoreFulfillment_upsell_discount_amount, 0) + ISNULL(df.StoreReturn_upsell_discount_amount, 0)
		AS fin_Store_sales_amount,

		ath.cashier_key,
		ISNULL(cte.merchandise_cost, 0) + ISNULL(cte.ES_Order_cost, 0) + ISNULL(cte.ES_Return_cost, 0) as merchandise_cost,
		ISNULL(cte.animal_cost, 0) as animal_cost,

		ISNULL(cte.merchandise_cost, 0) 
			- ISNULL(cte.animal_cost, 0) 
		AS non_animal_cost,

		ISNULL(cte.footwear_cost, 0) as footwear_cost,
		ISNULL(cte.accessories_cost, 0) as accessories_cost,
		ISNULL(cte.sounds_cost, 0) as sounds_cost,
		ISNULL(cte.Scents_cost, 0) as Scents_cost,
		ISNULL(cte.clothing_cost, 0) as clothing_cost,

		(ISNULL(merchandise_cost, 0) + ISNULL(cte.ES_Order_cost, 0) + ISNULL(cte.ES_Return_cost, 0)
			- ISNULL(animal_cost, 0) 
			- ISNULL(accessories_cost, 0)
			- ISNULL(clothing_cost, 0) 
			- ISNULL(footwear_cost, 0) 
			- ISNULL(sounds_cost, 0) 
			- ISNULL(sports_cost, 0)) 
		AS other_cost,

		ISNULL(cte.sports_cost, 0) as sports_cost,
		ISNULL(cte.prestuffed_cost, 0) as prestuffed_cost,
		ISNULL(ath.party_master, 0) as party_master,
		ISNULL(df.EmployeeDiscount,0) as EmployeeDiscountUGA,
		ISNULL(cte.ReturnUGA,0) as ReturnUGA,
		ISNULL(cte.ReturnUnits,0) as ReturnUnits,
		ISNULL(ath.party_key, 0) as party_key,
		w.OrderNum as WebOrderNumber,
		isnull(w.isPickupFromStore,0) as isPickupFromStore,
		isnull(w.isShipFromStore,0) as isShipFromStore,
		isnull(w.isCurbside,0) as isCurbside,
		isnull(w.isSameDay,0) as isSameDayShipt
	into dwstaging.dbo.TransactionFactsDynamicsStage
	FROM
		#tmpTrans t WITH (NOLOCK)
		INNER JOIN DWStaging.dbo.aw_Transaction_Header ath WITH (NOLOCK)
			ON t.transaction_id = ath.transaction_id
		LEFT JOIN #tmpTDF cte WITH (NOLOCK)
			ON cte.transaction_id = t.transaction_id
		LEFT OUTER JOIN #tmpDiscounts df
			ON df.transaction_id = t.transaction_id
		LEFT OUTER JOIN #tmpTender tender
			ON t.transaction_id = tender.transaction_id
		LEFT JOIN Transaction_Type_Dim ttd WITH (NOLOCK)
			ON ath.transaction_type = ttd.transaction_type
		LEFT OUTER JOIN tmpESRef es
			ON t.transaction_id = es.transaction_id
		left join DWStaging.dbo.WebToStoreLookup w on ath.transaction_id=w.transaction_id
```

