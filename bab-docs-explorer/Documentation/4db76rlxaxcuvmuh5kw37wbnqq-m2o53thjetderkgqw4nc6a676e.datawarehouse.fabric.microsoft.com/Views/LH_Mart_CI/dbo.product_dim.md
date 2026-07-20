# dbo.product_dim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.product_dim"]
    dbo_product_dim(["dbo.product_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.product_dim |

## View Code

```sql
;

CREATE VIEW dbo.product_dim AS SELECT product_key, sku, activation_date, style_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS style_code, style_desc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS style_desc, color_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS color_code, color_desc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS color_desc, product_desc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS product_desc, subclass COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS subclass, class COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS class, department COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS department, department_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS department_code, division COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS division, chain COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS chain, concept COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS concept, priceline_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS priceline_code, subclass_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS subclass_code, class_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS class_code, primary_vendor_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS primary_vendor_code, primary_vendor_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS primary_vendor_name, alt_primary_vendor_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS alt_primary_vendor_code, current_retail, original_retail, price_with_vat, reorder_flag, euro_value, merch_status COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS merch_status, wss_reportable COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS wss_reportable, style_id, color_id, current_selling_retail_home, jurisdiction_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS jurisdiction_code, jurisdiction_id, cdn_value, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID, GENDER COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS GENDER, CORE_FASH_CD COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CORE_FASH_CD, INLINE_CD COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS INLINE_CD, ScorecardCategory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ScorecardCategory FROM LH_Mart.dbo.product_dim;;
```

