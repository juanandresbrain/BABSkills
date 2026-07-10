# dbo.spMergeCRMde4

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeCRMde4"]
    CRMde4(["CRMde4"]) --> SP
    dbo_tmpCrmDe4(["dbo.tmpCrmDe4"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CRMde4 |
| dbo.tmpCrmDe4 |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeCRMde4]

as


set nocount on

merge into CRMde4 as target
using 
	(
	SELECT	
	  [transactionID],
      [units],
      [event_name],
      [category],
      [unit_gross_amount],
      [coupon_desc]
  from dwstaging.dbo.tmpCrmDe4 with (nolock)
	) as source
on 
	target.[transactionID]=source.[transactionID]
	and
	target.[units]=source.[units]
	and
	target.[event_name]=source.[event_name]
	and
	target.[category]=source.[category]
	and
	target.[unit_gross_amount]=source.[unit_gross_amount]
	and
	target.[coupon_desc]=source.[coupon_desc]

--when matched 
--	and 
--		isnull(target.unit_gross_amount,0)<>isnull(source.unit_gross_amount,0)
				
--then update
--	set
--		target.unit_gross_amount=source.unit_gross_amount,
--		target.UpdateDate=getdate()
when not matched by target
then insert
	(
	  [transactionID],
      [units],
      [event_name],
      [category],
      [unit_gross_amount],
      [coupon_desc],
	  [InsertDate]
	)
values
	(
	  source.[transactionID],
      source.[units],
      source.[event_name],
      source.[category],
      source.[unit_gross_amount],
      source.[coupon_desc],
	  getdate()
	)
--when not matched by source
--then delete
;
```

