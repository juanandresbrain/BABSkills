# dbo.get_clndr_chld_cnt_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.get_clndr_chld_cnt_$sp"]
    CLNDR_TMPLT_ALGRTHM(["CLNDR_TMPLT_ALGRTHM"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CLNDR_TMPLT_ALGRTHM |

## Stored Procedure Code

```sql
create proc [dbo].[get_clndr_chld_cnt_$sp] (@i_seq integer,
 @i_total_seq integer,
 @i_startdatetime datetime, 
 @i_perioddatetime datetime, 
 @i_chld_cnt_algrthm_id binary(16), 
 @i_chld_cnt integer OUT,
 @i_enddaynumber integer)
AS

DECLARE

/* Proc Name: get_clndr_chld_cnt_$sp
   Desc: Algorithm Parsing and Execution Routine - Child Count Generation for calendar
  
   This procedure will return to the caller a integer representing the number of children 
   a parent will contain based on an algorithm and a template definition                  
  
   Tokens understood by procedure :   [CalendarStartDate]                                 
                                  :   [CurrentPeriodDate]                                 
                                  :   [ChildSeq]                                          
                                  :   [TotalSeq]                                          
                                  :   [LevelLabel]                                        
                                                                                          
   Functions understood           :   YearNumber                                          
                                  :   MonthLabel                                          
                                  :   MonthNumber                                         
                                  :   WeekDayNumber                                       
                                  :   DayNumber                                           

HISTORY:
Date     Name		Def#     Desc
Jul30,10 Paul            119910  removed double quotes to avoid error due to quoted_identifier setting
Aug09,05 Ian/Paul       DV-1196  author          
                                     */

  @i_algrthm      varchar(500),
  @i_errmsg       varchar(50),
  @i_level_desc   varchar(100),
  @i_start_date_token  varchar(100),
  @i_period_date_token varchar(100),                              
  @i_cnt          integer,
  @i_end_bracket  integer,
  @i_strt_bracket integer,
  @i_cmd          nvarchar(1000),
  @i_bracketcnt   integer,
  @i_testchar     char(1),
  @ddno           integer

BEGIN

  SELECT @i_start_date_token  = 'convert(datetime,''' +convert(char(20),@i_startdatetime,113) + ''')'

  SELECT @i_period_date_token = 'convert(datetime,''' + convert(char(20),@i_perioddatetime,113) + ''')'

  /* Get Label Generation Alogorith */
  
  SELECT @i_algrthm = ALGRTHM
    FROM CLNDR_TMPLT_ALGRTHM
   WHERE CLNDR_TMPLT_ALGRTHM_ID = @i_chld_cnt_algrthm_id
        
  /* Fix MOD function (SQL Server Only) */

  
  WHILE 1=1
  BEGIN

     SELECT @i_cnt = CHARINDEX('MOD',@i_algrthm,1)
  
     IF @i_cnt = 0 OR @i_cnt IS NULL BREAK

     SELECT @i_algrthm = SUBSTRING(@i_algrthm,1,@i_cnt-1) +
                       SUBSTRING(@i_algrthm,@i_cnt+3,500)
     
     SELECT @i_bracketcnt = -1    
     
     WHILE 1=1
     BEGIN
     
       SELECT @i_testchar = SUBSTRING(@i_algrthm,@i_cnt,1)
       
       IF @i_testchar = '('
         SELECT @i_bracketcnt = @i_bracketcnt + 1
         
       IF @i_testchar = ')'
         SELECT @i_bracketcnt = @i_bracketcnt - 1
         
       IF @i_testchar = ',' AND @i_bracketcnt = 0
       BEGIN

         SELECT @i_algrthm = SUBSTRING(@i_algrthm,1,@i_cnt-1) + '%' +
                           SUBSTRING(@i_algrthm,@i_cnt+1,500)
                           
         BREAK
         
       END
       
       SELECT @i_cnt = @i_cnt + 1
       
       IF @i_cnt > 500
          BREAK
         
     END
  
  END

  /* Replace All YearNumber functions */
  
  WHILE 1=1
  BEGIN

     SELECT @i_cnt = CHARINDEX('YearNumber',@i_algrthm,1)
     
     IF @i_cnt = 0 OR @i_cnt IS NULL BREAK
  
     SELECT @i_end_bracket  = CHARINDEX(')',@i_algrthm,@i_cnt)
     SELECT @i_strt_bracket = CHARINDEX('(',@i_algrthm,@i_cnt)
     
     SELECT @i_algrthm = SUBSTRING(@i_algrthm,1,@i_cnt-1) + 'DatePart(yyyy,' +
                       SUBSTRING(@i_algrthm,@i_strt_bracket+1,@i_end_bracket-@i_strt_bracket-1) + ')' +
   SUBSTRING(@i_algrthm,@i_end_bracket+1,500)     
     
  END
   
  /* Replace All MonthNumber functions */
 
  WHILE 1=1
  BEGIN

SELECT @i_cnt = CHARINDEX('MonthNumber',@i_algrthm,1)
     
     IF @i_cnt = 0 OR @i_cnt IS NULL BREAK
  
     SELECT @i_end_bracket  = CHARINDEX(')',@i_algrthm,@i_cnt)
     SELECT @i_strt_bracket = CHARINDEX('(',@i_algrthm,@i_cnt)
     
     SELECT @i_algrthm = SUBSTRING(@i_algrthm,1,@i_cnt-1) + 'DatePart(mm,' +
                       SUBSTRING(@i_algrthm,@i_strt_bracket+1,@i_end_bracket-@i_strt_bracket-1) + ')' +
                       SUBSTRING(@i_algrthm,@i_end_bracket+1,500)     
     
  END   


  /* Replace All WeekDayNumber functions */
  
  WHILE 1=1
  BEGIN

    SELECT @i_cnt = CHARINDEX('WeekDayNumber',@i_algrthm,1)
     
     IF @i_cnt = 0 OR @i_cnt IS NULL BREAK
  
     SELECT @i_end_bracket  = CHARINDEX(')',@i_algrthm,@i_cnt)
     SELECT @i_strt_bracket = CHARINDEX('(',@i_algrthm,@i_cnt)
     
     SELECT @i_algrthm = SUBSTRING(@i_algrthm,1,@i_cnt-1) + 'DatePart(dw,' +
                       SUBSTRING(@i_algrthm,@i_strt_bracket+1,@i_end_bracket-@i_strt_bracket-1) + ')' +
                       SUBSTRING(@i_algrthm,@i_end_bracket+1,500)     
     
  END
  
    /* Replace All DayNumber functions */
  
  WHILE 1=1
  BEGIN

     SELECT @i_cnt = CHARINDEX('DayNumber',@i_algrthm,1)
     
     IF @i_cnt = 0 OR @i_cnt IS NULL BREAK
  
     SELECT @i_end_bracket  = CHARINDEX(')',@i_algrthm,@i_cnt)
     SELECT @i_strt_bracket = CHARINDEX('(',@i_algrthm,@i_cnt)
     
     SELECT @i_algrthm = SUBSTRING(@i_algrthm,1,@i_cnt-1) + 'DatePart(dd,' +
                         SUBSTRING(@i_algrthm,@i_strt_bracket+1,@i_end_bracket-@i_strt_bracket-1) + ')' +
                         SUBSTRING(@i_algrthm,@i_end_bracket+1,500)     
     
  END
  
  /* Replace Tokens */

  SELECT @i_algrthm = REPLACE(@i_algrthm,'[CalendarStartDate]',@i_start_date_token)

  SELECT @i_algrthm = REPLACE(@i_algrthm,'[CurrentPeriodDate]',@i_period_date_token)

  SELECT @i_algrthm = REPLACE(@i_algrthm,'[ChildSeq]',@i_seq)

  SELECT @i_algrthm = REPLACE(@i_algrthm,'[TotalSeq]',@i_total_seq)

  /* Execute resulting SQL */

  SELECT @i_cmd = 'SELECT @i_chld_cnt = ' + @i_algrthm

  /* Special Hack just for Fixed date calendars */

  IF @i_enddaynumber > 0
  BEGIN
    IF @i_total_seq=1
     BEGIN
      SELECT @ddno  = datepart(dd, @i_perioddatetime)
      IF @ddno > @i_enddaynumber
        SELECT @i_cmd = 'SELECT @i_chld_cnt = ' + @ddno - @i_enddaynumber
      ELSE
        SELECT @i_cmd = 'SELECT @i_chld_cnt = datediff(day,' + @i_period_date_token + ',dateadd(month,1,'+@i_period_date_token+'))'       
     END
    ELSE
     BEGIN
      SELECT @i_cmd = 'SELECT @i_chld_cnt = datediff(day,' + @i_period_date_token + ',dateadd(month,1,'+@i_period_date_token+'))'
     END
  END

  EXEC sp_executesql @i_cmd ,N'@i_chld_cnt integer output', @i_chld_cnt output
  
  RETURN

END
```

