# dbo.view_transfer_out

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.view_transfer_out"]
    dbo_transfer(["dbo.transfer"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transfer |

## View Code

```sql
create view dbo.view_transfer_out 	(doc_type,
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
 SELECT N'Transfer Out',
	document_no,
	from_location_id,
	to_location_id,
	convert(smalldatetime,convert(char(12),create_date,109)),
	convert(smalldatetime,convert(char(12),receive_date,109)),
	document_status,
	document_description,
	transfer_id,
	from_location_id,
	grouping_label,
	0,
	CAST(null AS nvarchar(20)),
	CAST(null AS nvarchar(50)),
	transaction_reason_id,
	packed_by,
	convert(smalldatetime,convert(char(12),ship_date,109)),
	print_flag,
        CAST(null AS smallint),
	CAST(null AS nvarchar(20)),
        document_source
FROM dbo.transfer
WHERE document_status <> 4
```

