# dbo.sp_GetBookedPartiesByCustomer_SS20170725

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_GetBookedPartiesByCustomer_SS20170725"]
    dbo_Comment(["dbo.Comment"]) --> SP
    dbo_Customer(["dbo.Customer"]) --> SP
    dbo_Event(["dbo.Event"]) --> SP
    dbo_OptionPartyXref(["dbo.OptionPartyXref"]) --> SP
    dbo_Party(["dbo.Party"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Comment |
| dbo.Customer |
| dbo.Event |
| dbo.OptionPartyXref |
| dbo.Party |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Tim Bytnar
-- Create date: 4/27/2017
-- Description:	Takes the parameter @CustomerNumber and will get an XML formatted list of all parties for that customer.
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetBookedPartiesByCustomer_SS20170725] 
	-- Add the parameters for the stored procedure here
	@CustomerNumber varchar(32) = NULL
AS
BEGIN
	SET NOCOUNT ON;

     SELECT '<?xml version="1.0" encoding="UTF-8"?>' + 
	CAST(
	    (SELECT(SELECT p.OccasionID,
		  ISNULL(p.TotalGuests, 0) as TotalGuests,
		  e.StoreID,
		  e.EventStart,
		  e.EventEnd,
		  ISNULL(p.GOHFirstName, 'None') as GOHFirstName,
		  ISNULL(p.GOHAge, 0) as GOHAge,
		  ISNULL(p.GuestAvgAge, 0) as GuestAvgAge,
		  (SELECT OptionID AS 'Option'
			 FROM OptionPartyXref o 
			 WHERE o.PartyID = p.PartyID 
			 FOR XML PATH (''),type) AS Options,
		  ISNULL(p.DepositAmount,0) as DepositAmount,
		  ISNULL(e.CreatedBy, 1) as CreatedBy,
		  (SELECT c.Comment AS 'CommentText', c.CreatedBy, c.CreatedDate
			 FROM Comment c
			 WHERE c.EventID = e.EventID 
			 FOR XML PATH ('Comment'),type)  
		  AS Comments,
		  ISNULL(c.CustomerNumber, 0) as CustomerNumber,
		  ISNULL(c.FirstName, 'None') as CustomerFirstName,
		  ISNULL(c.LastName, 'None') as CustomerLastName,
		  PrimaryPhone,
		  SecondaryPhone,
		  ISNULL(c.Address1, 'None') as Address1,
		  ISNULL(c.Address2, 'None') as Address2,
		  ISNULL(c.Organization, 'None') as Organization,
		  ISNULL(c.City, 'None') as City,
		  ISNULL(c.State, 'None') as State,
		  ISNULL(c.Country, 'None') as Country,
		  ISNULL(c.Zipcode, 'None') as ZipCode,
		  ISNULL(c.EmailAddress, 'None') as EmailAddress,
		  ISNULL(p.GOHGender, 0) as GOHGender,
		  ISNULL(p.PartyStateID, 0) as PartyStateID,
		  ISNULL(p.PartyThemeID, 0) as PartyThemeID

	   FROM Party p
		  LEFT JOIN Customer c WITH (NOLOCK) on p.CustomerID = c.CustomerID
		  LEFT JOIN Event e WITH (NOLOCK) on p.EventID = e.EventID
	   WHERE c.CustomerNumber = @CustomerNumber
	   AND e.Active = 1

	   FOR XML PATH ('PartyBooking'),type) FOR XML PATH ('PartyBookings')) 
    AS varchar(max))
END
```

