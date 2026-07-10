# dbo.spCRMdataExtension4FileOutput

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMdataExtension4FileOutput"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMdataExtension4FileOutput]
	@path varchar(200),
	@filepart varchar(100),
	@tablename varchar(128),
	@compress bit=1,
	@allRecords bit=0

as


Begin 

		--create Email file
		DECLARE @cmd varchar(1000),
				@filename varchar(100),
				@filename_header varchar(100),
				@filedate varchar(20),
				@selectstmnt varchar(5000),
				@bcpsql varchar(4000),
				@columnheaders varchar(4000)
		

		--CREATE TABLE CONTAINING COLUMN HEADERS FOR FILE EXPORT
		SET @columnheaders = ''
		--SET @tablename='tmp_ETUploadEmail'

		SELECT @columnheaders = @columnheaders + c.name + '|'
		 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 WHERE o.name = @tablename
		 and colid not in (7,8)
		 ORDER BY colid

		
		 --select * FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name = 'CRMde4'
		 --and colid not in (7,8)
		 --ORDER BY colid



		SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)

		if (Object_ID('dbo.tmp_DE1UploadHeaders') IS NOT NULL) DROP TABLE dbo.tmp_DE1UploadHeaders

		SELECT @columnheaders AS columnheader
		INTO dbo.tmp_DE1UploadHeaders

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			SET @filename = @filepart + @filedate + '.txt'
			SET @filename_header = @filepart + 'HEADER.txt'

		--CREATE FILE USING BCP COMMAND
		if @allRecords = 1
		begin
			SET @selectstmnt = 'select [transactionID],[units],NULLIF([event_name],'''') as event_name,NULLIF([category],'''') as category,[unit_gross_amount],NULLIF([coupon_desc],'''') as coupon_desc,[recID] '
			+ ' ,NULLIF([couponNumber],0) as couponNumber, NULLIF([certificateNumber],'''') as certificateNumber from DW.dbo.CRMde4'
			--+ ' where InsertDate > getdate() +1'
			--from DW.dbo.' + @tablename
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename 
			EXEC master..xp_cmdshell @cmd, no_output
		end

		if @allRecords = 0
		begin
			SET @selectstmnt = 'select [transactionID],[units],NULLIF([event_name],'''') as event_name,NULLIF([category],'''') as category,[unit_gross_amount],NULLIF([coupon_desc],'''') as coupon_desc,[recID], '
			+ ' NULLIF([couponNumber],0) as couponNumber, NULLIF([certificateNumber],'''') as certificateNumber from DW.dbo.CRMde4'
			--+ ' where transactionID in (select transactionID from DWStaging.dbo.tmpCrmDe4)'
			+ ' where InsertDate > getdate() -2 or UpdateDate > getdate() -2'
			--from DW.dbo.' + @tablename
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename 
			EXEC master..xp_cmdshell @cmd, no_output
		end

		if @compress = 1
		begin
			--COMPRESS FILE
			SELECT  @cmd = '"C:\Program Files\7-zip\7z.exe" a -tzip '
					+ @path + REPLACE(@filename, '.txt', '') + '.zip ' + @path
					+ @filename 
			EXEC master..xp_cmdshell @cmd--, no_output
		end

		if @compress = 1
		begin
			--DELETE TEXT FILE
			SELECT  @cmd = 'del ' + @path + @filepart + '*.txt /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
		end

		if @compress = 0
		begin
			SELECT  @cmd = 'del ' + @path + '*_HEADER.txt /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
		end

			SELECT  @cmd = 'del ' + @path + '*.data /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
END

Azure,spLoadMerchOnOrder,-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [Azure].[spLoadMerchOnOrder] 
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;


Declare @BegYear char(4)
Select @BegYear = (Select Cast(Fiscal_Year - 1 as char(4)) + '01' from date_Dim where Actual_Date between GetDate()-2 and GetDate()-1);
Truncate Table Azure.MerchOnOrder;

With D as (

select fiscal_Year,Fiscal_period,Min(Actual_Date) - 7 as NewStart,Max(Actual_date) -7 as NewEnd from date_dim group by Fiscal_year,Fiscal_period

),

D2 as (select d.fiscal_Year,d.Fiscal_period,t.Actual_Date as DateKey,DateDiff("d",t.Actual_Date,NewEnd) TotalFlag
 from date_Dim t inner join D on NewStart <= t.Actual_Date and NewEnd >= t.Actual_Date

where datePart("dw",t.actual_date) = 7 )

Insert into Azure.merchonOrder
select ProductKey,StoreKey, left(Merch_year_pd,4) as Fiscal_Year,    Right(Merch_year_pd,2) as Fiscal_Period,
sum(On_Order_Units) as On_Order,DateKey,((left(Merch_year_pd,4) - 2017) * 12) +  Right(Merch_year_pd,2) AS PeriodKey,TotalFlag

from bedrockdb02.ma_01.dbo.oo_all_style_loc_pd d
inner join D2 on (Fiscal_Year = left(Merch_year_pd,4) and Fiscal_period =  Right(Merch_year_pd,2))
inner join Azure.vwLocationToStoreKey t on d.location_ID = t.locationID
inner join bedrockdb02.ma_01.dbo.style a on d.style_ID = a.style_id
inner join azure.vwStyleToProdKey T2 on a.style_code = T2.style
where left(Merch_year_pd,4) >= @BegYear
group by  ProductKey,StoreKey, Left(Merch_year_pd,4),    Right(Merch_year_pd,2),DateKey,TotalFlag
having sum(On_Order_Units) > 0
END
```

