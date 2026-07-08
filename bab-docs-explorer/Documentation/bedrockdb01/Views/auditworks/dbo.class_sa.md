# dbo.class_sa

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.class_sa"]
    user_class(["user_class"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| user_class |

## View Code

```sql
create view dbo.class_sa AS
    SELECT upc_lookup_division, 
	class_code, 
	class_description, 
	class_short_description = substring(class_description, 1, 12), 
	department_code,
        tax_item_group_id,
        resource_id
FROM user_class c

dbo,flash_sales_postings,/* Dummy view needed for compilation and EXE without Flash. */
/* Will not overwrite existing view. */
/* Replaced with the installation of FLASH_SA */

create view dbo.flash_sales_postings
as 
select	class_code = null,
	store_no = 0,
	transaction_date = '01-JAN-1999',
	units_sold = 0,
	retail_sold = 0,
	cost_sold = 0,
	batch_no = 0
from dbo.code_description
```

