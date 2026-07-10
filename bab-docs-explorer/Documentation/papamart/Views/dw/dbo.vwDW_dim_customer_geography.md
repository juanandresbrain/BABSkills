# dbo.vwDW_dim_customer_geography

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_dim_customer_geography"]
    pm_repo_Customer_Geography_Dim(["pm_repo.Customer_Geography_Dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| pm_repo.Customer_Geography_Dim |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_dim_customer_geography]
AS
/*
SELECT
		0 AS customer_geography_key
		,'' AS country
		,0 AS state_key
		,'' AS state_region
		,0 AS county_key
		,'' AS county
		,0 AS city_key
		,'' AS city_locality
		,0 AS zip_key
		,'' AS zip_postal
		,0 AS dma_key
		,'' AS dma
		,0 AS msa_key
		,'' AS msa
		,0 AS cluster_key
		,'' AS cluster
		,'' AS block_group
*/

	SELECT
		[Customer_Geography_Key]
		,[Country_Key]
		,CASE WHEN [Country_Name] IS NULL THEN NULL ELSE [Country_Name] END AS [Country_Name]
		,[State_Province_Key]
		,CASE WHEN [State_Province_Name] IS NULL THEN [Country_Name] ELSE [State_Province_Name] END AS [State_Province_Name]
		,[County_Key]
		,CASE
			WHEN [County_Name] IS NULL THEN
				CASE WHEN [State_Province_Name] IS NULL THEN [Country_Name] ELSE [State_Province_Name] END
			ELSE [County_Name]
		END AS [County_Name] 
		,[City_Key]
		,CASE
			WHEN [City_Name] IS NULL THEN
				CASE
					WHEN [County_Name] IS NULL THEN
						CASE WHEN [State_Province_Name] IS NULL THEN [Country_Name] ELSE [State_Province_Name] END
					ELSE [County_Name]
				END
			ELSE [City_Name]
		END AS [City_Name] 
		,[Postal_Code_Key]
		,CASE
			WHEN [Postal_Code] IS NULL THEN
				CASE
					WHEN [City_Name] IS NULL THEN
						CASE
							WHEN [County_Name] IS NULL THEN
								CASE WHEN [State_Province_Name] IS NULL THEN [Country_Name] ELSE [State_Province_Name] END
							ELSE [County_Name]
						END
					ELSE [City_Name]
				END
			ELSE [Postal_Code]
		END AS [Postal_Code] 
		,[DMA_Key]
		,CASE WHEN [DMA_Name] IS NULL THEN NULL ELSE [DMA_Name] END AS [DMA_Name] 
		,[Metro_Key]
		,CASE WHEN [Metro_Name] IS NULL THEN [DMA_Name] ELSE [Metro_Name] END AS [Metro_Name] 
		,[Cluster_Key]
		,CASE
			WHEN [Cluster_Name] IS NULL THEN
				CASE
					WHEN [Metro_Name] IS NULL THEN [DMA_Name]
					ELSE [Metro_Name]
				END
			ELSE [Cluster_Name]
		END AS [Cluster_Name]
	FROM
	(
		SELECT
			[Customer_Geography_Key]
			,[Country_Key]
			,CASE WHEN LTRIM(RTRIM([Country_Name])) = '' OR [Country_Name] IS NULL THEN NULL ELSE [Country_Name] END AS [Country_Name]
			,[State_Province_Key]
			,CASE WHEN LTRIM(RTRIM([State_Province_Name])) = '' OR [State_Province_Name] IS NULL THEN NULL ELSE [State_Province_Name] END AS [State_Province_Name]
			,[County_Key]
			,CASE WHEN LTRIM(RTRIM([County_Name])) = '' OR [County_Name] IS NULL THEN NULL ELSE [County_Name] END AS [County_Name] 
			,[City_Key]
			,CASE WHEN LTRIM(RTRIM([City_Name])) = '' OR [City_Name] IS NULL THEN NULL ELSE [City_Name] END AS [City_Name] 
			,[Postal_Code_Key]
			,CASE WHEN LTRIM(RTRIM([Postal_Code])) = '' OR [Postal_Code] IS NULL THEN NULL ELSE [Postal_Code] END AS [Postal_Code] 
			,[DMA_Key]
			,CASE WHEN LTRIM(RTRIM([DMA_Name])) = '' OR [DMA_Name] IS NULL THEN NULL ELSE [DMA_Name] END AS [DMA_Name] 
			,[Metro_Key]
			,CASE WHEN LTRIM(RTRIM([Metro_Name])) = '' OR [Metro_Name] IS NULL THEN NULL ELSE [Metro_Name] END AS [Metro_Name] 
			,[Cluster_Key]
			,CASE WHEN LTRIM(RTRIM([Cluster_Name])) = '' OR [Cluster_Name] IS NULL THEN NULL ELSE [Cluster_Name] END AS [Cluster_Name]
		FROM [dw].[pm_repo].[Customer_Geography_Dim]
	) t
```

