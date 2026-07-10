# dbo.usp_get_bearbirthcert

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.usp_get_bearbirthcert"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROC [dbo].[usp_get_bearbirthcert]
-- =============================================================================================================
-- Name: usp_get_bearbirthcert
--
-- Description:	retrieves bear birth certificate information
--
-- Input:	@bearid		nvarchar(25)
--			@email		varchar(255)
--			@firstname	nvarchar(50)
--			@lastname	nvarchar(50)
--			@address	nvarchar(50)
--		    @city		NVARCHAR(50)
--			@state		NVARCHAR(50)
--			@zipcode	nvarchar(50)
--			@year		int
--
-- Output: Resultset containing following columns
--		SKU, product description, bear name, bear birth date, owner first name, owner last name
--		sender first name, sender last name, bear id
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Missey	9/27/2007		Created
--		GaryD			11/2/2009		Remove references to tblimportkioskdata.  Make parameters optional.
--		GaryD			11/16/2009		Remove references to recipient address
/*
exec usp_get_bearbirthcert
    @bearid = '0147830634624' --NULL --'Sophie' --NVARCHAR(25) = NULL,
    ,@email = 'DERIKITO@sbcglobal.net' --'GaryD@BAB.com' -- NVARCHAR(50) = NULL,
    ,@firstname = 'SHELBY' --= NULL --'Gary' --NVARCHAR(50) = NULL,
    ,@lastname = 'DERIKITO' -- NVARCHAR(50) = NULL,
    ,@address = '5 beaver ridge ct'--= NULL---'5 B' --NVARCHAR(50) = NULL,
    ,@city = 'st. peters' --= NULL--'St. Petes' -- NVARCHAR(50) = NULL,
    ,@state = 'Missouri (MO)'-- NULL--'MO' -- NVARCHAR(50) = NULL,
    ,@zipcode = 63376 --= NULL--'63555' --NVARCHAR(50) = NULL,
    ,@year = 2009 -- = NULL--2000 -- INT = NULL

*/
-- =============================================================================================================
    @bearid NVARCHAR(25) = NULL,
    @email NVARCHAR(50) = NULL,
    @sfsnum INT = NULL,
    @firstname NVARCHAR(50) = NULL,
    @lastname NVARCHAR(50) = NULL,
    @address NVARCHAR(50) = NULL,
    @city NVARCHAR(50) = NULL,
    @state NVARCHAR(50) = NULL,
    @zipcode NVARCHAR(50) = NULL
--    @year INT = NULL
AS 

--DECLARE 
--    @bearid NVARCHAR(25),
--    @email NVARCHAR(50),
--    @firstname NVARCHAR(50),
--    @lastname NVARCHAR(50),
--    @address NVARCHAR(50),
--    @city NVARCHAR(50),
--    @state NVARCHAR(50),
--    @zipcode NVARCHAR(50),
--    @year INT
    
--SELECT @bearid  = NULL,
--    @email  = NULL,
--    @firstname  = 'Benjamin',
--    @lastname = 'Barud',
--    @address  = NULL,
--    @city  = NULL,
--    @state  = NULL,
--    @zipcode  = NULL,
--    @year = NULL

DECLARE @CMD NVARCHAR(4000)
DECLARE @CMD1 NVARCHAR(4000)
DECLARE @WHERE1 NVARCHAR(2000)
DECLARE @GROUP1 NVARCHAR(1000)
DECLARE @CMD2 NVARCHAR(4000)
DECLARE @WHERE2 NVARCHAR(2000)
DECLARE @GROUP2 NVARCHAR(1000)


--HAVE TO DYNAMICALLY CREATE WHERE CLAUSE BASED ON INCOMING PARAMETERS

--Remember to remove the indexes from tblimportkioskdata!

SET @CMD1 = 
--'SELECT  CONVERT(VARCHAR, drstarttime, 111) AS regdate,
--							sranimalid AS SKU,
--                            product_desc AS [Product],
--                            sranimalname AS [Bear Name],
--                            CONVERT(VARCHAR,sranimalbirthdate,111) AS [Birth Date],
--                            srfirstname AS [Owner First Name],
--                            SRLastname AS [Owner Last Name],
--                            ssfirstname AS [Sender First Name],
--                            sslastname AS [Sender Last Name],
--                            srbarcodenumber AS [Bear ID],
--                            pin AS [Key Code],
--                            MAX(id) as id
--                    FROM    babw.dbo.tblcustomerrecipient (NOLOCK) 
--		LEFT JOIN papamart.dw.dbo.product_dim ON sranimalid = sku	'
'SELECT     tkf.TKF_ID, CONVERT(VARCHAR
			,tkf.KSK_REGIS_START_DT, 111) AS [Date Entered]
			,prod.sku AS SKU, prod.product_desc AS Product
			,tkf.ANML_NM AS [Bear Name]
			,CONVERT(VARCHAR, tkf.ANML_BRTH_DT, 111) AS [Birth Date]
			,NULLIF (rr.FRST_NM, ' + '''' + 'Rcpnt_Frst_Nm' + '''' + ') AS [Owner First Name]
			,NULLIF (rr.LAST_NM, ' + '''' + 'Rcpnt_Last_Nm' + '''' + ') AS [Owner Last Name]
			,cg.FRST_NM AS [Sender First Name]
			,cg.LAST_NM AS [Sender Last Name]
			,cg.LYLTY_GST_NBR AS [SFS Num]
			,tkf.ANML_BARCD_NBR AS [Bear ID]
			,m.pin AS [Key Code]
			,tkf.TKF_ID AS ID
FROM         TRN_KSK_FACT tkf WITH (NOLOCK)
					LEFT JOIN product_dim prod WITH (NOLOCK) ON tkf.PRDCT_ID = prod.product_key
					LEFT JOIN TKF_CLNSD_GST_BRDG cgb WITH (NOLOCK) ON cgb.TKF_ID = tkf.TKF_ID
					LEFT JOIN CLNSD_GST_DIM cg WITH (NOLOCK) on cgb.CLNSD_GST_ID = cg.CLNSD_GST_ID
					LEFT JOIN EMAIL_ADDR_DIM ea WITH (NOLOCK) ON cg.EMAIL_ADDR_ID = ea.EMAIL_ADDR_ID					 
					LEFT JOIN CLNSD_ADDR_DIM ca WITH (NOLOCK) ON cg.CLNSD_ADDR_ID = ca.CLNSD_ADDR_ID
					LEFT JOIN RAW_RCPNT_DIM rr WITH (NOLOCK) ON tkf.RAW_RCPNT_ID = rr.RAW_RCPNT_ID
					INNER JOIN mamamart.babw.dbo.tblcustomerrecipient m WITH (NOLOCK) ON tkf.TRN_NBR = m.id'
	
SET @WHERE1 = ''
IF @bearid IS NOT NULL
	SET @WHERE1 = @WHERE1 + 'AND tkf.ANML_BARCD_NBR = @bearid '
IF @email IS NOT NULL
	SET @WHERE1 = @WHERE1 + 'AND ea.EMAIL_ADDR_TXT = @email '
IF @sfsnum IS NOT NULL
	SET @WHERE1 = @WHERE1 + 'AND cg.LYLTY_GST_NBR = @sfsnum '
--IF @year IS NOT NULL
--	SET @WHERE1 = @WHERE1 + 'AND YEAR(drstarttime) = CAST(@year AS VARCHAR) '
IF @firstname IS NOT NULL
	SET @WHERE1 = @WHERE1 + 'AND (cg.FRST_NM = @firstname) '
IF LTRIM(ISNULL(@lastname,'')) <> ''
	SET @WHERE1 = @WHERE1 + 'AND (cg.LAST_NM = @lastname) '
IF @address IS NOT NULL
	--SET @WHERE = @WHERE + 'AND ((LEFT(ssaddress1 + (COALESCE(' + ''' ''' + ' + '+ ' ssaddress2, ' + '''''' + ')), LEN(@address)) = @address) OR (LEFT(sraddress1 + (COALESCE(' + ''' ''' +  ' +  sraddress2, ' + '''''' + ')), LEN(@address)) = @address)) '
	SET @WHERE1 = @WHERE1 + 'AND ((LEFT(ca.ADDR_LN_1_TXT + (COALESCE(' + ''' ''' + ' + '+ ' ca.ADDR_LN_2_TXT, ' + '''''' + ')), LEN(@address)) = @address)) '
IF @city IS NOT NULL
	--SET @WHERE = @WHERE + 'AND ((sscity = @city) OR (srcity = @city)) '
	SET @WHERE1 = @WHERE1 + 'AND ((ca.CTY_NM = @city)) '
IF @state IS NOT NULL
	--SET @WHERE = @WHERE + 'AND ((ssstate = @state) OR (srstate = @state)) '
	--SET @WHERE1 = @WHERE1 + 'AND (ca.ST_PRVNC_NM = @state OR ca.ST_PRVNC_ABBRV = @state) '
	SET @WHERE1 = @WHERE1 + 'AND (ca.ST_PRVNC_ABBRV = @state) '
IF @zipcode IS NOT NULL
	--SET @WHERE = @WHERE + 'AND ((sspostcode = @zipcode) OR (srpostcode = @zipcode)) '
	SET @WHERE1 = @WHERE1 + 'AND ((ca.PSTL_CD = @zipcode)) '
SET @GROUP1 = 
' GROUP BY CONVERT(VARCHAR, tkf.KSK_REGIS_START_DT, 111)
, prod.sku
, prod.product_desc
, tkf.ANML_NM
, CONVERT(VARCHAR, tkf.ANML_BRTH_DT, 111)
, rr.FRST_NM
, rr.LAST_NM
, cg.FRST_NM
, cg.LAST_NM
, tkf.ANML_BARCD_NBR
, m.pin
, cg.LYLTY_GST_NBR
, tkf.TKF_ID'

SET @CMD2 = 
'SELECT     tkf.TKF_ID, CONVERT(VARCHAR
			,tkf.KSK_REGIS_START_DT, 111) AS [Date Entered]
			,prod.sku AS SKU, prod.product_desc AS Product
			,tkf.ANML_NM AS [Bear Name]
			,CONVERT(VARCHAR, tkf.ANML_BRTH_DT, 111) AS [Birth Date]
			,NULLIF (rr.FRST_NM, ' + '''' + 'Rcpnt_Frst_Nm' + '''' + ') AS [Owner First Name]
			,NULLIF (rr.LAST_NM, ' + '''' + 'Rcpnt_Last_Nm' + '''' + ') AS [Owner Last Name]
			,cg.FRST_NM AS [Sender First Name]
			,cg.LAST_NM AS [Sender Last Name]
			,cg.LYLTY_GST_NBR AS [SFS Num]
			,tkf.ANML_BARCD_NBR AS [Bear ID]
			,m.pin AS [Key Code]
			,tkf.TKF_ID AS ID
FROM         TRN_KSK_FACT tkf WITH (NOLOCK)
					LEFT JOIN product_dim prod WITH (NOLOCK) ON tkf.PRDCT_ID = prod.product_key
					LEFT JOIN TKF_CLNSD_GST_BRDG cgb WITH (NOLOCK) ON cgb.TKF_ID = tkf.TKF_ID
					LEFT JOIN CLNSD_GST_DIM cg WITH (NOLOCK) on cgb.CLNSD_GST_ID = cg.CLNSD_GST_ID
					LEFT JOIN EMAIL_ADDR_DIM ea WITH (NOLOCK) ON cg.EMAIL_ADDR_ID = ea.EMAIL_ADDR_ID					 
					LEFT JOIN CLNSD_ADDR_DIM ca WITH (NOLOCK) ON cg.CLNSD_ADDR_ID = ca.CLNSD_ADDR_ID
					LEFT JOIN RAW_RCPNT_DIM rr WITH (NOLOCK) ON tkf.RAW_RCPNT_ID = rr.RAW_RCPNT_ID
					INNER JOIN mamamart.babw.dbo.tblcustomerrecipient m WITH (NOLOCK) ON tkf.TRN_NBR = m.id'
	
SET @WHERE2 = ''
IF @email IS NOT NULL
	SET @WHERE2= @WHERE2 + 'AND rr.EMAIL_ADDR_TXT = @email '
--IF @year IS NOT NULL
--	SET @WHERE2 = @WHERE2 + 'AND YEAR(drstarttime) = CAST(@year AS VARCHAR) '
IF @firstname IS NOT NULL
	SET @WHERE2 = @WHERE2 + 'AND (rr.FRST_NM = @firstname) '
IF @lastname IS NOT NULL
	SET @WHERE2 = @WHERE2 + 'AND (rr.LAST_NM = @lastname) '
IF @address IS NOT NULL
	SET @WHERE2 = @WHERE2 + 'AND ((LEFT(rr.ADDR_LN_1_TXT + (COALESCE(' + ''' ''' + ' + '+ ' rr.ADDR_LN_2_TXT, ' + '''''' + ')), LEN(@address)) = @address)) '
IF @city IS NOT NULL
	SET @WHERE2 = @WHERE2 + 'AND ((rr.CTY_NM = @city)) '
IF @state IS NOT NULL
	--SET @WHERE2 = @WHERE2 + 'AND ((rr.ST_PRVNC_TXT = @state)) '
	SET @WHERE2 = @WHERE2 + 'AND ((rr.ST_PRVNC_TXT LIKE ' + '''%' + @state + '%''' + ')) '
IF @zipcode IS NOT NULL
	SET @WHERE2 = @WHERE2 + 'AND ((rr.PSTL_CD = @zipcode)) '
SET @GROUP2 = 
' GROUP BY CONVERT(VARCHAR, tkf.KSK_REGIS_START_DT, 111)
, prod.sku
, prod.product_desc
, tkf.ANML_NM
, CONVERT(VARCHAR, tkf.ANML_BRTH_DT, 111)
, rr.FRST_NM
, rr.LAST_NM
, cg.FRST_NM
, cg.LAST_NM
, tkf.ANML_BARCD_NBR
, m.pin
, cg.LYLTY_GST_NBR
, tkf.TKF_ID'

IF LEN (@WHERE1) > 0
	SET @CMD1 = @CMD1 + ' WHERE ' + RIGHT(@WHERE1, LEN(@WHERE1) - 3) + @GROUP1--cut off leading AND
--select @CMD
IF LEN (@WHERE2) > 0
	SET @CMD2 = @CMD2 + ' WHERE ' + RIGHT(@WHERE2, LEN(@WHERE2) - 3) + @GROUP2--cut off leading AND
	
IF LEN (@WHERE2) > 0
	SET @CMD = @CMD1 + ' UNION ' + @CMD2
ELSE
	SET @CMD = @CMD1
--select @CMD
EXEC sp_executesql @CMD
						, N'@bearid NVARCHAR(25)
							,@email NVARCHAR(50)
							,@sfsnum INT
							,@firstname NVARCHAR(50)
							,@lastname NVARCHAR(50)
							,@address NVARCHAR(50)
							,@city NVARCHAR(50)
							,@state NVARCHAR(50)
							,@zipcode NVARCHAR(50)'
--							,@year INT' 
							,@bearid = @bearid
							,@email = @email
							,@sfsnum = @sfsnum
							,@firstname = @firstname
							,@lastname = @lastname
							,@address = @address
							,@city = @city
							,@state = @state
							,@zipcode = @zipcode
--							,@year = @year
```

