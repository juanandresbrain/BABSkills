# dbo.vwDW_Registrations_TourismBand_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Registrations_TourismBand_Dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Registrations_TourismBand_Dim]
AS
-- =============================================================================================================
-- Name: [dbo].[vwDW_Registrations_TourismBand_Dim]
--
-- Description: View underlying the SSAS Registrations Cube used on the dashboard.   
-- Used to indicate the Tourism Band of the recepient
--
--
-- Dependencies: 
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		4/13/2012		Initial deployment
-- =============================================================================================================
SELECT 1 AS TourismBand
	 , '1) 00.00 - 29.99 Miles' AS Description
UNION ALL
SELECT 2
	 , '2) 30.00 - 49.99 Miles'
UNION ALL
SELECT 3
	 , '3) 50.00 - 99.99 Miles'
UNION ALL
SELECT 4
	 , '4) 100+ Miles'
UNION ALL
SELECT 5
	 , '5) Foreign'
UNION ALL
SELECT -1
	 , '6) Unspecified'
```

