# dbo.inboundloyalty_customermasterde_merge

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.inboundloyalty_customermasterde_merge"]
    dbo_inboundloyalty_customermasterde_merge(["dbo.inboundloyalty_customermasterde_merge"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.inboundloyalty_customermasterde_merge |

## View Code

```sql
; CREATE   VIEW [dbo].[inboundloyalty_customermasterde_merge] AS SELECT [customerNumber] COLLATE Latin1_General_CI_AS AS [customerNumber], [status] COLLATE Latin1_General_CI_AS AS [status], [bonusClubMember], [bonusClubMembershipType] COLLATE Latin1_General_CI_AS AS [bonusClubMembershipType], [bonusClubPointsBalance], [bonusClubStartDate], [hasOnlineAccount], [bonusClubSignUpSource] COLLATE Latin1_General_CI_AS AS [bonusClubSignUpSource], [Country] COLLATE Latin1_General_CI_AS AS [Country], [address_1] COLLATE Latin1_General_CI_AS AS [address_1], [address_2] COLLATE Latin1_General_CI_AS AS [address_2], [address_3] COLLATE Latin1_General_CI_AS AS [address_3], [address_4] COLLATE Latin1_General_CI_AS AS [address_4], [post_code] COLLATE Latin1_General_CI_AS AS [post_code], [mobile] COLLATE Latin1_General_CI_AS AS [mobile], [locale] COLLATE Latin1_General_CI_AS AS [locale], [text_opt_in], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [LifetimePoints], [FirstName] COLLATE Latin1_General_CI_AS AS [FirstName], [LastName] COLLATE Latin1_General_CI_AS AS [LastName], [DataSource] COLLATE Latin1_General_CI_AS AS [DataSource] FROM [dbo].[inboundloyalty_customermasterde_merge]
```

