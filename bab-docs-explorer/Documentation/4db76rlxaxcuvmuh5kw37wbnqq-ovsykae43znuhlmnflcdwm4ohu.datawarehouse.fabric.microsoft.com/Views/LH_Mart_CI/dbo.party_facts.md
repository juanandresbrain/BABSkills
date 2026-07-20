# dbo.party_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.party_facts"]
    dbo_party_facts(["dbo.party_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.party_facts |

## View Code

```sql
; CREATE   VIEW [dbo].[party_facts] AS     SELECT [party_key], [PartyID], [OccasionName] COLLATE Latin1_General_CI_AS AS [OccasionName], [ThemeName] COLLATE Latin1_General_CI_AS AS [ThemeName], [PackageName] COLLATE Latin1_General_CI_AS AS [PackageName], [TotalGuests], [GOHAge], [GuestAvgAge], [IsCancelled], [IsPOParty], [CreatedDateKey], [ExecuteDateKey], [ExecuteTimeKey], [CreatedBy] COLLATE Latin1_General_CI_AS AS [CreatedBy], [BookingMethod] COLLATE Latin1_General_CI_AS AS [BookingMethod], [store_key], [INS_DT], [UPDT_DT], [PMRNumber]     FROM [dbo].[party_facts]
```

