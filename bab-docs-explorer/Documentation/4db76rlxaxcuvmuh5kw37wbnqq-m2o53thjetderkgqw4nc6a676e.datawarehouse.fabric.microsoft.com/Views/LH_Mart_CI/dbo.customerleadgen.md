# dbo.customerleadgen

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.customerleadgen"]
    dbo_customerleadgen(["dbo.customerleadgen"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.customerleadgen |

## View Code

```sql
;

CREATE VIEW dbo.customerleadgen AS SELECT EntryDate, CountryCode COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS CountryCode, Campaign COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Campaign, Source COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS Source, EmailAddress COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS EmailAddress, FileDate, FileName COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8  AS FileName, InsertDate, UpdateDate FROM LH_Mart.dbo.customerleadgen;;
```

