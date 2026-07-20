# dbo.vwdw_registrations_tourism_5to25_mileband_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_registrations_tourism_5to25_mileband_dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW vwdw_registrations_tourism_5to25_mileband_dim
AS  
-- =============================================================================================================  
-- Name: [dbo].[vwDW_Registrations_Tourism_5to25_MileBand_Dim]  
--  
-- Description: View underlying the SSAS Registrations Cube used on the dashboard.     
-- Used to indicate the Tourism 5to25 MileBand Band of the recepient  
--  
--  
-- Dependencies:   
--  
-- Revision History  
--  Name:    Date:   Comments:  
--  Gary Murrish  4/13/2012  Initial deployment  
-- =============================================================================================================  
SELECT 1 AS [5to25_mileband]  
  , '1) 00.00 - 4.99 Miles' AS [description]
UNION ALL  
SELECT 2  
  , '2) 5.00 - 9.99 Miles'  
UNION ALL  
SELECT 3  
  , '3) 10.00 - 14.99 Miles'  
UNION ALL  
SELECT 4  
  , '4) 15.00 - 19.99 Miles'  
UNION ALL  
SELECT 5  
  , '5) 20.00 - 24.99 Miles'  
UNION ALL  
SELECT 6  
  , '6) 25.00 - 49.99 Miles'  
UNION ALL  
SELECT 7  
  , '7) 50.00 - 74.99 Miles'  
UNION ALL  
SELECT 8  
  , '8) 75.00 - 99.99 Miles'  
UNION ALL  
SELECT 9  
  , '9) 100+ Miles'  
UNION ALL  
SELECT 900  
  , '10) Foreign'  
UNION ALL  
SELECT -1  
  , '11) Unspecified'
```

