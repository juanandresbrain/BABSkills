# dbo.spA360_discounts_FileOutput

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spA360_discounts_FileOutput"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spA360_discounts_FileOutput]
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

		SELECT @columnheaders = @columnheaders + c.name + ','
		 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 WHERE o.name = @tablename
		 --and colid not in (17,18,20)
		 ORDER BY colid 

		 --DECLARE @columnheaders varchar(4000)

		 --SET @columnheaders = ''

		 --SELECT @columnheaders = @columnheaders + c.name + ','
		 --FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name = 'A360_discounts'
		 ----and colid not in (17,18,20)
		 --ORDER BY colid

		 --	SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)

		 --select @columnheaders

		 --SELECT *
		 --FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name ='A360_discounts'
		 ----and colid not in (17,18,20)
		 --ORDER BY colid desc


		SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)

		if (Object_ID('dbo.tmp_DE1UploadHeaders') IS NOT NULL) DROP TABLE dbo.tmp_DE1UploadHeaders

		SELECT @columnheaders AS columnheader
		INTO dbo.tmp_DE1UploadHeaders

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			--SET @filename = @filepart + @filedate + '.csv'
			SET @filename = @filepart + '.csv'
			SET @filename_header = @filepart + 'HEADER.txt'

		--CREATE FILE USING BCP COMMAND
		if @allRecords = 1
		begin
		
		SET @selectstmnt = 'SELECT isnull([event_name],''''), isnull([category],''''), isnull([coupon_desc],'''') as coupon_desc, '
		+ 'isnull([couponNumber],''''), isnull([certificate_no],''''), [customerNumber], [transaction_id], [unit_gross_amount],'
		+ '[units], [ID]from DW.dbo.' + @tablename
		+ ' where ID > 0'
		--	--+ '	where ID in (132424550,132424553,132424554,132424555,132424557,132424560,132424562, 132424537,132424548)'
		
		--SET @selectstmnt = 'SELECT [ID],[units],[unit_gross_amount],[transaction_id],[customerNumber]'
		--+ ',ISNULL([certificate_no],'' ''),ISNULL([couponNumber],'' ''),ISNULL([coupon_desc],'' ''),ISNULL([category],'' ''),ISNULL([event_name],'' '')'
		--	+ ' from DW.dbo.' + @tablename
		--	+ ' where ID > 0'
			--+ ' where ID in (132952119, 132424541, 132426133, 132426134, 143291550,143291553,143291560)'
			--+ '	where ID in (132424550,132424553,132424554,132424555,132424557,132424560,132424562)'

		--	ISNULL(field,' ')

			--SET @selectstmnt = 'SELECT [units],[unit_gross_amount],[transaction_id]'
			--+ ' ,[customerNumber],isnull([certificate_no],''''),isnull([couponNumber],'''')'
			--+ ' ,isnull([coupon_desc],'''') as coupon_desc,isnull([category],''''),isnull([event_name],''''), [ID]'
			--+ ' from DW.dbo.' + @tablename
			--+ '	where ID in (132424550,132424553,132424554,132424555,132424557,132424560,132424562)'

			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename 
			EXEC master..xp_cmdshell @cmd, no_output
		end

	
		if @allRecords = 0
		begin
			--SET @selectstmnt = 'SELECT [ID],[units],[unit_gross_amount],[transaction_id]'
			--+ ',[customerNumber],[certificate_no],[couponNumber],[coupon_desc],[category],[event_name]'
			--+ ' from DW.dbo.' + @tablename

	
SET @selectstmnt = 'SELECT [ID],[units],[unit_gross_amount],[transaction_id],[customerNumber]'
+ ',[certificate_no],[couponNumber],[coupon_desc],[category],[event_name]'
			+ ' from DW.dbo.' + @tablename
			+ ' where ID > 0'

			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "," -T -c'
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
			SELECT  @cmd = 'del ' + @path + '*HEADER.txt /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
		end

			SELECT  @cmd = 'del ' + @path + '*.data /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
END
```

