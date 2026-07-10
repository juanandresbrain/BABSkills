# dbo.vwInverse_Static_Exchange_Rate

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwInverse_Static_Exchange_Rate"]
    dbo_Corp_Static_Exchange_Rate_Control(["dbo.Corp_Static_Exchange_Rate_Control"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Corp_Static_Exchange_Rate_Control |

## View Code

```sql
/***********************************************************************************************
Object Name:			dbo.[vwInverse_Static_Exchange_Rate]
Description/Purpose:	view used for creating inverse of rates

-- Dependencies: 
--
-- Revision History
--		Name:					Date:			Comments:
--		Brian Byas			2016-03-16		Added WITH (NOLOCK) on all DB references
**********************************************************************************************/
CREATE VIEW [dbo].[vwInverse_Static_Exchange_Rate]
AS

SELECT [TO_CURR_CODE] AS FR_CURR_CODE
	  ,[FR_CURR_CODE] AS TO_CURR_CODE
	  ,[TO_CURR_KEY] AS FR_CURR_KEY
	  ,[FR_CURR_KEY] AS TO_CURR_KEY
	  , CASE WHEN [RATE] = 0 THEN 0
			ELSE 1.0 / [RATE] END AS [RATE]
FROM [DWStaging].[dbo].[Corp_Static_Exchange_Rate_Control]  WITH (NOLOCK)
			
UNION 

SELECT [FR_CURR_CODE]
      ,[TO_CURR_CODE]
      ,[FR_CURR_KEY]
      ,[TO_CURR_KEY]
      ,[RATE]
  FROM [DWStaging].[dbo].[Corp_Static_Exchange_Rate_Control] WITH (NOLOCK)
```

