# dbo.MNTRNG_P_HSTRY_500028

**Database:** foundation_event  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.MNTRNG_P_HSTRY_500028"]
    EVNT_500028(["EVNT_500028"]) --> SP
    EVNT_STSTC_HSTRY_500028(["EVNT_STSTC_HSTRY_500028"]) --> SP
    EVNT_TYPE(["EVNT_TYPE"]) --> SP
    dbo_GET_MAX(["dbo.GET_MAX"]) --> SP
    TMP_HSTRY_COPY_EVNT_500028(["TMP_HSTRY_COPY_EVNT_500028"]) --> SP
    TMP_HSTRY_EVNT_500028(["TMP_HSTRY_EVNT_500028"]) --> SP
    TMP_HSTRY_KEY_500028(["TMP_HSTRY_KEY_500028"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| EVNT_500028 |
| EVNT_STSTC_HSTRY_500028 |
| EVNT_TYPE |
| dbo.GET_MAX |
| TMP_HSTRY_COPY_EVNT_500028 |
| TMP_HSTRY_EVNT_500028 |
| TMP_HSTRY_KEY_500028 |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[MNTRNG_P_HSTRY_500028] 

@BATCH_SIZE as int --Max number of records in a batch
AS

--Create temporary event table to keep a copy of the batch
IF EXISTS (SELECT * FROM sysobjects WHERE xtype = 'U' AND name = 'TMP_HSTRY_COPY_EVNT_500028')
   DROP TABLE dbo.TMP_HSTRY_COPY_EVNT_500028

CREATE TABLE dbo.TMP_HSTRY_COPY_EVNT_500028
(
   ID_CLMN integer NOT NULL,
   POST_YEAR smallint NOT NULL,
   POST_MNTH tinyint NOT NULL,
   POST_WEEK tinyint NOT NULL,
   POST_DAY tinyint NOT NULL,
   POST_DTM smalldatetime NOT NULL
      , FLD_1 smallint NULL 
   , FLD_2 smallint NULL 
   , FLD_3 smallint NULL 
   , FLD_28 datetime NULL 
   , FLD_35 smallint NULL 
   , FLD_34 nvarchar(50) NULL 
   , FLD_297 nvarchar(30) NULL 
   , FLD_279 smallint NULL 
   , FLD_280 int NULL 
   , FLD_250 int NULL 
   , FLD_251 tinyint NULL 
   , FLD_712 smallint NULL 
   , FLD_253 nvarchar(30) NULL 
   , FLD_255 smallint NULL 
   , FLD_708 nvarchar(2) NULL 
   , FLD_709 nvarchar(2) NULL 
   , FLD_710 nvarchar(4) NULL 
   , FLD_271 int NULL 
   , FLD_272 int NULL 
   , FLD_273 int NULL 
   , FLD_274 nvarchar(5) NULL 
   , FLD_275 int NULL 
   , FLD_276 int NULL 
   , FLD_277 nvarchar(20) NULL 
   , FLD_278 nvarchar(5) NULL 
   , FLD_259 smallint NULL 
   , FLD_260 nvarchar(8) NULL 
   , FLD_268 nvarchar(20) NULL 
   , FLD_261 nvarchar(5) NULL 
   , FLD_262 smallint NULL 
   , FLD_711 nvarchar(112) NULL 
   , FLD_466 smallint NULL 
   , FLD_4 smallint NULL 
   , FLD_5 smallint NULL 
   , FLD_7 smallint NULL 
   , FLD_264 tinyint NULL 
   , FLD_265 int NULL 
   , FLD_440 int NULL 
   , FLD_360 nvarchar(20) NULL 
   , FLD_361 nvarchar(20) NULL 
   , FLD_30 bigint NULL 
   , FLD_32 bigint NULL 
   , FLD_31 bigint NULL 
   , FLD_33 bigint NULL 

) ON [PRIMARY]

CREATE CLUSTERED INDEX TMP_HSTRY_COPY_EVNT_500028_1 ON dbo.TMP_HSTRY_COPY_EVNT_500028 (ID_CLMN) ON [PRIMARY]

--Create temporary event table
IF EXISTS (SELECT * FROM sysobjects WHERE xtype = 'U' AND name = 'TMP_HSTRY_EVNT_500028')
   DROP TABLE dbo.TMP_HSTRY_EVNT_500028

CREATE TABLE dbo.TMP_HSTRY_EVNT_500028
(
   ID_CLMN integer NOT NULL,
   POST_YEAR smallint NOT NULL,
   POST_MNTH tinyint NOT NULL,
   POST_WEEK tinyint NOT NULL,
   POST_DAY tinyint NOT NULL,
   POST_DTM smalldatetime NOT NULL
      , FLD_1 smallint NULL 
   , FLD_2 smallint NULL 
   , FLD_3 smallint NULL 
   , FLD_28 datetime NULL 
   , FLD_35 smallint NULL 
   , FLD_34 nvarchar(50) NULL 
   , FLD_297 nvarchar(30) NULL 
   , FLD_279 smallint NULL 
   , FLD_280 int NULL 
   , FLD_250 int NULL 
   , FLD_251 tinyint NULL 
   , FLD_712 smallint NULL 
   , FLD_253 nvarchar(30) NULL 
   , FLD_255 smallint NULL 
   , FLD_708 nvarchar(2) NULL 
   , FLD_709 nvarchar(2) NULL 
   , FLD_710 nvarchar(4) NULL 
   , FLD_271 int NULL 
   , FLD_272 int NULL 
   , FLD_273 int NULL 
   , FLD_274 nvarchar(5) NULL 
   , FLD_275 int NULL 
   , FLD_276 int NULL 
   , FLD_277 nvarchar(20) NULL 
   , FLD_278 nvarchar(5) NULL 
   , FLD_259 smallint NULL 
   , FLD_260 nvarchar(8) NULL 
   , FLD_268 nvarchar(20) NULL 
   , FLD_261 nvarchar(5) NULL 
   , FLD_262 smallint NULL 
   , FLD_711 nvarchar(112) NULL 
   , FLD_466 smallint NULL 
   , FLD_4 smallint NULL 
   , FLD_5 smallint NULL 
   , FLD_7 smallint NULL 
   , FLD_264 tinyint NULL 
   , FLD_265 int NULL 
   , FLD_440 int NULL 
   , FLD_360 nvarchar(20) NULL 
   , FLD_361 nvarchar(20) NULL 
   , FLD_30 bigint NULL 
   , FLD_32 bigint NULL 
   , FLD_31 bigint NULL 
   , FLD_33 bigint NULL 

) ON [PRIMARY]

--Indexes to speed up process
CREATE INDEX TMP_HSTRY_EVNT_500028_1 ON dbo.TMP_HSTRY_EVNT_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 ) ON [PRIMARY] 
CREATE CLUSTERED INDEX TMP_HSTRY_EVNT_500028_2 ON dbo.TMP_HSTRY_EVNT_500028 (ID_CLMN) ON [PRIMARY]

--Create temporary event table for history ids
IF EXISTS (SELECT * FROM sysobjects WHERE xtype = 'U' AND name = 'TMP_HSTRY_KEY_500028')
   DROP TABLE dbo.TMP_HSTRY_KEY_500028

CREATE TABLE dbo.TMP_HSTRY_KEY_500028
(
   POST_YEAR smallint NOT NULL,
   POST_MNTH tinyint NOT NULL,
   POST_WEEK tinyint NOT NULL,
   POST_DAY tinyint NOT NULL,
   POST_DTM smalldatetime NOT NULL
     , KEY_1 smallint NULL 
   , KEY_2 smallint NULL 
   , KEY_3 smallint NULL 
   , KEY_34 nvarchar(50) NULL 
   , KEY_5 smallint NULL 
   , KEY_7 smallint NULL 
   , FLD_30_SUM float NULL 
   , FLD_30_MAX bigint NULL 
   , FLD_32_SUM float NULL 
   , FLD_32_MAX bigint NULL 
   , FLD_31_SUM float NULL 
   , FLD_31_MAX bigint NULL 
   , FLD_33_SUM float NULL 
   , FLD_33_MAX bigint NULL 

 , CNT integer NOT NULL
 , MIN_ID integer NOT NULL
 , MAX_ID integer NOT NULL
)

--Indexes to speed up process
CREATE INDEX TMP_HSTRY_KEY_500028_1 ON dbo.TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7 ) ON [PRIMARY] 
CREATE CLUSTERED INDEX TMP_HSTRY_KEY_500028_2 ON dbo.TMP_HSTRY_KEY_500028 (MIN_ID, MAX_ID) ON [PRIMARY]

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

SELECT @EVNT_TYPE_ID = 500028, @ERROR = 0 , @ROWS = 0, @END_EVNT_ID = 0

--Get last event id processed during this cycle
SELECT @MAX_EVNT_ID = MAX(ISNULL(EVNT_ID,0))
  FROM EVNT_500028

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
   INSERT INTO TMP_HSTRY_COPY_EVNT_500028 (ID_CLMN, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY, POST_DTM , FLD_1 , FLD_2 , FLD_3 , FLD_28 , FLD_35 , FLD_34 , FLD_297 , FLD_279 , FLD_280 , FLD_250 , FLD_251 , FLD_712 , FLD_253 , FLD_255 , FLD_708 , FLD_709 , FLD_710 , FLD_271 , FLD_272 , FLD_273 , FLD_274 , FLD_275 , FLD_276 , FLD_277 , FLD_278 , FLD_259 , FLD_260 , FLD_268 , FLD_261 , FLD_262 , FLD_711 , FLD_466 , FLD_4 , FLD_5 , FLD_7 , FLD_264 , FLD_265 , FLD_440 , FLD_360 , FLD_361 , FLD_30 , FLD_32 , FLD_31 , FLD_33 )
   SELECT EVNT_ID,
         DATEPART(yy,EVNT_POST_DTM),
         DATEPART(mm,EVNT_POST_DTM),
         DATEPART(ww,EVNT_POST_DTM),
         DATEPART(dd,EVNT_POST_DTM),   
         DATEADD(ms, -DATEPART(ms, EVNT_POST_DTM), DATEADD(ss, -DATEPART(ss, EVNT_POST_DTM), DATEADD(mi, -DATEPART(mi, EVNT_POST_DTM), DATEADD(hh, -DATEPART(hh, EVNT_POST_DTM), EVNT_POST_DTM)))) 
         , FLD_1 , FLD_2 , FLD_3 , FLD_28 , FLD_35 , FLD_34 , FLD_297 , FLD_279 , FLD_280 , FLD_250 , FLD_251 , FLD_712 , FLD_253 , FLD_255 , FLD_708 , FLD_709 , FLD_710 , FLD_271 , FLD_272 , FLD_273 , FLD_274 , FLD_275 , FLD_276 , FLD_277 , FLD_278 , FLD_259 , FLD_260 , FLD_268 , FLD_261 , FLD_262 , FLD_711 , FLD_466 , FLD_4 , FLD_5 , FLD_7 , FLD_264 , FLD_265 , FLD_440 , FLD_360 , FLD_361 , FLD_30 , FLD_32 , FLD_31 , FLD_33 
    FROM EVNT_500028
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
      INSERT INTO TMP_HSTRY_EVNT_500028 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM 
             , FLD_1 , FLD_2 , FLD_3 , FLD_28 , FLD_35 , FLD_34 , FLD_297 , FLD_279 , FLD_280 , FLD_250 , FLD_251 , FLD_712 , FLD_253 , FLD_255 , FLD_708 , FLD_709 , FLD_710 , FLD_271 , FLD_272 , FLD_273 , FLD_274 , FLD_275 , FLD_276 , FLD_277 , FLD_278 , FLD_259 , FLD_260 , FLD_268 , FLD_261 , FLD_262 , FLD_711 , FLD_466 , FLD_4 , FLD_5 , FLD_7 , FLD_264 , FLD_265 , FLD_440 , FLD_360 , FLD_361 , FLD_30 , FLD_32 , FLD_31 , FLD_33 
        FROM TMP_HSTRY_COPY_EVNT_500028 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -4
         BREAK
      END
      
      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, MIN(POST_DAY) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY  FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -5
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500028 SET 
             EVNT_STSTC_HSTRY_500028.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500028.LAST_MDFD_DTM = getdate() 
             , EVNT_STSTC_HSTRY_500028.FLD_259_LAST = L.FLD_259 
 , EVNT_STSTC_HSTRY_500028.FLD_262_LAST = L.FLD_262 
 , EVNT_STSTC_HSTRY_500028.FLD_30_SUM = s.FLD_30_SUM + te.FLD_30_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_30_MAX = dbo.GET_MAX(s.FLD_30_MAX, te.FLD_30_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_32_SUM = s.FLD_32_SUM + te.FLD_32_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_32_MAX = dbo.GET_MAX(s.FLD_32_MAX, te.FLD_32_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_31_SUM = s.FLD_31_SUM + te.FLD_31_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_31_MAX = dbo.GET_MAX(s.FLD_31_MAX, te.FLD_31_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_33_SUM = s.FLD_33_SUM + te.FLD_33_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_33_MAX = dbo.GET_MAX(s.FLD_33_MAX, te.FLD_33_MAX) 
 
        FROM TMP_HSTRY_KEY_500028 te, EVNT_STSTC_HSTRY_500028 s, TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = te.POST_DAY 
              AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_3 = te.KEY_3 
  AND s.KEY_34 = te.KEY_34 
  AND s.KEY_5 = te.KEY_5 
  AND s.KEY_7 = te.KEY_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -6
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500028
        FROM TMP_HSTRY_EVNT_500028 te, EVNT_STSTC_HSTRY_500028 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = te.POST_DAY 
              AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_3 = te.FLD_3 
  AND s.KEY_34 = te.FLD_34 
  AND s.KEY_5 = te.FLD_5 
  AND s.KEY_7 = te.FLD_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -7
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, MIN(POST_DAY) , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , MIN(POST_DTM), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -8
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500028 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7 , CNT , FLD_259_LAST 
 , FLD_262_LAST 
 , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX )
      SELECT D.POST_DTM, D.POST_YEAR, D.POST_MNTH, 0, D.POST_DAY , D.KEY_1 , D.KEY_2 , D.KEY_3 , D.KEY_34 , D.KEY_5 , D.KEY_7 , D.CNT , L.FLD_259 , L.FLD_262 , D.FLD_30_SUM , D.FLD_30_MAX , D.FLD_32_SUM , D.FLD_32_MAX , D.FLD_31_SUM , D.FLD_31_MAX , D.FLD_33_SUM , D.FLD_33_MAX 
        FROM TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L, TMP_HSTRY_KEY_500028 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -9
         BREAK
      END

      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500028
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
   END

   --Week bucket
   IF (@WEEK_LVL > 0)
   BEGIN

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500028 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM 
             , FLD_1 , FLD_2 , FLD_3 , FLD_28 , FLD_35 , FLD_34 , FLD_297 , FLD_279 , FLD_280 , FLD_250 , FLD_251 , FLD_712 , FLD_253 , FLD_255 , FLD_708 , FLD_709 , FLD_710 , FLD_271 , FLD_272 , FLD_273 , FLD_274 , FLD_275 , FLD_276 , FLD_277 , FLD_278 , FLD_259 , FLD_260 , FLD_268 , FLD_261 , FLD_262 , FLD_711 , FLD_466 , FLD_4 , FLD_5 , FLD_7 , FLD_264 , FLD_265 , FLD_440 , FLD_360 , FLD_361 , FLD_30 , FLD_32 , FLD_31 , FLD_33  
        FROM TMP_HSTRY_COPY_EVNT_500028 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -10
         BREAK
      END

      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, MIN(POST_WEEK), 0 , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY  FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -11
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500028 SET 
             EVNT_STSTC_HSTRY_500028.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500028.LAST_MDFD_DTM = getdate()
             , EVNT_STSTC_HSTRY_500028.FLD_259_LAST = L.FLD_259 
 , EVNT_STSTC_HSTRY_500028.FLD_262_LAST = L.FLD_262 
 , EVNT_STSTC_HSTRY_500028.FLD_30_SUM = s.FLD_30_SUM + te.FLD_30_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_30_MAX = dbo.GET_MAX(s.FLD_30_MAX, te.FLD_30_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_32_SUM = s.FLD_32_SUM + te.FLD_32_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_32_MAX = dbo.GET_MAX(s.FLD_32_MAX, te.FLD_32_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_31_SUM = s.FLD_31_SUM + te.FLD_31_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_31_MAX = dbo.GET_MAX(s.FLD_31_MAX, te.FLD_31_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_33_SUM = s.FLD_33_SUM + te.FLD_33_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_33_MAX = dbo.GET_MAX(s.FLD_33_MAX, te.FLD_33_MAX) 
 
        FROM TMP_HSTRY_KEY_500028 te, EVNT_STSTC_HSTRY_500028 s, TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = te.POST_WEEK
         AND s.POST_DAY  = 0 
              AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_3 = te.KEY_3 
  AND s.KEY_34 = te.KEY_34 
  AND s.KEY_5 = te.KEY_5 
  AND s.KEY_7 = te.KEY_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -12
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500028
        FROM TMP_HSTRY_EVNT_500028 te, EVNT_STSTC_HSTRY_500028 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = te.POST_WEEK
         AND s.POST_DAY  = 0 
              AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_3 = te.FLD_3 
  AND s.KEY_34 = te.FLD_34 
  AND s.KEY_5 = te.FLD_5 
  AND s.KEY_7 = te.FLD_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -13
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, MIN(POST_WEEK), 0 , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , MIN(DATEADD(dd, DATEPART(dy, POST_DTM) - DATEPART(dw, POST_DTM), DATEADD(mm, -DATEPART(mm, POST_DTM) + 1, DATEADD(dd, -DATEPART(dd, POST_DTM) + 1, POST_DTM)))), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY POST_YEAR, POST_WEEK , FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -14
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500028 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7 , CNT , FLD_259_LAST 
 , FLD_262_LAST 
 , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX )
      SELECT D.POST_DTM, D.POST_YEAR, 0, D.POST_WEEK, 0 , D.KEY_1 , D.KEY_2 , D.KEY_3 , D.KEY_34 , D.KEY_5 , D.KEY_7 , D.CNT , L.FLD_259 , L.FLD_262 , D.FLD_30_SUM , D.FLD_30_MAX , D.FLD_32_SUM , D.FLD_32_MAX , D.FLD_31_SUM , D.FLD_31_MAX , D.FLD_33_SUM , D.FLD_33_MAX 
        FROM TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L, TMP_HSTRY_KEY_500028 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -15
         BREAK
      END

      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500028
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
   END

   --Month bucket
   IF (@MNTH_LVL > 0)
   BEGIN

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500028 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM
             , FLD_1 , FLD_2 , FLD_3 , FLD_28 , FLD_35 , FLD_34 , FLD_297 , FLD_279 , FLD_280 , FLD_250 , FLD_251 , FLD_712 , FLD_253 , FLD_255 , FLD_708 , FLD_709 , FLD_710 , FLD_271 , FLD_272 , FLD_273 , FLD_274 , FLD_275 , FLD_276 , FLD_277 , FLD_278 , FLD_259 , FLD_260 , FLD_268 , FLD_261 , FLD_262 , FLD_711 , FLD_466 , FLD_4 , FLD_5 , FLD_7 , FLD_264 , FLD_265 , FLD_440 , FLD_360 , FLD_361 , FLD_30 , FLD_32 , FLD_31 , FLD_33  
        FROM TMP_HSTRY_COPY_EVNT_500028 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -16
         BREAK
      END

      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, 0 , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY  FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -17
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500028 SET 
             EVNT_STSTC_HSTRY_500028.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500028.LAST_MDFD_DTM = getdate()
             , EVNT_STSTC_HSTRY_500028.FLD_259_LAST = L.FLD_259 
 , EVNT_STSTC_HSTRY_500028.FLD_262_LAST = L.FLD_262 
 , EVNT_STSTC_HSTRY_500028.FLD_30_SUM = s.FLD_30_SUM + te.FLD_30_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_30_MAX = dbo.GET_MAX(s.FLD_30_MAX, te.FLD_30_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_32_SUM = s.FLD_32_SUM + te.FLD_32_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_32_MAX = dbo.GET_MAX(s.FLD_32_MAX, te.FLD_32_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_31_SUM = s.FLD_31_SUM + te.FLD_31_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_31_MAX = dbo.GET_MAX(s.FLD_31_MAX, te.FLD_31_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_33_SUM = s.FLD_33_SUM + te.FLD_33_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_33_MAX = dbo.GET_MAX(s.FLD_33_MAX, te.FLD_33_MAX) 
 
        FROM TMP_HSTRY_KEY_500028 te, EVNT_STSTC_HSTRY_500028 s, TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0 
              AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_3 = te.KEY_3 
  AND s.KEY_34 = te.KEY_34 
  AND s.KEY_5 = te.KEY_5 
  AND s.KEY_7 = te.KEY_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -18
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500028
        FROM TMP_HSTRY_EVNT_500028 te, EVNT_STSTC_HSTRY_500028 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = te.POST_MNTH
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0
              AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_3 = te.FLD_3 
  AND s.KEY_34 = te.FLD_34 
  AND s.KEY_5 = te.FLD_5 
  AND s.KEY_7 = te.FLD_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -19
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), MIN(POST_MNTH), 0, 0 , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , MIN(DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM)), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY POST_YEAR, POST_MNTH , FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -20
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500028 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7 , CNT , FLD_259_LAST 
 , FLD_262_LAST 
 , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX )
      SELECT D.POST_DTM, D.POST_YEAR, D.POST_MNTH, 0, 0 , D.KEY_1 , D.KEY_2 , D.KEY_3 , D.KEY_34 , D.KEY_5 , D.KEY_7 , D.CNT , L.FLD_259 , L.FLD_262 , D.FLD_30_SUM , D.FLD_30_MAX , D.FLD_32_SUM , D.FLD_32_MAX , D.FLD_31_SUM , D.FLD_31_MAX , D.FLD_33_SUM , D.FLD_33_MAX 
        FROM TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L, TMP_HSTRY_KEY_500028 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -21
         BREAK
      END
      
      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500028
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
   END

   --Year bucket
   IF (@YEAR_LVL > 0)
   BEGIN

      --Step 0-Populate the temporary event table from the copy
      INSERT INTO TMP_HSTRY_EVNT_500028 
      SELECT ID_CLMN,
             POST_YEAR,
             POST_MNTH,
             POST_WEEK,
             POST_DAY,
             POST_DTM
             , FLD_1 , FLD_2 , FLD_3 , FLD_28 , FLD_35 , FLD_34 , FLD_297 , FLD_279 , FLD_280 , FLD_250 , FLD_251 , FLD_712 , FLD_253 , FLD_255 , FLD_708 , FLD_709 , FLD_710 , FLD_271 , FLD_272 , FLD_273 , FLD_274 , FLD_275 , FLD_276 , FLD_277 , FLD_278 , FLD_259 , FLD_260 , FLD_268 , FLD_261 , FLD_262 , FLD_711 , FLD_466 , FLD_4 , FLD_5 , FLD_7 , FLD_264 , FLD_265 , FLD_440 , FLD_360 , FLD_361 , FLD_30 , FLD_32 , FLD_31 , FLD_33 
        FROM TMP_HSTRY_COPY_EVNT_500028 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -22
         BREAK
      END

      --Step 1-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, 0, 0 , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , '01/01/1900 12:01:00 AM', COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY  FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -23
         BREAK
      END

      --Step 2-Update actual statistics using the computed value temporary table
      UPDATE EVNT_STSTC_HSTRY_500028 SET 
             EVNT_STSTC_HSTRY_500028.CNT = s.CNT + te.CNT,
             EVNT_STSTC_HSTRY_500028.LAST_MDFD_DTM = getdate()
             , EVNT_STSTC_HSTRY_500028.FLD_259_LAST = L.FLD_259 
 , EVNT_STSTC_HSTRY_500028.FLD_262_LAST = L.FLD_262 
 , EVNT_STSTC_HSTRY_500028.FLD_30_SUM = s.FLD_30_SUM + te.FLD_30_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_30_MAX = dbo.GET_MAX(s.FLD_30_MAX, te.FLD_30_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_32_SUM = s.FLD_32_SUM + te.FLD_32_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_32_MAX = dbo.GET_MAX(s.FLD_32_MAX, te.FLD_32_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_31_SUM = s.FLD_31_SUM + te.FLD_31_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_31_MAX = dbo.GET_MAX(s.FLD_31_MAX, te.FLD_31_MAX) 
 , EVNT_STSTC_HSTRY_500028.FLD_33_SUM = s.FLD_33_SUM + te.FLD_33_SUM 
 , EVNT_STSTC_HSTRY_500028.FLD_33_MAX = dbo.GET_MAX(s.FLD_33_MAX, te.FLD_33_MAX) 
 
        FROM TMP_HSTRY_KEY_500028 te, EVNT_STSTC_HSTRY_500028 s, TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L
       WHERE te.MIN_ID = F.ID_CLMN 
         AND te.MAX_ID = L.ID_CLMN
         AND s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0 
              AND s.KEY_1 = te.KEY_1 
  AND s.KEY_2 = te.KEY_2 
  AND s.KEY_3 = te.KEY_3 
  AND s.KEY_34 = te.KEY_34 
  AND s.KEY_5 = te.KEY_5 
  AND s.KEY_7 = te.KEY_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -24
         BREAK
      END

      --Step 3-clean the computed value temp table
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
      
      --Step 4-Delete temporary events already used to update statistics
      DELETE TMP_HSTRY_EVNT_500028
        FROM TMP_HSTRY_EVNT_500028 te, EVNT_STSTC_HSTRY_500028 s
       WHERE s.POST_YEAR = te.POST_YEAR
         AND s.POST_MNTH = 0
         AND s.POST_WEEK = 0
         AND s.POST_DAY  = 0 
          AND s.KEY_1 = te.FLD_1 
  AND s.KEY_2 = te.FLD_2 
  AND s.KEY_3 = te.FLD_3 
  AND s.KEY_34 = te.FLD_34 
  AND s.KEY_5 = te.FLD_5 
  AND s.KEY_7 = te.FLD_7 
    

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -25
         BREAK
      END

      --Step 5-Insert computed values from the temp event table
      INSERT TMP_HSTRY_KEY_500028 (POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7  , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX , POST_DTM, CNT, MIN_ID, MAX_ID)
      SELECT MIN(POST_YEAR), 0, 0, 0 , MIN(FLD_1) , MIN(FLD_2) , MIN(FLD_3) , MIN(FLD_34) , MIN(FLD_5) , MIN(FLD_7) , SUM(FLD_30) , MAX(FLD_30) , SUM(FLD_32) , MAX(FLD_32) , SUM(FLD_31) , MAX(FLD_31) , SUM(FLD_33) , MAX(FLD_33) , MIN(DATEADD(mm, -DATEPART(mm, POST_DTM)+1, DATEADD(dd, -DATEPART(dd, POST_DTM)+1, POST_DTM))), COUNT(*), MIN(ID_CLMN), MAX(ID_CLMN)
        FROM TMP_HSTRY_EVNT_500028
        GROUP BY POST_YEAR , FLD_1 , FLD_2 , FLD_3 , FLD_34 , FLD_5 , FLD_7 

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -26
         BREAK
      END

      --Step 6-Insert new keys using the computed value temporary table
      INSERT EVNT_STSTC_HSTRY_500028 (POST_DTM, POST_YEAR, POST_MNTH, POST_WEEK, POST_DAY , KEY_1 , KEY_2 , KEY_3 , KEY_34 , KEY_5 , KEY_7 , CNT , FLD_259_LAST 
 , FLD_262_LAST 
 , FLD_30_SUM , FLD_30_MAX , FLD_32_SUM , FLD_32_MAX , FLD_31_SUM , FLD_31_MAX , FLD_33_SUM , FLD_33_MAX )
      SELECT D.POST_DTM, D.POST_YEAR, 0, 0, 0 , D.KEY_1 , D.KEY_2 , D.KEY_3 , D.KEY_34 , D.KEY_5 , D.KEY_7 , D.CNT , L.FLD_259 , L.FLD_262 , D.FLD_30_SUM , D.FLD_30_MAX , D.FLD_32_SUM , D.FLD_32_MAX , D.FLD_31_SUM , D.FLD_31_MAX , D.FLD_33_SUM , D.FLD_33_MAX 
        FROM TMP_HSTRY_EVNT_500028 F, TMP_HSTRY_EVNT_500028 L, TMP_HSTRY_KEY_500028 D
       WHERE D.MIN_ID = F.ID_CLMN 
         AND D.MAX_ID = L.ID_CLMN

      IF (@@ERROR <> 0)
      BEGIN
         ROLLBACK TRAN
         SELECT @ERROR = -27
         BREAK
      END

      --Step 7-Clean temp tables
      TRUNCATE TABLE TMP_HSTRY_EVNT_500028
      TRUNCATE TABLE TMP_HSTRY_KEY_500028
   END

   TRUNCATE TABLE TMP_HSTRY_COPY_EVNT_500028

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

DROP TABLE TMP_HSTRY_COPY_EVNT_500028
DROP TABLE TMP_HSTRY_EVNT_500028
DROP TABLE TMP_HSTRY_KEY_500028

IF @ERROR <> 0
   RETURN @ERROR
ELSE
   RETURN @ROWS
```

