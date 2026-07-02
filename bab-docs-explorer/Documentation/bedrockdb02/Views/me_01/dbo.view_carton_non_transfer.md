# dbo.view_carton_non_transfer

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_carton_non_transfer"]
    dbo_carton_document_map(["dbo.carton_document_map"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.carton_document_map |

## View Code

```sql
create view dbo.view_carton_non_transfer 	 (doc_type,
	 doc_no,
	 from_location_id,
	 to_location_id,
	 create_date,
	 receive_date,
	 status,
	 description,
	 doc_id,
	 display_location_id,
	 grouping_label,
	 secondary_type,
	 vendor_code,
	 vendor_name,
	 transaction_reason_id,
	 performed_by,
	 cartons_arrived,
	 total_cartons,
	 match_status,
	 shipment_ref_no)
AS
SELECT DISTINCT N'Carton',
		carton_no,
		CAST(null AS smallint),
		location_id,
		CAST(null AS smalldatetime),
		CAST(null AS smalldatetime),
		CAST(carton_arrived_flag + 20 AS smallint),
		CAST(null AS nvarchar(60)),
		0,
		location_id,
		CAST(null AS nvarchar(20)),
		document_type,
		CAST(null AS nvarchar(20)),
		CAST(null AS nvarchar(50)),
		CAST(null AS smallint),
		CAST(null AS nvarchar(60)),
		CAST(null AS int),
		CAST(null AS int),
                CAST(null AS smallint),
               CAST(null AS nvarchar(30))
 FROM carton_document_map
 WHERE document_type IN (2, 5)
```

