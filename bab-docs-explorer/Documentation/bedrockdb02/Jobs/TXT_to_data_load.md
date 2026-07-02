# Job: TXT to data load

**Enabled:** No  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["TXT to data load"]
    JOB --> TXT_Dataload_Config_1["Step 1: TXT Dataload Config [TSQL]"]`n```

## Steps

### Step 1: TXT Dataload Config
**Subsystem:** TSQL  

```sql
DECLARE @StartFiscalYear INT
	, @StartFiscalWeek INT
	, @EndFiscalYear INT
	, @EndFiscalWeek INT
	, @MaxConcurrentProcess INT
	, @StartWeekName INT
	, @EndWeekName INT
	, @ServerName VARCHAR(40)

SELECT @EndWeekName = WEEK_NAME FROM bedrockdb02.[ma_01].[MerchandisingPlanning].[vwTXT_CalculatedTime]
WHERE WEEK_DATE = (SELECT CONVERT(DATE,DATEADD(wk, DATEDIFF(wk,6,GETDATE()), 6)-7)) --Get Previous Sunday
	SELECT WEEK_NUMBER FROM bedrockdb02.[ma_01].[MerchandisingPlanning].[vwTXT_CalculatedTime]
	WHERE WEEK_NAME = @EndWeekName


SELECT @StartWeekName = WEEK_NAME FROM bedrockdb02.[ma_01].[MerchandisingPlanning].[vwTXT_CalculatedTime]
WHERE WEEK_DATE = (SELECT CONVERT(DATE,DATEADD(wk, DATEDIFF(wk,6,GETDATE()), 6)-35)) --Get -5 Prog
	SELECT WEEK_NUMBER FROM bedrockdb02.[ma_01].[MerchandisingPlanning].[vwTXT_CalculatedTime]
	WHERE WEEK_NAME = @StartWeekName

----------------------------------------------------------------
-- PROD
----------------------------------------------------------------
SET @StartFiscalYear = LEFT(@StartWeekName,4)
SET @StartFiscalWeek = RIGHT(@StartWeekName,2)
--SET @StartFiscalWeek  = '34' --Temp added on 11/18/20 to include 04SEP2020
SET @EndFiscalYear = LEFT(@EndWeekName,4)
SET @EndFiscalWeek = RIGHT(@EndWeekName,2)
SET @MaxConcurrentProcess = 12
SET @ServerName = 'TXTDB01'
----------------------------------------------------------------
-- TEST
----------------------------------------------------------------
--SET @StartFiscalYear = 2023
--SET @StartFiscalWeek = 16
--SET @EndFiscalYear = 2023
--SET @EndFiscalWeek = 21
--SET @MaxConcurrentProcess = 12
--SET @ServerName = 'TXTTESTDB01'

--EXEC [PAPAMART].DWStaging.MerchandisingPlanning.spTXTDataLoad_Coordinator @StartFiscalYear,@StartFiscalWeek,@EndFiscalYear,@EndFiscalWeek,@MaxConcurrentProcess,@ServerName

EXEC TXTStaging.MerchandisingPlanning.spTXTDataLoad_Coordinator @StartFiscalYear,@StartFiscalWeek,@EndFiscalYear,@EndFiscalWeek,@MaxConcurrentProcess,@ServerName
```


