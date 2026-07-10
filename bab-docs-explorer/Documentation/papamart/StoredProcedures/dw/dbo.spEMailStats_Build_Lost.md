# dbo.spEMailStats_Build_Lost

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEMailStats_Build_Lost"]
    dbo_CLNSD_GST_DIM(["dbo.CLNSD_GST_DIM"]) --> SP
    date_dim(["date_dim"]) --> SP
    dbo_date_dim(["dbo.date_dim"]) --> SP
    dbo_EMAIL_ADDR_DIM(["dbo.EMAIL_ADDR_DIM"]) --> SP
    dbo_EMAIL_ADDR_PRFRNCE_DIM(["dbo.EMAIL_ADDR_PRFRNCE_DIM"]) --> SP
    dbo_EMAIL_ADDR_PRSNLZTN_ATTR_DIM(["dbo.EMAIL_ADDR_PRSNLZTN_ATTR_DIM"]) --> SP
    dbo_fnDateOnly(["dbo.fnDateOnly"]) --> SP
    SFSCube_EMail_DaysSinceAcquisition_Dim(["SFSCube_EMail_DaysSinceAcquisition_Dim"]) --> SP
    SFSCube_EMail_Lost(["SFSCube_EMail_Lost"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CLNSD_GST_DIM |
| date_dim |
| dbo.date_dim |
| dbo.EMAIL_ADDR_DIM |
| dbo.EMAIL_ADDR_PRFRNCE_DIM |
| dbo.EMAIL_ADDR_PRSNLZTN_ATTR_DIM |
| dbo.fnDateOnly |
| SFSCube_EMail_DaysSinceAcquisition_Dim |
| SFSCube_EMail_Lost |

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spEMailStats_Build_Lost
--
-- Description:	
--		This procedure will generate the number of email records that were lost due to Bounce, ... for the last n days
--		
-- Input:
--		numDays - This is the number of days to go back from the current date to rebuild information
--
-- Output: 
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec dw.dbo.spEMailStats_Build_Lost @numDays=5
--
-- Revision History
--		Name:				Date:			Comments:
--		Gary Murrish		6/16/2011		created
-- =============================================================================================================
CREATE PROCEDURE dbo.spEMailStats_Build_Lost
-- These are the number of days to go back and regenerate information
@numDays INT = 5
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE
	   @effDate DATETIME;
	SET @effDate = DATEADD(d, -1 * @numDays, dbo.fnDateOnly(GETDATE()));

	DECLARE
	   @effDate_Key INT;
	SET @effDate_Key = (SELECT
							   date_key
						  FROM date_dim WITH (NOLOCK)
						  WHERE actual_date = @effDate);

	--TRUNCATE TABLE queries..SFSCube_EMail_Lost

	DELETE FROM queries..SFSCube_EMail_Lost
	  WHERE
			date_key >= @effDate_Key;

	INSERT INTO queries..SFSCube_EMail_Lost(
				date_key
			  , EMAIL_STAT_CD
			  , ORIG_SRC_SYS_CD
			  , daysSinceID
			  , isSFSMember
			  , CNTRY_ABBRV
			  , numEmailsLost
			  , numDaysSinceAcquisition)
	SELECT
		   BASE.date_key
		 , BASE.EMAIL_STAT_CD
		 , BASE.ORIG_SRC_SYS_CD
		 , DYA.daysSinceID
		 , base.isSFSMember
		 , base.CNTRY_ABBRV
		 , COUNT(*)AS numEMailsLost
		 , SUM(CASE
			   WHEN base.DaysSinceAcquisition < 0 THEN 0
				   ELSE base.DaysSinceAcquisition
			   END)AS numDaysSinceAcquisition
	  FROM
		  (
		   SELECT
				  DTE.date_key
				, em.EMAIL_STAT_CD
				, prf.ORIG_SRC_SYS_CD
				, DATEDIFF(DAY, em.INS_DT, em.EMAIL_STAT_DT)AS DaysSinceAcquisition
				, CASE
				  WHEN LEN((
		   SELECT
				  MIN(LYLTY_GST_NBR)AS LYLTY_GST_NBR
			 FROM dbo.CLNSD_GST_DIM GSTR WITH (NOLOCK)
			 WHERE GSTR.EMAIL_ADDR_ID = em.EMAIL_ADDR_ID
			 GROUP BY
					  GSTR.EMAIL_ADDR_ID)) > 0 THEN 1
					  ELSE 0
				  END AS isSFSMember
				, ISNULL(PERS.CNTRY_ABBRV, 'USA')AS CNTRY_ABBRV
			 FROM
				  dbo.EMAIL_ADDR_DIM EM WITH (NOLOCK)
				  INNER JOIN dbo.date_dim DTE WITH (NOLOCK)
					  ON DTE.actual_date = dbo.fnDateOnly(EM.EMAIL_STAT_DT)
				  INNER JOIN dbo.EMAIL_ADDR_PRSNLZTN_ATTR_DIM PERS WITH (NOLOCK)
					  ON PERS.EMAIL_ADDR_ID = EM.EMAIL_ADDR_ID
				  INNER JOIN dbo.EMAIL_ADDR_PRFRNCE_DIM PRF WITH (NOLOCK)
					  ON EM.EMAIL_ADDR_ID = PRF.EMAIL_ADDR_ID
			 WHERE EMAIL_STAT_CD <> 'Valid'
			   AND em.email_stat_dt >= @effDate)AS BASE
		  INNER JOIN queries..SFSCube_EMail_DaysSinceAcquisition_Dim DYA WITH (NOLOCK)
			  ON BASE.DaysSinceAcquisition BETWEEN DYA.minDays
			 AND DYA.maxDays
	  WHERE 1 = 1
	  GROUP BY
			   BASE.date_key
			 , BASE.EMAIL_STAT_CD
			 , BASE.ORIG_SRC_SYS_CD
			 , base.CNTRY_ABBRV
			 , DYA.daysSinceID
			 , base.isSFSMember
	  ORDER BY
			   BASE.date_key, BASE.EMAIL_STAT_CD, BASE.ORIG_SRC_SYS_CD, base.CNTRY_ABBRV, DYA.daysSinceID, base.isSFSMember;

-- Took 3:55 Minutes		   
END;
```

