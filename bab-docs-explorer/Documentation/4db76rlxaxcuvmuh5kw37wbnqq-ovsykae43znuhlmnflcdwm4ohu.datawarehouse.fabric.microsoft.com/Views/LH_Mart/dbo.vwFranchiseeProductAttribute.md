# dbo.vwFranchiseeProductAttribute

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwFranchiseeProductAttribute"]
    dbo_franchiseeproductattribute(["dbo.franchiseeproductattribute"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeproductattribute |

## View Code

```sql
CREATE VIEW [dbo].[vwFranchiseeProductAttribute]  as with  Attr1 as 	( 		select  			Franchisee,  			StyleCode, 			min(CustomAttribute1) Attr1 		from [dbo].[franchiseeproductattribute] 		group by Franchisee, StyleCode  	), FilterOutAttr1 as 	( 		select  			a2.Franchisee, 			a2.StyleCode, 			a2.CustomAttribute1 		from [dbo].[franchiseeproductattribute] a2 		where not exists (select a1.StyleCode from Attr1 a1 where a1.Franchisee = a2.Franchisee and a1.StyleCode = a2.StyleCode and a1.Attr1 = a2.CustomAttribute1) 	), Attr2 as  	( 		select  			Franchisee, 			StyleCode, 			min(CustomAttribute1) Attr2 		from FilterOutAttr1  		group by Franchisee, StyleCode  	), FranchiseeAttributes as 	( 		select  			a1.Franchisee, 			a1.StyleCode, 			a1.Attr1, 			a2.Attr2 		from Attr1 a1  		left join Attr2 a2 on a1.Franchisee = a2.Franchisee and a1.StyleCode = a2.StyleCode  	) select  	StyleCode, 	case when Franchisee = 'AU' then Attr1 end as AU_CustomAttribute1, 	case when Franchisee = 'AU' then Attr2 end as AU_CustomAttribute2 FROM FranchiseeAttributes
```

