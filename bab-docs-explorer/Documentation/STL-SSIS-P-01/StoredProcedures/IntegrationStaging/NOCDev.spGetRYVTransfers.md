# NOCDev.spGetRYVTransfers

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["NOCDev.spGetRYVTransfers"]
    dbo_Orders(["dbo.Orders"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Orders |

## Stored Procedure Code

```sql
CREATE proc [NOCDev].[spGetRYVTransfers]

as

-------------------------------------------------------------------------					
-- 2021-11-10 - Brandon Hickey - Created Proc
-------------------------------------------------------------------------

set nocount on

SELECT CAST(format(CAST(DATEPART(HOUR, AudioTransferDate)AS INT), '00')AS VARCHAR(2)) + ':00' AS AudioTransferHour, 
                COUNT(*) AS AudioTransferCountByHour 
                FROM [KODIAK].[RecordYourVoice].[dbo].[Orders] 
                WHERE AudioTransferDate IS NOT NULL 
				AND AudioTransferDate > DATEADD(HOUR, -11, GETDATE())
                GROUP BY DATEPART(HOUR, AudioTransferDate)
				ORDER BY MIN(AudioTransferDate);
```

