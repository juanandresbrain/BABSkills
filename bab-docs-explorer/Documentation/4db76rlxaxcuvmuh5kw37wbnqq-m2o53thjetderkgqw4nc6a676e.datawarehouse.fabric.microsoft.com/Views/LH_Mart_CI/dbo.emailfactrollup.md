# dbo.emailfactrollup

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailfactrollup"]
    dbo_emailfactrollup(["dbo.emailfactrollup"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailfactrollup |

## View Code

```sql
;

CREATE VIEW dbo.emailfactrollup AS SELECT EmailAddress COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS EmailAddress, LastSendDate, LastClickDate, LastOpenDate, LastBounceDate, LastUnSubscribeDate FROM LH_Mart.dbo.emailfactrollup;;
```

