# dbo.party_facts

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

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
;

CREATE VIEW dbo.party_facts AS SELECT party_key, PartyID, OccasionName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS OccasionName, ThemeName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS ThemeName, PackageName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS PackageName, TotalGuests, GOHAge, GuestAvgAge, IsCancelled, IsPOParty, CreatedDateKey, ExecuteDateKey, ExecuteTimeKey, CreatedBy COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CreatedBy, BookingMethod COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS BookingMethod, store_key, INS_DT, UPDT_DT, PMRNumber FROM LH_Mart.dbo.party_facts;;
```

