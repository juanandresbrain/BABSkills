# dbo.weborders

**Database:** LH_Mart_CI  
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

CREATE VIEW dbo.weborders AS SELECT SourceSite COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS SourceSite, TransactionID, OrderID, OrderNum COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS OrderNum, OrderDate, ShippingAmount, OrderStatus COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS OrderStatus, StatusDate, Physical COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Physical, StatusSortOrder, ShipToPostalCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipToPostalCode, ShipToState COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipToState, ShipToCountry COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ShipToCountry, ESReferenceNbr COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ESReferenceNbr, InsertDate, UpdateDate, BillToFirstName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToFirstName, BillToLastName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToLastName, BillToCity COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToCity, BillToState COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToState, BillToPostCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToPostCode, BillToCountry COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToCountry, BillToEmailAddress COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToEmailAddress, BillToCustomerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BillToCustomerNumber FROM LH_Mart.dbo.weborders;;
```

