# dbo.vwPOS_JMC_SLS_TRANS_bak20230808

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOS_JMC_SLS_TRANS_bak20230808"]
    JMC_sls_retail_line_item(["JMC_sls_retail_line_item"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| JMC_sls_retail_line_item |

## View Code

```sql
--JMC_sls_trans

create view [dbo].[vwPOS_JMC_SLS_TRANS_bak20230808]
as 
select device_id,
	case 
		when left(device_id,1)='2'
			then left(device_id,4)
		else cast(right((cast('0000' as varchar) + cast(right(left(device_id,4),3) as varchar)),4) as int)
	end as StoreID,
	cast(right(device_id,3) as int) as RegisterNumber,
	cast(business_date as date) BusinessDate,	
	sequence_number,	
	line_sequence_number,	
	pos_item_id,	
	item_id,	
	item_description,	
	item_type,	
	regular_unit_price,	
	actual_unit_price,	
	loyalty_unit_price,	
	quantity,	
	extended_amount,	
	discount_amount,	
	extended_discounted_amount,	
	rtn_extended_discounted_amount,	
	tax_amount,	
	reason_code_group_id,	
	reason_code,
	disposition_code,	
	gift_receipt,	
	item_returnable,
	item_taxable,	
	quantity_avail_for_return,	
	item_discountable,	
	employee_discount_allowed,	
	item_price_overridable,	
	discount_applied,	
	damage_discount_applied,	
	tax_included_in_price,	
	tax_group_id,	
	orig_line_sequence_number,	
	orig_sequence_number,	
	orig_business_date,	
	orig_device_id,	
	orig_order_id,	
	orig_username,	
	orig_business_unit_id,	
	return_policy_id,	
	item_returned,	
	iso_currency_code,	
	tare_weight	item_weight,	
	item_weight_plus_tare,	
	weight_unit_of_measure,	
	weight_entry_method_code,	
	family_code,	
	item_length,	
	length_unit_of_measure,	
	quantity_modifiable,	
	save_value,	
	save_value_type,	
	coupon_allowed,	
	eletronic_coupon_allowed,	
	coupon_multiply_allowed,	
	username,	
	external_system_id,	
	product_id,	
	item_name,	
	item_long_description,	
	additional_classifiers,	
	order_line_number,	
	order_id,	
	line_item_type,	
	inquiry_method_code,	
	voided,	
	override_user_id,	
	entry_method_code,	
	create_time,	
	create_by,	
	last_update_time,	
	last_update_by,	
	stuff_info,	
	find_a_bear_id,	
	serialized_coupon_barcode,	
	classifier_class,	
	classifier_style,	
	classifier_brand,	
	classifier_department,	
	InsertDate,	
	UpdateDate
from JMC_sls_retail_line_item
```

