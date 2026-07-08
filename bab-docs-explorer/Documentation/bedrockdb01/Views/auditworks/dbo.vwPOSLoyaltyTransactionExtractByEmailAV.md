# dbo.vwPOSLoyaltyTransactionExtractByEmailAV

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSLoyaltyTransactionExtractByEmailAV"]
    dbo_CRMCustomerDim(["dbo.CRMCustomerDim"]) --> VIEW
    av_customer(["av_customer"]) --> VIEW
    av_transaction_header(["av_transaction_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRMCustomerDim |
| av_customer |
| av_transaction_header |

## View Code

```sql
CREATE view [dbo].[vwPOSLoyaltyTransactionExtractByEmailAV]

--gets customers with customer number not in CRMCustomerDim, but the email address IS in CRMCustomerDim so we use that person's CustomerNumber
as
with
Trans as
	(
		select
			c.email_address,
			c.av_transaction_id
		from av_customer c with (nolock)
		join av_transaction_header th on c.av_transaction_id=th.av_transaction_id
		where 1=1
		and c.customer_role in (1,4)
		--and th.store_no in (13,2013)
		--and c.customer_no=0
		--and c.customer_no = 14921959
		and c.transaction_date >= getdate()-45
		and c.email_address not like '%@marketplace.amazon%'
		and not exists (select cd.CustomerNumber from PAPAMART.dw.dbo.CRMCustomerDim cd 
							where cd.CustomerNumber collate SQL_Latin1_General_CP1_CI_AS = cast(c.customer_no as varchar))
		group by
			c.email_address,
			c.av_transaction_id
	)
select
	max(cd.CustomerNumber) as CustomerNumber,
	--x.transaction_id as SATransactionID,
	cast(x.av_transaction_id as int) as SATransactionID,
	NULL as LoyaltyTransactionType,
	1 as matchedByEMail
from Trans x
join PAPAMART.dw.dbo.CRMCustomerDim cd on x.email_address collate SQL_Latin1_General_CP1_CI_AS  =cd.EmailAddress
group by av_transaction_id
```

