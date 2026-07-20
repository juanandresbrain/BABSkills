# dbo.loyaltygcranges

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

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
; CREATE   VIEW [dbo].[loyaltygcranges] AS     SELECT [Style_Code] COLLATE Latin1_General_CI_AS AS [Style_Code], [GiftCardRangeStart] COLLATE Latin1_General_CI_AS AS [GiftCardRangeStart], [GiftCardRangeEnd] COLLATE Latin1_General_CI_AS AS [GiftCardRangeEnd], [Department] COLLATE Latin1_General_CI_AS AS [Department], [Class] COLLATE Latin1_General_CI_AS AS [Class], [SubClass] COLLATE Latin1_General_CI_AS AS [SubClass], [InsertDate], [UpdateDate]     FROM [dbo].[loyaltygcranges]
```

