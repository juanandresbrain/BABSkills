# dbo.loyaltyproductsnostyle

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.loyaltyproductsnostyle"]
    dbo_loyaltyproductsnostyle(["dbo.loyaltyproductsnostyle"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.loyaltyproductsnostyle |

## View Code

```sql
;

CREATE VIEW dbo.loyaltyproductsnostyle AS SELECT ProductKey, Style COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Style, StyleDescription COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS StyleDescription, Color COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Color, Concept COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Concept, Chain COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Chain, Division COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Division, Department COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Department, Class COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Class, SubClass COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS SubClass, DeptCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS DeptCode, SubClassCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS SubClassCode, ScorecardCategory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS ScorecardCategory, PrimaryVendorCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS PrimaryVendorCode, PrimaryVendorName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS PrimaryVendorName, AltPrimaryVendorCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS AltPrimaryVendorCode, CurrentRetail, OriginalRetail, CurrentSellingRetailHome, PriceWithVat, EuroValue, CanValue, MerchStatus COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS MerchStatus, JurisdictionCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS JurisdictionCode, Gender COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Gender, CoreFashCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS CoreFashCode, InlineCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS InlineCode, ActivationDate, KeyStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS KeyStory, LicenseCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS LicenseCode FROM LH_Mart.dbo.loyaltyproductsnostyle;
```

