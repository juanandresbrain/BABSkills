# dbo.vwJumpMindSalesRetailLineItem

**Database:** LH_Source  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwJumpMindSalesRetailLineItem"]
    jumpmind_sls_retail_line_item(["jumpmind_sls_retail_line_item"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| jumpmind_sls_retail_line_item |

## View Code

```sql
CREATE view vwJumpMindSalesRetailLineItem ---see postgres vwbab_sls_retail_line_item used for storeforce
as

select
	t.device_id,
    cast(t.create_time as date) AS BusinessDate,
    left(t.device_id, 4) AS StoreID,
    right(t.device_id, 3) AS RegisterNumber,
    t.sequence_number,
    t.line_sequence_number,
    t.pos_item_id,
    t.item_id,
    t.item_type,
    cast(t.regular_unit_price as numeric(20,2)) as regular_unit_price,
    cast(t.actual_unit_price as numeric(20,2)) as actual_unit_price,
    cast(t.quantity as int) as quantity,
    cast(t.extended_amount as numeric(20,2)) as extended_amount,
    cast(t.discount_amount as numeric(20,2)) as discount_amount,
    cast(t.extended_discounted_amount as numeric(20,2)) as extended_discounted_amount,
    cast(t.rtn_extended_discounted_amount as numeric(20,2)) as rtn_extended_discounted_amount,
    cast(t.tax_amount as numeric(20,2)) as tax_amount,
    t.line_item_type,
    t.voided,
    t.entry_method_code,
    t.create_time,
    t.find_a_bear_id,
    t.serialized_coupon_barcode,
    concat(cast(t.create_time as date), t.device_id, t.sequence_number) AS TransactionKey
 FROM jumpmind_sls_retail_line_item t
  WHERE t.device_id not like '%customerdisplay%'
  AND left(t.device_id, 1) <> '-'
  AND (t.line_item_type in ('STORE_SALE', 'ORDER_IN_STORE')) 
  AND (t.item_type in ('STOCK', 'DONATION', 'GIFTCARD')) 
  AND (left(t.device_id, 4) not in ('1013','2013')) 
  AND t.voided = 0 
  AND cast(t.create_time as date) = cast(dateadd(hh, -7, getdate()) as date) ---ensures the date is always 'today' from perspective of west coast US
```

