# dbo.view_po_detail_retail_notx_rep

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_po_detail_retail_notx_rep"]
    dbo_view_po_pack_detail_retail_rep(["dbo.view_po_pack_detail_retail_rep"]) --> VIEW
    dbo_view_po_pack_detail_tax_rep(["dbo.view_po_pack_detail_tax_rep"]) --> VIEW
    dbo_view_po_sc_detail_retail_rep(["dbo.view_po_sc_detail_retail_rep"]) --> VIEW
    dbo_view_po_sc_detail_tax_rep(["dbo.view_po_sc_detail_tax_rep"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.view_po_pack_detail_retail_rep |
| dbo.view_po_pack_detail_tax_rep |
| dbo.view_po_sc_detail_retail_rep |
| dbo.view_po_sc_detail_tax_rep |

## View Code

```sql
create view [dbo].[view_po_detail_retail_notx_rep] 



AS
SELECT 	pd.po_id,
		pd.po_detail_id,
		SUM(unit_retail) AS unit_retail
FROM	(
			SELECT	vpr.po_id,
					vpr.po_detail_id,		
					CONVERT(NUMERIC(14, 2), ROUND(vpr.unit_retail * total_exclude_tax_ratio, 2)) AS unit_retail
			FROM	view_po_sc_detail_retail_rep vpr
					INNER JOIN view_po_sc_detail_tax_rep vpt
					ON (vpr.po_id = vpt.po_id
						AND vpr.po_detail_id = vpt.po_detail_id)
			UNION ALL
			SELECT	vpr.po_id,
					vpr.po_detail_id,		
					CONVERT(NUMERIC(14, 2), ROUND(vpr.unit_retail * total_exclude_tax_ratio, 2)) AS unit_retail
			FROM	view_po_pack_detail_retail_rep vpr
					INNER JOIN view_po_pack_detail_tax_rep vpt
					ON (vpr.po_id = vpt.po_id
						AND vpr.po_detail_id = vpt.po_detail_id)
		) pd
GROUP BY pd.po_id,
		pd.po_detail_id
```

