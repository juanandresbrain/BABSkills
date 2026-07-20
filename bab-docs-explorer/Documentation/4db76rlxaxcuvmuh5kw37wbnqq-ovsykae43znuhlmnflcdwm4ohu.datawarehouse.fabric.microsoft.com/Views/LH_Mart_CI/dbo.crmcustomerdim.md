# dbo.crmcustomerdim

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[crmcustomerdim] AS     SELECT [CRMCustomerKey], [CustomerID], [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [MembershipDate], [Gender] COLLATE Latin1_General_CI_AS AS [Gender], [BirthDate], [LanguageCode] COLLATE Latin1_General_CI_AS AS [LanguageCode], [CRMUpdateDate], [StoreKey], [CountryCode] COLLATE Latin1_General_CI_AS AS [CountryCode], [PostalCode] COLLATE Latin1_General_CI_AS AS [PostalCode], [PointsEligible], [MembershipType] COLLATE Latin1_General_CI_AS AS [MembershipType], [InsertedDate], [UpdatedDate], [InsertedBy] COLLATE Latin1_General_CI_AS AS [InsertedBy], [UpdatedBy] COLLATE Latin1_General_CI_AS AS [UpdatedBy], [ETLLogID], [ETLEventID], [Emailable], [SubscriberKey], [DirectMailOptIn], [HasPhoneNumber], [Locale] COLLATE Latin1_General_CI_AS AS [Locale], [TextOptIn], [PhoneNumber] COLLATE Latin1_General_CI_AS AS [PhoneNumber], [EmailOptInDate], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [ClubStatus] COLLATE Latin1_General_CI_AS AS [ClubStatus], [CurrentRewardPoints], [SignUpSource] COLLATE Latin1_General_CI_AS AS [SignUpSource], [address_1] COLLATE Latin1_General_CI_AS AS [address_1], [address_2] COLLATE Latin1_General_CI_AS AS [address_2], [address_3] COLLATE Latin1_General_CI_AS AS [address_3], [address_4] COLLATE Latin1_General_CI_AS AS [address_4], [hasOnlineAccount], [isBonusClubMember], [LifetimeTotalPointsEarned], [FirstName] COLLATE Latin1_General_CI_AS AS [FirstName], [LastName] COLLATE Latin1_General_CI_AS AS [LastName], [MembershipPlan] COLLATE Latin1_General_CI_AS AS [MembershipPlan], [OriginDate], [DataSource] COLLATE Latin1_General_CI_AS AS [DataSource]     FROM [dbo].[crmcustomerdim]
```

