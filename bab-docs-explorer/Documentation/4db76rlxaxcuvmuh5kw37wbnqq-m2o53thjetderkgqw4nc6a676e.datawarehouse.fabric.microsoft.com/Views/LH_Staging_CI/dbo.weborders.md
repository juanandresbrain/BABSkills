# dbo.weborders

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.weborders"]
    dbo_weborders(["dbo.weborders"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.weborders |

## View Code

```sql
;
CREATE   VIEW [dbo].[weborders]
AS
    SELECT [SourceSite] COLLATE Latin1_General_CI_AS AS [SourceSite], [TransactionID], [OrderID], [OrderNum] COLLATE Latin1_General_CI_AS AS [OrderNum], [OrderDate], [ShippingAmount], [OrderStatus] COLLATE Latin1_General_CI_AS AS [OrderStatus], [StatusDate], [Physical] COLLATE Latin1_General_CI_AS AS [Physical], [StatusSortOrder], [ShipToPostalCode] COLLATE Latin1_General_CI_AS AS [ShipToPostalCode], [ShipToState] COLLATE Latin1_General_CI_AS AS [ShipToState], [ShipToCountry] COLLATE Latin1_General_CI_AS AS [ShipToCountry], [ESReferenceNbr] COLLATE Latin1_General_CI_AS AS [ESReferenceNbr], [BillToFirstName] COLLATE Latin1_General_CI_AS AS [BillToFirstName], [BillToLastName] COLLATE Latin1_General_CI_AS AS [BillToLastName], [BillToCity] COLLATE Latin1_General_CI_AS AS [BillToCity], [BillToState] COLLATE Latin1_General_CI_AS AS [BillToState], [BillToPostCode] COLLATE Latin1_General_CI_AS AS [BillToPostCode], [BillToCountry] COLLATE Latin1_General_CI_AS AS [BillToCountry], [BillToEmailAddress] COLLATE Latin1_General_CI_AS AS [BillToEmailAddress], [BillToCustomerNumber] COLLATE Latin1_General_CI_AS AS [BillToCustomerNumber]
    FROM LH_Staging.[dbo].[weborders]
```

