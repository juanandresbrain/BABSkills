# dbo.sv_av_merchandise_detail

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_av_merchandise_detail"]
    av_merchandise_detail(["av_merchandise_detail"]) --> VIEW
    av_transaction_line(["av_transaction_line"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| av_merchandise_detail |
| av_transaction_line |

## View Code

```sql
create view dbo.sv_av_merchandise_detail   AS
SELECT transaction_id = m.av_transaction_id, m.line_id, merchandise_category,
	upc_lookup_division, upc_no, units, salesperson, salesperson2,
	sku_id, style_reference_id, class_code, subclass_code, price_override,
	pos_iplu_missing, upc_on_file_flag, pos_deptclass, ticket_price,
	sold_at_price, pos_identifier, l.db_cr_none, l.voiding_reversal_flag, l.line_void_flag, l.line_object, l.line_action,
	plu_price, pos_identifier_type, scanned, originating_store_no, source_store_no, fulfillment_store_no, m.cost
	FROM av_merchandise_detail m, av_transaction_line l
	WHERE m.av_transaction_id = l.av_transaction_id
	AND m.line_id = l.line_id
```

