# dbo.vwdw_registration_product_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_registration_product_dim"]
    dbo_vwdw_product_dim_v3(["dbo.vwdw_product_dim_v3"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwdw_product_dim_v3 |

## View Code

```sql
CREATE VIEW dbo.vwdw_registration_product_dim
AS
SELECT        product_key,
sku,
activation_date,
style_code,
style_desc,
color_code,
color_desc,
product_desc,
subclass,
class,
department,
department_code,
division,
chain,
concept,
priceline_code,
subclass_code,
class_code,
classcodekey,
divisioncodekey,
stylecodekey,
primary_vendor_code,
primary_vendor_name,
alt_primary_vendor_code,
current_retail,
price_with_vat,
euro_value,
merch_status,
wss_reportable,
reorder_flag,
usdollarcurrentretail,
cadollarcurrentretail,
jurisdictioncodekey,
jurisdiction,
merchclasscodekey,
merchsubclasscodekey,
merchstylecodekey,
plain_jurisdiction,
exclude_from_wss,
omit_from_wss,
cmn_department_code,
cmn_department,
cmn_class_code,
cmn_class,
cmn_subclass_code,
cmn_subclass,
cmn_style_code,
cmn_style,
gender,
corefashion,
inline
FROM            dbo.vwdw_product_dim_v3
```

