# dbo.Sl_Md_PeriodGroupDimension

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Md_PeriodGroupDimension"]
    dbo_Md_PeriodGroupDimension(["dbo.Md_PeriodGroupDimension"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Md_PeriodGroupDimension |

## View Code

```sql
create view dbo.Sl_Md_PeriodGroupDimension 


(
	period_group_id,
	table_id,
	dim_table_id
)
AS SELECT 
	period_group_id,
	table_id,
	dim_table_id
FROM foundation.dbo.Md_PeriodGroupDimension
```

