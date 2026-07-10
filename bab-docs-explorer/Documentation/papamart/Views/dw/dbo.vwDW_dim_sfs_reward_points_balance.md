# dbo.vwDW_dim_sfs_reward_points_balance

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_sfs_reward_points_balance"]
    dbo_dim_lifetime_dollars(["dbo.dim_lifetime_dollars"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dim_lifetime_dollars |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_dim_sfs_reward_points_balance]
AS
SELECT
	[lifetime_dollars_key] AS sfs_reward_points_balance_key
	,[range_min]
	,[range_max]
	,[group1_min]
	,[group1_max]
	,[group2_min]
	,[group2_max]
	,[group3_min]
	,[group3_max]
	,SUBSTRING(CONVERT(varchar, CAST(range_min AS money), 1), 1, LEN(CONVERT(varchar, CAST(range_min AS money), 1)) - 3) + ' - ' +
		SUBSTRING(CONVERT(varchar, CAST(range_max AS money), 1), 1, LEN(CONVERT(varchar, CAST(range_max AS money), 1)) - 3) AS group0_label
	,SUBSTRING(CONVERT(varchar, CAST(group1_min AS money), 1), 1, LEN(CONVERT(varchar, CAST(group1_min AS money), 1)) - 3) + ' - ' +
		SUBSTRING(CONVERT(varchar, CAST(group1_max AS money), 1), 1, LEN(CONVERT(varchar, CAST(group1_max AS money), 1)) - 3) AS group1_label
	,SUBSTRING(CONVERT(varchar, CAST(group2_min AS money), 1), 1, LEN(CONVERT(varchar, CAST(group2_min AS money), 1)) - 3) + ' - ' +
		SUBSTRING(CONVERT(varchar, CAST(group2_max AS money), 1), 1, LEN(CONVERT(varchar, CAST(group2_max AS money), 1)) - 3) AS group2_label
	,SUBSTRING(CONVERT(varchar, CAST(group3_min AS money), 1), 1, LEN(CONVERT(varchar, CAST(group3_min AS money), 1)) - 3) + ' - ' +
		SUBSTRING(CONVERT(varchar, CAST(group3_max AS money), 1), 1, LEN(CONVERT(varchar, CAST(group3_max AS money), 1)) - 3) AS group3_label
FROM [dw].[dbo].[dim_lifetime_dollars]
```

