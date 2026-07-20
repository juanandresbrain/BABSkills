# dbo.vwdw_registrations_gender_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_registrations_gender_dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW vwdw_registrations_gender_dim
AS  
-- =============================================================================================================  
-- Name: [dbo].[vwDW_Registrations_Gender_Dim]  
--  
-- Description: View underlying the SSAS Registrations Cube used on the dashboard.     
-- Used to indicate the Gender of the recepient  
--  
--  
-- Dependencies:   
--  
-- Revision History  
--  Name:    Date:   Comments:  
--  Gary Murrish  4/13/2012  Initial deployment  
-- =============================================================================================================  
SELECT 'M' AS gndr_cd  
  , 'Boy' AS descr  
  , 10 AS seq  
UNION ALL  
SELECT 'F' AS GNDR_CD  
  , 'Girl' AS descr  
  , 20 AS seq  
UNION ALL  
SELECT 'U' AS GNDR_CD  
  , 'Unknown' AS descr  
  , 30 AS seq
```

