# dbo.sp_GetBookedPartiesByCustomer_BJB

**Database:** BABWPartyPlanner_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_GetBookedPartiesByCustomer_BJB"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Tim Bytnar
-- Create date: 4/27/2017
-- Description:	Takes the parameter @CustomerNumber and will get an XML formatted list of all parties for that customer.
-- =============================================
CREATE PROCEDURE [dbo].[sp_GetBookedPartiesByCustomer_BJB] 
	-- Add the parameters for the stored procedure here
	@LastName varchar(64) = NULL,
	@PartyID int = NULL,
	@PrimaryPhone varchar(32) = NULL,
	@EmailAddress varchar(128) = NULL,
	@CustomerNumber varchar(32) = NULL
AS
BEGIN
	SET NOCOUNT ON;

       DECLARE @WhereClause varchar(max) = ''
       DECLARE @sql varchar(max)
       if @LastName is not null AND @LastName <> ''
       BEGIN 
              SET @WhereClause = 'c.LastName = ''' + @LastName + ''' and '
       END
	   if @PartyID is not null AND @PartyID <> ''
       BEGIN 
              SET @WhereClause = 'p.PartyID = ' + CAST(@PartyID AS VARCHAR) + ' and '
       END
	   if @PrimaryPhone is not null AND @PrimaryPhone <> ''
       BEGIN 
              SET @WhereClause = 'c.PrimaryPhone = ''' + @PrimaryPhone + ''' and '
       END
	   if @EmailAddress is not null AND @EmailAddress <> ''
       BEGIN 
              SET @WhereClause = 'c.EmailAddress = ''' + @EmailAddress + ''' and '
       END
       if @CustomerNumber is not null AND @CustomerNumber <> ''
       BEGIN 
              SET @WhereClause = 'c.CustomerNumber = ''' + @CustomerNumber + ''' and '
       END
	   
	   IF LEN(@WhereClause) > 0
	   BEGIN
		SET @WhereClause = SUBSTRING(@WhereClause, 0, LEN(@WhereClause)-3)
	   END
  
    SET @sql = 'WITH ActiveEvents (EventID, StoreID, EventStart, EventEnd, CreatedBy)
	AS
	(
		SELECT EventID, StoreID, EventStart, EventEnd, CreatedBy
		FROM Event
		WHERE Active = 1
	)SELECT ''' + '<?xml version="1.0" encoding="UTF-8"?> ' + ''' +
       CAST(
           (SELECT(SELECT p.OccasionID,
                ISNULL(p.TotalGuests, 0) as TotalGuests,
                e.StoreID,
                e.EventStart,
                e.EventEnd,
                ISNULL(p.GOHFirstName, ''' + 'None' + ''') as GOHFirstName,
                ISNULL(p.GOHAge, 0) as GOHAge,
                ISNULL(p.GuestAvgAge, 0) as GuestAvgAge,
                (SELECT OptionID AS ''' + 'Option' + '''
                     FROM OptionPartyXref o 
                      WHERE o.PartyID = p.PartyID 
                      FOR XML PATH (' + '''''' + '),type) AS Options,
                ISNULL(p.DepositAmount,0) as DepositAmount,
                ISNULL(e.CreatedBy, 1) as CreatedBy,
                (SELECT c.Comment AS ''' + 'CommentText' + ''', c.CreatedBy, c.CreatedDate
                     FROM Comment c
                     WHERE c.EventID = e.EventID 
                      FOR XML PATH (''' + 'Comment' + '''),type)  
                AS Comments,
                ISNULL(c.CustomerNumber, 0) as CustomerNumber,
                ISNULL(c.FirstName, ''' + 'None' + ''') as CustomerFirstName,
                ISNULL(c.LastName, ''' + 'None' + ''') as CustomerLastName,
                PrimaryPhone,
                SecondaryPhone,
                ISNULL(c.Address1, ''' + 'None' + ''') as Address1,
                ISNULL(c.Address2, ''' + 'None' + ''') as Address2,
                ISNULL(c.Organization, ''' + 'None' + ''') as Organization,
                ISNULL(c.City, ''' + 'None' + ''') as City,
                ISNULL(c.State, ''' + 'None' + ''') as State,
                ISNULL(c.Country, ''' + 'None' + ''') as Country,
                ISNULL(c.Zipcode, ''' + 'None' + ''' ) as ZipCode,
                ISNULL(c.EmailAddress, ''' + 'None' + ''') as EmailAddress,
                ISNULL(p.GOHGender, 0) as GOHGender,
                ISNULL(p.PartyStateID, 0) as PartyStateID,
                ISNULL(p.PartyThemeID, 0) as PartyThemeID

          FROM Party p
                LEFT JOIN Customer c WITH (NOLOCK) on p.CustomerID = c.CustomerID
                LEFT JOIN ActiveEvents e WITH (NOLOCK) on p.EventID = e.EventID   
          WHERE ' + @WhereClause + '

          FOR XML PATH (''' + 'PartyBooking' + '''),type) FOR XML PATH (''' + 'PartyBookings' + ''')) 
    AS varchar(max))'

	SELECT @sql
END
```

