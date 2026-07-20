# dbo.crmde1

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmde1"]
    dbo_crmde1(["dbo.crmde1"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmde1 |

## View Code

```sql
;

CREATE VIEW dbo.crmde1 AS SELECT customerNumber COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS customerNumber, SubscriberKey COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS SubscriberKey, status COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS status, dateJoined, LastSentDate, LastOpenDate, LastClickDate, bonusClubMember, bonusClubMembershipType COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS bonusClubMembershipType, bonusClubPointsBalance, hasOnlineAccount, bonusClubSignUpSource COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS bonusClubSignUpSource, Country COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Country, FrequencyCount3m, FrequencyCount6m, FrequencyCount12m, FrequencyCount18m, FrequencyCount24m, FrequencyCountTTL, RecencyCount3m, RecencyCount6m, RecencyCount12m, RecencyCount18m, RecencyCount24m, RecencyCountTTL, MonetarySum3m, MonetarySum6m, MonetarySum12m, MonetarySum18m, MonetarySum24m, MonetarySumTTL, FrequencyCount1m, RecencyCount1m, MonetarySum1m, address_1 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_1, address_2 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_2, address_3 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_3, address_4 COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS address_4, post_code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS post_code, mobile COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS mobile, locale COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS locale, text_opt_in, InsertDate, UpdateDate, EmailAddress COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS EmailAddress, LastTransactionDate, LastTransactionStore COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS LastTransactionStore, PreferredStory COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PreferredStory, Emailable, FrequencyCount36m, RecencyCount36m, MonetarySum36m, LifetimePoints, FirstTransactionDate, FirstStoreConcept COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FirstStoreConcept, FirstName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FirstName, LastName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS LastName, UpdateDateRecency, MembershipPlan COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS MembershipPlan FROM LH_Mart.dbo.crmde1;;
```

