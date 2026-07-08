# dbo.MNTRNG_P_HSTRY

**Database:** COMM_EVENT  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.MNTRNG_P_HSTRY"]
    EVNT_STSTC_HSTRY_X(["EVNT_STSTC_HSTRY_X"]) --> SP
    EVNT_TYPE(["EVNT_TYPE"]) --> SP
    EVNT_X(["EVNT_X"]) --> SP
    dbo_GET_MAX(["dbo.GET_MAX"]) --> SP
    dbo_GET_MIN(["dbo.GET_MIN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| EVNT_STSTC_HSTRY_X |
| EVNT_TYPE |
| EVNT_X |
| dbo.GET_MAX |
| dbo.GET_MIN |

## Stored Procedure Code

```sql
/**************************************************************** 
 Name           : MNTRNG_P_HSTRY 
 Purpose        : Create Day, Week, Month, Year and Continuous statistics for this event type
 Parameters     : Batch size
 Returns        : > 0 - successful (number of events processed), -1 to -24 - unsuccessful 
 Created by     : Philippe Lanthier 
 Creation Date  : Dec-14-2004
****************************************************************/ 
CREATE PROCEDURE [dbo].[MNTRNG_P_HSTRY] 
@BATCH_SIZE as int			--Max number of records in a batch
AS
--Create temporary event table to keep a copy of the batch
CREATE TABLE dbo.#TMP_COPY_EVNT_X
(
	POST_YEAR smallint NOT NULL,
	POST_MNTH tinyint NOT NULL,
	POST_WEEK tinyint NOT NULL,
	POST_DAY tinyint NOT NULL,
	POST_DTM smalldatetime NOT NULL,
	FLD_1 int NOT NULL,
	FLD_2 int NOT NULL,
	FLD_3 int NOT NULL,
	FLD_4 int NOT NULL
) ON [PRIMARY]
--Create temporary event table
CREATE TABLE dbo.#TMP_EVNT_X
(
	POST_YEAR smallint NOT NULL,
	POST_MNTH tinyint NOT NULL,
	POST_WEEK tinyint NOT NULL,
	POST_DAY tinyint NOT NULL,
	POST_DTM smalldatetime NOT NULL,
	FLD_1 int NOT NULL,
	FLD_2 int NOT NULL,
	FLD_3 int NOT NULL,
	FLD_4 int NOT NULL
) ON [PRIMARY]
 
--Variables
DECLARE @MAX_EVNT_ID as int,		   --Last event id processed during this cycle
        @STRT_EVNT_ID as int,		   --First event of batch
		@END_EVNT_ID as int,		   --Last event of batch
		@LAST_HSTRY_EVNT_ID as int,	   --Last event id processed in the previous cycle
		@EVNT_TYPE_ID as int, 		   --Constant for Event Type ID
 	    @ERROR as int,				   --Error return code
        @ROWS as int,                  --Total number of events processed
        @ROWCOUNT as int,              --Number of events processed in a batch
        @DAY_LVL as int,		       --Day level
        @MNTH_LVL as int,		       --Month level
        @WEEK_LVL as int,		       --Week level
        @YEAR_LVL as int,		       --Year level
        @STSTC_LVL as int              --Statistics level
SELECT @EVNT_TYPE_ID = 1 --TO BE CHANGED
SELECT @ERROR = 0 , @ROWS = 0, @END_EVNT_ID = 0
--Get last event id processed during this cycle
SELECT @MAX_EVNT_ID = MAX(ISNULL(EVNT_ID,0))
  FROM EVNT_X
SELECT @DAY_LVL = NUM_STSTC_KEEP_DAY,
       @MNTH_LVL = NUM_STSTC_KEEP_MNTH,
       @WEEK_LVL = NUM_STSTC_KEEP_WEEK,
       @YEAR_LVL = NUM_STSTC_KEEP_YEAR,
       @STSTC_LVL = STSTC_LVL
  FROM EVNT_TYPE
 WHERE EVNT_TYPE_ID = @EVNT_TYPE_ID
IF (@@ERROR <> 0)
BEGIN
   SELECT @ERROR = -1
	RETURN @ERROR
END
--Loop to process all events by doing it in smaller batch
WHILE @END_EVNT_ID < @MAX_EVNT_ID
BEGIN
	BEGIN TRAN
	--Get last event id processed in the previous cycle and the statistics levels
	SELECT @LAST_HSTRY_EVNT_ID = ISNULL(LAST_HSTRY_EVNT_ID,0)
	  FROM EVNT_TYPE
	 WHERE EVNT_TYPE_ID = @EVNT_TYPE_ID
	
	IF (@@ERROR <> 0)
	BEGIN
		ROLLBACK TRAN
		SELECT @ERROR = -2
		BREAK
	END
	--Set the batch range
	SELECT @STRT_EVNT_ID = @LAST_HSTRY_EVNT_ID + 1, 
	       @END_EVNT_ID = @LAST_HSTRY_EVNT_ID + @BATCH_SIZE
	
	--Make sure to stay within the range of events to process
	IF @END_EVNT_ID > @MAX_EVNT_ID
		SELECT @END_EVNT_ID = @MAX_EVNT_ID
   
   IF @STRT_EVNT_ID > @END_EVNT_ID
   BEGIN
      COMMIT TRAN
      SELECT @ERROR = @ROWS 
      BREAK
   END
   --Populate the temporary event table using only the new events
   INSERT INTO #TMP_COPY_EVNT_X (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, POST_DTM, FLD_1, FLD_2, FLD_3,FLD_4)
   SELECT 	
         DATEPART(yy,EVNT_POST_DTM),
      	DATEPART(mm,EVNT_POST_DTM),
      	DATEPART(ww,EVNT_POST_DTM),
      	DATEPART(dd,EVNT_POST_DTM),	
      	DATEADD(ms, -DATEPART(ms, EVNT_POST_DTM), DATEADD(ss, -DATEPART(ss, EVNT_POST_DTM), DATEADD(mi, -DATEPART(mi, EVNT_POST_DTM), DATEADD(hh, -DATEPART(hh, EVNT_POST_DTM), EVNT_POST_DTM)))),
      	FLD_1,
      	FLD_2,
      	FLD_3,
      	FLD_4
    FROM EVNT_X
	WHERE EVNT_ID >= @STRT_EVNT_ID 
	  AND EVNT_ID <= @END_EVNT_ID
   --Get the number of rows processed
   SELECT @ROWCOUNT = @@ROWCOUNT, @ERROR = @@ERROR
	IF (@ERROR <> 0)
	BEGIN
		ROLLBACK TRAN
		SELECT @ERROR = -3
		BREAK
	END
   --Add the processed rows
   SELECT @ROWS = @ROWS + @ROWCOUNT
   --Day bucket
   IF (@DAY_LVL > 0)
   BEGIN
   
   	--Populate the temporary event table from the copy
   	INSERT INTO #TMP_EVNT_X 
   	SELECT POST_YEAR,
         	 POST_MNTH,
         	 POST_WEEK,
         	 POST_DAY,
         	 POST_DTM,
   		    FLD_1,
       		 FLD_2,
   		    FLD_3,
   		    FLD_4
   	 FROM #TMP_COPY_EVNT_X 
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -4
   		BREAK
   	END   
   	--Update statistics for existing buckets of the temporary statistic table
   	UPDATE EVNT_STSTC_HSTRY_X SET 
   		    EVNT_STSTC_HSTRY_X.LAST_MDFD_DTM = getdate(),
   		    EVNT_STSTC_HSTRY_X.FLD_4_SUM = s.FLD_4_SUM + te.FLD_4,
   		    EVNT_STSTC_HSTRY_X.FLD_4_MIN = dbo.GET_MIN(s.FLD_4_MIN, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_MAX = dbo.GET_MAX(s.FLD_4_MAX, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_LAST = te.FLD_4
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = te.POST_MNTH
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = te.POST_DAY 
        AND s.KEY_1 = te.FLD_1
        AND s.KEY_2 = te.FLD_2
        AND s.KEY_3 = te.FLD_3
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -5
   		BREAK
   	END
   
  		--Delete temporary events already used to update statistics
   	DELETE #TMP_EVNT_X
     	  FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = te.POST_MNTH
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = te.POST_DAY 
        AND s.KEY_1 = te.FLD_1
        AND s.KEY_2 = te.FLD_2
        AND s.KEY_3 = te.FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -6
   		BREAK
   	END
   	--Insert statistics using the remaining temporary events
   	INSERT EVNT_STSTC_HSTRY_X (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, KEY_1, KEY_2, KEY_3, POST_DTM, CNT, FLD_4_SUM, FLD_4_MIN, FLD_4_MAX, FLD_4_FRST, FLD_4_LAST)
   	SELECT POST_YEAR, POST_MNTH, 0, POST_DAY, FLD_1, FLD_2, FLD_3, MIN(POST_DTM), COUNT(*), SUM(FLD_4), MIN(FLD_4), MAX(FLD_4), MIN(FLD_4), MAX(FLD_4)
    	  FROM #TMP_EVNT_X
    	 GROUP BY POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, FLD_1, FLD_2, FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -7
   		BREAK
   	END
   	
      TRUNCATE TABLE #TMP_EVNT_X
   END
   --Week bucket
   IF (@WEEK_LVL > 0)
   BEGIN
   	--Populate the temporary event table from the copy
   	INSERT INTO #TMP_EVNT_X 
   	SELECT POST_YEAR,
           POST_MNTH,
           POST_WEEK,
           POST_DAY,
           POST_DTM,
   		   FLD_1,
       	   FLD_2,
   		   FLD_3,
   		   FLD_4
   	 FROM #TMP_COPY_EVNT_X 
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -8
   		BREAK
   	END
   	--Update statistics for existing buckets of the temporary statistic table
   	UPDATE EVNT_STSTC_HSTRY_X SET 
   		    EVNT_STSTC_HSTRY_X.LAST_MDFD_DTM = getdate(),
   		    EVNT_STSTC_HSTRY_X.FLD_4_SUM = s.FLD_4_SUM + te.FLD_4,
   		    EVNT_STSTC_HSTRY_X.FLD_4_MIN = dbo.GET_MIN(s.FLD_4_MIN, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_MAX = dbo.GET_MAX(s.FLD_4_MAX, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_LAST = te.FLD_4
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = 0
   	  AND s.POST_WEEK = te.POST_WEEK
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -9
   		BREAK
   	END
   
   	DELETE #TMP_EVNT_X
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = 0
   	  AND s.POST_WEEK = te.POST_WEEK
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -10
   		BREAK
   	END
   	--Insert statistics using the remaining temporary events
   	INSERT EVNT_STSTC_HSTRY_X (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, KEY_1, KEY_2, KEY_3, POST_DTM, CNT, FLD_4_SUM, FLD_4_MIN, FLD_4_MAX, FLD_4_FRST, FLD_4_LAST)
   	SELECT POST_YEAR, 0, POST_WEEK, 0, FLD_1, FLD_2, FLD_3, MIN(DATEADD(mm, -DATEPART(mm, POST_DTM)+1, DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM))), COUNT(*), SUM(FLD_4), MIN(FLD_4), MAX(FLD_4), MIN(FLD_4), MAX(FLD_4)
   	  FROM #TMP_EVNT_X
   	 GROUP BY POST_YEAR, POST_WEEK, FLD_1, FLD_2, FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -11
   		BREAK
   	END
   	
      TRUNCATE TABLE #TMP_EVNT_X
   END
   --Month bucket
   IF (@MNTH_LVL > 0)
   BEGIN
   
   	--Populate the temporary event table from the copy
   	INSERT INTO #TMP_EVNT_X 
   	SELECT POST_YEAR,
           POST_MNTH,
           POST_WEEK,
           POST_DAY,
           POST_DTM,
   	 	   FLD_1,
       	   FLD_2,
   		   FLD_3,
   		   FLD_4
   	 FROM #TMP_COPY_EVNT_X 
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -12
   		BREAK
   	END
   	--Update statistics for existing buckets of the temporary statistic table
   	UPDATE EVNT_STSTC_HSTRY_X SET 
   		    EVNT_STSTC_HSTRY_X.LAST_MDFD_DTM = getdate(),
   		    EVNT_STSTC_HSTRY_X.FLD_4_SUM = s.FLD_4_SUM + te.FLD_4,
   		    EVNT_STSTC_HSTRY_X.FLD_4_MIN = dbo.GET_MIN(s.FLD_4_MIN, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_MAX = dbo.GET_MAX(s.FLD_4_MAX, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_LAST = te.FLD_4
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = te.POST_MNTH
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -13
   		BREAK
   	END
   
   	--Delete temporary events already used to update statistics
   	DELETE #TMP_EVNT_X
      FROM #TMP_EVNT_X b, EVNT_STSTC_HSTRY_X s
   		 WHERE s.POST_YEAR = b.POST_YEAR
   		   AND s.POST_MNTH = b.POST_MNTH
   		   AND s.POST_WEEK = 0
   		   AND s.POST_DAY  = 0
   		   AND s.KEY_1 = b.FLD_1
   		   AND s.KEY_2 = b.FLD_2
   		   AND s.KEY_3 = b.FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -14
   		BREAK
   	END
   	--Insert statistics using the remaining temporary events
   	INSERT EVNT_STSTC_HSTRY_X (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, KEY_1, KEY_2, KEY_3, POST_DTM, CNT, FLD_4_SUM, FLD_4_MIN, FLD_4_MAX, FLD_4_FRST, FLD_4_LAST)
   	SELECT POST_YEAR, POST_MNTH, 0, 0, FLD_1, FLD_2, FLD_3, MIN(DATEADD(mm, -DATEPART(mm, POST_DTM)+1, DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM))), COUNT(*), SUM(FLD_4), MIN(FLD_4), MAX(FLD_4), MIN(FLD_4), MAX(FLD_4)
        FROM #TMP_EVNT_X
   	 GROUP BY POST_YEAR, POST_MNTH, FLD_1, FLD_2, FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -15
   		BREAK
   	END
   	
      TRUNCATE TABLE #TMP_EVNT_X
   END
   --Year bucket
   IF (@YEAR_LVL > 0)
   BEGIN
   
   	--Populate the temporary event table from the copy
   	INSERT INTO #TMP_EVNT_X 
   	SELECT POST_YEAR,
           POST_MNTH,
           POST_WEEK,
           POST_DAY,
           POST_DTM,
   		   FLD_1,
       	   FLD_2,
   		   FLD_3,
   		   FLD_4
   	 FROM #TMP_COPY_EVNT_X 
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -16
   		BREAK
   	END
   	--Update statistics for existing buckets of the temporary statistic table
   	UPDATE EVNT_STSTC_HSTRY_X SET 
   		    EVNT_STSTC_HSTRY_X.LAST_MDFD_DTM = getdate(),
   		    EVNT_STSTC_HSTRY_X.FLD_4_SUM = s.FLD_4_SUM + te.FLD_4,
   		    EVNT_STSTC_HSTRY_X.FLD_4_MIN = dbo.GET_MIN(s.FLD_4_MIN, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_MAX = dbo.GET_MAX(s.FLD_4_MAX, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_LAST = te.FLD_4
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = 0
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -17
   		BREAK
   	END
   
   	--Delete temporary events already used to update statistics
   	DELETE #TMP_EVNT_X
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = te.POST_YEAR
   	  AND s.POST_MNTH = 0
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -18
   		BREAK
   	END
   	--Insert statistics using the remaining temporary events
   	INSERT EVNT_STSTC_HSTRY_X (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, KEY_1, KEY_2, KEY_3, POST_DTM, CNT, FLD_4_SUM, FLD_4_MIN, FLD_4_MAX, FLD_4_FRST, FLD_4_LAST)
   	SELECT POST_YEAR, 0, 0, 0, FLD_1, FLD_2, FLD_3, MIN(DATEADD(mm, -DATEPART(mm, POST_DTM)+1, DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM))), COUNT(*), SUM(FLD_4), MIN(FLD_4), MAX(FLD_4), MIN(FLD_4), MAX(FLD_4)
   	  FROM #TMP_EVNT_X
   	 GROUP BY POST_YEAR, FLD_1, FLD_2, FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -19
   		BREAK
   	END
   	
      TRUNCATE TABLE #TMP_EVNT_X
   END
   --Continuous bucket
   IF (@STSTC_LVL <> 0)
   BEGIN 
 
   	--Populate the temporary event table from the copy
   	INSERT INTO #TMP_EVNT_X 
   	SELECT POST_YEAR,
           POST_MNTH,
           POST_WEEK,
           POST_DAY,
           POST_DTM,
   		   FLD_1,
       	   FLD_2,
   		   FLD_3,
   		   FLD_4
   	 FROM #TMP_COPY_EVNT_X 
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -20
   		BREAK
   	END
   	--Update statistics for existing buckets of the temporary statistic table
   	UPDATE EVNT_STSTC_HSTRY_X SET 
   		    EVNT_STSTC_HSTRY_X.LAST_MDFD_DTM = getdate(),
   		    EVNT_STSTC_HSTRY_X.FLD_4_SUM = s.FLD_4_SUM + te.FLD_4,
   		    EVNT_STSTC_HSTRY_X.FLD_4_MIN = dbo.GET_MIN(s.FLD_4_MIN, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_MAX = dbo.GET_MAX(s.FLD_4_MAX, te.FLD_4),
   		    EVNT_STSTC_HSTRY_X.FLD_4_LAST = te.FLD_4
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = 0
   	  AND s.POST_MNTH = 0
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -21
   		BREAK
   	END
   
   	--Delete temporary events already used to update statistics
   	DELETE #TMP_EVNT_X
   	FROM #TMP_EVNT_X te, EVNT_STSTC_HSTRY_X s
   	WHERE s.POST_YEAR = 0
   	  AND s.POST_MNTH = 0
   	  AND s.POST_WEEK = 0
   	  AND s.POST_DAY  = 0 
      AND s.KEY_1 = te.FLD_1
      AND s.KEY_2 = te.FLD_2
      AND s.KEY_3 = te.FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -22
   		BREAK
   	END
   	--Insert statistics using the remaining temporary events
   	INSERT EVNT_STSTC_HSTRY_X (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, KEY_1, KEY_2, KEY_3, POST_DTM, CNT, FLD_4_SUM, FLD_4_MIN, FLD_4_MAX, FLD_4_FRST, FLD_4_LAST)
   	SELECT 0, 0, 0, 0, FLD_1, FLD_2, FLD_3, '01/01/1900 12:01:00 AM', COUNT(*), SUM(FLD_4), MIN(FLD_4), MAX(FLD_4), MIN(FLD_4), MAX(FLD_4)
   	  FROM #TMP_EVNT_X
   	 GROUP BY FLD_1, FLD_2, FLD_3
   	
   	IF (@@ERROR <> 0)
   	BEGIN
   		ROLLBACK TRAN
   		SELECT @ERROR = -23
   		BREAK
   	END
   	
      TRUNCATE TABLE #TMP_EVNT_X
   END
   TRUNCATE TABLE #TMP_COPY_EVNT_X
	--Update the last event id processed
	UPDATE EVNT_TYPE
	   SET LAST_HSTRY_EVNT_ID = @END_EVNT_ID
	 WHERE EVNT_TYPE_ID = @EVNT_TYPE_ID 
	
	IF (@@ERROR <> 0)
	BEGIN
		ROLLBACK TRAN
		SELECT @ERROR = -24
		BREAK
	END
	
	COMMIT TRAN
END --WHILE
DROP TABLE #TMP_COPY_EVNT_X
DROP TABLE #TMP_EVNT_X
IF @ERROR <> 0
   RETURN @ERROR
ELSE
   RETURN @ROWS
```

