# dbo.spExportWebCouponFilesCancelled

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spExportWebCouponFilesCancelled"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
-- =============================================================================================================
-- Name: spExportWebCouponFiles
--
-- Description: Executes spGenerateWebCouponXML for each of the distinct coupons by Country Code, Discount Amount and Ending Date
--
-- Output: XML File containing coupons and their serialized coupon codes
--
-- Revision History
--		Name:			Date:			Comments:
--		Tim Bytnar	   07/13/2017		   Creation
--	    Ian Wallace	   09/06/2022		   copied proc from kodiak and adjusted it to use new SerializedVoucher table as source
-- =============================================================================================================

CREATE PROCEDURE [dbo].[spExportWebCouponFilesCancelled] 
			@discountID int,
			--@discountAmount varchar(100) = '9.9999',
			--@endingDate varchar(100) = '1-1-2111',
			@cntryAbbr varchar(100) -- = 'ZZ'
AS
BEGIN
	
	SET NOCOUNT ON;

	IF OBJECT_ID('tempdb..#tmpRankedDiscounts') IS NOT NULL DROP TABLE #tmpRankedDiscounts

DECLARE @cmd varchar(8000),
			@currentFileName varchar(100) = NULL,
			@timeStamp varchar(30);

		
set @timeStamp =  
(SELECT FORMAT(GETDATE(), 'yy') +  RIGHT('00' + CONVERT(NVARCHAR(2), DATEPART(MONTH, GETDATE())), 2) + RIGHT('00' + CONVERT(NVARCHAR(2), DATEPART(DAY, GETDATE())), 2)
  + REPLACE(CONVERT(varchar(5), GETDATE(), 108), ':', '') + RIGHT('00' + CONVERT(NVARCHAR(2), DATEPART(ss, GETDATE())), 2) + RIGHT('000' + CONVERT(NVARCHAR(3), DATEPART(ms, GETDATE())), 3))


		SET @currentFileName = @cntryAbbr + '_' + 
							   --@discountAmount + '_' +
							   --CAST(CAST(@endingDate as Date) as varchar(20)) + '_' 
							   --+ 
							   CAST(@discountID as varchar(100)) + '_' + 'CouponDelete' + @timeStamp + '.xml'

		SET @cmd = 'bcp.exe "EXEC [DW].[dbo].[spGenerateWebCouponsXMLcancelled] @discountID = ' + CAST(@discountID as varchar) + ' ,@cntryAbbr = ''' + @cntryAbbr + ''' " queryout \\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Coupons\' + @currentFileName + ' -c -T -C RAW'
		--PRINT @cmd
		EXEC xp_cmdshell @cmd;
END

dbo,usp_FlashGAAPSales5.0_20140724,


CREATE PROC [dbo].[usp_FlashGAAPSales5.0] 
-- =============================================================================================================
-- Name: usp_FlashGAAPSales
--
-- Description:	version for comparison between 4 and 5
--test version

--
-- Input:		@transaction_date		datetime		reporting date
--
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Brad Atkinson	12/3/2007		modified
--		Keith Missey	1/6/2008		added Kim West
--		Keith Missey	3/26/2008		Merch 4.2 Upgrades
--		Keith Missey	4/1/2008		updated stores with zero sales to account for updated store_dim	
--		Keith Missey	4/19/2008		updated line object for VAT calc to mirror line object in GAAP calc	
--		Keith Missey	4/29/2008		added line object 296 for customer service
--		Keith Missey	9/8/2008		updated stores with zero sales e-mail
--		Keith Missey	9/29/2008		updated for addition of France and Ireland stores
--		Keith Missey	10/16/2008		Updated to use dbmail following SQL 2005 upgrade
--		Keith Missey	10/31/2008		updated GAAP line objects
--		Keith Missey	5/18/2009		added line object 102,103 for virtual world
--		Garyd			08/19/2010		Update server name for SA 5.0.
--		Dave Rice		10/11/2010		commented out zero sales email, this has been suplanted by a report from Paul
--		garyd			10/30/2010		test version
--		Mike Pelikan	01/14/2014		Modified email address comments to reduce false positives when looking for
--										exipired users

-- exec [usp_FlashGAAPSales5.0] '2010-10-30'
-- =============================================================================================================
    @transaction_date DATETIME = NULL
AS 

    DECLARE @salesdate DATETIME
    DECLARE @str_salesdate CHAR(8)
    DECLARE @total DECIMAL(12, 4)
    DECLARE @str_message VARCHAR(1000)
    DECLARE @recipients VARCHAR(500)
    DECLARE @recipients_uk VARCHAR(500)
    DECLARE @copy_recipients VARCHAR(500)
    DECLARE @recipients_polling VARCHAR(500)
    DECLARE @subject VARCHAR(100)
    DECLARE @query VARCHAR(8000)
    DECLARE @resultseparator CHAR(1)

    SET @recipients = 'databears@buildabear.com'
    SET @recipients_uk = @recipients + ';databears@buildabear.com'
    SET @copy_recipients = 'databears@buildabear.com'
    SET @recipients_polling = 'databears@buildabear.com'

    SET @resultseparator = CHAR(9)
--set @recipients_uk=@recipients  -- used for testing purposes
--set @copy_recipients='it-data@buildabear.com' -- used for testing purposes
--set @recipients_polling = @recipients -- used for testing purposes

--print @recipients
--print @recipients_uk
--print @copy_recipients

    IF @transaction_date IS NULL 
        BEGIN
            SET @transaction_date = CAST(CONVERT(CHAR(10), GETDATE() - 1, 101) AS DATETIME)
        END

    SET @salesdate = @transaction_date
    SET @str_salesdate = ( SELECT   CONVERT(CHAR(8), @salesdate, 1)
                         )

    IF EXISTS ( SELECT  *
                FROM    sysobjects
                WHERE   id = OBJECT_ID('dbo.tmp_FlashGAAP')
                        AND sysstat & 0xf = 3 ) 
        DROP TABLE dbo.tmp_FlashGAAP
    IF EXISTS ( SELECT  *
                FROM    sysobjects
                WHERE   id = OBJECT_ID('dbo.tmp_VAT')
                        AND sysstat & 0xf = 3 ) 
        DROP TABLE dbo.tmp_VAT
    IF EXISTS ( SELECT  *
                FROM    sysobjects
                WHERE   id = OBJECT_ID('dbo.tmp_ValidateGAAP')
                        AND sysstat & 0xf = 3 ) 
        DROP TABLE dbo.tmp_ValidateGAAP
    IF EXISTS ( SELECT  *
                FROM    sysobjects
                WHERE   id = OBJECT_ID('dbo.tmp_ValidateVat')
                        AND sysstat & 0xf = 3 ) 
        DROP TABLE dbo.tmp_ValidateVat

    SELECT  h.store_no AS 'StoreNo',
            c.store_name AS 'Store Name',
            ( SUM(( (l.gross_line_amount - l.pos_discount_amount) )
                  * l.db_cr_none * l.voiding_reversal_flag) ) * -1 AS 'GAAPSales'
    INTO    dbo.tmp_FlashGAAP
    FROM    POSDbsSA.auditworks.dbo.transaction_header h
            JOIN POSDbsSA.auditworks.dbo.transaction_line l ON h.transaction_id = l.transaction_id
            JOIN POSDbsSA.auditworks.dbo.sv_store c ON h.store_no = c.store_no
    WHERE   ( h.transaction_date = @salesdate
              AND h.transaction_void_flag = 0
              AND h.transaction_category IN ( 1, 2 )
            )
            AND l.line_object IN ( 100, 102,103, 200, 202, 203, 204, 206, 210, 250, 290,
                                   291, 293, 295, 296, 623, 640, 690, 691, 1630, 1631 )
--            AND l.[line_object] IN ( 200, 200, 202, 203, 204, 210, 250, 290, 296,
--                                     291, 640, 690, 1606, 1607, 1610, 1611,
--                                     1612, 1613, 1614, 1616, 1617, 1618, 1621,
--                                     1622, 1623, 1625, 1626, 1627, 1629, 1630,
--                                     1631, 1800, 1801, 1802, 1803, 1804, 1805,
--                                     1806, 1807, 1808, 1809, 1810, 1811, 1900 )
            AND l.line_void_flag = 0
    GROUP BY h.store_no,
            c.store_name
    ORDER BY h.store_no,
            c.store_name

    SELECT  h.store_no AS 'StoreNo',
            h.transaction_id,
            ( SUM(( (l.gross_line_amount - l.pos_discount_amount) )
                  * l.db_cr_none * l.voiding_reversal_flag) ) * -1 AS 'GAAPSales'
    INTO    dbo.tmp_ValidateGAAP
    FROM    POSDbsSA.auditworks.dbo.transaction_header h
            JOIN POSDbsSA.auditworks.dbo.transaction_line l ON h.transaction_id = l.transaction_id
            JOIN POSDbsSA.auditworks.dbo.sv_store c ON h.store_no = c.store_no
    WHERE   ( h.transaction_date = @salesdate
              AND h.transaction_void_flag = 0
              AND h.transaction_category IN ( 1, 2 )
            )
            AND l.line_object IN ( 100, 102,103, 200, 202, 203, 204, 206, 210, 250, 290,
                                   291, 293, 295, 296, 623, 640, 690, 691, 1630, 1631 )
--            AND l.[line_object] IN ( 200, 200, 202, 203, 204, 210, 250, 290, 296,
--                                     291, 640, 690, 1606, 1607, 1610, 1611,
--                                     1612, 1613, 1614, 1616, 1617, 1618, 1621,
--                                     1622, 1623, 1625, 1626, 1627, 1629, 1630,
--                                     1631, 1800, 1801, 1802, 1803, 1804, 1805,
--                                     1806, 1807, 1808, 1809, 1810, 1811, 1900 )
            AND l.line_void_flag = 0
    GROUP BY h.store_no,
            c.store_name,
            h.transaction_id

--CALCULATE TOTAL VAT FOR STORES' SALES
    SELECT  h.store_no AS 'StoreNo',
            SUM(( l.gross_line_amount * CASE [line_action]
                                          WHEN 13 THEN -1
                                          WHEN 21 THEN 1
                                        END )) AS 'VAT'
    INTO    dbo.tmp_VAT
    FROM    POSDbsSA.auditworks.dbo.transaction_header h
            JOIN POSDbsSA.auditworks.dbo.transaction_line l ON h.transaction_id = l.transaction_id
    WHERE   ( h.transaction_date = @salesdate
              AND h.transaction_void_flag = 0
              AND h.transaction_category IN ( 1, 2 )
            )
            AND l.line_object IN ( 1150 )
            AND l.line_void_flag = 0
    GROUP BY h.store_no
    ORDER BY h.store_no

--select * from tmp_VAT return


    SELECT  h.store_no AS 'StoreNo',
            l.transaction_id,
            SUM(( CAST([line_note] AS NUMERIC(9, 2)) * CASE [line_action]
                                                         WHEN 1 THEN -1
                                                         WHEN 2 THEN 1
                                                         WHEN 11 THEN -1
                                                         WHEN 12 THEN 1
                                                       END )) AS VAT
    INTO    dbo.tmp_ValidateVat
    FROM    POSDbsSA.auditworks.dbo.transaction_header h
            INNER JOIN POSDbsSA.auditworks.dbo.transaction_line l ON h.transaction_id = l.transaction_id
            INNER JOIN POSDbsSA.auditworks.dbo.line_note ln ON l.transaction_id = ln.transaction_id
                                                                AND l.line_id = ln.line_id
    WHERE   ( h.transaction_date = @salesdate
              AND h.transaction_void_flag = 0
              AND h.transaction_category IN ( 1, 2 )
            )
            AND (l.line_object IN ( 100, 102,103, 200, 202, 203, 204, 206, 210, 250, 290,
                                   291, 293, 295, 296, 623, 640, 690, 691, 1630, 1631 ))
--            AND ( l.[line_object] IN ( 200, 200, 202, 203, 204, 210, 250, 290, 296,
--                                       291, 640, 690, 1606, 1607, 1610, 1611,
--                                       1612, 1613, 1614, 1616, 1617, 1618,
--                                       1621, 1622, 1623, 1625, 1626, 1627,
--                                       1629, 1630, 1631, 1800, 1801, 1802,
--                                       1803, 1804, 1805, 1806, 1807, 1808,
--                                       1809, 1810, 1811, 1900 ) )
            AND l.line_void_flag = 0
            AND ln.[note_type] = 35
    GROUP BY h.[store_no],
            l.transaction_id
    ORDER BY h.[store_no],
            l.transaction_id

--UPDATE GAAP SALES BY STRIPPING OUT VAT
    UPDATE  tmp_flashgaap
    SET     gaapsales = gaapsales + vat
    FROM    tmp_flashgaap f
            INNER JOIN tmp_vat v ON v.storeno = f.storeno
	
    UPDATE  tmp_ValidateGAAP
    SET     gaapsales = gaapsales + vat
    FROM    tmp_ValidateGAAP f
            INNER JOIN tmp_validatevat v ON v.storeno = f.storeno
                                            AND v.transaction_id = f.transaction_id


select * from tmp_flashgaap
--Canada: where StoreNo IN (119, 124, 130, 136, 150, 174, 177, 188, 204, 205, 215, 217, 228, 229, 250, 269, 270, 279, 280, 282, 283, 293, 303, 995)
--where StoreNo IN (2201, 2202, 2203) --FR
where StoreNo IN (2036, 2054) --IR
return

--N.America--

    SET @total = ( SELECT   SUM(GAAPSales)
                   FROM     dw.dbo.tmp_FlashGAAP
                   WHERE    StoreNo < 1500
                 )

    SET @str_message = ( SELECT 'Attached is the Flash GAAP Sales report at the store level.  

Here is the Flash GAAP Summary info:

Date Range:  ' + @str_salesdate + ' - ' + @str_salesdate + '
GAAP Sales:  ' + CAST(@total AS VARCHAR(20))
                                + '


Please provide Databear Services (it-data@buildabear.com) with any feedback you have with the Report.  (do not reply to SQL Services;  it will not get delivered)'
                       )

    SET @query = 'SET ANSI_WARNINGS OFF 
SET NOCOUNT ON

DECLARE 
@startdt datetime,
@enddt datetime

SET @startdt =  CAST(CONVERT(char(10),' + '''' + @str_salesdate + ''''
        + ',101) as datetime)
SET @enddt =  CAST(CONVERT(char(10),' + '''' + @str_salesdate + ''''
        + ',101) as datetime)

select case when sd.store_id = 473 then 13 else sd.store_id end as store_id
, @startdt as date_beg
, @enddt as date_end
, f.GAAPSales
, case 	when sd.store_id in (13,473) then 9500 
		when sd.store_id =136 then 9400 
		when sd.bearea = ''Canada Stores'' then 8000
		when sd.store_id between 470 and 2900 and sd.store_id not in (480,482,485) then 9999
	else 0 end as ''sortorder''
into ##tmp_FlashGAAP
from dw.dbo.store_dim sd
	left join dw.dbo.tmp_FlashGAAP f on sd.store_id = f.storeno
where sd.store_id between 0 and 1499
order by case when sd.store_id =13 then 9999 else 0 end, store_id 


select store_id, date_beg, date_end, GAAPSales, sortorder
into ##tmpFlashGAAP2
from ##tmp_FlashGAAP
union all 
select  8 , @startdt, @enddt, 0, 0
union all 
select 17 , @startdt, @enddt, 0, 0
union all
select 155, @startdt, @enddt, 0, 0

select CAST(store_id as numeric(4,0)) as Stores_US 
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''
from ##tmpFlashGAAP2
where sortorder =0
group by store_id, 	date_beg, date_end, sortorder
order by sortorder

select CAST(store_id as numeric(4,0)) as Stores_CA
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''		
from ##tmpFlashGAAP2
where sortorder =8000
group by store_id, 	date_beg, date_end, sortorder
order by sortorder

select CAST(store_id as numeric(4,0)) as Stores_Web
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''	
from ##tmpFlashGAAP2
where sortorder in (9400,9500)
group by store_id, 	date_beg, date_end, sortorder
order by sortorder


select CAST(store_id as numeric(4,0)) as Stores_Other
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''	
from ##tmpFlashGAAP2
where sortorder =9999 or sortorder not in (0,8000,9400,9500)
group by store_id, 	date_beg, date_end, sortorder
order by sortorder
'

--exec master..xp_sendmail @recipients=@recipients
--,@copy_recipients=@copy_recipients
--,@subject = 'Flash GAAP Sales from AW'
--,@attach_results = 'TRUE'
--,@separator = @resultseparator
--,@attachments =  'FlashGAAPSales.csv'
--,@ansi_attachment='TRUE'
--,@no_header ='FALSE'
--,@width =80 
--,@message = @str_message
--,@query = @query

/*Remove for testing
    EXEC msdb.dbo.sp_send_dbmail @recipients = @recipients,
        @copy_recipients = @copy_recipients,
        @subject = '5.0 Flash GAAP Sales from AW',
        @attach_query_result_as_file = 'TRUE',
        @query_result_separator = @resultseparator,
        @query_attachment_filename = '50FlashGAAPSales.csv',
        @query_result_header = 'TRUE', @query_result_width = 80,
        @body = @str_message, @query = @query
*/
--UK--

    SET @total = ( SELECT   SUM(GAAPSales)
                   FROM     dw.dbo.tmp_FlashGAAP
                   WHERE    storeNo >= 2000
                 )

    SET @str_message = ( SELECT 'Attached is the Flash Europe GAAP Sales report at the store level.  

Here is the Flash GAAP Summary info:

Date Range:  ' + @str_salesdate + ' - ' + @str_salesdate + '
GAAP Sales:  ' + CAST(@total AS VARCHAR(20))
                                + '


Please provide Databear Services (it-data@buildabear.com) with any feedback you have with the Report.  (do not reply to SQL Services;  it will not get delivered)'
                       )

    SET @query = 'SET ANSI_WARNINGS OFF 
SET NOCOUNT ON

DECLARE 
@startdt datetime,
@enddt datetime

SET @startdt =  CAST(CONVERT(char(10),' + '''' + @str_salesdate + ''''
        + ',101) as datetime)
SET @enddt =  CAST(CONVERT(char(10),' + '''' + @str_salesdate + ''''
        + ',101) as datetime)

select sd.store_id as store_id
, @startdt as date_beg
, @enddt as date_end
, f.GAAPSales
, case when sd.store_id =2013 then 9999 else 0 end as ''sortorder''
into ##tmp_FlashGAAP_UK
from dw.dbo.store_dim sd
	left join dw.dbo.tmp_FlashGAAP f on sd.store_id = f.storeno
where sd.store_id between 2000 and 3000
order by case when sd.store_id =2013 then 9999 else 0 end, store_id 


select store_id, date_beg, date_end, GAAPSales, sortorder
into ##tmpFlashGAAP2_UK
from ##tmp_FlashGAAP_UK



select CAST(store_id as numeric(4,0)) as Stores_Europe 
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''
from ##tmpFlashGAAP2_UK
where sortorder in (0, 9999)
group by store_id,  date_beg, date_end, sortorder
order by sortorder
'

--exec master..xp_sendmail @recipients=@recipients_uk
--,@copy_recipients=@copy_recipients
--,@subject = 'Flash Europe GAAP Sales from AW'
--,@attach_results = 'TRUE'
--,@separator = @resultseparator
--,@attachments =  'FlashEuropeGAAPSales.csv'
--,@ansi_attachment='TRUE'
--,@no_header ='FALSE'
--,@width =80 
--,@message = @str_message
--,@query = @query
/*
    EXEC msdb.dbo.sp_send_dbmail @recipients = @recipients_uk,
        @copy_recipients = @copy_recipients,
        @subject = '5.0 Flash Europe GAAP Sales from AW',
        @attach_query_result_as_file = 'TRUE',
        @query_result_separator = @resultseparator,
        @query_attachment_filename = '50FlashEuropeGAAPSales.csv',
        @query_result_header = 'TRUE'  
--,@query_result_width =80   
        , @body = @str_message, @query = @query
*/

--Ridemakerz--

    SET @total = ( SELECT   SUM(GAAPSales)
                   FROM     dw.dbo.tmp_FlashGAAP
                   WHERE    StoreNo BETWEEN 1500 AND 1599
                 )

    SET @str_message = ( SELECT 'Attached is the Ridemakerz Flash GAAP Sales report at the store level.  

Here is the Flash GAAP Summary info:

Date Range:  ' + @str_salesdate + ' - ' + @str_salesdate + '
GAAP Sales:  ' + CAST(@total AS VARCHAR(20))
                                + '

Please provide Databear Services (it-data@buildabear.com) with any feedback you have with the Report.  (do not reply to SQL Services;  it will not get delivered)'
                       )

    SET @query = 'SET ANSI_WARNINGS OFF 
SET NOCOUNT ON

DECLARE 
@startdt datetime,
@enddt datetime

SET @startdt =  CAST(CONVERT(char(10),' + '''' + @str_salesdate + ''''
        + ',101) as datetime)
SET @enddt =  CAST(CONVERT(char(10),' + '''' + @str_salesdate + ''''
        + ',101) as datetime)

select store_id
, @startdt as date_beg
, @enddt as date_end
, f.GAAPSales
, case 	when sd.store_id in (1513) then 9500 
		when sd.store_id in (1590) then 9999
	else 0 end as ''sortorder''
into ##tmp_FlashGAAP_RZ
from dw.dbo.store_dim sd
	left join dw.dbo.tmp_FlashGAAP f on sd.store_id = f.storeno
where sd.store_id between 1500 and 2000

select CAST(store_id as numeric(4,0)) as Stores_US 
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''
from ##tmp_FlashGAAP_RZ
where sortorder = 0
group by store_id, 	date_beg, date_end, sortorder
order by sortorder

select CAST(store_id as numeric(4,0)) as Stores_Web
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''	
from ##tmp_FlashGAAP_RZ
where sortorder = 9500
group by store_id, 	date_beg, date_end, sortorder
order by sortorder


select CAST(store_id as numeric(4,0)) as Stores_Other
	, CONVERT(char(8),date_beg,1) as ''Begin''
	, CONVERT(char(8),date_end,1) as ''End''
	, CAST(SUM(COALESCE(GAAPSales,0)) as numeric(10,2)) as ''GAAPSales''	
from ##tmp_FlashGAAP_RZ
where sortorder = 9999
group by store_id, 	date_beg, date_end, sortorder
order by sortorder
'

--exec master..xp_sendmail @recipients=@recipients
--,@copy_recipients=@copy_recipients
--,@subject = 'Ridemakerz Flash GAAP Sales from AW'
--,@attach_results = 'TRUE'
--,@separator = @resultseparator
--,@attachments =  'FlashGAAPSales_RZ.csv'
--,@ansi_attachment='TRUE'
--,@no_header ='FALSE'
--,@width =80 
--,@message = @str_message
--,@query = @query

/*remove for testing
    EXEC msdb.dbo.sp_send_dbmail @recipients = @recipients,
        @copy_recipients = @copy_recipients,
        @subject = '5.0 Ridemakerz Flash GAAP Sales from AW',
        @attach_query_result_as_file = 'TRUE',
        @query_result_separator = @resultseparator,
        @query_attachment_filename = '50FlashGAAPSales_RZ.csv',
        @query_result_header = 'TRUE', @query_result_width = 80,
        @body = @str_message, @query = @query
*/

---- validation email for overnight polling consultants
--    SELECT  @subject = 'Stores with ZERO sales for ' + @str_salesdate
--    SET @query = 'select sd.store_id, sd.store_name
--from dw.dbo.store_dim sd
--	left join dw.dbo.tmp_FlashGAAP f on sd.store_id = f.storeno
--where 1=1
--and sd.store_id <= 3000
--and sd.store_id not in (1590, 1591, 1502, 1570, 1580, 1592)
--and f.GAAPSales is null
--and sd.opening_date <= ' + '''' + @str_salesdate + ''''
--        + 'and sd.closing_date is null
--and sd.region not in (''US-Corporate'',''Canada-Corporate'',''Corporate - UK'')
--and sd.bearea not in (''UK - Closed Stores'')
--and sd.region not in (''US Corporate'',''Canada Corporate'',''Corporate UK'')
--and sd.bearea not in (''Closed Stores UK'')
--order by store_id'
--
----exec master..xp_sendmail @recipients=@recipients_polling
----,@copy_recipients=@copy_recipients
----,@subject = @subject
----,@query = @query
--
--    EXEC msdb.dbo.sp_send_dbmail @recipients = @recipients_polling,
--        @subject = @subject, @copy_recipients = @copy_recipients,
--        @query = @query


-- create file with sales info
/* remove for 5.0 testing
    IF ( OBJECT_ID('tmp_edin_GAAPSales') IS NOT NULL ) 
        DROP TABLE tmp_edin_GAAPSales
    SELECT  StoreNo,
            SalesDate,
            SUM(GAAPSales) AS GAAPSales
    INTO    tmp_edin_GAAPSales
    FROM    ( SELECT    CASE WHEN StoreNo IN ( 13, 473 ) THEN 13
                             ELSE StoreNo
                        END AS StoreNo,
                        CONVERT(CHAR(10), @salesdate, 101) AS SalesDate,
                        GAAPSales
              FROM      tmp_FlashGAAP
            ) d
    GROUP BY StoreNo,
            SalesDate
    ORDER BY StoreNo

    EXEC master..xp_cmdshell 'osql -S PAPAMART -d dw -U link_readonly -P l1nkr -s "," -o "\\sharebear1\groups\it\retail systems\polling\flash_gaap\FlashGAAPSales.csv" -Q "select * from tmp_edin_GAAPSales"',
        no_output
*/
```

