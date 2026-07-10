# dbo.vwDW_Registrations_NearBirthday_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Registrations_NearBirthday_Dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Registrations_NearBirthday_Dim]
AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_Registrations_NearBirthday_Dim]
--
-- Description: View underlying the SSAS Registrations Cube used on the dashboard.   
-- Used to indicate the whether or not the Purchaser or Recipient are near their birthday
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		4/13/2012		Initial deployment
-- =============================================================================================================
SELECT 1 AS isNearBirthday
	 , 'Yes' AS descr
	 , 10 AS seq
UNION ALL
SELECT 0 AS isNearBirthday
	 , 'No' AS descr
	 , 20 AS seq
UNION ALL
SELECT -1 AS isNearBirthday
	 , 'Unknown' AS descr
	 , 90 AS seq
```

