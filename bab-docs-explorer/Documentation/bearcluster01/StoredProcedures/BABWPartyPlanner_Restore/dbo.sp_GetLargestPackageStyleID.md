# dbo.sp_GetLargestPackageStyleID

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_GetLargestPackageStyleID"]
    dbo_PackageStyle(["dbo.PackageStyle"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PackageStyle |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetLargestPackageStyleID]
@PackageID varchar(20)


AS
BEGIN


	SELECT [PackageStyleID]
    
  FROM [BABWPartyPlanner].[dbo].[PackageStyle]
  where PackageID = @PackageID

	
END
```

