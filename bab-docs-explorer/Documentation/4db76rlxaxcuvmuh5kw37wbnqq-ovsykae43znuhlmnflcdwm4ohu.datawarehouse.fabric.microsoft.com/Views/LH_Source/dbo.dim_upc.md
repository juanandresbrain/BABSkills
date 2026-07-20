# dbo.dim_upc

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.dim_upc"]
    dbo_jumpmind_sls_retail_line_item(["dbo.jumpmind_sls_retail_line_item"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.jumpmind_sls_retail_line_item |

## View Code

```sql
CREATE   VIEW dbo.dim_upc AS WITH pos_observations AS (     SELECT         CAST(rli.item_id AS varchar(14))                 AS upc,         MAX(rli.item_description)                        AS item_description,         MAX(rli.item_type)                               AS item_type,         MAX(rli.classifier_department)                   AS classifier_department,         MAX(rli.classifier_class)                        AS classifier_class,         MAX(rli.find_a_bear_id)                          AS find_a_bear_id       FROM LH_Source.dbo.jumpmind_sls_retail_line_item AS rli      WHERE rli.item_id IS NOT NULL      GROUP BY CAST(rli.item_id AS varchar(14)) ) SELECT     p.upc,     p.item_description,     p.item_type,     /* Descriptive dept/class for Power BI display */     CASE         WHEN p.classifier_department IS NOT NULL AND p.classifier_class IS NOT NULL              THEN p.classifier_department + ' / ' + p.classifier_class         WHEN p.classifier_department IS NOT NULL THEN p.classifier_department         WHEN p.classifier_class      IS NOT NULL THEN p.classifier_class         ELSE NULL     END                                                  AS dept_class,     /* Aptos M-record field 12 integer code — was sourced from        mulesoft_productextract.DepartmentID. JumpMind retail_line_item only        carries the text classifier_department; no integer DepartmentID        column. Emit NULL until mulesoft_productextract or another source        provides the integer encoding. */     CAST(NULL AS int)                                    AS aptos_dept_class_code,     p.find_a_bear_id,     CASE WHEN p.item_type = 'GIFTCARD' THEN 1 ELSE 0 END  AS is_giftcard,     CASE WHEN p.item_type = 'DONATION' THEN 1 ELSE 0 END  AS is_donation,     CASE WHEN p.item_type IN ('SERVICE','EMBROIDERY','STORE_ORDER_SHIPPING','TIP') THEN 1 ELSE 0 END AS is_service   FROM pos_observations AS p;
```

