# dbo.vwHugsNHopeParties

**Database:** BABWPartyPlanner  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwHugsNHopeParties"]
    dbo_Country(["dbo.Country"]) --> VIEW
    dbo_Customer(["dbo.Customer"]) --> VIEW
    dbo_Event(["dbo.Event"]) --> VIEW
    dbo_Package(["dbo.Package"]) --> VIEW
    dbo_Party(["dbo.Party"]) --> VIEW
    dbo_Store(["dbo.Store"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Country |
| dbo.Customer |
| dbo.Event |
| dbo.Package |
| dbo.Party |
| dbo.Store |

## View Code

```sql
CREATE VIEW [dbo].[vwHugsNHopeParties]
AS
SELECT        TOP (100) PERCENT p.PartyID AS 'PMREventID', e.EventStart, cust.LastName AS 'GuestLastName', e.CreatedBy AS 'SubmittedBy', 1 AS 'PartyStatusID', GETDATE() 
                         AS 'DateCreated', GETDATE() AS 'DateUpdated', s.StoreNumber, c.CountryAbbr, pkg.PackageShortDesc, p.TotalGuests
FROM            dbo.Event AS e 
                LEFT JOIN dbo.Party AS p ON e.EventID = p.EventID 
				LEFT JOIN dbo.Store AS s ON e.StoreID = s.StoreID 
				LEFT JOIN dbo.Package AS pkg ON p.PackageID = pkg.PackageID AND pkg.Enabled = 1 
				LEFT JOIN dbo.Customer AS cust ON p.CustomerID = cust.CustomerID
				LEFT JOIN dbo.Country AS c ON s.CountryID = c.CountryID
WHERE        (pkg.PackageShortDesc LIKE 'HUGS N_ HOPE%')
```

