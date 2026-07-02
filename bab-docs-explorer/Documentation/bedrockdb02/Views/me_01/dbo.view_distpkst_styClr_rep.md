# dbo.view_distpkst_styClr_rep

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_distpkst_styClr_rep"]
    dbo_view_dist_pkstr_sku_rep(["dbo.view_dist_pkstr_sku_rep"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.view_dist_pkstr_sku_rep |

## View Code

```sql
CREATE VIEW dbo.view_distpkst_styClr_rep 
AS
SELECT vw1.distribution_id,vw1.po_id,
vw1.volume_grade_id, 
vw1.grade_code, 
vw1.style_id, vw1.style_color_id,
SUM(vw1.dq_per_location) AS total_styClr_pergrd_perloc
FROM view_dist_pkstr_sku_rep vw1
GROUP BY vw1.distribution_id,
vw1.po_id,
vw1.volume_grade_id, 
vw1.grade_code, 
vw1.style_id, vw1.style_color_id
```

