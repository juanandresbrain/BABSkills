# dbo.vwTransactionLineCount

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwTransactionLineCount"]
    dbo_transaction_detail_facts(["dbo.transaction_detail_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transaction_detail_facts |

## View Code

```sql
Create view [dbo].[vwTransactionLineCount] as
select [transaction_id], [store_key], [date_key], count(*) LineCount
		from dw.dbo.[transaction_detail_facts] WITH (NOLOCK) 
--		where date_key between 4012 and 4018 and
		where transaction_line_seq > 0
		group by  [transaction_id], [store_key], [date_key]
```

