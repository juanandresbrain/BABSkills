# dbo.spA360_store_dim_FileOutput

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spA360_store_dim_FileOutput"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spA360_store_dim_FileOutput]
	@path varchar(200),
	@filepart varchar(100),
	@tablename varchar(128),
	@compress bit=1,
	@allRecords bit=0

as


Begin 

--declare @path varchar(200)
--declare	@filepart varchar(100)
--declare @tablename varchar(128)
--declare @compress bit=1
--declare @allRecords bit=0 

--set @path = '\\stl-ssis-p-01\IntegrationStaging\CRM\DataExtension\a360\'
--set @filepart = 'store_dim'
--set @tablename = 'vwStores'
--set @compress = 0
--set @allRecords=1


		--create Email file
		DECLARE @cmd varchar(1000),
				@filename varchar(100),
				@filenameBK varchar(100),
				@filename_header varchar(100),
				@filedate varchar(20),
				@selectstmnt varchar(5000),
				@bcpsql varchar(4000),
				@columnheaders varchar(4000)
		

		--CREATE TABLE CONTAINING COLUMN HEADERS FOR FILE EXPORT
		SET @columnheaders = ''
		--SET @tablename='tmp_ETUploadEmail'

		SELECT @columnheaders = @columnheaders + c.name + ','
		 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 WHERE o.name = @tablename
		 --and colid not in (17,18,20)
		 ORDER BY colid

		 --SELECT *
		 --FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name ='A360_trans_header'
		 ----and colid not in (17,18,20)
		 --ORDER BY colid


		SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)

		if (Object_ID('dbo.tmp_DE1UploadHeaders') IS NOT NULL) DROP TABLE dbo.tmp_DE1UploadHeaders

		SELECT @columnheaders AS columnheader
		INTO dbo.tmp_DE1UploadHeaders

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			SET @filenameBK = @filepart + '_' + @filedate + '.csv'
			SET @filename = @filepart + '.csv'
			SET @filename_header = @filepart + 'HEADER.txt'

		--CREATE FILE USING BCP COMMAND
		if @allRecords = 1
		begin
		
SET @selectstmnt = 'SELECT [StoreID],[StoreNumber],[StoreKey],[PermCloseStatus],[StoreNameAbbr],replace([StoreNameFull],'','',''-''),[StorePhoneNumber],[StoreFaxNumber],[StoreEmail],[TimeZoneDesc]'
  + ',[StateProvinceNameAbbr],[StateProvinceNameFull],replace([StoreLocator],'','',''-''),replace([StoreMallWebsiteURL],'','',''-'')'
  + ',[StoreLongitude],[StoreLatitude],replace([StoreLegalDescription],'','',''-''),[Channel],[TradingGroup],[CountryNameAbbr],[CountryNameFull],[SubChannel],[Zone],[Area],[District],[CompanyLevel]'
  + ',[BearRange],[bearea],[bearritory],[DCSource],[DistroDay],[DeliveryDay],[SoundStore],[StoreConcept],[FocusFifty],[LocationType],[StoreOpenStatus],[StoreDesign],[isBRFstore],[WebOrStore]'
  	+ ' from DW.azure.' + @tablename
			--+ ' FROM A360_trans_header'
			--+ ' where cast(purchaseDate as date) >= ''11/24/2024'' and cast(purchaseDate as date) <= ''11/30/2024'''
			--from DW.dbo.' + @tablename
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename 
			EXEC master..xp_cmdshell @cmd, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + '\archive\' + @filenameBK 
			EXEC master..xp_cmdshell @cmd, no_output

		end

	
		if @allRecords = 0
		begin
		
SET @selectstmnt = 'SELECT [StoreID],[StoreNumber],[StoreKey],[PermCloseStatus],[StoreNameAbbr],replace([StoreNameFull],'','',''-''),[StorePhoneNumber],[StoreFaxNumber],[StoreEmail],[TimeZoneDesc]'
  + ',[StateProvinceNameAbbr],[StateProvinceNameFull],replace([StoreLocator],'','',''-''),replace([StoreMallWebsiteURL],'','',''-'')'
  + ',[StoreLongitude],[StoreLatitude],replace([StoreLegalDescription],'','',''-''),[Channel],[TradingGroup],[CountryNameAbbr],[CountryNameFull],[SubChannel],[Zone],[Area],[District],[CompanyLevel]'
  + ',[BearRange],[bearea],[bearritory],[DCSource],[DistroDay],[DeliveryDay],[SoundStore],[StoreConcept],[FocusFifty],[LocationType],[StoreOpenStatus],[StoreDesign],[isBRFstore],[WebOrStore]'
  	+ ' from DW.azure.' + @tablename

			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename 
			EXEC master..xp_cmdshell @cmd, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + '\archive\' + @filenameBK 
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
			SELECT  @cmd = 'del ' + @path + '*HEADER.txt /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
		end

			SELECT  @cmd = 'del ' + @path + '*.data /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
END
```

