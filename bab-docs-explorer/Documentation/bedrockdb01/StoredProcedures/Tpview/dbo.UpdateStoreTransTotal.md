# dbo.UpdateStoreTransTotal

**Database:** Tpview  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.UpdateStoreTransTotal"]
    Alarm8(["Alarm8"]) --> SP
    tblTransacLocStat(["tblTransacLocStat"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| Alarm8 |
| tblTransacLocStat |

## Stored Procedure Code

```sql
create proc UpdateStoreTransTotal -- updating Transaction Store and Store Totals.
	@storenumber 	INT,  
	@response		DECIMAL,
	@servicetype	VARCHAR(2)
AS
DECLARE @HourlyTotal 		int
DECLARE @DailyTotal 		int
DECLARE @WeeklyTotal		int
DECLARE @HourlyRespTotal  	DECIMAL(10,3)
DECLARE @DailyRespTotal 	DECIMAL(10,3)
DECLARE @WeeklyRespTotal 	DECIMAL(10,3)
--getting hourly total for store
IF(NOT EXISTS(SELECT TransacStatLocID FROM tblTransacLocStat WHERE RemoteNumber = @storenumber AND Service = @servicetype))
BEGIN
	INSERT INTO tblTransacLocStat(	RemoteNumber,
									MsgType,
									Service,
									Card,
									HourlyNbrTransac,
									DailyNbrTransac,
									WeeklyNbrTransac,
									HourlyRespAvg,
									DailyRespAvg,
									WeeklyRespAvg,
									LastEventTime)
	VALUES(	@storenumber,0,@servicetype,0,0,0,0,0,0,0,GETDATE())
END
SELECT 	@HourlyTotal = HourlyNbrTransac,
		@DailyTotal = DailyNbrTransac,
		@WeeklyTotal = WeeklyNbrTransac,
		@HourlyRespTotal = HourlyRespAvg ,
		@DailyRespTotal = DailyRespAvg ,
		@WeeklyRespTotal = WeeklyRespAvg 	  
FROM tblTransacLocStat 
WHERE 	RemoteNumber = @storenumber AND Service = @servicetype
--hourly calc for store totals
	IF((SELECT DATEPART(hh,LastEventTime) FROM tblTransacLocStat 	
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype)) = DATEPART(hh,GETDATE())
		BEGIN
			PRINT 'UPDATE'
			Update tblTransacLocStat 
			SET HourlyNbrTransac = (@HourlyTotal+1),
				HourlyRespAvg = ((@HourlyRespTotal*@HourlyTotal)+@response) / (@HourlyTotal+1),
				LastEventTime = GETDATE()
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype
		END
	IF((SELECT DATEPART(hh,LastEventTime) FROM tblTransacLocStat 	
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype)) <> DATEPART(hh,GETDATE())
	--Check for hourly alarms only for a certain service
	BEGIN
		EXEC Alarm8 @storenumber,@servicetype,1
			PRINT 'NEW'
			Update tblTransacLocStat 
			SET HourlyNbrTransac = (1),
				HourlyRespAvg = @response,
				LastEventTime = GETDATE()
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype
	END
--daily calc fot store totals
							
	IF((SELECT DATEPART(dd,LastEventTime) FROM tblTransacLocStat 	
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype) = DATEPART(dd,GETDATE()))
		BEGIN
			Update tblTransacLocStat 
			SET DailyNbrTransac = (@DailyTotal+1),
				DailyRespAvg = ((@DailyRespTotal*@DailyTotal)+@response) / (@DailyTotal+1),
				LastEventTime = GETDATE()
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype
		END
	ELSE
		BEGIN
			-- 2 means check for daily alarms for this service.
			EXEC Alarm8 @storenumber,@servicetype,2
			Update tblTransacLocStat 
			SET DailyNbrTransac = (1),
				DailyRespAvg = (@response /(1)),
				LastEventTime = GETDATE()
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype
		END
--weekly totals
	
	IF((SELECT DATEPART(dd,LastEventTime) FROM tblTransacLocStat 	
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype) = DATEPART(dd,GETDATE()))
		BEGIN
			Update tblTransacLocStat 
			SET WeeklyNbrTransac = (@WeeklyTotal+1),
				WeeklyRespAvg = (((@WeeklyRespTotal*@WeeklyTotal)+@response) / (@WeeklyTotal+1)),
				LastEventTime = GETDATE()
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype
		END
	ELSE
		BEGIN
			-- 3 means check for weekly alarms for this service
			EXEC Alarm8 @storenumber,@servicetype,3
			Update tblTransacLocStat 
			SET WeeklyNbrTransac = (1),
				WeeklyRespAvg = (@response),
				LastEventTime = GETDATE()
			WHERE 	RemoteNumber = @storenumber 
					AND Service = @servicetype
		END
```

