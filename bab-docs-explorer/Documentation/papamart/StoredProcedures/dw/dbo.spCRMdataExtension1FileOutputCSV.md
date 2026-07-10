# dbo.spCRMdataExtension1FileOutputCSV

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMdataExtension1FileOutputCSV"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMdataExtension1FileOutputCSV]
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
		 and colid not in (44,45,50,51,52,53,55,56)
		 ORDER BY colid


		 --select * FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name = 'CRMde1'
		 ----and colid not in (43,44,50,51,52,53,54,55,56)
		 --and colid not in (44,45,50,51,52,53,55,56)
		 --ORDER BY colid

		SELECT @columnheaders = @columnheaders + 'RecordTypeId'

		--SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)

		if (Object_ID('dbo.tmp_DE1UploadHeaders') IS NOT NULL) DROP TABLE dbo.tmp_DE1UploadHeaders

		SELECT @columnheaders AS columnheader
		INTO dbo.tmp_DE1UploadHeaders

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			SET @filename = @filepart + @filedate + '.csv'
			SET @filename_header = @filepart + 'HEADER.csv'

		--CREATE FILE USING BCP COMMAND
		if @allRecords = 1
		begin
			--SET @selectstmnt = 'select top 10 [customerNumber],REPLACE([SubscriberKey],'','','' '') as SubscriberKey,[status],'
			SET @selectstmnt = 'select top 350000 [customerNumber],REPLACE([SubscriberKey],'','','' '') as SubscriberKey,NULLIF([status],'' '') as ''status'','
			--[dateJoined],[LastSentDate],[LastOpenDate],'
			+ ' convert (varchar(10), [dateJoined], 101) as ''dateJoined'', convert (varchar(10), [LastSentDate], 101) as ''LastSentDate'',' 
			+ ' convert (varchar(10), [LastOpenDate], 101) as ''LastOpenDate'', convert (varchar(10), [LastClickDate], 101) as ''LastClickDate'','
			+ '[bonusClubMember],NULLIF([bonusClubMembershipType],'' '') as ''bonusClubMembershipType'',[bonusClubPointsBalance],[hasOnlineAccount],NULLIF(REPLACE([bonusClubSignUpSource],'','','' ''),'' '') as bonusCLubSignUpSource,'
			+ 'case when country = '' '' then null when [country] = ''SGP'' then ''SG'' when [country] = ''ESP'' then ''ES'' when [country] = ''DEU'' then	''DE'' when [country] = ''COL'' then ''CO'' when [country] = ''ARE'' then ''AE'''
			+ ' when [country] = ''SWE'' then	''SE'' when [country] = ''PHL'' then ''PH'' when [country] = ''AUS'' then ''AU'' when [country] = ''BEL'' then ''BE'' when [country] = ''NOR'' then	''NO'''
			+ '	when [country] = ''USA'' then	''US'' when [country] = ''FIN'' then ''FI'' when [country] = ''IRL'' then ''IE'' when [country] = ''''	then '''' when [country] = ''ISL'' then	''IS'''
			+ '	when [country] = ''MEX'' then	''MX'' when [country] = ''LIE'' then ''LI'' when [country] = ''CAF'' then ''CF'' when [country] = ''ITA'' then ''IT'' when [country] = ''NZL'' then	''NZ'''
			+ '	when [country] = ''JPN'' then	''JP'' when [country] =  ''PRI'' then ''PR'' when [country] = ''LUX'' then	''LU'' when [country] = ''CAN'' then ''CA'' when [country] = ''CHE'' then	''CH'''
			+ '	when [country] = ''CHN'' then	''CN'' when [country] = ''IDN'' then ''ID'' when [country] = ''IRE'' then ''IE'' when [country] = ''THA'' then	''TH'' when [country] = ''ZAF'' then	''ZA'''
			+ '	when [country] = ''AUT'' then	''AT'' when [country] = ''DNK'' then ''DK'' when [country] = ''HKG'' then ''HK'' when [country] = ''BRA'' then ''BR'' when [country] = ''UNK'' then	'''''
			+ '	when [country] = ''EUR'' then	''UK'' when [country] = ''GBR'' then ''UK'' when [country] = ''GRC'' then ''GR'' when [country] = ''FRA'' then ''FR'' when [country] = ''KOR'' then	''KR'''
			+ '	when [country] = ''PRT'' then	''PT'' when [country] = ''NLD'' then ''NL'' when [country] = ''TUR'' then ''TR'' when [country] = ''ARG'' then ''AR'' when [country] = ''TWN'' then	''TW'' end as ''Country'','	
			+ '[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],'
			+ '[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],[MonetarySum3m],'
			+ '[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],[RecencyCount1m],'
			+ '[MonetarySum1m],NULLIF(REPLACE([address_1],'','','' ''),'''') as address_1,NULLIF(REPLACE([address_2],'','','' ''),'' '') as address_2,NULLIF(REPLACE([address_3],'','','' ''),'' '') as address_3,'
			+ 'NULLIF(REPLACE([address_4],'','','' ''),'' '') as address_4,NULLIF(REPLACE([post_code],'','','' ''),'' '') as post_code,'
			+ 'NULLIF(REPLACE([mobile],'','','' ''),'' '') as mobile,NULLIF(REPLACE([locale],'','','' ''),'' '') as locale,[text_opt_in],REPLACE([EmailAddress],'','','' '') as EmailAddress,'
			--+ ',NULLIF([LastTransactionDate],'''') as LastTransactionDate,NULLIF([LastTransactionStore],'''') as LastTransactionDate from DW.dbo.CRMde1'
			+ 'NULLIF([LastTransactionDate],'' '') as LastTransactionDate,NULLIF(REPLACE([LastTransactionStore],'','','' ''),'' '') as LastTransactionStore,'
			+ 'NULLIF(REPLACE([PreferredStory],'','','' ''),'' '') as PreferredStory, [LifetimePoints],'
			+ 'NULLIF(REPLACE([FirstName],'','','' ''),'' '') as FirstName, NULLIF(REPLACE([LastName],'','','' ''),'' '') as LastName, ''0124R000001ZDUzQAO'' as RecordTypeId from DW.dbo.CRMde1'
			--+ ' where SubscriberKey in (''ian.david.wallace@gmail.com'',''discomamalives@gmail.com'')'
			--+ ' where customerNumber in (''851697791'',''848148649'',''851697845'',''726166117'',''923428210'',''923163002'')'
			--+ ' where customerNumber in (''851697791'',''848148649'',''851697845'',''848148731'',''848169999'',''851697876'',''848170057'',''851697898'',''726166117'',''923428210'')'
			--+ ' where customerNumber in (''823266886'',''824139020'')'
			--+ ' from DW.dbo.CRMde1'
			--from DW.dbo.' + @tablename
			
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

		if @allRecords = 0
		begin
			--SET @selectstmnt = 'select top 10 [customerNumber],REPLACE([SubscriberKey],'','','' '') as SubscriberKey,[status],[dateJoined],[LastSentDate],[LastOpenDate],'
			SET @selectstmnt = 'select [customerNumber],REPLACE([SubscriberKey],'','','' '') as SubscriberKey,NULLIF([status],'' '') as ''status'','
			--[dateJoined],[LastSentDate],[LastOpenDate],'
			+ ' convert (varchar(10), [dateJoined], 101) as ''dateJoined'', convert (varchar(10), [LastSentDate], 101) as ''LastSentDate'',' 
			+ ' convert (varchar(10), [LastOpenDate], 101) as ''LastOpenDate'', convert (varchar(10), [LastClickDate], 101) as ''LastClickDate'','
			+ '[bonusClubMember],NULLIF([bonusClubMembershipType],'' '') as ''bonusClubMembershipType'',[bonusClubPointsBalance],[hasOnlineAccount],NULLIF(REPLACE([bonusClubSignUpSource],'','','' ''),'' '') as bonusCLubSignUpSource,'
			+ 'case when country = '' '' then null when [country] = ''SGP'' then ''SG'' when [country] = ''ESP'' then ''ES'' when [country] = ''DEU'' then	''DE'' when [country] = ''COL'' then ''CO'' when [country] = ''ARE'' then ''AE'''
			+ ' when [country] = ''SWE'' then	''SE'' when [country] = ''PHL'' then ''PH'' when [country] = ''AUS'' then ''AU'' when [country] = ''BEL'' then ''BE'' when [country] = ''NOR'' then	''NO'''
			+ '	when [country] = ''USA'' then	''US'' when [country] = ''FIN'' then ''FI'' when [country] = ''IRL'' then ''IE'' when [country] = ''''	then '''' when [country] = ''ISL'' then	''IS'''
			+ '	when [country] = ''MEX'' then	''MX'' when [country] = ''LIE'' then ''LI'' when [country] = ''CAF'' then ''CF'' when [country] = ''ITA'' then ''IT'' when [country] = ''NZL'' then	''NZ'''
			+ '	when [country] = ''JPN'' then	''JP'' when [country] =  ''PRI'' then ''PR'' when [country] = ''LUX'' then	''LU'' when [country] = ''CAN'' then ''CA'' when [country] = ''CHE'' then	''CH'''
			+ '	when [country] = ''CHN'' then	''CN'' when [country] = ''IDN'' then ''ID'' when [country] = ''IRE'' then ''IE'' when [country] = ''THA'' then	''TH'' when [country] = ''ZAF'' then	''ZA'''
			+ '	when [country] = ''AUT'' then	''AT'' when [country] = ''DNK'' then ''DK'' when [country] = ''HKG'' then ''HK'' when [country] = ''BRA'' then ''BR'' when [country] = ''UNK'' then	'''''
			+ '	when [country] = ''EUR'' then	''UK'' when [country] = ''GBR'' then ''UK'' when [country] = ''GRC'' then ''GR'' when [country] = ''FRA'' then ''FR'' when [country] = ''KOR'' then	''KR'''
			+ '	when [country] = ''PRT'' then	''PT'' when [country] = ''NLD'' then ''NL'' when [country] = ''TUR'' then ''TR'' when [country] = ''ARG'' then ''AR'' when [country] = ''TWN'' then	''TW'' end as ''Country'','	
			+ '[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],'
			+ '[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],[MonetarySum3m],'
			+ '[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],[RecencyCount1m],'
			+ '[MonetarySum1m],NULLIF(REPLACE([address_1],'','','' ''),'''') as address_1,NULLIF(REPLACE([address_2],'','','' ''),'' '') as address_2,NULLIF(REPLACE([address_3],'','','' ''),'' '') as address_3,'
			+ 'NULLIF(REPLACE([address_4],'','','' ''),'' '') as address_4,NULLIF(REPLACE([post_code],'','','' ''),'' '') as post_code,'
			+ 'NULLIF(REPLACE([mobile],'','','' ''),'' '') as mobile,NULLIF(REPLACE([locale],'','','' ''),'' '') as locale,[text_opt_in],REPLACE([EmailAddress],'','','' '') as EmailAddress,'
			--+ ',NULLIF([LastTransactionDate],'''') as LastTransactionDate,NULLIF([LastTransactionStore],'''') as LastTransactionDate from DW.dbo.CRMde1'
			+ 'NULLIF([LastTransactionDate],'' '') as LastTransactionDate,NULLIF(REPLACE([LastTransactionStore],'','','' ''),'' '') as LastTransactionStore,'
			+ 'NULLIF(REPLACE([PreferredStory],'','','' ''),'' '') as PreferredStory, [LifetimePoints],'
			+ 'NULLIF(REPLACE([FirstName],'','','' ''),'' '') as FirstName, NULLIF(REPLACE([LastName],'','','' ''),'' '') as LastName, ''0124R000001ZDUzQAO'' as RecordTypeId from DW.dbo.CRMde1'
			+ ' where cast(InsertDate as date) = cast(getdate() as date) or cast(UpdateDate as date)  = cast(getdate() as date)'
			--+ ' and SubscriberKey in (''ian.david.wallace@gmail.com'',''discomamalives@gmail.com'')'
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
			SELECT  @cmd = 'del ' + @path + '*_HEADER.csv /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
		end

			SELECT  @cmd = 'del ' + @path + '*.data /Q /F'
			EXEC master..xp_cmdshell @cmd, no_output
END
```

