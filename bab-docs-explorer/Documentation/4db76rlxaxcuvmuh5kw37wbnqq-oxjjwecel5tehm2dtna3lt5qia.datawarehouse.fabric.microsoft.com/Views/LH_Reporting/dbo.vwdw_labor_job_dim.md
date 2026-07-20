# dbo.vwdw_labor_job_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_labor_job_dim"]
    dbo_labor_job_dim(["dbo.labor_job_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.labor_job_dim |

## View Code

```sql
CREATE VIEW vwdw_labor_job_dim
 AS  
 -- =============================================================================================================  
 -- Name: dbo.vwDW_Labor_Job_Dim  
 --  
 -- Description: View Job Dimension used in the Cube  
 -- Classifies the Work Classification of the hours.  
 --  
 --  
 -- Dependencies:   
 --  
 -- Revision History  
 --  Name:    Date:   Comments:  
 --  Gary Murrish  5/7/2012  Initial deployment  
 -- =============================================================================================================  
 SELECT top 1 job_key  
   , descr  
   , abrv  
 FROM  LH_Mart.dbo.labor_job_dim
```

