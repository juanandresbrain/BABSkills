# dbo.vwDW_Store_NewHearMe

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Store_NewHearMe"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Store_NewHearMe] 
-- =============================================================================================================
-- Name: [dbo].[vwDW_Store_NewHearMe]
--
-- Description: This returns the stores which have the new HearMe sound stations.
--
-- Dependencies: 
--
-- Revision History

--		Name:			Date:			Comments:
--		G. Murrish		11/14/2013		Added a bunch of stores...
--		G. Murrish		5/8/2013		Added Stores 10,21,96
--		G. Murrish		10/22/2012		Added Store 30
--		G. Murrish		10/10/2012		Added stores 307,079,020,107,012
--		G. Murrish		9/21/2012		Added stores 64 and 80
--		G. Murrish		6/29/2012		Added store 603
--		G. Murrish		6/4/2012		Added store 2019 
--		G. Murrish		5/8/2012		Added stores 38
--		G. Murrish		4/5/2012		Added stores 46 and 19
--		G. Murrish		11/8/2011		Initial Deployment


AS

	SELECT 105 AS store_key, cast('5/10/2011' AS DATETIME) AS startingDate
UNION ALL SELECT 48 AS store_key, cast('8/10/2011' AS DATETIME) AS startingDate
UNION ALL SELECT 210 AS store_key, cast('9/7/2011' AS DATETIME) AS startingDate -- Store 200 MOA
UNION ALL SELECT 324 AS store_key, cast('9/14/2011' AS DATETIME) AS startingDate -- Store 248 La Plaza
UNION ALL SELECT 55 AS store_key, cast('9/15/2011' AS DATETIME) AS startingDate -- Store 055 Baybrook	
UNION ALL SELECT 100 AS store_key, cast('9/20/2011' AS DATETIME) AS startingDate -- Roosevelt Field	
UNION ALL SELECT 3 AS store_key, cast('10/4/2011' AS DATETIME) AS startingDate -- Woodfield Mall
UNION ALL SELECT 4 AS store_key, cast('10/7/2011' AS DATETIME) AS startingDate -- Oakbrook Center
UNION ALL SELECT 16 AS store_key, cast('10/12/2011' AS DATETIME) AS startingDate -- Easton	
UNION ALL SELECT 1 AS store_key, cast('10/19/2011' AS DATETIME) AS startingDate -- Galleria (REAL IMPLEMENTATION)
UNION ALL SELECT 46 AS store_key, cast('1/1/2012' AS DATETIME) AS startingDate -- Washington Square
UNION ALL SELECT 19 AS store_key, cast('4/1/2012' AS DATETIME) AS startingDate -- Opry Mills
UNION ALL SELECT 56 AS store_key, cast('4/30/2012' AS DATETIME) AS startingDate -- Ross Park
UNION ALL SELECT 38 AS store_key, cast('5/12/2012' AS DATETIME) AS startingDate -- Rivertown
UNION ALL SELECT 281 AS store_key, cast('6/1/2012' AS DATETIME) AS startingDate -- 2019 (Hamley's)
UNION ALL SELECT 615 AS store_key, cast('6/22/2012' AS DATETIME) AS startingDate -- 603 Gurnee Mills POP
UNION ALL SELECT 64 AS store_key, cast('7/12/2012' AS DATETIME) AS startingDate -- 64 Palisades
UNION ALL SELECT 79 AS store_key, cast('6/22/2012' AS DATETIME) AS startingDate -- 80 Paramus
UNION ALL SELECT 686 AS store_key, cast('10/1/2012' AS DATETIME) AS startingDate -- 307 Stonebridge
UNION ALL SELECT 78 AS store_key, cast('10/15/2012' AS DATETIME) AS startingDate -- 079 Westfield Anapolis
UNION ALL SELECT 20 AS store_key, cast('10/22/2012' AS DATETIME) AS startingDate -- 020 Somerset Collection
UNION ALL SELECT 107 AS store_key, cast('11/5/2012' AS DATETIME) AS startingDate -- 107 Fair Oaks
UNION ALL SELECT 12 AS store_key, cast('11/12/2012' AS DATETIME) AS startingDate -- 012 Castleton Square
UNION ALL SELECT 30 AS store_key, cast('10/5/2012' AS DATETIME) AS startingDate -- 030 King of Prussia
UNION ALL SELECT 10 AS store_key, cast('4/22/2013' AS DATETIME) AS startingDate -- 010 Mall of Georgia
UNION ALL SELECT 21 AS store_key, cast('4/29/2013' AS DATETIME) AS startingDate -- 021 Orland Square
UNION ALL SELECT 96 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 096 Northshore Mall
UNION ALL SELECT 9 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 9 The Gardens of Palm Beaches
UNION ALL SELECT 15 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 15 The Florida Mall
UNION ALL SELECT 40 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 40 Crabtree Valley Mall
UNION ALL SELECT 41 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 41 Westfield Valley Fair
UNION ALL SELECT 47 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 47 Smith Haven Mall 
UNION ALL SELECT 63 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 63 Great Lakes Mall
UNION ALL SELECT 72 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 72 The Oaks
UNION ALL SELECT 88 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 88 Westfield Montgomery
UNION ALL SELECT 89 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 89 Memorial City Mall
UNION ALL SELECT 139 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 137 Cherry Hill Mall
UNION ALL SELECT 141 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 139 The Mall at Fairfield Commons
UNION ALL SELECT 157 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 154 Cool Springs Galleria
UNION ALL SELECT 160 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 157 The Mall at Tuttle Crossing 
UNION ALL SELECT 692 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 308 Galleria at Roseville
UNION ALL SELECT 693 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 309 Park Meadows
UNION ALL SELECT 695 AS store_key, cast('5/6/2013' AS DATETIME) AS startingDate -- 310 Friendly Center
```

