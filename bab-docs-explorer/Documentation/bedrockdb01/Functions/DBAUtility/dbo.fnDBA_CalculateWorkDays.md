# dbo.fnDBA_CalculateWorkDays

**Database:** DBAUtility  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** int(4)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDBA_CalculateWorkDays"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @StartDate | datetime | 8 | NO |
| @EndDate | datetime | 8 | NO |
| @bolAbsolute | bit | 1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[fnDBA_CalculateWorkDays]
/***************************************************************************************

FROM http://www.sqlservercentral.com/articles/Advanced+Querying/calculatingworkdays/1660/

 Purpose:
 1.  Given any valid start date and end date, this function will calculate and return
     the number of workdays (Mon - Fri).
 2.  Given only a valid start date (end date has DEFAULT in it), this function will
     return a 1 if the start date is a weekday and a 0 if not a weekday.

 Usage:
 1. MASTER.dbo.fn_WorkDays(@StartDate,@EndDate)
 2. MASTER.dbo.fn_WorkDays(@StartDate,DEFAULT)    --Always returns 1 or 0
 3. MASTER.dbo.fn_WorkDays(@EndDate,@StartDate)
 4. MASTER.dbo.fn_WorkDays(@StartDate,@StartDate) --Always returns 1 or 0
 5. MASTER.dbo.fn_WorkDays(@EndDate,@EndDate)     --Always returns 1 or 0

 Notes:
 1.  Holidays are NOT considered.
 2.  Because of the way SQL Server calculates weeks and named days of the week, no
     special consideration for the value of DATEFIRST is given.  In other words, it
     doesn't matter what DATEFIRST is set to for this function.
 3.  If the input dates are in the incorrect order, they will be reversed prior to any
     calculations.
 4.  Only whole days are considered.  Times are NOT used.
 5.  The number of workdays INCLUDES both dates
 6.  Inputs may be literal representations of dates, datetime datatypes, numbers that
     represent the number of days since 1/1/1900 00:00:00.000, or anything else that can
     be implicitly converted to or already is a datetime datatype.
 7.  Undocumented: The DATEPART(dw,date) does not actually count weeks... It counts the
     transition to a Sunday regardless of the DATEFIRST setting.  In essence, it counts
     only whole weekends in any given date range.
 8.  This UDF does NOT create a tally table or sequence table to operate.  Not only is
     it set based, it is truly "tableless".

 Error Indications:
 1.  If either the @StartDate or the @EndDate parameter is an invalid date, the
     following error is returned...
     "Server: Msg 242, Level 16, State 3, Line 3
      The conversion of a char data type to a datetime data type resulted in an
      out-of-range datetime value."
 2.  If either the @StartDate or the @EndDate parameter is a string not resembling a
     date, the following error is returned...
     "Server: Msg 241, Level 16, State 1, Line 3
      Syntax error converting datetime from character string."
 3.  If only one parameter is passed, the following error is returned...
     "Server: Msg 313, Level 16, State 2, Line 3
      An insufficient number of arguments were supplied for the procedure or
      function MASTER.dbo.fn_WorkDays."

 Revisions:
 Rev 00 - 12/12/2004 - Jeff Moden - Initial creation and test.
 Rev 01 - 12/12/2004 - Jeff Moden - Load test, cleanup, document, release.
 Rev 02 - 12/26/2004 - Jeff Moden - Return NULL if @StartDate is NULL or DEFAULT and
                                    modify to be insensitive to DATEFIRST settings.
 Rev 03	- 08/19/2014 - Mike Pelikan - Added @bolAbsolute logic
***************************************************************************************/
--======================================================================================
--      Presets
--======================================================================================
--===== Define the input parameters (ok if reversed by mistake)
        (
         @StartDate DATETIME,
         @EndDate   DATETIME = NULL, --@EndDate replaced by @StartDate when DEFAULTed
        @bolAbsolute bit = 1)

--===== Define the output data type
RETURNS INT

AS
--======================================================================================
--      Calculate the RETURN of the function
--======================================================================================
  BEGIN
        --===== Declare local variables
        --Temporarily holds @EndDate during date reversal
        DECLARE @Swap DATETIME

        --===== If the Start Date is null, return a NULL and exit
             IF @StartDate IS NULL
                RETURN NULL

        --===== If the End Date is null, populate with Start Date value
             -- so will have two dates (required by DATEDIFF below)
             IF @EndDate IS NULL
                SELECT @EndDate = @StartDate

        --===== Strip the time element from both dates (just to be safe) by converting
             -- to whole days and back to a date.  Usually faster than CONVERT.
             -- 0 is a date (01/01/1900 00:00:00.000)
         SELECT @StartDate = DATEADD(dd,DATEDIFF(dd,0,@StartDate),0),
                @EndDate   = DATEADD(dd,DATEDIFF(dd,0,@EndDate)  ,0)

		IF @bolAbsolute = 1
		BEGIN
        --===== If the inputs are in the wrong order, reverse them
             IF @StartDate > @EndDate
                SELECT @Swap      = @EndDate,
                       @EndDate   = @StartDate,
                       @StartDate = @Swap
		END
        --===== Calculate and return the number of workdays using the
             -- input parameters.  This is the meat of the function.
             -- This is really just one formula with a couple of parts
             -- that are listed on separate lines for documentation
             -- purposes.
         RETURN (
                SELECT
              --Start with total number of days including weekends
                (DATEDIFF(dd,@StartDate,@EndDate)+1)

              --Subtact 2 days for each full weekend
               -(DATEDIFF(wk,@StartDate,@EndDate)*2)

              --If StartDate is a Sunday, Subtract 1
               -(CASE WHEN DATENAME(dw,@StartDate) = 'Sunday'
                      THEN 1
                      ELSE 0
                  END)

              --If EndDate is a Saturday, Subtract 1
               -(CASE WHEN DATENAME(dw,@EndDate) = 'Saturday'
                      THEN 1
                      ELSE 0
                  END)
                )
    END
```

