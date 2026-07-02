# dbo.sp_InsertNewParty_V2

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_InsertNewParty_V2"]
    dbo_Party(["dbo.Party"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Party |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Tim Bytnar
-- Create date: 5/2/2017
-- Description:	This stored proc will insert the Party record data and return the newly created PartyID
-- =============================================
CREATE PROCEDURE [dbo].[sp_InsertNewParty_V2] 
	@OccasionID int,
	@TotalGuests int,
	@CustomerID int,
	@EventID int,
	@GOHAge int,
	@GOHFirstName varchar(50),
	@GOHGender int,
	@GuestAvgAge int,
	@PartyStateID int = 0,
	@DepositAmount decimal(9,2),
	@PackageID int,
	@POID int = NULL,
	@ThemeID int,
	@PartyID int OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
    BEGIN TRY
	   BEGIN TRAN
		   DECLARE @PartyIDResult table(id int)

		   INSERT INTO BABWPartyPlanner.dbo.Party (OccasionID, TotalGuests, CustomerID, EventID, GOHAge, GOHFirstName, GOHGender, GuestAvgAge, PartyStateID, DepositAmount, PackageID, POID, ThemeID)
			 OUTPUT inserted.PartyID into @PartyIDResult
		   VALUES (@OccasionID, @TotalGuests, @CustomerID, @EventID, @GOHAge, @GOHFirstName, @GOHGender, @GuestAvgAge, @PartyStateID, @DepositAmount, @PackageID, @POID, @ThemeID)

		   SET @PartyID = (SELECT ID from @PartyIDResult)
	   COMMIT
    END TRY
    BEGIN CATCH
	   IF(@@TRANCOUNT > 0)
		  ROLLBACK TRAN
    END CATCH
END
```

