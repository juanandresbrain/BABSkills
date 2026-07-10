# dbo.spMetricFactsArchive

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMetricFactsArchive"]
    metric_facts(["metric_facts"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| metric_facts |

## Stored Procedure Code

```sql
CREATE procedure spMetricFactsArchive
as

if exists (select * from sysobjects where id = object_id('dbo.metric_facts_archive') and sysstat & 0xf = 3)
	drop table metric_facts_archive


select * 
into metric_facts_archive
from metric_facts


CREATE  INDEX [idxN_NU_metric_facts_arch_dim_key] ON [dbo].[metric_facts_archive] ([metric_dim_key])
WITH FILLFACTOR = 100

CREATE INDEX [idxN_NU_metric_facts_arch_store_key] ON [dbo].[metric_facts_archive] ([store_key])
WITH  FILLFACTOR = 100

CREATE INDEX [idxN_NU_metric_facts_arch_date_key] ON [dbo].[metric_facts_archive] ([date_key])
WITH FILLFACTOR = 100
```

