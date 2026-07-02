# dbo.vwMaxPriceID_KL_03102017

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwMaxPriceID_KL_03102017"]
    dbo_ib_audit_trail(["dbo.ib_audit_trail"]) --> VIEW
    dbo_ib_price(["dbo.ib_price"]) --> VIEW
    dbo_vwPriceChange(["dbo.vwPriceChange"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ib_audit_trail |
| dbo.ib_price |
| dbo.vwPriceChange |

## View Code

```sql
CREATE view [dbo].[vwMaxPriceID_KL_03102017]

as

select ip.style_id, ip.jurisdiction_id, ip.location_id, max(ip.ib_price_id) ib_price_id
from ib_price ip with (nolock)
--left join price_change pc with (nolock) on ip.document_number = pc.price_change_no 
	--and pc.approval_status = 2
	--and pc.price_change_status = 4
where ip.start_date <= getdate()
--OLD and (ip.end_date > getdate() or ip.end_date is NULL)
and (ip.end_date >= cast(left(getdate(), 11) as smalldatetime)  or ip.end_date is NULL)
and not exists (select application_identifier from ib_audit_trail with (nolock) where application_identifier = ip.document_number and application_type = 'PC' and action = 'delete')
--and not exists (select price_change_no from price_change with (nolock) where price_change_no = ip.document_number and ( approval_status <> '2' or price_change_status <> '4' ) )
--and (ip.document_number in (select price_change_no from price_change with (nolock) where ( approval_status = '2' and price_change_status = '4' ) ) or ip.document_number is NULL)
and 	(ip.document_number in 
						(
							select document_number
							from vwPriceChange
							where (document_type = 'Permanent'
									and document_status in ('Effective', 'Completed')
									and approval_status = 'Approved')
							or (document_type in ('Promotional', 'Deal')
--OLD									and document_status = 'Effective'
									and document_status in ('Effective')
									and approval_status = 'Approved')
							or (document_type in ('Promotional', 'Deal')
									and document_status in ('Completed')
									and approval_status = 'Approved'
									and	effective_to_date = cast(left(getdate(), 11) as smalldatetime))
						) 
	OR
		ip.document_number is NULL)
group by ip.style_id, ip.jurisdiction_id, ip.location_id


dbo,vwMerchantNumber,CREATE view [dbo].[vwMerchantNumber]
as

select cast(location_code as int) as store_no, 
--	a.custom_property_id, 
	cust_prop_code, 
--	cust_prop_label, 
	LTRIM(RTRIM(REPLACE(custom_property_value,' ',''))) as merchant_number--substring(convert(char,a.entity_custom_property_id),4,3),a.custom_property_id 
from entity_custom_property a
	join location l on substring(convert(char,a.entity_custom_property_id),4,3) = l.location_id
	join custom_property c on a.custom_property_id = c.custom_property_id
--where c.custom_property_id in (4, 5, 6, 7, 8, 9, 12 ) -- (4=VISA, 5=AMEX, 6=Discover, 7=JCB, 8=CHECK, 9=GiftCard, 12=DebitCard)
where c.cust_prop_code in ('MC/V','AX','DISC','JCB','CHECK','GC','DB')


dbo,vwPBICompSetName,CREATE view vwPBICompSetName 

as 

SELECT DISTINCT b.style_code, 
c.comp_set_name as CompSetName
FROM me_01.dbo.sku a, me_01.dbo.style b, me_01.dbo.comp_set c, me_01.dbo.comp_set_style_color d, me_01.dbo.style_color e 
WHERE a.style_id =b.style_id  
    AND a.style_color_id = e.style_color_id 
    AND e.style_color_id = d.style_color_id  
    AND c.comp_set_id = d.comp_set_id
```

