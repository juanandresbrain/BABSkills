# dbo.vwDW_Registrations_Tourism_5to25_MileBand_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Registrations_Tourism_5to25_MileBand_Dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Registrations_Tourism_5to25_MileBand_Dim]
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
--		Name:				Date:			Comments:
--		Gary Murrish		4/13/2012		Initial deployment
-- =============================================================================================================
SELECT 1 AS [5to25_MileBand]
	 , '1) 00.00 - 4.99 Miles' AS DESCRIPTION
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

