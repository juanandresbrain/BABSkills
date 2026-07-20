# dbo.giftcard_detail_international_stage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_detail_international_stage"]
    dbo_giftcard_detail_international_stage(["dbo.giftcard_detail_international_stage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_detail_international_stage |

## View Code

```sql
; CREATE   VIEW [dbo].[giftcard_detail_international_stage] AS SELECT [FileID], [line_number], [merchant_id] COLLATE Latin1_General_CI_AS AS [merchant_id], [alternate_merchant_number], [store_key], [terminal_id], [terminal_transaction_number], [account_number] COLLATE Latin1_General_CI_AS AS [account_number], [request_code], [transaction_amount], [base_amount], [reporting_amount], [base_currency_code], [local_currency_code], [reporting_currency_code], [exchange_rate], [response_code], [source_code], [clerk_id] COLLATE Latin1_General_CI_AS AS [clerk_id], [reversal_flag] COLLATE Latin1_General_CI_AS AS [reversal_flag], [balance], [consortium_code], [promotion_code], [FDMS_local_timestamp], [terminal_local_timestamp], [replaced_by_account_number] COLLATE Latin1_General_CI_AS AS [replaced_by_account_number], [authcode] COLLATE Latin1_General_CI_AS AS [authcode], [userid] COLLATE Latin1_General_CI_AS AS [userid], [card_class], [expiration_date], [card_cost], [escheatable_transaction] COLLATE Latin1_General_CI_AS AS [escheatable_transaction], [reference_number] COLLATE Latin1_General_CI_AS AS [reference_number], [user1] COLLATE Latin1_General_CI_AS AS [user1], [user2] COLLATE Latin1_General_CI_AS AS [user2], [cashback], [base_cashback], [reporting_cashback], [local_lock_amount], [lock_amount], [reversed_timestamp], [processed_date], [original_request_code], [internal_request_code], [exported_date] FROM [dbo].[giftcard_detail_international_stage]
```

