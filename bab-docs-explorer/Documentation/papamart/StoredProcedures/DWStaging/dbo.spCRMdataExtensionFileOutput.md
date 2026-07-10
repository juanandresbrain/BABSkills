# dbo.spCRMdataExtensionFileOutput

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMdataExtensionFileOutput"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMfileSalesForceDe1]
	@path varchar(200),
	@filepart varchar(100),
	@tablename varchar(128),
	@compress bit=1

as

/*
--Test

exec spEmail_ET_Upload_Output_Files @path = 'T:\FileRepository\ExactTarget\', @filepart = 'BABW_EMAIL_', @tablename = 'ETUploadEmail', @compress = 1

exec spCRMfileSalesForceDe1 @path = '\\stl-ssis-p-01\IntegrationStaging\CRM\DataExtension\', @filepart = 'DE_1_',@tablename = 'tmpCrmDe1',@compress = 1

-- \\stl-ssis-p-01\IntegrationStaging\CRM\DataExtension
*/

--If (object_id('##stagetable') is not null) drop table ##stagetable
--DECLARE @SQL varchar (100)
--Select @SQL = 'select count(*) as rowz into ##stagetable from ' + @tablename
--EXEC (@SQL) 
--If (select sum(rowz) from ##stagetable) > 0

Begin 

		--create Email file
		DECLARE @cmd varchar(1000),
				@filename varchar(100),
				@filename_header varchar(100),
				@filedate varchar(20),
				@selectstmnt varchar(5000),
				@bcpsql varchar(500),
				@columnheaders varchar(4000)
		

		--CREATE TABLE CONTAINING COLUMN HEADERS FOR FILE EXPORT
		SET @columnheaders = ''
		--SET @tablename='tmp_ETUploadEmail'

		SELECT @columnheaders = @columnheaders + c.name + '| '
		 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 WHERE o.name = @tablename
		 ORDER BY colid

		SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 2)

		if (Object_ID('dbo.tmp_DE1UploadHeaders') IS NOT NULL) DROP TABLE dbo.tmp_DE1UploadHeaders

		SELECT @columnheaders AS columnheader
		INTO dbo.tmp_DE1UploadHeaders

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			SET @filename = @filepart + @filedate + '.txt'
			SET @filename_header = @filepart + 'HEADER.txt'

		--CREATE FILE USING BCP COMMAND
			SET @selectstmnt = 'select * from DWStaging.dbo.' + @tablename
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename
				+ '.data" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DWStaging.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename 
			EXEC master..xp_cmdshell @cmd, no_output

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
```

