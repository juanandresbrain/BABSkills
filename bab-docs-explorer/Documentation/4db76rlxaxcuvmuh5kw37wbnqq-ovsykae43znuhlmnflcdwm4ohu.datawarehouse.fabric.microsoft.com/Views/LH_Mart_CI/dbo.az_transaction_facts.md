# dbo.az_transaction_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.az_transaction_facts"]
    dbo_az_transaction_facts(["dbo.az_transaction_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.az_transaction_facts |

## View Code

```sql
;    CREATE  VIEW [dbo].[az_transaction_facts] AS     SELECT [transaction_id] COLLATE Latin1_General_CI_AS AS [transaction_id], [store_key], [date_key], [time_key], [transaction_type_key], [currency_key], [transaction_key] COLLATE Latin1_General_CI_AS AS [transaction_key], [party_key], [cashier_key], [transaction_no] COLLATE Latin1_General_CI_AS AS [transaction_no], [register_no], [line_count], [party_flag], [GAAP_transaction_flag], [donation_only_flag], [giftcard_only_flag], [party_deposit_only_flag], [GAAP_sales_amount], [net_sales_amount], [total_units], [unit_net_amount], [unit_gross_amount], [receipt_total_amount], [merchandise_uga], [merchandise_units], [donations_units], [party_deposit_units], [giftcard_units], [animal_units], [non_animal_units], [footwear_units], [accessories_units], [sounds_units], [clothing_units], [other_units], [sports_units], [prestuffed_units], [fin_GAAP_sales_amount], [upsell_discount_amount], [Store_transaction_flag], [Store_sales_amount], [Store_units], [fin_Store_sales_amount], [Enterprise_selling_amount], [Enterprise_selling_only_flag], [Gaap_units], [Enterprise_selling_units], [party_master], [ReturnUGA], [ReturnUnits], [isShipFromStore], [isPickupFromStore], [isCurbside], [isSameDayShipt], [WebOrderNumber] COLLATE Latin1_General_CI_AS AS [WebOrderNumber], [isWebGift]     FROM LH_Mart.[dbo].[az_transaction_facts]
```

