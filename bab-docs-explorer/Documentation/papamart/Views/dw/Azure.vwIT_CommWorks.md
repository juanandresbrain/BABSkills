# Azure.vwIT_CommWorks

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["Azure.vwIT_CommWorks"]
    dbo_IT_commworks(["dbo.IT_commworks"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.IT_commworks |

## View Code

```sql
CREATE view [Azure].[vwIT_CommWorks]

AS
-- =============================================================================================================
--		Name:				Date:			Comments:
--		Ian Wallace			12/15/2021		Initial creation
-- =============================================================================================================


SELECT [id]
      ,[summary]
      ,[recordType]
      ,[boardName]
      ,[statusName]
      ,[companyName]
      ,[siteName]
      ,[addressLine1]
      ,[addressLine2]
      ,[city]
      ,[stateIdentifier]
      ,[zip]
      ,[countryName]
      ,[contactName]
      ,[contactPhoneNumber]
      ,[contactPhoneExtension]
      ,[contactEmailAddress]
      ,[typeName]
      ,[itemName]
      ,[priorityName]
      ,[prioritySort]
      ,[severity]
      ,[impact]
      ,[closedDate]
      ,[closedBy]
      ,[closedFlag]
      ,[actualHours]
      ,[approved]
      ,[dateResolved]
      ,[dateResplan]
      ,[dateResponded]
      ,[resolveMinutes]
      ,[resPlanMinutes]
      ,[respondMinutes]
      ,[isInSla]
      ,[resources]
      ,[parentTicketId]
      ,[hasChildTicket]
      ,[lastUpdated]
      ,[updatedBy]
	  ,cast([dateEntered1] as date) as dateEntered1
      --,[dateEntered1]
      ,[enteredBy1]
      ,[subTypeName]
      ,[carrierTicket]
      ,[InsertDate]
      ,[UpdateDate]
  FROM [dbo].[IT_commworks]
```

