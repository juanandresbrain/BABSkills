# dbo.vwFranchiseeProductAttribute

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwFranchiseeProductAttribute"]
    FranchiseeProductAttribute(["FranchiseeProductAttribute"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| FranchiseeProductAttribute |

## View Code

```sql
CREATE VIEW [dbo].[vwFranchiseeProductAttribute] 
as

with 
Attr1 as
	(
		select 
			Franchisee, 
			StyleCode,
			min(CustomAttribute1) Attr1
		from FranchiseeProductAttribute
		group by Franchisee, StyleCode 
	),
FilterOutAttr1 as
	(
		select 
			a2.Franchisee,
			a2.StyleCode,
			a2.CustomAttribute1
		from FranchiseeProductAttribute a2
		where not exists (select a1.StyleCode from Attr1 a1 where a1.Franchisee = a2.Franchisee and a1.StyleCode = a2.StyleCode and a1.Attr1 = a2.CustomAttribute1)
	),
Attr2 as 
	(
		select 
			Franchisee,
			StyleCode,
			min(CustomAttribute1) Attr2
		from FilterOutAttr1 
		group by Franchisee, StyleCode 
	),
FranchiseeAttributes as
	(
		select 
			a1.Franchisee,
			a1.StyleCode,
			a1.Attr1,
			a2.Attr2
		from Attr1 a1 
		left join Attr2 a2 on a1.Franchisee = a2.Franchisee and a1.StyleCode = a2.StyleCode 
	)
select --HOPEFULLY NEVER NEEDED, BUT IF MORE FRANCHISEES NEED TO USE CUSTOM PRODUCT ATTRIBUTES, WE CAN USE THE CODE
	StyleCode,
	--case when Franchisee = 'AE' then Attr1 end as AE_CustomAttribute1,
	--case when Franchisee = 'AE' then Attr2 end as AE_CustomAttribute2,
	case when Franchisee = 'AU' then Attr1 end as AU_CustomAttribute1,
	case when Franchisee = 'AU' then Attr2 end as AU_CustomAttribute2
	--case when Franchisee = 'CN' then Attr1 end as CN_CustomAttribute1,
	--case when Franchisee = 'CN' then Attr2 end as CN_CustomAttribute2,
	--case when Franchisee = 'DE' then Attr1 end as DE_CustomAttribute1,
	--case when Franchisee = 'DE' then Attr2 end as DE_CustomAttribute2,
	--case when Franchisee = 'DK' then Attr1 end as DK_CustomAttribute1,
	--case when Franchisee = 'DK' then Attr2 end as DK_CustomAttribute2,
	--case when Franchisee = 'MX' then Attr1 end as MX_CustomAttribute1,
	--case when Franchisee = 'MX' then Attr2 end as MX_CustomAttribute2,
	--case when Franchisee = 'SG' then Attr1 end as SG_CustomAttribute1,
	--case when Franchisee = 'SG' then Attr2 end as SG_CustomAttribute2,
	--case when Franchisee = 'TH' then Attr1 end as TH_CustomAttribute1,
	--case when Franchisee = 'TH' then Attr2 end as TH_CustomAttribute2,
	--case when Franchisee = 'TR' then Attr1 end as TR_CustomAttribute1,
	--case when Franchisee = 'TR' then Attr2 end as TR_CustomAttribute2,
	--case when Franchisee = 'ZA' then Attr1 end as ZA_CustomAttribute1,
	--case when Franchisee = 'ZA' then Attr2 end as ZA_CustomAttribute2
FROM FranchiseeAttributes
```

