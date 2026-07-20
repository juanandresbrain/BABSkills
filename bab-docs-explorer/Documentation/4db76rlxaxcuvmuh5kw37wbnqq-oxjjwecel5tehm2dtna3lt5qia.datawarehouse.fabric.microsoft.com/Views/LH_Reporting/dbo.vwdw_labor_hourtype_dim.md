# dbo.vwdw_labor_hourtype_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_labor_hourtype_dim"]
    dbo_labor_hourtype_dim(["dbo.labor_hourtype_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.labor_hourtype_dim |

## View Code

```sql
CREATE VIEW vwdw_labor_hourtype_dim  
 AS  
 -- =============================================================================================================  
 -- Name: [dbo].[vwDW_Labor_HourType_Dim]  
 --  
 -- Description: View HourType Dimension used in the Cube  
 -- Classifies the Type of Labor Hours.  
 --  
 --  
 -- Dependencies:   
 --  
 -- Revision History  
 --  Name:    Date:   Comments:  
 --  Gary Murrish  5/7/2012  Initial deployment  
 -- =============================================================================================================  
 SELECT top 1 HourType_key AS   hourtype_key
   , descr  
   , CASE WHEN isPaid = 1 THEN 'Paid' ELSE 'Not Paid' END AS ispaid  
 FROM  
  LH_Mart.dbo.labor_hourtype_dim
```

