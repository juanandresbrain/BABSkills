# dbo.crmcustomerdim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmcustomerdim"]
    dbo_crmcustomerdim(["dbo.crmcustomerdim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmcustomerdim |

## View Code

```sql
;

CREATE VIEW dbo.crmcustomerdim AS SELECT CRMCustomerKey, CustomerID, CustomerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CustomerNumber, MembershipDate, Gender COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Gender, BirthDate, LanguageCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS LanguageCode, CRMUpdateDate, StoreKey, CountryCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CountryCode, PostalCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PostalCode, PointsEligible, MembershipType COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS MembershipType, InsertedDate, UpdatedDate, InsertedBy COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS InsertedBy, UpdatedBy COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS UpdatedBy, ETLLogID, ETLEventID, Emailable, SubscriberKey, DirectMailOptIn, HasPhoneNumber, Locale COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Locale, TextOptIn, PhoneNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PhoneNumber, EmailOptInDate, EmailAddress COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS EmailAddress, ClubStatus COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ClubStatus, CurrentRewardPoints, SignUpSource COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS SignUpSource, address_1 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_1, address_2 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_2, address_3 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_3, address_4 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_4, hasOnlineAccount, isBonusClubMember, LifetimeTotalPointsEarned, FirstName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FirstName, LastName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS LastName, MembershipPlan COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS MembershipPlan, OriginDate, DataSource COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS DataSource FROM LH_Mart.dbo.crmcustomerdim;;
```

