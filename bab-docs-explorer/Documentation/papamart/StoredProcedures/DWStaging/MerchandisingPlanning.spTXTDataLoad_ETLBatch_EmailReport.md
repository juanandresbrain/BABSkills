# MerchandisingPlanning.spTXTDataLoad_ETLBatch_EmailReport

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["MerchandisingPlanning.spTXTDataLoad_ETLBatch_EmailReport"]
    dbo_sp_sEND_dbmail(["dbo.sp_sEND_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_sEND_dbmail |

## Stored Procedure Code

```sql
CREATE PROCEDURE [MerchandisingPlanning].[spTXTDataLoad_ETLBatch_EmailReport]
@ETLBatchID INT
AS

BEGIN

    /**

        Convert's the specified table or view into an html table and emails it to Admin Group. 
        Brian Byas


    **/
    DECLARE @subject nvarchar(max),
            @body    nvarchar(max),
			@body1    nvarchar(max),
			@body2    nvarchar(max),
			@email   nvarchar(max);


------------------------------------------------------------------------- 
-- Get Store Load Errors
-------------------------------------------------------------------------


    --  Get columns for table headers..
	

    EXEC( '

    DECLARE col_cur cursor for

        SELECT CASE 
		WHEN NAME = ''address'' THEN ''ADDRESS''
		WHEN NAME = ''STR_NUM'' THEN ''STORE'' END AS NAME
		FROM papamart.dwstaging.sys.columns
        WHERE object_id = 1933458162
        AND NAME in (''STR_NUM'',''address'')

        ' )

 

    OPEN col_cur
------------------------------------------------------------------------- 
-- HTML Header
------------------------------------------------------------------------- 

    DECLARE @col_name sysname
    DECLARE @col_list nvarchar(max)
    FETCH NEXT FROM col_cur into @col_name
    SET @body = N'<table border=1 cellpadding=1 cellspacing=1><tr>'
    WHILE @@fetch_status = 0
    BEGIN

        SET @body = cast( @body as nvarchar(max) ) 

                  + N'<th>' + @col_name + '</th>'

        SET @col_list = coalesce( @col_list + ',', '' ) + ' td = ' + cast( @col_name as nvarchar(max) ) + ', ''''' 

        FETCH NEXT FROM col_cur into @col_name

 

    END

 

    DEALLOCATE col_cur
------------------------------------------------------------------------- 
-- HTML Footer & Query
------------------------------------------------------------------------- 
 SET @body = cast( @body as nvarchar(max) ) 

              + '</tr>'



    DECLARE @query_result nvarchar(max)

    DECLARE @nsql nvarchar(max)

 

    --  Form the query, use XML PATH to get the HTML

    SET @nsql = '

        select @qr = 
CAST(( SELECT 	
( SELECT CAST(ISNULL(l.location_code,RIGHT (''000'' + CONVERT(VARCHAR,VW.STR_NUM),4)) + '' '' + ISNULL(l.location_name,vw.str_name) AS NVARCHAR(40)) FOR XML Path (''td''),type)
,( SELECT CAST(ISNULL(a.address_line1 + ''  '' +  ISNULL(a.address_line2,''''),VW.ADDRESS) AS NVARCHAR(512)) FOR  XML Path (''td''),type)
FROM BEDROCKDB02.me_01.dbo.location l WITH (NOLOCK)
		INNER JOIN BEDROCKDB02.me_01.dbo.address a WITH (NOLOCK)
			ON l.location_id = a.parent_id 
				AND a.parent_type = 2 
				AND a.address_type_id = 1
		INNER JOIN BEDROCKDB02.me_01.dbo.country c WITH(NOLOCK)
			ON a.country_id = c.country_id
		INNER JOIN BEDROCKDB02.me_01.dbo.currency cu WITH(NOLOCK)
			ON c.currency_id = cu.currency_id
		INNER JOIN BEDROCKDB02.me_01.dbo.location_group lg WITH(NOLOCK)
			ON l.location_id = lg.location_id
		INNER JOIN bedrockdb02.dw_mirror.dbo.store_dim s WITH(NOLOCK)
			ON l.location_code = s.store_id
		FULL OUTER JOIN papamart.dwstaging.[MerchandisingPlanning].[vwStoreDataForTXT] VW WITH(NOLOCK)
			ON l.location_code = RIGHT(''000'' + CAST(VW.STR_NUM AS VARCHAR(4)), 4)
		LEFT OUTER JOIN BEDROCKDB02.[TXTStaging].[lookup].[MerchandisingPlanningLocationHierarchy] gw WITH(NOLOCK)
			ON VW.STR_NUM = gw.code or L.location_code = gw.CODE
	WHERE GW.CHANNEL IS NULL


                       for xml path( ''tr'' ), type

                       ) as nvarchar(max) )'

 

    EXEC sp_EXECutesql @nsql, N'@qr nvarchar(max) output', @query_result output


    SET @body = cast( @body as nvarchar(max) )

              + @query_result
	SET @body1 = @body + cast( '</table>' as nvarchar(max) )
------------------------------------------------------------------------- 
-- Get Measure Errors
-------------------------------------------------------------------------


    --  Get columns for table headers..

    EXEC( '

    DECLARE col_cur cursor for

        SELECT CASE 
   WHEN NAME = ''BatchParameter_FiscalYear'' THEN ''FiscalYear''
   WHEN NAME = ''BatchParameter_FiscalWeek'' THEN ''FiscalWeek'' 
   ELSE NAME END AS NAME
        FROM papamart.dwstaging.sys.columns
        WHERE object_id = 184700056
        AND Name in (''MeasureName'',
					''LocationCount'',
					''ProductCount'',
					''BatchParameter_FiscalYear'',
					''BatchParameter_FiscalWeek'')
        ' )

 

    OPEN col_cur

------------------------------------------------------------------------- 
-- HTML Header
------------------------------------------------------------------------- 

    FETCH NEXT FROM col_cur into @col_name
    SET @body = N'<table border=1 cellpadding=1 cellspacing=1><tr>'
    WHILE @@fetch_status = 0
    BEGIN

        SET @body = cast( @body as nvarchar(max) ) 

                  + N'<th>' + @col_name + '</th>'

 

        SET @col_list = coalesce( @col_list + ',', '' ) + ' td = ' + cast( @col_name as nvarchar(max) ) + ', ''''' 
		--SET @col_list = coalesce( '' + ',', '' ) + ' td = ' + cast( '' as nvarchar(max) ) + ', ''''' 
 

        FETCH NEXT FROM col_cur into @col_name

    END


    DEALLOCATE col_cur

------------------------------------------------------------------------- 
-- HTML Footer & Query
-------------------------------------------------------------------------

    SET @body = cast( @body as nvarchar(max) ) 

              + '</tr>'

 

    --  Form the query, use XML PATH to get the HTML

    SET @nsql = '
        select @qr = 
				CAST( (  SELECT ( SELECT REPLACE(REPLACE(SUBSTRING([MeasureName],40,90),''_SingleFiscalWeek_Value_Validation]'',''''),''_SingleFiscalWeek_Validation]'','''') FOR  XML Path (''td''),type) 
			,( SELECT  [LocationCount] FOR  XML Path (''td''),type)
			,( SELECT  [ProductCount] FOR  XML Path (''td''),type)
			,( SELECT  [BatchParameter_FiscalYear] AS FiscalYear FOR  XML Path (''td''),type)
			,( SELECT  [BatchParameter_FiscalWeek] AS FiscalWeek FOR  XML Path (''td''),type)
			FROM [DWStaging].[MerchandisingPlanning].[TXTDataLoad_ValidationEmailDetailLog]
			WHERE ETLBatchID = ' + CONVERT(VARCHAR,@ETLBatchID) +'
			AND (LocationCount != 0 OR ProductCount != 0)

                       for xml path( ''tr'' ), type

                       ) as nvarchar(max) )'

 

    EXEC sp_EXECutesql @nsql, N'@qr nvarchar(max) output', @query_result output

    SET @body = cast(@body as nvarchar(max))
              + @query_result
	
	

	SET @body2 = @body + cast( '</table>' as nvarchar(max) )
	
	
------------------------------------------------------------------------- 
-- SEND Email
-------------------------------------------------------------------------

    --  SEND notification

    SET @subject = 'TXTDataLoad Summary'

	
	SET @body2 = 'These Stores need MDM information' + @body1 + '<br>'+ 'These Measures had Validation violations but were cleansed and pass Validation Successful.' + @body2 + '<br><br><font face =arial size = 1.5>This email has been generated from papamart.DWStaging.MerchandisingPlanning.spTXTDataLoad_ETLBatch_EmailReport</font>'

    EXEC msdb.dbo.sp_sEND_dbmail  @from_address = 'BIAdmin@buildabear.com',
                                  @recipients = 'biadmin@buildabear.com;MerchADmin@buildabear.com',
								  --@recipients = 'brianb@buildabear.com', --TESTING
								  --@recipients = 'lizzyt@buildabear.com', --TESTING
                                  @body = @body2,
                                  @body_format = 'HTML',
                                  @subject = @subject

 


END
```

