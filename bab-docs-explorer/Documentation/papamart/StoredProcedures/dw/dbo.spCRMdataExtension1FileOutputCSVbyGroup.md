# dbo.spCRMdataExtension1FileOutputCSVbyGroup

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMdataExtension1FileOutputCSVbyGroup"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMdataExtension1FileOutputCSVbyGroup]
	@path varchar(200),
	@filepart varchar(100),
	@tablename varchar(128),
	@compress bit=1,
	@allRecords bit=0,
	@groupNum integer

as


Begin 

		--create Email file
		DECLARE @cmd varchar(1000),
				@filename varchar(100),
				@filename_header varchar(100),
				@filedate varchar(20),
				@selectstmnt varchar(5000),
				@bcpsql varchar(4000),
				@columnheaders varchar(4000),
				@groupNumString varchar(20)

		--CREATE TABLE CONTAINING COLUMN HEADERS FOR FILE EXPORT
		SET @columnheaders = ''
		--SET @tablename='tmp_ETUploadEmail'

		
set @groupNumString = convert(varchar, @groupNum)



		if @allRecords = 1
		begin

		SELECT @columnheaders = @columnheaders + c.name + ','
		 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 WHERE o.name = @tablename
		 and colid not in (21,22,23,24,25,26,34,44,45,50,51,52,53,55,56,59)
		 --and colid in (2,3)
		 ORDER BY colid

		 -- select * FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name = 'CRMDE1' --and colid in (2,3)
		 --and colid not in (21,22,23,24,25,26,34,44,45,50,51,52,53,55,56,59)
		 --ORDER BY colid


		SELECT @columnheaders = @columnheaders + 'RecordTypeId,SFCC_update__c'
		--SELECT @columnheaders = 'customerNumber,EmailAddress'


		end


		if @allRecords = 0
		begin

		--USE DWStaging

		--SELECT @columnheaders = @columnheaders + c.name + ','
		-- FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		-- WHERE o.name = 'tmpCRMserviceCloudDelta'
		-- and colid not in (51,52,53)
		-- ORDER BY colid

		 
		SELECT @columnheaders = @columnheaders + c.name + ','
		 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 WHERE o.name = @tablename
		 and colid not in (21,22,23,24,25,26,34,44,45,50,51,52,53,55,56,59)
		 ORDER BY colid


		 --select * FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
		 --WHERE o.name = 'tmpCRMserviceCloudDelta'
		 --and colid not in (51,52,53)
		 ----and colid not in (44,45,50,51,52,53,55,56)
		 --ORDER BY colid

		SELECT @columnheaders = @columnheaders + 'RecordTypeId,SFCC_update__c'

		--SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)
		end




		if (Object_ID('dbo.tmp_DE1UploadHeaders') IS NOT NULL) DROP TABLE dbo.tmp_DE1UploadHeaders

		SELECT @columnheaders AS columnheader
		INTO dbo.tmp_DE1UploadHeaders

		if @allRecords = 0
		begin

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			SET @filename = @filepart + @filedate + '_FILE_' + @groupNumString + '.csv'
			SET @filename_header = @filepart + 'HEADER.csv'

		end

		if @allRecords = 1
		begin

			--SET @path = 'I:\Responsys\ExactTarget\'
			SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
			SET @filename = @filepart + @filedate + '_FILE_' + @groupNumString + '.csv'
			SET @filename_header = @filepart + 'HEADER.csv'

		end


		--CREATE FILE USING BCP COMMAND
		if @allRecords = 1
		begin
			

	  
SET @selectstmnt = 'select [customerNumber],[SubscriberKey]'
 + ',[status],'
 + ' NULLIF(convert(varchar, [dateJoined], 101),'' '') as dateJoined,'
+ ' NULLIF(convert(varchar, [LastSentDate], 101),'' '') as LastSentDate,'
 + 'NULLIF(convert(varchar, [LastOpenDate], 101),'' '') as LastOpenDate,'
 + 'NULLIF(convert(varchar, [LastClickDate], 101),'' '') as LastClickDate,'
+ '[bonusClubMember],[bonusClubMembershipType],[bonusClubPointsBalance],'
	+ '[hasOnlineAccount],[bonusClubSignUpSource],[Country],[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],'
	-- + '[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],
	 + ' [MonetarySum3m],[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],'
	 --[RecencyCount1m],
	 + '[MonetarySum1m],[address_1],[address_2],[address_3],[address_4],[post_code],[mobile],[locale],[text_opt_in],[EmailAddress],'
	 + '  NULLIF(convert(varchar, [LastTransactionDate], 101),'' '') as LastTransactionDate'
	 + ' ,[LastTransactionStore],[PreferredStory],[LifetimePoints],[FirstName]'
     + '  ,case when [LastName] = '' '' then [EmailAddress] when [LastName] is null then [EmailAddress] else [LastName] end as LastName,'
	 + '  [RecordTypeId],[SFCC_update__c] '
	 + ' FROM DW.dbo.tmpCRMserviceCloudDelta where [groupNum] = ' + @groupNumString



			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "|" -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename  + '/b'
			EXEC master..xp_cmdshell @cmd, no_output
		end

		if @allRecords = 0
		begin
		

	   
--SET @selectstmnt = 'select [customerNumber],[SubscriberKey],[status],'
-- + ' NULLIF(convert(varchar, [dateJoined], 101),'' '') as dateJoined,'
--+ ' NULLIF(convert(varchar, [LastSentDate], 101),'' '') as LastSentDate,'
-- + 'NULLIF(convert(varchar, [LastOpenDate], 101),'' '') as LastOpenDate,'
-- + 'NULLIF(convert(varchar, [LastClickDate], 101),'' '') as LastClickDate,'
--+ '[bonusClubMember],[bonusClubMembershipType],[bonusClubPointsBalance],'
--	+ '[hasOnlineAccount],[bonusClubSignUpSource],[Country],[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],[RecencyCount3m],[RecencyCount6m],[RecencyCount12m]'
--	  + ',[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],[MonetarySum3m],[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],[RecencyCount1m],[MonetarySum1m]'
--     + ' ,[address_1],[address_2],[address_3],[address_4],[post_code],[mobile],[locale],[text_opt_in],[EmailAddress],'
--	 + '  NULLIF(convert(varchar, [LastTransactionDate], 101),'' '') as LastTransactionDate'
--	 + ' ,[LastTransactionStore],[PreferredStory],[LifetimePoints],[FirstName]'
--     + '  ,case when [LastName] = '' '' then [EmailAddress] when [LastName] is null then [EmailAddress] else [LastName] end as LastName,'
--	  + '  [RecordTypeId], [SFCC_update__c] FROM DW.dbo.tmpCRMserviceCloudDelta where [groupNum] = ' + @groupNumString
	-- + '  [RecordTypeId] FROM DW.dbo.tmpCRMserviceCloudDelta where customerNumber = ''724360135'' and [groupNum] = ' + @groupNumString

	SET @selectstmnt = 'select [customerNumber],[SubscriberKey],[status],'
 + ' NULLIF(convert(varchar, [dateJoined], 101),'' '') as dateJoined,'
+ ' NULLIF(convert(varchar, [LastSentDate], 101),'' '') as LastSentDate,'
 + 'NULLIF(convert(varchar, [LastOpenDate], 101),'' '') as LastOpenDate,'
 + 'NULLIF(convert(varchar, [LastClickDate], 101),'' '') as LastClickDate,'
+ '[bonusClubMember],[bonusClubMembershipType],[bonusClubPointsBalance],'
	+ '[hasOnlineAccount],[bonusClubSignUpSource],[Country],[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],'
	-- + '[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],
	 + ' [MonetarySum3m],[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],'
	 --[RecencyCount1m],
	 + '[MonetarySum1m],[address_1],[address_2],[address_3],[address_4],[post_code],[mobile],[locale],[text_opt_in],[EmailAddress],'
	 + '  NULLIF(convert(varchar, [LastTransactionDate], 101),'' '') as LastTransactionDate'
	 + ' ,[LastTransactionStore],[PreferredStory],[LifetimePoints],[FirstName]'
     + '  ,case when [LastName] = '' '' then [EmailAddress] when [LastName] is null then [EmailAddress] else [LastName] end as LastName,'
	 + '  [RecordTypeId],[SFCC_update__c] FROM DW.dbo.tmpCRMserviceCloudDelta where [groupNum] = ' + @groupNumString


			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename + '.data" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @selectstmnt = 'SELECT * FROM DW.dbo.tmp_DE1UploadHeaders'
			SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
				+ '" -t "," -T -c'
			EXEC master..xp_cmdshell @bcpsql--, no_output

			SET @cmd = 'copy ' + @path + @filename_header + '+' + @path + @filename
					+ '.data ' + @path + @filename + '/b'
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

