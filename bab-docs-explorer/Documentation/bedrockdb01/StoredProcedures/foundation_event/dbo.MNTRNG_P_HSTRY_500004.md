# dbo.MNTRNG_P_HSTRY_500004

**Database:** foundation_event  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.MNTRNG_P_HSTRY_500004"]
    EVNT_500004(["EVNT_500004"]) --> SP
    EVNT_STSTC_HSTRY_500004(["EVNT_STSTC_HSTRY_500004"]) --> SP
    EVNT_TYPE(["EVNT_TYPE"]) --> SP
    dbo_GET_MAX(["dbo.GET_MAX"]) --> SP
    dbo_GET_MIN(["dbo.GET_MIN"]) --> SP
    TMP_HSTRY_COPY_EVNT_500004(["TMP_HSTRY_COPY_EVNT_500004"]) --> SP
    TMP_HSTRY_EVNT_500004(["TMP_HSTRY_EVNT_500004"]) --> SP
    TMP_HSTRY_KEY_500004(["TMP_HSTRY_KEY_500004"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| EVNT_500004 |
| EVNT_STSTC_HSTRY_500004 |
| EVNT_TYPE |
| dbo.GET_MAX |
| dbo.GET_MIN |
| TMP_HSTRY_COPY_EVNT_500004 |
| TMP_HSTRY_EVNT_500004 |
| TMP_HSTRY_KEY_500004 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[MNTRNG_P_HSTRY_500004] 

@BATCH_SIZE as int --Max number of records in a batch
AS

--Create temporary event table to keep a copy of the batch
IF EXISTS (SELECT * FROM sysobjects WHERE xtype = 'U' AND name = 'TMP_HSTRY_COPY_EVNT_500004')
   DROP TABLE dbo.TMP_HSTRY_COPY_EVNT_500004

CREATE TABLE dbo.TMP_HSTRY_COPY_EVNT_500004
(
   ID_CLMN integer NOT NULL,
   POST_YEAR smallint NOT NULL,
   POST_MNTH tinyint NOT NULL,
   POST_WEEK tinyint NOT NULL,
   POST_DAY tinyint NOT NULL,
   POST_DTM smalldatetime NOT NULL
   , SRVR_NAME nvarchar(50) NOT NULL 
 , APP_ID decimal NOT NULL 
 , PRDCT_ID nvarchar(30) NOT NULL 
 , INSTNC_NUM smallint NOT NULL 
    , FLD_1 smallint NULL 
   , FLD_2 smallint NULL 
   , FLD_4 smallint NULL 
   , FLD_5 smallint NULL 
   , FLD_26 bigint NULL 
   , FLD_27 smallint NULL 

) ON [PRIMARY]

CREATE CLUSTERED INDEX TMP_HSTRY_COPY_EVNT_500004_1 ON dbo.TMP_HSTRY_COPY_EVNT_500004 (ID_CLMN) ON [PRIMARY]

--Create temporary event table
IF EXISTS (SELECT * FROM sysobjects WHERE xtype = 'U' AND name = 'TMP_HSTRY_EVNT_500004')
   DROP TABLE dbo.TMP_HSTRY_EVNT_500004

CREATE TABLE dbo.TMP_HSTRY_EVNT_500004
(
   ID_CLMN integer NOT NULL,
   POST_YEAR smallint NOT NULL,
   POST_MNTH tinyint NOT NULL,
   POST_WEEK tinyint NOT NULL,
   POST_DAY tinyint NOT NULL,
   POST_DTM smalldatetime NOT NULL
   , SRVR_NAME nvarchar(50) NOT NULL 
 , APP_ID decimal NOT NULL 
 , PRDCT_ID nvarchar(30) NOT NULL 
 , INSTNC_NUM smallint NOT NULL 
    , FLD_1 smallint NULL 
   , FLD_2 smallint NULL 
   , FLD_4 smallint NULL 
   , FLD_5 smallint NULL 
   , FLD_26 bigint NULL 
   , FLD_27 smallint NULL 

) ON [PRIMARY]

--Indexes to speed up process
CREATE INDEX TMP_HSTRY_EVNT_500004_1 ON dbo.TMP_HSTRY_EVNT_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 ) ON [PRIMARY] 
CREATE CLUSTERED INDEX TMP_HSTRY_EVNT_500004_2 ON dbo.TMP_HSTRY_EVNT_500004 (ID_CLMN) ON [PRIMARY]

--Create temporary event table for history ids
IF EXISTS (SELECT * FROM sysobjects WHERE xtype = 'U' AND name = 'TMP_HSTRY_KEY_500004')
   DROP TABLE dbo.TMP_HSTRY_KEY_500004

CREATE TABLE dbo.TMP_HSTRY_KEY_500004
(
   POST_YEAR smallint NOT NULL,
   POST_MNTH tinyint NOT NULL,
   POST_WEEK tinyint NOT NULL,
   POST_DAY tinyint NOT NULL,
   POST_DTM smalldatetime NOT NULL
  , SRVR_NAME nvarchar(50) NOT NULL 
 , APP_ID decimal NOT NULL 
 , PRDCT_ID nvarchar(30) NOT NULL 
 , INSTNC_NUM smallint NOT NULL 
    , KEY_1 smallint NULL 
   , KEY_2 smallint NULL 
   , KEY_4 smallint NULL 
   , KEY_5 smallint NULL 
   , FLD_26_SUM float NULL 
   , FLD_26_MIN bigint NULL 
   , FLD_26_MAX bigint NULL 
   , FLD_27_SUM float NULL 

 , CNT integer NOT NULL
 , MIN_ID integer NOT NULL
 , MAX_ID integer NOT NULL
)

--Indexes to speed up process
CREATE INDEX TMP_HSTRY_KEY_500004_1 ON dbo.TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5 ) ON [PRIMARY] 
CREATE CLUSTERED INDEX TMP_HSTRY_KEY_500004_2 ON dbo.TMP_HSTRY_KEY_500004 (MIN_ID, MAX_ID) ON [PRIMARY]

--Variables
DECLARE @MAX_EVNT_ID as int,        --Last event id processed during this cycle
        @STRT_EVNT_ID as int,       --First event of batch
        @END_EVNT_ID as int,        --Last event of batch
        @LAST_HSTRY_EVNT_ID as int, --Last event id processed in the previous cycle
        @EVNT_TYPE_ID as int,       --Constant for Event Type ID
        @ERROR as int,              --Error return code
        @ROWS as int,               --Total number of events processed
        @ROWCOUNT as int,           --Number of events processed in a batch
        @DAY_LVL as int,            --Day level
        @MNTH_LVL as int,           --Month level
        @WEEK_LVL as int,           --Week level
        @YEAR_LVL as int,           --Year level
        @STSTC_LVL as int           --Statistics level

SELECT @EVNT_TYPE_ID = 500004, @ERROR = 0 , @ROWS = 0, @END_EVNT_ID = 0

--Get last event id processed during this cycle
SELECT @MAX_EVNT_ID = MAX(ISNULL(EVNT_ID,0))
  FROM EVNT_500004

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

   --Get last event id processed in the previous cycle and the statistics levels
   SELECT @LAST_HSTRY_EVNT_ID = ISNULL(LAST_HSTRY_EVNT_ID,0)
     FROM EVNT_TYPE
    WHERE EVNT_TYPE_ID = @EVNT_TYPE_ID

   IF (@@ERROR <> 0)
   BEGIN
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
      SELECT @ERROR = @ROWS 
      BREAK
   END

   BEGIN TRAN

   --Populate the temporary event table using only the new events
   INSERT INTO TMP_HSTRY_COPY_EVNT_500004 (ID_CLMN, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, POST_DTM , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 , FLD_26 , FLD_27 )
   SELECT EVNT_ID,
         DATEPART(yy,EVNT_POST_DTM),
         DATEPART(mm,EVNT_POST_DTM),
         DATEPART(ww,EVNT_POST_DTM),
         DATEPART(dd,EVNT_POST_DTM),   
         DATEADD(ms, -DATEPART(ms, EVNT_POST_DTM), DATEADD(ss, -DATEPART(ss, EVNT_POST_DTM), DATEADD(mi, -DATEPART(mi, EVNT_POST_DTM), DATEADD(hh, -DATEPART(hh, EVNT_POST_DTM), EVNT_POST_DTM)))) 
         , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 , FLD_26 , FLD_27 
    FROM EVNT_500004
   WHERE EVNT_ID BETWEEN @STRT_EVNT_ID AND @END_EVNT_ID

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

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500004 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM 
             , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 , FLD_26 , FLD_27 
        FROM TMP_HSTRY_COPY_EVNT_500004 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -4
         BREAK
      END
      
      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, MIN(POST_DAY) , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY  SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -5
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500004 SET 
             EVNT_STSTC_HSTRY_500004.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500004.LAST_MDFD_DTM = getdate() 
             , EVNT_STSTC_HSTRY_500004.FLD_26_SUM = s.FLD_26_SUM + te.FLD_26_SUM 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MIN = dbo.GET_MIN(s.FLD_26_MIN, te.FLD_26_MIN) 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MAX = dbo.GET_MAX(s.FLD_26_MAX, te.FLD_26_MAX) 
 , EVNT_STSTC_HSTRY_500004.FLD_27_SUM = s.FLD_27_SUM + te.FLD_27_SUM 
 
        FROM TMP_HSTRY_KEY_500004 te, EVNT_STSTC_HSTRY_500004 s, TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = te.POST_DAY 
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_4 = te.KEY_4 
  AND s.KEY_5 = te.KEY_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -6
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500004
        FROM TMP_HSTRY_EVNT_500004 te, EVNT_STSTC_HSTRY_500004 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = te.POST_DAY 
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_4 = te.FLD_4 
  AND s.KEY_5 = te.FLD_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -7
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, MIN(POST_DAY) , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , MIN(POST_DTM), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -8
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500004 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5 , CNT , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM )
      SELECT D.POST_DTM, D.POST_YEAR, D.POST_MNTH, 0, D.POST_DAY , D.SRVR_NAME , D.APP_ID , D.PRDCT_ID , D.INSTNC_NUM , D.KEY_1 , D.KEY_2 , D.KEY_4 , D.KEY_5 , D.CNT , D.FLD_26_SUM , D.FLD_26_MIN , D.FLD_26_MAX , D.FLD_27_SUM 
        FROM TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L, TMP_HSTRY_KEY_500004 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -9
         BREAK
      END

      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500004
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
   END

   --Week bucket
   IF (@WEEK_LVL > 0)
   BEGIN

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500004 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM 
             , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 , FLD_26 , FLD_27  
        FROM TMP_HSTRY_COPY_EVNT_500004 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -10
         BREAK
      END

      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, MIN(POST_WEEK), 0 , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY  SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -11
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500004 SET 
             EVNT_STSTC_HSTRY_500004.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500004.LAST_MDFD_DTM = getdate()
             , EVNT_STSTC_HSTRY_500004.FLD_26_SUM = s.FLD_26_SUM + te.FLD_26_SUM 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MIN = dbo.GET_MIN(s.FLD_26_MIN, te.FLD_26_MIN) 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MAX = dbo.GET_MAX(s.FLD_26_MAX, te.FLD_26_MAX) 
 , EVNT_STSTC_HSTRY_500004.FLD_27_SUM = s.FLD_27_SUM + te.FLD_27_SUM 
 
        FROM TMP_HSTRY_KEY_500004 te, EVNT_STSTC_HSTRY_500004 s, TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = te.POST_WEEK
         AND s.POST_DAY  = 0 
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_4 = te.KEY_4 
  AND s.KEY_5 = te.KEY_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -12
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500004
        FROM TMP_HSTRY_EVNT_500004 te, EVNT_STSTC_HSTRY_500004 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = te.POST_WEEK
         AND s.POST_DAY  = 0 
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_4 = te.FLD_4 
  AND s.KEY_5 = te.FLD_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -13
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, MIN(POST_WEEK), 0 , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , MIN(DATEADD(dd, DATEPART(dy, POST_DTM) - DATEPART(dw, POST_DTM), DATEADD(mm, -DATEPART(mm, POST_DTM) + 1, DATEADD(dd, -DATEPART(dd, POST_DTM) + 1, POST_DTM)))), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY POST_YEAR, POST_WEEK , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -14
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500004 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5 , CNT , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM )
      SELECT D.POST_DTM, D.POST_YEAR, 0, D.POST_WEEK, 0 , D.SRVR_NAME , D.APP_ID , D.PRDCT_ID , D.INSTNC_NUM , D.KEY_1 , D.KEY_2 , D.KEY_4 , D.KEY_5 , D.CNT , D.FLD_26_SUM , D.FLD_26_MIN , D.FLD_26_MAX , D.FLD_27_SUM 
        FROM TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L, TMP_HSTRY_KEY_500004 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -15
         BREAK
      END

      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500004
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
   END

   --Month bucket
   IF (@MNTH_LVL > 0)
   BEGIN

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500004 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM
             , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 , FLD_26 , FLD_27  
        FROM TMP_HSTRY_COPY_EVNT_500004 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -16
         BREAK
      END

      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, 0 , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY  SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -17
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500004 SET 
             EVNT_STSTC_HSTRY_500004.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500004.LAST_MDFD_DTM = getdate()
             , EVNT_STSTC_HSTRY_500004.FLD_26_SUM = s.FLD_26_SUM + te.FLD_26_SUM 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MIN = dbo.GET_MIN(s.FLD_26_MIN, te.FLD_26_MIN) 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MAX = dbo.GET_MAX(s.FLD_26_MAX, te.FLD_26_MAX) 
 , EVNT_STSTC_HSTRY_500004.FLD_27_SUM = s.FLD_27_SUM + te.FLD_27_SUM 
 
        FROM TMP_HSTRY_KEY_500004 te, EVNT_STSTC_HSTRY_500004 s, TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0 
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_4 = te.KEY_4 
  AND s.KEY_5 = te.KEY_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -18
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500004
        FROM TMP_HSTRY_EVNT_500004 te, EVNT_STSTC_HSTRY_500004 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_4 = te.FLD_4 
  AND s.KEY_5 = te.FLD_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -19
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, 0 , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , MIN(DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM)), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY POST_YEAR, POST_MNTH , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -20
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500004 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5 , CNT , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM )
      SELECT D.POST_DTM, D.POST_YEAR, D.POST_MNTH, 0, 0 , D.SRVR_NAME , D.APP_ID , D.PRDCT_ID , D.INSTNC_NUM , D.KEY_1 , D.KEY_2 , D.KEY_4 , D.KEY_5 , D.CNT , D.FLD_26_SUM , D.FLD_26_MIN , D.FLD_26_MAX , D.FLD_27_SUM 
        FROM TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L, TMP_HSTRY_KEY_500004 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -21
         BREAK
      END
      
      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500004
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
   END

   --Year bucket
   IF (@YEAR_LVL > 0)
   BEGIN

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500004 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM
             , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 , FLD_26 , FLD_27 
        FROM TMP_HSTRY_COPY_EVNT_500004 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -22
         BREAK
      END

      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, 0, 0 , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY  SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -23
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500004 SET 
             EVNT_STSTC_HSTRY_500004.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500004.LAST_MDFD_DTM = getdate()
             , EVNT_STSTC_HSTRY_500004.FLD_26_SUM = s.FLD_26_SUM + te.FLD_26_SUM 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MIN = dbo.GET_MIN(s.FLD_26_MIN, te.FLD_26_MIN) 
 , EVNT_STSTC_HSTRY_500004.FLD_26_MAX = dbo.GET_MAX(s.FLD_26_MAX, te.FLD_26_MAX) 
 , EVNT_STSTC_HSTRY_500004.FLD_27_SUM = s.FLD_27_SUM + te.FLD_27_SUM 
 
        FROM TMP_HSTRY_KEY_500004 te, EVNT_STSTC_HSTRY_500004 s, TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0 
              AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_4 = te.KEY_4 
  AND s.KEY_5 = te.KEY_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -24
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500004
        FROM TMP_HSTRY_EVNT_500004 te, EVNT_STSTC_HSTRY_500004 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0 
          AND s.SRVR_NAME = te.SRVR_NAME 
  AND s.APP_ID = te.APP_ID 
  AND s.PRDCT_ID = te.PRDCT_ID 
  AND s.INSTNC_NUM = te.INSTNC_NUM 
  AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_4 = te.FLD_4 
  AND s.KEY_5 = te.FLD_5 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -25
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500004 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5  , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, 0, 0 , MIN(SRVR_NAME) , MIN(APP_ID) , MIN(PRDCT_ID) , MIN(INSTNC_NUM) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_4) , MIN(FLD_5) , SUM(FLD_26) , MIN(FLD_26) , MAX(FLD_26) , SUM(FLD_27) , MIN(DATEADD(mm, -DATEPART(mm, POST_DTM)+1, DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM))), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500004
        GROUP BY POST_YEAR , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , FLD_1 , FLD_2 , FLD_4 , FLD_5 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -26
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500004 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , SRVR_NAME , APP_ID , PRDCT_ID , INSTNC_NUM , KEY_1 , KEY_2 , KEY_4 , KEY_5 , CNT , FLD_26_SUM , FLD_26_MIN , FLD_26_MAX , FLD_27_SUM )
      SELECT D.POST_DTM, D.POST_YEAR, 0, 0, 0 , D.SRVR_NAME , D.APP_ID , D.PRDCT_ID , D.INSTNC_NUM , D.KEY_1 , D.KEY_2 , D.KEY_4 , D.KEY_5 , D.CNT , D.FLD_26_SUM , D.FLD_26_MIN , D.FLD_26_MAX , D.FLD_27_SUM 
        FROM TMP_HSTRY_EVNT_500004 F, TMP_HSTRY_EVNT_500004 L, TMP_HSTRY_KEY_500004 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -27
         BREAK
      END

      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500004
      TRUNCATE TABLE TMP_HSTRY_KEY_500004
   END

   TRUNCATE TABLE TMP_HSTRY_COPY_EVNT_500004

   --Update the last event id processed
   UPDATE EVNT_TYPE
      SET LAST_HSTRY_EVNT_ID = @END_EVNT_ID
    WHERE EVNT_TYPE_ID = @EVNT_TYPE_ID 
   
   IF (@@ERROR <> 0)
   BEGIN
      ROLLBACK TRAN
      SELECT @ERROR = -28
      BREAK
   END

   COMMIT TRAN

END --WHILE

DROP TABLE TMP_HSTRY_COPY_EVNT_500004
DROP TABLE TMP_HSTRY_EVNT_500004
DROP TABLE TMP_HSTRY_KEY_500004

IF @ERROR <> 0
   RETURN @ERROR
ELSE
   RETURN @ROWS
```

