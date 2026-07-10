# dbo.spImportFranchiseeStoreCompDetailsStaging

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spImportFranchiseeStoreCompDetailsStaging"]
    dbo_franchisee_store_comp_details_staging(["dbo.franchisee_store_comp_details_staging"]) --> SP
    dbo_vw_Store_Details_AsOf_Today(["dbo.vw_Store_Details_AsOf_Today"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchisee_store_comp_details_staging |
| dbo.vw_Store_Details_AsOf_Today |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spImportFranchiseeStoreCompDetailsStaging]
-- =============================================================================================================
-- Name: spImportFranchiseeStoreCompDetailsStaging
--
-- Description:	
--	Generate the records to Insert into staging table. This extracts the information on bidb01
--		and makes it available to insert by way of spGet_Region_StoreCount.
--
-- Input:		
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Outside Contractor	4/14/2015		Created
--		Gary Murrish		8/31/2015		Added ISNull for Region and Bearitory

-- =============================================================================================================
AS

	SET NOCOUNT ON

	TRUNCATE TABLE DWStaging.dbo.[franchisee_store_comp_details_staging]

	INSERT INTO DWStaging.dbo.franchisee_store_comp_details_staging
		SELECT
			FranchiseeName,
			ISNULL(RegionName, 'N/A') AS RegionName,
			CAST(ISNULL(BearitoryName, 'N/A') AS varchar(50)) AS BearitoryName,
			CAST(Country AS varchar(50)) AS Country,
			CountryName,
			StoreNo,
			store_name,
			CONVERT(datetime, new.openDate, 126) AS openDate,
			CASE
				WHEN closeDate = '12/31/2399' THEN NULL
				ELSE CONVERT(datetime, new.closeDate, 126)
			END AS closeDate,
			CAST('ENG' AS varchar(3)) AS Language
		FROM
			KODIAK.FranchMstrData.dbo.vw_Store_Details_AsOf_Today AS new WITH (NOLOCK)
```

