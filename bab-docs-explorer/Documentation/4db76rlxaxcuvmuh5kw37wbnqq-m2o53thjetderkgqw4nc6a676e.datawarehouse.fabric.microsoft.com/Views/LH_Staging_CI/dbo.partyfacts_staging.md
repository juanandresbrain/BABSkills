# dbo.partyfacts_staging

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.partyfacts_staging"]
    dbo_partyfacts_staging(["dbo.partyfacts_staging"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.partyfacts_staging |

## View Code

```sql
;
CREATE   VIEW [dbo].[partyfacts_staging]
AS
    SELECT [PartyID], [OccasionName] COLLATE Latin1_General_CI_AS AS [OccasionName], [PackageName] COLLATE Latin1_General_CI_AS AS [PackageName], [TotalGuests], [GOHAge], [GuestAvgAge], [IsCancelled], [IsPOParty], [CreatedDateKey], [ExecuteDateKey], [ExecuteTimeKey], [CreatedBy] COLLATE Latin1_General_CI_AS AS [CreatedBy], [BookingMethod] COLLATE Latin1_General_CI_AS AS [BookingMethod], [store_key], [PMRNumber], [ThemeName] COLLATE Latin1_General_CI_AS AS [ThemeName]
    FROM LH_Staging.[dbo].[partyfacts_staging]
```

