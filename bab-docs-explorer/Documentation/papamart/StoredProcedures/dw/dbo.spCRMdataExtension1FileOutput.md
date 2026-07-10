# dbo.spCRMdataExtension1FileOutput

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMdataExtension1FileOutput"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMdataExtension1FileOutput]
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
		 and colid not in (44,45,50,51,52,53,55,56)
		 ORDER BY colid


		 --select * FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name = 'CRMde1'
		 ----and colid not in (43,44,50,51,52,53,54,55,56)
		 --and colid not in (44,45,50,51,52,53,55,56)
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
			SET @selectstmnt = 'select [customerNumber],NULLIF([SubscriberKey], '' '') as ''SubscriberKey'',NULLIF([status],'' '') as ''status'',[dateJoined],[LastSentDate],[LastOpenDate],'
			+ '[LastClickDate],[bonusClubMember],NULLIF([bonusClubMembershipType],'' '') as ''bonusClubMembershipType'',[bonusClubPointsBalance],[hasOnlineAccount],NULLIF([bonusClubSignUpSource],'''') as bonusCLubSignUpSource,'
			+ 'NULLIF([Country],'' '') as ''Country'',[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],'
			+ '[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],[MonetarySum3m],'
			+ '[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],[RecencyCount1m],'
			+ '[MonetarySum1m],NULLIF([address_1],'''') as address_1,NULLIF([address_2],'''') as address_2,NULLIF([address_3],'''') as address_3,'
			+ 'NULLIF([address_4],'''') as address_4,NULLIF([post_code],'''') as post_code,'
			+ 'NULLIF([mobile],'''') as mobile,NULLIF([locale],'''') as locale,[text_opt_in],NULLIF([EmailAddress], '' '') as ''EmailAddress'''
			--+ ',NULLIF([LastTransactionDate],'''') as LastTransactionDate,NULLIF([LastTransactionStore],'''') as LastTransactionDate from DW.dbo.CRMde1'
			+ ',NULLIF([LastTransactionDate],'''') as LastTransactionDate,NULLIF([LastTransactionStore],'''') as LastTransactionDate,  NULLIF([PreferredStory],'''') as PreferredStory,'
			+ '[LifetimePoints],NULLIF([FirstName],'''') as FirstName,NULLIF([LastName],'''') as LastName from DW.dbo.CRMde1'
			--+ ' where SubscriberKey in (''ian.david.wallace@gmail.com'',''discomamalives@gmail.com'')'
			--+ ' where customerNumber in (''823266886'', ''824139020'', ''728265835'')'
			+ ' where Country <> '' '' '
			--+ ' and LastTransactionDate >= getdate()-5'
			--+ ' from DW.dbo.CRMde1'
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
			SET @selectstmnt = 'select [customerNumber],[SubscriberKey],[status],[dateJoined],[LastSentDate],[LastOpenDate],'
			+ '[LastClickDate],[bonusClubMember],[bonusClubMembershipType],[bonusClubPointsBalance],[hasOnlineAccount],NULLIF([bonusClubSignUpSource],'''') as bonusCLubSignUpSource,'
			+ '[Country],[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],'
			+ '[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],[MonetarySum3m],'
			+ '[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],[RecencyCount1m],'
			+ '[MonetarySum1m],NULLIF([address_1],'''') as address_1,NULLIF([address_2],'''') as address_2,NULLIF([address_3],'''') as address_3,'
			+ 'NULLIF([address_4],'''') as address_4,NULLIF([post_code],'''') as post_code,'
			+ 'NULLIF([mobile],'''') as mobile,NULLIF([locale],'''') as locale,[text_opt_in],[EmailAddress]'
			--+ ',NULLIF([LastTransactionDate],'''') as LastTransactionDate,NULLIF([LastTransactionStore],'''') as LastTransactionDate from DW.dbo.CRMde1'
			+ ',NULLIF([LastTransactionDate],'''') as LastTransactionDate,NULLIF([LastTransactionStore],'''') as LastTransactionDate,  NULLIF([PreferredStory],'''') as PreferredStory,'
			+ '[LifetimePoints],NULLIF([FirstName],'''') as FirstName,NULLIF([LastName],'''') as LastName from DW.dbo.CRMde1'
			+ ' where cast(InsertDate as date) = cast(getdate() as date) or cast(UpdateDate as date)  = cast(getdate() as date)'
			--+ ' and SubscriberKey in (''ian.david.wallace@gmail.com'',''discomamalives@gmail.com'')'
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
```

