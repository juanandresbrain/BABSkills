# dbo.spMergeCRMde1_V2

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMergeCRMde1_V2"]
    CRMde1(["CRMde1"]) --> SP
    dbo_tmpCrmDe1(["dbo.tmpCrmDe1"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CRMde1 |
| dbo.tmpCrmDe1 |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spMergeCRMde1_V2]

as


set nocount on

merge into CRMde1 as target
using 
	(
	SELECT	 [CustomerNumber],
			 isnull([EmailAddress],'') as EmailAddress,
			 isnull([status],'') as status,
			 isnull([dateJoined],'') as dateJoined,
			 isnull([LastSentDate],'')                as [LastSentDate],
			 isnull([LastOpenDate],	'')			as [LastOpenDate],
			 isnull([LastClickDate],'')				as [LastClickDate],
			 isnull([bonusClubMember],0)				as [bonusClubMember],
			 isnull([bonusClubMembershipType],'')		as [bonusClubMembershipType],
			 isnull([bonusClubPointsBalance],0)		as [bonusClubPointsBalance],
			 isnull([hasOnlineAccount],	0)		as [hasOnlineAccount],
			 isnull([bonusClubSignUpSource],'')		as [bonusClubSignUpSource],
			 isnull([Country],'')						as [Country],
			 isnull([FrequencyCount3m],0)			as [FrequencyCount3m],
			 isnull([FrequencyCount6m],	0)		as [FrequencyCount6m],
			 isnull([FrequencyCount12m],0)			as [FrequencyCount12m],
			 isnull([FrequencyCount18m],0)			as [FrequencyCount18m],
			 isnull([FrequencyCount24m],0)			as [FrequencyCount24m],
			 isnull([FrequencyCount36m],0)			as [FrequencyCount36m],
			 isnull([FrequencyCountTTL],0)			as [FrequencyCountTTL],
			 isnull([RecencyCount3m],0)				as [RecencyCount3m],
			 isnull([RecencyCount6m],0)				as [RecencyCount6m],
			 isnull([RecencyCount12m],0)				as [RecencyCount12m],
			 isnull([RecencyCount18m],0)				as [RecencyCount18m],
		     isnull([RecencyCount24m],0)				as [RecencyCount24m],
			 isnull([RecencyCount36m],0)				as [RecencyCount36m],
			 isnull([RecencyCountTTL],0)				as [RecencyCountTTL],
			 isnull([MonetarySum3m],0)				as [MonetarySum3m],
			 isnull([MonetarySum6m],0)				as [MonetarySum6m],
			 isnull([MonetarySum12m],0)				as [MonetarySum12m],
			 isnull([MonetarySum18m],0)				as [MonetarySum18m],
			 isnull([MonetarySum24m],0)				as [MonetarySum24m],
			 isnull([MonetarySum36m],0)				as [MonetarySum36m],
			 isnull([MonetarySumTTL],0)				as [MonetarySumTTL],
			 isnull([FrequencyCount1m],0)			as [FrequencyCount1m],
			 isnull([RecencyCount1m],0)				as [RecencyCount1m],
			 isnull([MonetarySum1m],0)				as [MonetarySum1m],
			 isnull([address_1],'')					as [address_1],
			 isnull([address_2],'')					as [address_2],
			 isnull([address_3],'')					as [address_3],
			 isnull([address_4],'')					as [address_4],
			 isnull([post_code],'')					as [post_code],
			 isnull([mobile],'')						as [mobile],
			 isnull([locale],'')						as [locale],
			 isnull([text_opt_in],0)					as [text_opt_in],
			 isnull([LastTransactionDate],	'')		as [LastTransactionDate],
			 isnull([LastTransactionStore],	'')	as [LastTransactionStore],
			 isnull([PreferredStory],'')			as [PreferredStory],
			 isnull([Emailable],0)			as [Emailable],
			 isnull(LifetimePoints,0) as LifetimePoints,
			 FirstTransactionDate,
			 FirstStoreConcept,
			 isnull([FirstName],'')						as [FirstName],
			 isnull([LastName],'')						as [LastName]
		from dwstaging.dbo.tmpCrmDe1 with (nolock)
	) as source
on 
	target.customerNumber=source.CustomerNumber
when matched 
	and 
		isnull(target.[subscriberKey],'x')<>isnull(source.[EmailAddress],'x')
		or
		isnull(target.status,'x')<>isnull(source.status,'x')
		or
		isnull(target.[LastSentDate],'3030-12-31')<>isnull(source.[LastSentDate],'3030-12-31')
		or
		isnull(target.[LastOpenDate],'3030-12-31')<>isnull(source.[LastOpenDate],'3030-12-31')	 
		or
		isnull(target.[LastClickDate],'3030-12-31')<>isnull(source.[LastClickDate],'3030-12-31')
		or
		isnull(target.bonusClubMember,0)<>isnull(source.bonusClubMember,0)
		or 
		isnull(target.bonusClubMembershipType,'x')<>isnull(source.bonusClubMembershipType,'x')
		or
		isnull(target.[bonusClubPointsBalance],0)<>isnull(source.[bonusClubPointsBalance],0)
		or
		isnull(target.[hasOnlineAccount],0)<>isnull(source.[hasOnlineAccount],0)
		or
		isnull(target.[bonusClubSignUpSource],'x')<>isnull(source.[bonusClubSignUpSource],'x')	  
		or
		isnull(target.[Country],'x')<>isnull(source.[Country],'x')	  
		or
		isnull(target.[FrequencyCount3m],0)<>isnull(source.[FrequencyCount3m],0)
		or
		isnull(target.[FrequencyCount6m],0)<>isnull(source.[FrequencyCount6m],0)
		or
		isnull(target.[FrequencyCount12m],0)<>isnull(source. [FrequencyCount12m],0)
		or
		isnull(target.[FrequencyCount18m],0)<>isnull(source.	[FrequencyCount18m],0)  
		or
		isnull(target.[FrequencyCount24m],0)<>isnull(source.[FrequencyCount24m],0)
		or
		isnull(target.[FrequencyCount36m],0)<>isnull(source.[FrequencyCount36m],0)
		or
		isnull(target.[FrequencyCountTTL],0)<>isnull(source.[FrequencyCountTTL],0)	 
		or
		isnull(target.[RecencyCount3m],0)<>isnull(source.[RecencyCount3m],0)	 
		or
		isnull(target.[RecencyCount6m],0)<>isnull(source.[RecencyCount6m],0)
		or
		isnull(target.[RecencyCount12m],0)<>isnull(source.[RecencyCount12m],0)
		or
		isnull(target.[RecencyCount18m],0)<>isnull(source.[RecencyCount18m],0)   
		or
		isnull(target.[RecencyCount24m],0)<>isnull(source.[RecencyCount24m],0)	 
		or
		isnull(target.[RecencyCount36m],0)<>isnull(source.[RecencyCount36m],0)	
		or
		isnull(target.[RecencyCountTTL],0)<>isnull(source.[RecencyCountTTL],0)	 
		or
		isnull(target.[MonetarySum3m],0)<>isnull(source.[MonetarySum3m],0)	  
		or
		isnull(target.[MonetarySum6m],0)<>isnull(source.[MonetarySum6m],0)	 
		or
		isnull(target.[MonetarySum12m],0)<>isnull(source.[MonetarySum12m],0)	  
		or
		isnull(target.[MonetarySum18m],0)<>isnull(source.[MonetarySum18m],0)	  
		or
		isnull(target.[MonetarySum24m],0)<>isnull(source.[MonetarySum24m],0)
		or
		isnull(target.[MonetarySum36m],0)<>isnull(source.[MonetarySum36m],0)
		or
		isnull(target.[MonetarySumTTL],0)<>isnull(source.[MonetarySumTTL],0)	  
		or
		isnull(target.[FrequencyCount1m],0)<>isnull(source.[FrequencyCount1m],0)  
		or
		isnull(target.[RecencyCount1m],0)<>isnull(source.[RecencyCount1m],0)	  
		or
		isnull(target.[MonetarySum1m],0)<>isnull(source. [MonetarySum1m],0)
		or
		isnull(target.[address_1],'x')<>isnull(source.[address_1],'x')	 
		or
		isnull(target.[address_2],'x')<>isnull(source.[address_2],'x') 
		or
		isnull(target.[address_3],'x')<>isnull(source.[address_3],'x')	  
		or
		isnull(target.[address_4],'x')<>isnull(source.[address_4],'x')  
		or
		isnull(target.[post_code],'x')<>isnull(source.[post_code],'x')	  
		or
		isnull(target.[mobile],'x')<>isnull(source.[mobile],'x') 
		or
		isnull(target.[locale],'x')<>isnull(source.[locale],'x') 
		or
		isnull(target.[text_opt_in],0)<>isnull(source.[text_opt_in],0)
		or
		isnull(target.[LastTransactionDate],'3030-12-31')<>isnull(source.[LastTransactionDate],'3030-12-31')
		 or
		isnull(target.[LastTransactionStore],'x')<>isnull(source.[LastTransactionStore],'x')	
		  or
		isnull(target.[PreferredStory],'x')<>isnull(source.[PreferredStory],'x')
		  or
		isnull(target.[Emailable],0)<>isnull(source.[Emailable],0)
		or isnull(target.LifetimePoints,0)<>isnull(source.LifetimePoints,0)
		or isnull(target.FirstTransactionDate,getdate())<>isnull(source.FirstTransactionDate,getdate())
		or isnull(target.FirstStoreConcept,'x')<>isnull(source.FirstStoreConcept,'x')
		or isnull(target.FirstName,'x')<>isnull(source.FirstName,'x')
		or isnull(target.LastName,'x')<>isnull(source.LastName,'x')
		 
then update
	set
		target.subscriberKey=source.EmailAddress,
		target.emailAddress=source.EmailAddress,
		target.status=source.status,
		target.[LastSentDate]=source.[LastSentDate],
		target.[LastOpenDate]=source.[LastOpenDate],
		target.[LastClickDate]=source.[LastClickDate],
		target.bonusClubMember=source.bonusClubMember,
		target.bonusClubMembershipType=source.bonusClubMembershipType,
		target.[bonusClubPointsBalance]=source.[bonusClubPointsBalance],
		target.[hasOnlineAccount]=source.[hasOnlineAccount],
		target.[bonusClubSignUpSource]=source.[bonusClubSignUpSource],
		target.[Country]=source.[Country],
		target.[FrequencyCount3m]=source.[FrequencyCount3m],
		target.[FrequencyCount6m]=source.[FrequencyCount6m],
		target.[FrequencyCount12m]=source.[FrequencyCount12m],
		target.[FrequencyCount18m]=source.[FrequencyCount18m],
		target.[FrequencyCount24m]=source.[FrequencyCount24m],
		target.[FrequencyCount36m]=source.[FrequencyCount36m],
		target.[FrequencyCountTTL]=source.[FrequencyCountTTL],
		target.[RecencyCount3m]=source.[RecencyCount3m],
		target.[RecencyCount6m]=source.[RecencyCount6m],
		target.[RecencyCount12m]=source.[RecencyCount12m],
		target.[RecencyCount18m]=source.[RecencyCount18m],
		target.[RecencyCount24m]=source.[RecencyCount24m],
		target.[RecencyCount36m]=source.[RecencyCount36m],
		target.[RecencyCountTTL]=source.[RecencyCountTTL],
		target.[MonetarySum3m]=source.[MonetarySum3m],
		target.[MonetarySum6m]=source.[MonetarySum6m],
		target.[MonetarySum12m]=source.[MonetarySum12m],
		target.[MonetarySum18m]=source.[MonetarySum18m],
		target.[MonetarySum24m]=source.[MonetarySum24m],
		target.[MonetarySum36m]=source.[MonetarySum36m],
		target.[MonetarySumTTL]=source.[MonetarySumTTL],
		target.[FrequencyCount1m]=source.[FrequencyCount1m],
		target.[RecencyCount1m]=source.[RecencyCount1m],
		target.[MonetarySum1m]=source.[MonetarySum1m],
		target.[address_1]=source.[address_1],
		target.[address_2]=source.[address_2],
		target.[address_3]=source.[address_3],
		target.[address_4]=source.[address_4],
		target.[post_code]=source.[post_code],
		target.[mobile]=source.[mobile],
		target.[locale]=source.[locale],
		target.[text_opt_in]=source.[text_opt_in],
		target.[LastTransactionDate]=source.[LastTransactionDate],
		target.[LastTransactionStore]=source.[LastTransactionStore],
		target.[PreferredStory]=source.[PreferredStory],
		target.[Emailable]=source.[Emailable],
		target.LifetimePoints=source.LifetimePoints,
		target.FirstTransactionDate=source.FirstTransactionDate,
		target.FirstStoreConcept=source.FirstStoreConcept,
		target.FirstName=source.FirstName,
		target.LastName=source.LastName,
		target.UpdateDate=getdate()
when not matched by target
then insert
	(
	   [customerNumber],
       [SubscriberKey],
	   [emailAddress],
       [status],
       [dateJoined],
       [LastSentDate],
       [LastOpenDate],
       [LastClickDate],
       [bonusClubMember],
       [bonusClubMembershipType],
       [bonusClubPointsBalance],
       [hasOnlineAccount],
       [bonusClubSignUpSource],
       [Country],
       [FrequencyCount3m],
       [FrequencyCount6m],
       [FrequencyCount12m],
       [FrequencyCount18m],
       [FrequencyCount24m],
	   [FrequencyCount36m],
       [FrequencyCountTTL],
       [RecencyCount3m],
       [RecencyCount6m],
       [RecencyCount12m],
       [RecencyCount18m],
       [RecencyCount24m],
	   [RecencyCount36m],
       [RecencyCountTTL],
       [MonetarySum3m],
       [MonetarySum6m],
       [MonetarySum12m],
       [MonetarySum18m],
       [MonetarySum24m],
	   [MonetarySum36m],
       [MonetarySumTTL],
       [FrequencyCount1m],
       [RecencyCount1m],
       [MonetarySum1m],
       [address_1],
       [address_2],
       [address_3],
       [address_4],
       [post_code],
       [mobile],
       [locale],
       [text_opt_in],
       [InsertDate],
	   [LastTransactionDate],
	   [LastTransactionStore],
	   [PreferredStory],
	   [Emailable],
	   LifetimePoints,
	   FirstTransactionDate,
	   FirstStoreConcept,
	   FirstName,
	   LastName
	)
values
	(
       source.[CustomerNumber],
       source.[EmailAddress],
	   source.[EmailAddress],
       source.[status],
       source.[dateJoined],
       source.[LastSentDate],
       source.[LastOpenDate],
       source.[LastClickDate],
       source.[bonusClubMember],
       source.[bonusClubMembershipType],
       source.[bonusClubPointsBalance],
       source.[hasOnlineAccount],
       source.[bonusClubSignUpSource],
       source.[Country],
       source.[FrequencyCount3m],
       source.[FrequencyCount6m],
       source.[FrequencyCount12m],
       source.[FrequencyCount18m],
       source.[FrequencyCount24m],
	   source.[FrequencyCount36m],
       source.[FrequencyCountTTL],
       source.[RecencyCount3m],
       source.[RecencyCount6m],
       source.[RecencyCount12m],
       source.[RecencyCount18m],
       source.[RecencyCount24m],
	   source.[RecencyCount36m],
       source.[RecencyCountTTL],
       source.[MonetarySum3m],
       source.[MonetarySum6m],
       source.[MonetarySum12m],
       source.[MonetarySum18m],
       source.[MonetarySum24m],
	   source.[MonetarySum36m],
       source.[MonetarySumTTL],
       source.[FrequencyCount1m],
       source.[RecencyCount1m],
       source.[MonetarySum1m],
       source.[address_1],
       source.[address_2],
       source.[address_3],
       source.[address_4],
       source.[post_code],
       source.[mobile],
       source.[locale],
       source.[text_opt_in],
		getdate(),
	   source.[LastTransactionDate],
	   source.[LastTransactionStore],
	   source.[PreferredStory],
	   source.[Emailable],
	   source.LifetimePoints,
	   source.FirstTransactionDate,
	   source.FirstStoreConcept,
	   source.FirstName,
	   source.LastName
	)
--when not matched by source
--then delete
;
```

