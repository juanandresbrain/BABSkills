# dbo.loyaltygcranges

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.loyaltygcranges"]
    dbo_loyaltygcranges(["dbo.loyaltygcranges"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.loyaltygcranges |

## View Code

```sql
;

CREATE VIEW dbo.loyaltygcranges AS SELECT Style_Code COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Style_Code, GiftCardRangeStart COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS GiftCardRangeStart, GiftCardRangeEnd COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS GiftCardRangeEnd, Department COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Department, Class COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Class, SubClass COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS SubClass, InsertDate, UpdateDate FROM LH_Mart.dbo.loyaltygcranges;
```

