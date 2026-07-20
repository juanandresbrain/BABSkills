# dbo.emaileventfact

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emaileventfact"]
    dbo_emaileventfact(["dbo.emaileventfact"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emaileventfact |

## View Code

```sql
;

CREATE VIEW dbo.emaileventfact AS SELECT ClientID, SendID, Subject COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Subject, EmailName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS EmailName, EventDate, InsertDate, UpdateDate FROM LH_Mart.dbo.emaileventfact;;
```

