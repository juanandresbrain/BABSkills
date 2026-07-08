# dbo.sv_av_discount_detail

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.sv_av_discount_detail"]
    av_discount_detail(["av_discount_detail"]) --> VIEW
    av_transaction_line(["av_transaction_line"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| av_discount_detail |
| av_transaction_line |

## View Code

```sql
create view dbo.sv_av_discount_detail  as
SELECT transaction_id = d.av_transaction_id, d.line_id, d.applied_by_line_id,
	d.pos_discount_level, d.pos_discount_type, d.pos_discount_amount,
	d.applied_flag, d.pos_discount_serial_no, l.db_cr_none
	FROM av_discount_detail d, av_transaction_line l
	WHERE d.av_transaction_id =l.av_transaction_id
	AND d.line_id = l.line_id
```

