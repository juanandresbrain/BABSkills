# dbo.view_transfer_in

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_transfer_in"]
    dbo_carton_document_map(["dbo.carton_document_map"]) --> VIEW
    dbo_transfer(["dbo.transfer"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.carton_document_map |
| dbo.transfer |

## View Code

```sql
create view dbo.view_transfer_in 
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
          performed_by, 
	  cartons_arrived, 
          total_cartons,
          match_status,
          shipment_ref_no)
AS
   SELECT N'Transfer In',
          document_no,
          from_location_id,
          to_location_id,
	  convert(smalldatetime,convert(char(12),create_date,109)),
	  convert(smalldatetime,convert(char(12),receive_date,109)),
          document_status,
          document_description,
          transfer_id,
          to_location_id,
          grouping_label,
          0,
          CAST(null AS nvarchar(20)),
          CAST(null AS nvarchar(50)),
          transaction_reason_id,
          performed_by,
            (select count(*) from carton_document_map 
		where document_type = 1 
		  and document_id = transfer_id 
		  and carton_arrived_flag = 1),
            (select count(*) from carton_document_map 
		where document_type = 1 
		  and document_id = transfer_id),
          CAST(null AS smallint),
          CAST(null AS nvarchar(30))
     FROM dbo.transfer
    WHERE document_status IN (3, 4)
```

