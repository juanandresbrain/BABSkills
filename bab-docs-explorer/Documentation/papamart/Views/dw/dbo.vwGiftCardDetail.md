# dbo.vwGiftCardDetail

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwGiftCardDetail"]
    dbo_GiftCard_Detail(["dbo.GiftCard_Detail"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.GiftCard_Detail |

## View Code

```sql
CREATE view [dbo].[vwGiftCardDetail] 
as
SELECT [merchant_id] as original_merchant_id
		,case when ([merchant_id] is null ) or ([merchant_id] not in ('97001100007','97016000002','97020300000','97032000002','97088700000',
		'97136200003','97153900006','99909049997','99909049998','99909049999','99089599997','99089599998',
		'99087799999','99085839999','37020300000','37023000000','37032000002','99084239999','37023000002',
		'97023100239','19708','29708','97005600002','97088750003','60312233979','60312247248','60312255649')) 
		then '97020300000' else [merchant_id] end as [merchant_id]
	  ,[alternate_merchant_number] as original_alt_merchant_no
      ,case when [alternate_merchant_number] is null 
	   then '0' else [alternate_merchant_number] end as [alternate_merchant_number]
        ,[store_key] as [orginal_store_key]
      ,case when ((alternate_merchant_number <> 0) and ([store_key] is null or store_key < 1) ) then -50 
		else [store_key] end as [store_key]
      ,[terminal_id]
      ,[account_number]
      ,[request_code]
      ,[transaction_amount]
      ,[base_amount]
      ,[reporting_amount]
      ,[response_code]
      ,[source_code]
      ,[clerk_id]
      ,[reversal_flag]
      ,[balance]
      ,[consortium_code]
      ,[promotion_code]
      ,[FDMS_local_timestamp]
	  ,cast(convert(varchar(10),dbo.GiftCard_Detail.FDMS_local_timestamp,101) 
		as datetime) TransactionDate
      ,[escheatable_transaction]
	  ,cast(convert(varchar(10),dbo.GiftCard_Detail.processed_date,101) 
		as datetime) [processed_date]
      ,[original_request_code]
      ,[internal_request_code]
 	  ,cast(convert(varchar(10),dbo.GiftCard_Detail.exported_date,101) 
		as datetime) [exported_date]
  FROM [dw].[dbo].[GiftCard_Detail]

WHERE internal_request_code in (8,18,28,43,68,155,23,167,1) --and (alternate_merchant_number <> 0 and store_key = 0)
```

