# dbo.vwPOSLoyaltyTransactionExtractAv

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSLoyaltyTransactionExtractAv"]
    av_customer(["av_customer"]) --> VIEW
    av_transaction_header(["av_transaction_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| av_customer |
| av_transaction_header |

## View Code

```sql
CREATE view [dbo].[vwPOSLoyaltyTransactionExtractAv]

as

with
Trans as
	(
		select 
			cast(max(c.customer_no) as varchar(20)) as customer_no,
			c.av_transaction_id
		from av_customer c with (nolock) 
		where 1=1
		and c.customer_role in (1,204) 
		and c.customer_no is not null
		and c.customer_no<>'0'
		and c.transaction_date between '05/03/2026' and '05/30/2026'
		group by 
			c.av_transaction_id
	),
Tranz as
	(
		select 
			t.customer_no,
			t.av_transaction_id
			--t.transaction_date
		from Trans t
		join av_customer c 
			on t.av_transaction_id=c.av_transaction_id
			and t.customer_no=c.customer_no
			and c.customer_role in (1,204) 
			and c.customer_no is not null
			and c.customer_no<>'0'
		join av_transaction_header th on t.av_transaction_id=th.av_transaction_id
		where 1=1
		--and cast(t.transaction_date as date) >= '02/04/2024' and store_no = 13
		group by 
			t.customer_no,
			t.av_transaction_id
	
	)
select
	t.customer_no as CustomerNumber,
	cast(t.av_transaction_id as int) as SATransactionID,
	NULL as LoyaltyTransactionType,
	0 as matchedByEMail
from Tranz t 
--join PAPAMART.dw.dbo.CRMCustomerDim cd on t.customer_no collate SQL_Latin1_General_CP1_CI_AS  =cd.CustomerNumber
group by 
	t.customer_no,
	cast(t.av_transaction_id as int)
```

