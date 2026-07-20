# dbo.franchiseeproductattributestage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseeproductattributestage"]
    dbo_franchiseeproductattributestage(["dbo.franchiseeproductattributestage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseeproductattributestage |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseeproductattributestage] AS SELECT [Franchisee] COLLATE Latin1_General_CI_AS AS [Franchisee], [StyleCode] COLLATE Latin1_General_CI_AS AS [StyleCode], [CustomAttribute1] COLLATE Latin1_General_CI_AS AS [CustomAttribute1] FROM [dbo].[franchiseeproductattributestage]
```

