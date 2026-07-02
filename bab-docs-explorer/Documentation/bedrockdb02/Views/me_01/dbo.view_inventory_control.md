# dbo.view_inventory_control

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_inventory_control"]
    dbo_inventory_control(["dbo.inventory_control"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.inventory_control |

## View Code

```sql
create view dbo.view_inventory_control 	(doc_type,
	 doc_no,
	 create_date,
	 count_date,
 	 valuation_date, 
	 status, description,
	 doc_id,
	 grouping_label,
	 merch_level,
	 update_type)
AS
SELECT	 N'ICD',
	  document_no,
	  CONVERT (smalldatetime, CONVERT (char(12), create_date, 109)),
	  CONVERT (smalldatetime, CONVERT (char(12), count_date, 109)),
	  CONVERT (smalldatetime, CONVERT (char(12), valuation_date, 109)),
	  document_status,
                    document_description,
                    inventory_control_id,
                   grouping_label,
                   ISNULL (hierarchy_level_id, 0),
                   update_type
 FROM inventory_control
```

