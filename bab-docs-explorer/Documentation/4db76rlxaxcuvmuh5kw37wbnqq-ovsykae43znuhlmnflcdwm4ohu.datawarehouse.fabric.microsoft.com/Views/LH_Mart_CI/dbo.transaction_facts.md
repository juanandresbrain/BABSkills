# dbo.transaction_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transaction_facts"]
    dbo_transaction_facts(["dbo.transaction_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_facts |

## View Code

```sql
;  --drop view [dbo].[transaction_facts]  CREATE   VIEW [dbo].[transaction_facts] AS     SELECT [transaction_id], [store_key], [date_key], [time_key], [transaction_type_key], [currency_key], [transaction_key] COLLATE Latin1_General_CI_AS AS [transaction_key], [transaction_no], [register_no], [line_count], [party_flag], [GAAP_transaction_flag], [donation_only_flag], [giftcard_only_flag], [party_deposit_only_flag], [GAAP_sales_amount], [net_sales_amount], [total_units], [unit_net_amount], [unit_gross_amount], [reward_certificate_amount], [buy_stuff_amount], [tax_amount], [redemption_amount], [unit_discount_amount], [coupon_discount_amount], [coupon_discount_units], [giftcard_discount_amount], [total_discount_amount], [receipt_total_amount], [merchandise_UGA], [merchandise_units], [donations_UGA], [donations_units], [party_deposit_UGA], [party_deposit_units], [giftcard_UGA], [giftcard_units], [animal_UGA], [animal_units], [non_animal_UGA], [non_animal_units], [footwear_UGA], [footwear_units], [accessories_UGA], [accessories_units], [sounds_UGA], [sounds_units], [clothing_UGA], [clothing_units], [other_UGA], [other_units], [shipping_UGA], [shipping_units], [other_fees_UGA], [other_fees_units], [cub_cash_UGA], [cub_cash_units], [paid_outs_UGA], [paid_outs_units], [stuffing_supplies_UGA], [stuffing_supplies_units], [sports_UGA], [sports_units], [prestuffed_UGA], [prestuffed_units], [fin_GAAP_sales_amount], [upsell_discount_amount], [cashier_key], [merchandise_cost], [animal_cost], [non_animal_cost], [footwear_cost], [accessories_cost], [sounds_cost], [clothing_cost], [other_cost], [sports_cost], [prestuffed_cost], [Scents_UGA], [Scents_units], [Scents_cost], [Store_transaction_flag], [Store_Sales_Amount], [Store_Units], [fin_Store_Sales_Amount], [Enterprise_Selling_Amount], [Enterprise_Selling_Only_Flag], [Gaap_Units], [Enterprise_Selling_Units], [party_master], [EmployeeDiscountUGA], [ReturnUGA], [ReturnUnits], [party_key], [isShipFromStore], [isPickupFromStore], [isCurbside], [isSameDayShipt], [webOrderNumber] COLLATE Latin1_General_CI_AS AS [webOrderNumber], [isWebGift]     FROM LH_Mart.[dbo].[transaction_facts]
```

