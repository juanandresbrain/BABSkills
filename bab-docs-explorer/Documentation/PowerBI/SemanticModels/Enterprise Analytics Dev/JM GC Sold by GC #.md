# JM GC Sold by GC #

**Workspace:** Enterprise Analytics Dev  
**Dataset ID:** a8eb92f5-ab46-4174-ba03-31395dc2f224  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| jumpmind_sls_trans | 8 | 0 |  |
| DateTableTemplate_b6814105-aadb-4fa7-b980-25d97abf98b3 | 8 | 0 | Yes |
| LocalDateTable_c016d6f9-8b82-4007-b64e-31f9dc1dd6eb | 8 | 0 | Yes |

## Measures

_No measures detected._

## Power Query Source (per table)

### jumpmind_sls_trans

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source",
    [Query="select t.business_unit_id
, CAST(t.create_time AS DATE) AS transaction_date
, c.card_number as reference_no
, CAST(l.quantity AS INT) as units
, ROUND(l.regular_unit_price, 2) as gross_gift_card_sales
, ROUND(l.actual_unit_price, 2) as net_gift_card_sales
, 0 as avg_activation
from dbo.jumpmind_sls_trans t
join dbo.jumpmind_sls_retail_line_item l
	on t.device_id = l.device_id
	and t.business_date = l.business_date
	and t.sequence_number = l.sequence_number
join dbo.jumpmind_sls_card_line_item c 
	on t.device_id = c.device_id
	and t.business_date = c.business_date
	and t.sequence_number = c.sequence_number
	and l.line_sequence_number = c.ref_line_sequence_number
where cast(t.create_time as date) >= '2024-01-01'
order by t.business_unit_id, t.create_time"])
in
    Source
```

### DateTableTemplate_b6814105-aadb-4fa7-b980-25d97abf98b3

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### LocalDateTable_c016d6f9-8b82-4007-b64e-31f9dc1dd6eb

```sql
Calendar(Date(Year(MIN('jumpmind_sls_trans'[transaction_date])), 1, 1), Date(Year(MAX('jumpmind_sls_trans'[transaction_date])), 12, 31))
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
