# dbo.serializedvoucher

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.serializedvoucher"]
    dbo_serializedvoucher(["dbo.serializedvoucher"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.serializedvoucher |

## View Code

```sql
;

CREATE VIEW dbo.serializedvoucher AS SELECT SerializedNumber, StartDate, DiscountAmount, CustomerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CustomerNumber, Email COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Email, ExpirationDate, isExported, InsertDate, UpdateDate, FirstName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FirstName, LastName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS LastName, Address1 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Address1, Address2 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Address2, City COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS City, State COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS State, ZipCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ZipCode, Country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Country, ExportedDate, ExportedDateXML, CouponID, Description COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Description, Status COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Status, title COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS title FROM LH_Mart.dbo.serializedvoucher;;
```

