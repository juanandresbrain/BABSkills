# dbo.FiscalDateGet

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.FiscalDateGet"]
    CurrentDateInformation(["CurrentDateInformation"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CurrentDateInformation |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Zac Doerr
-- Create date: October 23 2008
-- Modifictions
--	G Murrish		10/8/2012	Changed to get use new dataset which is created
--								in the stored procedure generateCurrentDateInformation
-- =============================================
CREATE PROCEDURE [dbo].[FiscalDateGet]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SELECT [MDX Fiscal]
		 , Fiscal
		 , [MDX Fiscal Week]
		 , weekEndingDate

	FROM
		CurrentDateInformation
END
```

