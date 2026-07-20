# dbo.vwdw_party_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_party_dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwdw_party_dim]  
AS  
  
 SELECT 0 AS party_key, 'Non-party' AS party_dim_description  
 UNION  
 SELECT 1 AS party_key, 'Party' AS party_dim_description
```

