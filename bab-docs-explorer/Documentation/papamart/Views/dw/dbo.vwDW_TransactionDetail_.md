# dbo.vwDW_TransactionDetail_

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_TransactionDetail_"]
    dbo_transaction_detail_facts(["dbo.transaction_detail_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_detail_facts |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_TransactionDetail]
AS
SELECT product_key, currency_key, transaction_id, transaction_line_seq, register_num,
		channel_key, cashier_id, time_key, store_key, promotion_key, unit_gross_amount, transaction_detail_facts.date_key,
		units, unit_disc_amount, party_y_n, coupon_group_key, tender_group_key, transaction_type_key,
		line_object_key, party_deposit, non_merch, Party, Loyality, tdf_key, source_key, process_name,
		process_date, transaction_no, CASE party_y_n WHEN 'y' THEN 1 ELSE 0 END AS PartyFlag,
		CAST(transaction_id AS varchar) + '-' + CAST(store_key AS varchar) + '-' + CAST(transaction_detail_facts.date_key AS varchar) AS transaction_key
	FROM dbo.transaction_detail_facts WITH (NOLOCK)
	WHERE transaction_line_seq > 0
		--AND date_key >= (SELECT MIN(date_key) FROM date_dim d WHERE fiscal_year = (SELECT fiscal_year - 3 FROM date_dim d2 WHERE actual_date = convert(datetime, convert(char(10), getdate(), 101))))
		--AND date_key IN (2920,2921,2922,2923,2924,2925,2926,2927,2928,2929,2930,2931,2932,2933,2934,2935,2936,2937,2938,2939,2940,2941,2942,2943,2944,2945,2946,2947,3284,3285,3286,3287,3288,3289,3290,3291,3292,3293,3294,3295,3296,3297,3298,3299,3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311)
```

