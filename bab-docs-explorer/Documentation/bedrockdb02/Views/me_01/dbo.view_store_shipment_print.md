# dbo.view_store_shipment_print

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_store_shipment_print"]
    dbo_store_shipment(["dbo.store_shipment"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.store_shipment |

## View Code

```sql
create view dbo.view_store_shipment_print 
	(doc_type,
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
	 packed_by,
	 ship_date,
	 print_flag,
         match_status,
         po_no,
         document_source)
AS
SELECT	N'Store shipment',
         document_no,
         from_location_id,
         location_id,
	 convert(smalldatetime,convert(char(12),create_date,109)),
	 convert(smalldatetime,convert(char(12),receive_date,109)),
         document_status,
         CAST(null AS nvarchar(60)),
         store_shipment_id,
         location_id,
         CAST(null AS nvarchar(20)),
         0,
         CAST(null AS nvarchar(20)),
         CAST(null AS nvarchar(50)),
         CAST(null AS smallint),
	 CAST(null AS nvarchar(60)),
	 convert(smalldatetime,convert(char(12),ship_date,109)),
	 print_flag,
         CAST(null AS smallint),
         CAST(null AS nvarchar(20)),
         CAST(null AS nvarchar(20))
FROM dbo.store_shipment
WHERE print_flag = 0
AND document_status = 3
```

