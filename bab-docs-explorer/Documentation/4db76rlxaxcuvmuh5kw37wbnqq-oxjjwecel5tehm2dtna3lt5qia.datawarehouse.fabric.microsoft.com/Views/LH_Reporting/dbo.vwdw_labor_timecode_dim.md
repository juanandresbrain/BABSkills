# dbo.vwdw_labor_timecode_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_labor_timecode_dim"]
    dbo_labor_timecode_dim(["dbo.labor_timecode_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.labor_timecode_dim |

## View Code

```sql
CREATE VIEW vwdw_labor_timecode_dim
 AS
 -- =============================================================================================================  
 -- Name: dbo.vwDW_Labor_TimeCode_Dim  
 --  
 -- Description: View TimeCode Dimension used in the Cube  
 -- Classifies the Type of Labor Hours.  
 --  
 --  
 -- Dependencies:   
 --  
 -- Revision History  
 --  Name:    Date:   Comments:  
 --  Gary Murrish  5/7/2012  Initial deployment  
 -- =============================================================================================================  
 SELECT TOP 1 timeCode_key  
   , descr  
   , abrv  
   , CASE WHEN isWork = 1 THEN 'Work' ELSE 'Not Work' END AS iswork  
 FROM  LH_Mart.dbo.labor_timecode_dim
```

