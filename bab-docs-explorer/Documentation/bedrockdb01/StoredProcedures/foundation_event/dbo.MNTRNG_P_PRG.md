# dbo.MNTRNG_P_PRG

**Database:** foundation_event  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.MNTRNG_P_PRG"]
    ALRM_DFNTN(["ALRM_DFNTN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ALRM_DFNTN |

## Stored Procedure Code

```sql
/**************************************************************** 
 Name           : MNTRNG_P_PRG 
 Purpose        : Purge the event, the statistic and the history tables                  
 Parameters     : @BatchSize: number of record purged at a time
                  @EventTypeID: Event Type ID 
                  @Level: 0-Event, 1-Continuous, 2-Hour, 3-Day, 4-Week, 5-Month, 6-Year
                  @Keep: Keep the current year + NUM_STSTC_KEEP_YEAR
                         Keep the current month + NUM_STSTC_KEEP_MNTH
                         Keep the current week + NUM_STSTC_KEEP_WEEK
                         Keep the current day + NUM_STSTC_KEEP_DAY
                         Keep the current hour + NUM_STSTC_KEEP_HOUR
                         Keep the current day = all the continous that have not been modified since CONT_INCTVTY_DLY days
                         Keep all events created since NUM_DAYS_KEEP_EVENT days                  
 Returns        : > 0 - successful (number of records deleted), < 0 - unsuccessful 
 Created by     : Philippe Lanthier 
 Creation Date  : Dec-15-2004
****************************************************************/ 
CREATE PROCEDURE [dbo].[MNTRNG_P_PRG]
@BatchSize int,
@EventTypeID int,
@Level int,
@Keep int

AS

DECLARE  @SQL nvarchar(200),	      --Query to run
	      @ERROR int,		            --Error code
	      @ROWS int,		            --Number of deleted rows per batch
	      @DELETEDROWS int,	         --Total number of deleted rows
	      @EVNT_ID int,	            --Last processed event id
         @DELETE_DTM datetime,      --Datetime to use to delete
         @CURRENT_DATE datetime,    --Current date time
         @CURRENT_UTC_DATE datetime,--Current UTC date time
         @LAST_ALRM_DTM datetime, --Last time the alarm was ran
         @mmUTC int,                --Current UTC month
         @ddUTC int,                --Current UTC day
         @miUTC int,                --Current UTC minute
         @msUTC int,                --Current UTC millisecond
         @ssUTC int,                --Current UTC second
         @dwUTC int                 --Current UTC day of week

IF @BatchSize < 1 
   SET @BatchSize = 1

SELECT @CURRENT_DATE = getdate()
SELECT @CURRENT_UTC_DATE = getutcdate()

SELECT @mmUTC = -DATEPART(mm, @CURRENT_UTC_DATE), @ddUTC = -DATEPART(dd, @CURRENT_UTC_DATE), @miUTC = -DATEPART(mi, @CURRENT_UTC_DATE),
       @msUTC = -DATEPART(ms, @CURRENT_UTC_DATE), @ssUTC = -DATEPART(ss, @CURRENT_UTC_DATE), @dwUTC = -DATEPART(dw, @CURRENT_UTC_DATE)

--Get the last processed event 
SELECT @EVNT_ID = MIN(LAST_EVNT_ID)
  FROM ALRM_DFNTN
 WHERE EVNT_TYPE_ID = @EventTypeID AND ENBLD = 1 AND TEST_BCKT_LVL = 0

IF @@ERROR <> 0
	RETURN -1

--Get the last processed alarm datetime
SELECT @LAST_ALRM_DTM = MIN(LAST_ALRM_DTM)
  FROM ALRM_DFNTN
 WHERE EVNT_TYPE_ID = @EventTypeID AND ENBLD = 1 AND TEST_BCKT_LVL > 0

IF @@ERROR <> 0
	RETURN -2

IF @LAST_ALRM_DTM IS NULL
   SET @LAST_ALRM_DTM = @CURRENT_DATE

--Event 
IF @Level = 0 
   SELECT @DELETE_DTM = DATEADD(ss, 86399, DATEADD(dd, -@Keep - 1, convert(varchar, @CURRENT_DATE, 102)))

--Continous
IF @Level = 1
   SELECT @DELETE_DTM = DATEADD(dd, -@Keep - 1, convert(varchar, @CURRENT_DATE, 102))

--Hour
IF @Level = 2
   SELECT @DELETE_DTM =  DATEADD(ss, -1, DATEADD(hh, -@Keep, DATEADD(mi, @miUTC, DATEADD(ss, @ssUTC, DATEADD(ms, @msUTC, @CURRENT_UTC_DATE)))))

--Day
IF @Level = 3
   SELECT @DELETE_DTM = DATEADD(ss, 86399, DATEADD(dd, -@Keep - 1, convert(varchar, @CURRENT_UTC_DATE, 102)))

--Week
IF @Level = 4
   SELECT @DELETE_DTM =  DATEADD(ss, 86399, DATEADD(dd, -(@Keep * 7), DATEADD(dw, @dwUTC, convert(varchar, @CURRENT_UTC_DATE, 102))))

--Month
IF @Level = 5
   SELECT @DELETE_DTM =  DATEADD(ss, -1, DATEADD(mm, -@Keep, DATEADD(dd, @ddUTC + 1, convert(varchar, @CURRENT_UTC_DATE,102))))

--Year
IF @Level = 6
   SELECT @DELETE_DTM =  DATEADD(ss, -1, DATEADD(yy, -@Keep, DATEADD(dd, @ddUTC + 1, DATEADD(mm, @mmUTC + 1, convert(varchar, @CURRENT_UTC_DATE, 102)))))

SET ROWCOUNT @BatchSize

SELECT @ROWS = @BatchSize, @DELETEDROWS = 0

WHILE @ROWS = @BatchSize
BEGIN

   BEGIN TRAN
   
   --Event
   IF @Level = 0
   BEGIN
      IF @EVNT_ID IS NULL
         SELECT @SQL = 'DELETE FROM EVNT_' + ltrim(str(@EventTypeID)) + ' WHERE EVNT_CRTN_DTM <= ''' + convert(varchar, @DELETE_DTM) + ''''
      ELSE
         SELECT @SQL = 'DELETE FROM EVNT_' + ltrim(str(@EventTypeID)) + ' WHERE EVNT_ID <= ' + ltrim(str(@EVNT_ID)) + ' AND EVNT_CRTN_DTM <= ''' + convert(varchar, @DELETE_DTM) + ''''
      END 

   --Continuous
   IF @Level = 1
      SELECT @SQL = 'DELETE FROM EVNT_STSTC_HSTRY_' + ltrim(str(@EventTypeID)) + ' WHERE LAST_MDFD_DTM <= ''' + convert(varchar, @DELETE_DTM) + '''  AND LAST_MDFD_DTM <= ''' + convert(varchar, @LAST_ALRM_DTM) + '''' + ' AND POST_YEAR = 0 AND POST_MNTH = 0 AND POST_WEEK = 0 AND POST_DAY = 0'

   --Statistics (hour)
   IF @Level = 2
      SELECT @SQL = 'DELETE FROM EVNT_STSTC_' + ltrim(str(@EventTypeID)) + ' WHERE POST_DTM <= ''' + convert(varchar, convert(datetime, @DELETE_DTM, 113)) + ''' AND POST_DTM <= ''' + convert(varchar, convert(datetime, @LAST_ALRM_DTM, 113)) + ''''

   --History (day)
   IF @Level = 3
      SELECT @SQL = 'DELETE FROM EVNT_STSTC_HSTRY_' + ltrim(str(@EventTypeID)) + ' WHERE POST_DTM <= ''' + convert(varchar, @DELETE_DTM) + ''' AND POST_DTM <= ''' + convert(varchar, @LAST_ALRM_DTM) + '''' + ' AND POST_YEAR <> 0 AND POST_MNTH <> 0 AND POST_WEEK = 0 AND POST_DAY <> 0'

   --History (week)
   IF @Level = 4
      SELECT @SQL = 'DELETE FROM EVNT_STSTC_HSTRY_' + ltrim(str(@EventTypeID)) + ' WHERE POST_DTM <= ''' + convert(varchar, @DELETE_DTM) + ''' AND POST_DTM <= ''' + convert(varchar, @LAST_ALRM_DTM) + '''' + ' AND POST_YEAR <> 0 AND POST_MNTH = 0 AND POST_WEEK <> 0 AND POST_DAY = 0'

   --History (month)
   IF @Level = 5
      SELECT @SQL = 'DELETE FROM EVNT_STSTC_HSTRY_' + ltrim(str(@EventTypeID)) + ' WHERE POST_DTM <= ''' + convert(varchar, @DELETE_DTM) + ''' AND POST_DTM <= ''' + convert(varchar, @LAST_ALRM_DTM) + '''' + ' AND POST_YEAR <> 0 AND POST_MNTH <> 0 AND POST_WEEK = 0 AND POST_DAY = 0'

   --History (year)
   IF @Level = 6
      SELECT @SQL = 'DELETE FROM EVNT_STSTC_HSTRY_' + ltrim(str(@EventTypeID)) + ' WHERE POST_DTM <= ''' + convert(varchar, @DELETE_DTM) + ''' AND POST_DTM <= ''' + convert(varchar, @LAST_ALRM_DTM) + '''' + ' AND POST_YEAR <> 0 AND POST_MNTH = 0 AND POST_WEEK = 0 AND POST_DAY = 0'

   EXECUTE sp_executesql @SQL
   
   SELECT @ROWS = @@ROWCOUNT, @ERROR = @@ERROR

   IF @ERROR <> 0
      BREAK

   SELECT @DELETEDROWS = @DELETEDROWS + @ROWS
   COMMIT TRAN

END

SET ROWCOUNT 0

IF @ERROR <> 0
BEGIN
   ROLLBACK TRAN
	RETURN -3
END
ELSE
   RETURN @DELETEDROWS
```

