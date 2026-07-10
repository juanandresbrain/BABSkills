# dbo.fnGetCubeSQL

**Database:** dw  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** varchar(8000)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnGetCubeSQL"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @p_start_key | varchar | 100 | NO |
| @p_end_key | varchar | 100 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION fnGetCubeSQL
(
	@p_start_key varchar(100)
	, @p_end_key varchar(100)
)
RETURNS varchar(8000)
AS
BEGIN
	
	declare @w_SQL varchar(8000)
	set @w_SQL = 'SELECT 	tdf.tdf_key as underlying_table_key
			  , ''tdf'' as source
			  , tdf.[currency_key]
			  ,	tdf.[transaction_id]
			  , tdf.[product_key]
			  , tdf.[store_key]
		  , tdf.[date_key]
			  , tdf.[time_key]
			  , tdf.register_num
			  , tdf.cashier_id
			  ,	CASE tdf.party_y_n WHEN ''y'' THEN 1 ELSE 0 END AS PartyFlag  
			  , tdf.party_y_n
			  , tdf.transaction_type_key
			  , tdf.transaction_no
			  , tdf.reference_no
			  , tdf.[line_object_key]
			  , null as [coupon_key]
			  , tdf.[unit_gross_amount]
			  , tdf.[units]
			  , tdf.[unit_disc_amount]
  			  , null as tender_key 
			  , null as tender_amount			
			,isnull(CASE WHEN (tdf.unit_gross_amount > 0 AND tdf.unit_disc_amount > 0) 
										THEN tdf.unit_gross_amount - tdf.unit_disc_amount
										WHEN (tdf.unit_gross_amount > 0 AND tdf.unit_disc_amount < 0)
										THEN tdf.unit_gross_amount - tdf.unit_disc_amount
										WHEN (tdf.unit_gross_amount < 0 AND tdf.unit_disc_amount > 0)
										THEN tdf.unit_gross_amount + tdf.unit_disc_amount
										WHEN (tdf.unit_gross_amount < 0 AND tdf.unit_disc_amount < 0)	
										THEN tdf.unit_gross_amount + tdf.unit_disc_amount
										WHEN (tdf.unit_gross_amount = 0 AND tdf.unit_disc_amount < 0)
										THEN tdf.unit_gross_amount + tdf.unit_disc_amount
										WHEN (tdf.unit_gross_amount = 0 AND tdf.unit_disc_amount > 0)
										THEN tdf.unit_gross_amount - tdf.unit_disc_amount
										WHEN (tdf.unit_disc_amount = 0)
										THEN tdf.unit_gross_amount 
										ELSE tdf.unit_gross_amount
						END,0) as [unit_net_amount]

			, isnull(CASE WHEN tdf.unit_gross_amount >= 0 AND tdf.line_object_key IN (490,16,18,19,20,21,22,227) 
						THEN (tdf.unit_disc_amount*-1)
						WHEN tdf.unit_gross_amount < 0  AND 
						tdf.line_object_key IN (490,16,18,19,20,21,22,227)
						THEN tdf.unit_disc_amount END ,0) as [GiftCardDiscountInc101]

			, isnull(CASE WHEN tdf.unit_gross_amount >= 0 AND tdf.line_object_key IN (16,18,19,20,21,22,227) 
						THEN (tdf.unit_disc_amount*-1)
						WHEN tdf.unit_gross_amount < 0  AND 
						tdf.line_object_key IN (16,18,19,20,21,22,227)
						THEN tdf.unit_disc_amount END ,0) as [GiftCardDiscount]
			  FROM dw.dbo.[transaction_detail_facts] tdf WITH (NOLOCK) 
				where tdf.date_key between ' + @p_start_key  + ' and ' + @p_end_key + '
		UNION ALL
		SELECT  df.uid as underlying_table_key
			  , ''df'' as source
			  , tdf.[currency_key]
			  ,	df.[transaction_id]
			  , null as [product_key]
			  , df.[store_key]
			  , df.[date_key]
			  , tdf.[time_key]
			  , tdf.register_num
			  , tdf.cashier_id
			  ,	tdf.PartyFlag  
			  , tdf.party_y_n
			  , tdf.transaction_type_key
			  , tdf.transaction_no
			  , df.reference_no
			  , df.[line_object_key]
			  , df.[coupon_key]
			  , df.[unit_gross_amount]
			  , df.[units]
			  , null as [unit_disc_amount]
  			  , null as tender_key 
			  , null as tender_amount
			  , null as [unit_net_amount]
			  , null as [GiftCardDiscountInc101]
			  , null as [GiftCardDiscount]
			from dw.dbo.[discount_facts] df WITH (NOLOCK) 

			left join (select tdf.[transaction_id]
					  , tdf.[store_key]
					  , tdf.[date_key]
					  , tdf.[currency_key]
					  , tdf.[time_key]
					  , tdf.register_num
					  , tdf.cashier_id
					  ,	CASE tdf.party_y_n WHEN ''y'' THEN 1 ELSE 0 END AS PartyFlag  
					  , tdf.party_y_n
					  , tdf.transaction_type_key
					  , tdf.transaction_no
					from dw.dbo.transaction_detail_facts tdf with (nolock)
					group by tdf.[transaction_id]
					  , tdf.[store_key]
					  , tdf.[date_key]
					  , tdf.[currency_key]
					  , tdf.[time_key]
					  , tdf.register_num
					  , tdf.cashier_id
					  , tdf.party_y_n
					  , tdf.transaction_type_key
					  , tdf.transaction_no) tdf
			on		 df.transaction_id = tdf.transaction_id and
				 df.store_key = tdf.store_key and 
				 df.date_key = tdf.date_key

			where df.date_key between ' + @p_start_key  + ' and ' + @p_end_key + '
		UNION ALL
		SELECT 	tgd.[tender_group_key] as underlying_table_key
			  , ''tgd'' as source
			  , tdf.[currency_key]
			  ,	tdf.[transaction_id]
			  , null as [product_key]
			  , tdf.[store_key]
			  , tdf.[date_key]
			  , tdf.[time_key]
			  , tdf.register_num
			  , tdf.cashier_id
			  ,	tdf.PartyFlag  
			  , tdf.party_y_n
			  , tdf.transaction_type_key
			  , tdf.transaction_no
			  , null as reference_no
			  , null as [line_object_key]
			  , null as [coupon_key]
			  , null as [unit_gross_amount] 
			  , null as [units]
			  , null as [unit_disc_amount]
  			  , tgd.tender_key 
			  , tgd.tender_amt  as tender_amount
			  , null as [unit_net_amount]
			  , null as [GiftCardDiscountInc101]
			  , null as [GiftCardDiscount]
			from dw.dbo.tender_group_dim tgd 

			inner join (select tdf.[tender_group_key]
					  , tdf.[currency_key]
					  ,	tdf.[transaction_id]
					  , tdf.[store_key]
					  , tdf.[date_key]
					  , tdf.[time_key]
					  , tdf.register_num
					  , tdf.cashier_id
					  ,	CASE tdf.party_y_n WHEN ''y'' THEN 1 ELSE 0 END AS PartyFlag  
					  , tdf.party_y_n
					  , tdf.transaction_type_key
					  , tdf.transaction_no
					from dw.dbo.transaction_detail_facts tdf  with (nolock)
					where tdf.date_key between ' + @p_start_key  + ' and ' + @p_end_key + '
					group by  tdf.[tender_group_key]
					  , tdf.[currency_key]
					  ,	tdf.[transaction_id]
					  , tdf.[store_key]
					  , tdf.[date_key]
					  , tdf.[time_key]
					  , tdf.register_num
					  , tdf.cashier_id
					  ,	tdf.party_y_n
					  , tdf.transaction_type_key
					  , tdf.transaction_no) tdf
			on tgd.tender_group_key = tdf.tender_group_key '
	return @w_SQL

END
```

