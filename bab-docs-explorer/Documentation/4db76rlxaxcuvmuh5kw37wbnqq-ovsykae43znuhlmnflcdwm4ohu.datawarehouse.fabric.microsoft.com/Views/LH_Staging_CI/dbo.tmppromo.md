# dbo.tmppromo

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmppromo"]
    dbo_tmppromo(["dbo.tmppromo"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmppromo |

## View Code

```sql
; CREATE   VIEW [dbo].[tmppromo] AS SELECT [TransactionID], [hasCountYourCandles], [hasBirthdayGift], [hasHalfBirthday], [hasWinback], [hasOther] FROM [dbo].[tmppromo]
```

