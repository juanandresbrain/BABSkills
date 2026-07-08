# dbo.UpdateConnectionTotal

**Database:** Tpview  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateConnectionTotal"]
    tblConnectionStat(["tblConnectionStat"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| tblConnectionStat |

## Stored Procedure Code

```sql
create proc UpdateConnectionTotal -- updating connections for a certain store.
   	@storenumber int,
	@register	 int,
	@connecttype int	  
AS
DECLARE @hourlytotal INT
DECLARE @dailytotal INT
DECLARE @weeklytotal INT
--Check if the record exists.
IF(NOT EXISTS(SELECT ConnectionStatID FROM tblConnectionStat WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register))
BEGIN
	INSERT INTO tblConnectionStat (RemoteNumber,
									ConnectType,
									LastConnectTime,
									HourlyNbrConnect,
									DailyNbrConnect,
									WeeklyNbrConnect,
									LastDisconnectTime,
									HourlyNbrDisconnect,
									DailyNbrDisconnect,
									WeeklyNbrDisconnect,
									LastDurationTime,
									HourlyDuration,
									DailyDuration,
									WeeklyDuration,
									RegisterNumber)
	VALUES (@storenumber,@connecttype,GETDATE(),0,0,0,GETDATE(),0,0,0,GETDATE(),0,0,0,@register)
END
							
--Getting the current hourlytotal.
SELECT @hourlytotal = HourlyNbrConnect 
FROM tblConnectionStat 
WHERE RemoteNumber = @storenumber AND RegisterNumber = @register
--Getting the current dailytotal.
SELECT @dailytotal = DailyNbrConnect 
FROM tblConnectionStat 
WHERE RemoteNumber = @storenumber AND RegisterNumber = @register
--Getting the current weeklytotal
SELECT @weeklytotal = WeeklyNbrConnect 
FROM tblConnectionStat 
WHERE RemoteNumber = @storenumber AND RegisterNumber = @register
--performing the update.
--hourly total
IF(SELECT DATEPART(hh,LastConnectTime) FROM tblConnectionStat WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register) = DATEPART(hh,GETDATE())
	BEGIN
		UPDATE tblConnectionStat 
		SET HourlyNbrConnect = (@hourlytotal + 1)  
		WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
	END
ELSE	
	BEGIN
		UPDATE tblConnectionStat 
		SET HourlyNbrConnect = 1 
		WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
	END
--daily total
IF(SELECT DATEPART(dd,LastConnectTime) FROM tblConnectionStat WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register) = DATEPART(dd,GETDATE())
	BEGIN
		UPDATE tblConnectionStat 
		SET DailyNbrConnect = (@dailytotal + 1) 
		WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
	END
ELSE	
	BEGIN
		UPDATE tblConnectionStat 
		SET DailyNbrConnect = 1 
		WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
	END
--weekly total
IF(SELECT DATEPART(wk,LastConnectTime) FROM tblConnectionStat WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register) = DATEPART(wk,GETDATE())
	BEGIN
		UPDATE tblConnectionStat 
		SET WeeklyNbrConnect = (@weeklytotal + 1) 
		WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
	END
ELSE	
	BEGIN
		UPDATE tblConnectionStat 
		SET WeeklyNbrConnect = 1 
		WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
	END
--Update LastConnectTime Event
UPDATE tblConnectionStat 
SET  LastConnectTime = GETDATE() 
WHERE RemoteNumber = @storenumber AND ConnectType = @connecttype AND RegisterNumber = @register
```

