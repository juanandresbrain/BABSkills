# dbo.spCRMdataExtension1MCFileOutputNtileResultsDelta

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMdataExtension1MCFileOutputNtileResultsDelta"]
    dbo_CRMde1(["dbo.CRMde1"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.CRMde1 |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMdataExtension1MCFileOutputNtileResultsDelta]
	
as


Begin 

		--create Email file
		DECLARE @ntile_var int;

		--set @ntile_var = (select (count(*)/350000)+1 as varNumberOfGroups from DW.dbo.CRMde1)

		--set @ntile_var = (select (count(*)/1900000)+1 as varNumberOfGroups from DW.dbo.CRMde1 where cast(InsertDate as date) = cast(getdate() as date) or cast(UpdateDate as date)  = cast(getdate() as date))

		set @ntile_var = 1

		--select @ntile_var

			select [customerNumber],[SubscriberKey],[status],[dateJoined],[LastSentDate],[LastOpenDate],
			[LastClickDate],[bonusClubMember],[bonusClubMembershipType],[bonusClubPointsBalance],[hasOnlineAccount],NULLIF([bonusClubSignUpSource],'''') as bonusCLubSignUpSource,
			[Country],[FrequencyCount3m],[FrequencyCount6m],[FrequencyCount12m],[FrequencyCount18m],[FrequencyCount24m],[FrequencyCountTTL],
			[RecencyCount3m],[RecencyCount6m],[RecencyCount12m],[RecencyCount18m],[RecencyCount24m],[RecencyCountTTL],[MonetarySum3m],
			[MonetarySum6m],[MonetarySum12m],[MonetarySum18m],[MonetarySum24m],[MonetarySumTTL],[FrequencyCount1m],[RecencyCount1m],
			[MonetarySum1m],NULLIF([address_1],'') as address_1,NULLIF([address_2],'') as address_2,NULLIF([address_3],'') as address_3,
			NULLIF([address_4],'') as address_4,NULLIF([post_code],'') as post_code,
			NULLIF([mobile],'') as mobile,NULLIF([locale],'') as locale,[text_opt_in],[EmailAddress]
			,NULLIF([LastTransactionDate],'') as LastTransactionDate,NULLIF([LastTransactionStore],'') as LastTransactionDate,  NULLIF([PreferredStory],'') as PreferredStory,
			[LifetimePoints],NULLIF([FirstName],'') as FirstName,NULLIF([LastName],'') as LastName, [InsertDate], [UpdateDate],
			NTILE(@ntile_var) OVER (order by customerNumber asc ) as groupNum
			from DW.dbo.CRMde1
			--where cast(InsertDate as date) = cast(getdate() as date) or cast(UpdateDate as date)  = cast(getdate() as date) or cast(UpdateDateRecency as date)  = cast(getdate() as date)
			where cast(InsertDate as date) >= cast(getdate()-2 as date) or cast(UpdateDate as date)  >= cast(getdate()-2 as date) or cast(UpdateDateRecency as date)  >= cast(getdate()-2 as date)
			--where cast(InsertDate as date) >= cast(getdate()-5 as date) or cast(UpdateDate as date)  >= cast(getdate()-5 as date)
			-- and SubscriberKey in (''ian.david.wallace@gmail.com'',''discomamalives@gmail.com'')'



END
```

