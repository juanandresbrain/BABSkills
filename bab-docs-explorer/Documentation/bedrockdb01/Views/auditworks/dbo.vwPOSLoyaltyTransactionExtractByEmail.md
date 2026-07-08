# dbo.vwPOSLoyaltyTransactionExtractByEmail

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPOSLoyaltyTransactionExtractByEmail"]
    dbo_CRMCustomerDim(["dbo.CRMCustomerDim"]) --> VIEW
    customer(["customer"]) --> VIEW
    transaction_header(["transaction_header"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRMCustomerDim |
| customer |
| transaction_header |

## View Code

```sql
CREATE view [dbo].[vwPOSLoyaltyTransactionExtractByEmail]

as
with
Trans as
	(
		select
			c.email_address,
			c.transaction_id
		from customer c with (nolock)
		join transaction_header th on c.transaction_id=th.transaction_id
		where 1=1
		and c.customer_role in (1,204)
		and th.store_no in (13,2013)
		and c.customer_no=0
		and c.email_address not like '%@marketplace.amazon%'
		group by
			c.email_address,
			c.transaction_id
	)
select
	max(cd.CustomerNumber) as CustomerNumber,
	--x.transaction_id as SATransactionID,
	cast(x.transaction_id as int) as SATransactionID,
	NULL as LoyaltyTransactionType,
	1 as matchedByEMail
from Trans x
join PAPAMART.dw.dbo.CRMCustomerDim cd on x.email_address collate SQL_Latin1_General_CP1_CI_AS  =cd.EmailAddress
group by transaction_id
```

