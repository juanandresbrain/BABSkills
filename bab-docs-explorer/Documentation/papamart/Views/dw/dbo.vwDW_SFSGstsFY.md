# dbo.vwDW_SFSGstsFY

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SFSGstsFY"]
    vwDW_SFSGsts(["vwDW_SFSGsts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| vwDW_SFSGsts |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SFSGstsFY]
as
select fiscal_year,store_key,
count(distinct NewSFSValidEmail_GstID) NewSFSGstsWEmail,
count(distinct New_SFSGstID) NewSFSGsts,
count(distinct SFSValidEmail_GstID) SFSGstsWEmail,
count(distinct SFSGstID) SFSGsts
from [vwDW_SFSGsts]  with (nolock) 
where  ( date_key > 2555) --(date_key > 4010 and date_key < 4595) --(date_key > 3280 and date_key < 4595) -- and store_key in (1) 
group by fiscal_year,store_key
```

