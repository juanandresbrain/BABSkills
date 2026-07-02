# dbo.sp_AddPackageStyleData

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_AddPackageStyleData"]
    dbo_PackageStyle(["dbo.PackageStyle"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.PackageStyle |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Nigel Thomas
-- Create date: 11/29/2018
-- Description:	Gets counts for count of items submitted to the inv_supplies tables
-- =============================================
create PROCEDURE [dbo].[sp_AddPackageStyleData]
	-- Add the parameters for the stored procedure here
	@PackageID varchar(20)
	--,
	--@StartDate datetime,
	--@EndDate datetime,
	--@CreatedBy varchar(20),
	--@CreatedDate datetime
AS
BEGIN
	SET NOCOUNT ON;

    -- Insert statements for procedure here
insert into 
[BABWPartyPlanner].[dbo].[PackageStyle] (PackageID, StartDate, EndDate, CreatedBy, CreatedDate) values(@PackageID,'2018-05-14 00:00:00.000','2050-01-01 00:00:00.000','BAB\BENB','2018-09-20 10:05:52.337')


END
```

