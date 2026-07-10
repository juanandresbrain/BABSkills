# dbo.spEmail_ET_Upload_Output_Files

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmail_ET_Upload_Output_Files"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmail_ET_Upload_Output_Files]
	@path varchar(200),
	@filepart varchar(100),
	@tablename varchar(128),
	@compress bit=1

as

/*
--Test
exec spEmail_ET_Upload_Output_Files @path = 'I:\Responsys\ExactTarget\', @filepart = 'BABW_EMAIL_', @tablename = 'tmp_ETUploadEmail'
*/

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

if (Object_ID('dw.dbo.tmp_ETUploadHeaders') IS NOT NULL) DROP TABLE dw.dbo.tmp_ETUploadHeaders

SELECT @columnheaders AS columnheader
INTO dw.dbo.tmp_ETUploadHeaders

    --SET @path = 'I:\Responsys\ExactTarget\'
	SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
    SET @filename = @filepart + @filedate + '.txt'
	SET @filename_header = @filepart + 'HEADER.txt'

--CREATE FILE CONTAINING EMAILS USING BCP COMMAND
    SET @selectstmnt = 'SELECT * FROM dw.dbo.' + @tablename
    SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename
        + '.data" -t "|" -T -c'
    EXEC master..xp_cmdshell @bcpsql--, no_output

    SET @selectstmnt = 'SELECT * FROM dw.dbo.tmp_ETUploadHeaders'
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
```

