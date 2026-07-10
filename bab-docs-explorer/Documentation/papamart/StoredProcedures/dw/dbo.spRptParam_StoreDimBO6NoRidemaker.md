# dbo.spRptParam_StoreDimBO6NoRidemaker

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRptParam_StoreDimBO6NoRidemaker"]
    dbo_vwStore_dimBO6(["dbo.vwStore_dimBO6"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwStore_dimBO6 |

## Stored Procedure Code

```sql
CREATE PROCEDURE dbo.spRptParam_StoreDimBO6NoRidemaker

AS
SET NOCOUNT ON;
BEGIN

	SELECT DISTINCT vsdbo.division
	FROM dbo.vwStore_dimBO6 vsdbo
	WHERE vsdbo.division NOT IN ('US Ridemakerz', '')

END
```

