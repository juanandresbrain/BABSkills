# Azure.vwPOSOutbound_tax_item_group

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwPOSOutbound_tax_item_group"]
    dbo_tax_item_group(["dbo.tax_item_group"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tax_item_group |

## View Code

```sql
CREATE VIEW [Azure].[vwPOSOutbound_tax_item_group] AS

select * from bedrockdb01.auditworks.dbo.tax_item_group


--select 10 as tax_item_group_id, 'N' as tax_item_group_code, 'Non-Taxable' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 20 as tax_item_group_id, 'T' as tax_item_group_code, 'Taxable' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 21 as tax_item_group_id, 'C' as tax_item_group_code, 'Clothing' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 22 as tax_item_group_id, 'S' as tax_item_group_code, 'School Supplies' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 30 as tax_item_group_id, 'LN' as tax_item_group_code, 'Non-Taxable' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 40 as tax_item_group_id, 'LT' as tax_item_group_code, 'Taxable' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 41 as tax_item_group_id, 'Cookies' as tax_item_group_code, 'Cookies' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
--union
--select 53 as tax_item_group_id, 'DIGI' as tax_item_group_code, 'Digital Goods' as 	tax_item_group_description, null as resource_id, null as line_object, null as auto_gen_datetime, null as auto_gen_source
```

