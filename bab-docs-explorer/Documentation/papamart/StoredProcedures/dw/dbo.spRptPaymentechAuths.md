# dbo.spRptPaymentechAuths

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRptPaymentechAuths"]
    dbo_vwPT_Auth(["dbo.vwPT_Auth"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwPT_Auth |

## Stored Procedure Code

```sql
CREATE  procedure spRptPaymentechAuths
(@FirstDate as smalldatetime)
 as
/*
SELECT sMessageType, iClientId,sClientCountryCode, sOrderNumber,
 sOrderNumber_BABW, iPaymentNumber_BABW, sCC, sCC_secure, iCreditCardExpMonth, 
iCreditCardExpYear, sCreditCardType, iCurrencyCode, iCurrencyExponent, mAmount, mTaxAmount, 
 sBillToCountryCode, sShipToCountryCode, iStoreID, sEmployeeId, dTimeStamp, iProcStatus
, bIsApproved, sApprovalStatus, sRespCode, sAuthCode, sAvsResponseCode, sCvv2ResponseCode, sCavvResponseCode, sStatusMsg
, sTransactionId, sTransactionIndex, iBabwResponseCode
, sGuestErrorMessage, sDevErrorMessage, iExportStatus, dDateExported, sAWTransNo 
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1
and bisapproved=0

7316 total records
*/

declare @DateCCWebServiceOnEachServer as smalldatetime
set @DateCCWebServiceOnEachServer='11/2/06'

SELECT count(*) NUMBER, sum(mAmount) Total$, max(mAmount) Max$
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1 and dTimeStamp > @DateCCWebServiceOnEachServer
and dtimestamp > @FirstDate

SELECT count(*) NUMBER, bIsApproved
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1 and dTimeStamp > @DateCCWebServiceOnEachServer
and dtimestamp > @FirstDate
GROUP BY bIsApproved
order BY  count(*) DESC

SELECT count(*) NUMBER, bIsApproved,sMessageType, iClientId
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1 and dTimeStamp > @DateCCWebServiceOnEachServer
and dtimestamp > @FirstDate
GROUP BY bIsApproved,sMessageType, iClientId
order BY  count(*) DESC, iClientId, sMessageType, bIsApproved


SELECT count(*) NUMBER, bIsApproved,sMessageType, iClientId, sGuestErrorMessage
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1 and dTimeStamp > @DateCCWebServiceOnEachServer
and dtimestamp > @FirstDate
GROUP BY bIsApproved,sMessageType, iClientId, sGuestErrorMessage
order BY  count(*) DESC,iClientId, sMessageType, bIsApproved, sGuestErrorMessage



SELECT --count(*) NUMBER, 
bIsApproved, sRespCode,sMessageType, iClientId, sGuestErrorMessage
, sOrderNumber,  sOrderNumber_BABW, iPaymentNumber_BABW, sCC, sCC_secure, iCreditCardExpMonth, 
 iCreditCardExpYear, sCreditCardType, iCurrencyCode, iCurrencyExponent, mAmount, mTaxAmount, 
  sBillToCountryCode, sShipToCountryCode, iStoreID, sEmployeeId, dTimeStamp, iProcStatus
 , sApprovalStatus, sAuthCode
, sAvsResponseCode, sCvv2ResponseCode, sCavvResponseCode, sStatusMsg
 , sTransactionId, sTransactionIndex, iBabwResponseCode
-- , sDevErrorMessage, iExportStatus, dDateExported, sAWTransNo 
into #invalidData
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1 and dTimeStamp > @DateCCWebServiceOnEachServer
and dtimestamp > @FirstDate

and (
-- 	sGuestErrorMessage in (' Invalid value in message If you need further assistance please call a guest service representative at 0800 542 0635',
-- 		' An invalid character was entered. A-Z, 0-9, @, $, -, comma and <space> are valid characters. If you need further assistance please call a guest service representative at 0800 542 0635')
-- 	--or bIsApproved=1
	bIsApproved=0
     )
--GROUP BY bIsApproved,sMessageType, iClientId, sGuestErrorMessage
order BY  sOrderNumber
--count(*) DESC,
--sMessageType, bIsApproved, sGuestErrorMessage






SELECT [bIsApproved],sCC_secure
into #invalid2
 FROM bearwebdb.[WebCart_Commerce].[dbo].[vwPT_Auth]
where sordernumber in (select sordernumber from #invalidData)
group by  [bIsApproved],sCC_secure


SELECT count(*), [bIsApproved], [sRespCode] ,[sGuestErrorMessage], [sStatusMsg], [sAvsResponseCode]
	, [sCvv2ResponseCode], [iProcStatus], [sCavvResponseCode]
FROM bearwebdb.[WebCart_Commerce].[dbo].[vwPT_Auth]
where sordernumber in (select sordernumber from #invalidData)
group by  [bIsApproved], [sRespCode] ,[sGuestErrorMessage], [sStatusMsg], [sAvsResponseCode]
	, [sCvv2ResponseCode], [iProcStatus], [sCavvResponseCode]
order by  [bIsApproved], [sRespCode] ,[sGuestErrorMessage], [sStatusMsg], [sAvsResponseCode]
	, [sCvv2ResponseCode], [iProcStatus], [sCavvResponseCode]



SELECT  [bIsApproved], [sRespCode] ,[sGuestErrorMessage], [sStatusMsg], [sTransactionId], [sAvsResponseCode], [sCvv2ResponseCode]
,sOrderNumber, sCC_secure,  [sApprovalStatus], iCreditCardExpMonth, iCreditCardExpYear, sCreditCardType, mAmount
, [sBillToName], [sBillToAddress1], [sBillToAddress2], [sBillToAddress3], [sBillToAddress4]
, [sBillToCity], [sBillToStateProvince], [sBillToPostalCode], [sBillToCountryCode]
, [sBillToEmail], [sBillToPhone]
, [sShipToName], [sShipToAddress1], [sShipToAddress2], [sShipToAddress3], [sShipToAddress4]
, [sShipToCity], [sShipToStateProvince], [sShipToPostalCode], [sShipToCountryCode]
, [sShipToEmail], [sShipToPhone]
, [dTimeStamp], [iProcStatus]
, [sCavvResponseCode]
 FROM bearwebdb.[WebCart_Commerce].[dbo].[vwPT_Auth]
where sordernumber in (select sordernumber from #invalidData)
--and sordernumber='2789779x000001'
order by sCC_secure, sOrderNumber


/*
SELECT count(*) NUMBER, bIsApproved,sMessageType, iClientId, sGuestErrorMessage
--, sOrderNumber,
--  sOrderNumber_BABW, iPaymentNumber_BABW, sCC, sCC_secure, iCreditCardExpMonth, 
-- iCreditCardExpYear, sCreditCardType, iCurrencyCode, iCurrencyExponent, mAmount, mTaxAmount, 
--  sBillToCountryCode, sShipToCountryCode, iStoreID, sEmployeeId, dTimeStamp, iProcStatus
-- , sApprovalStatus, sRespCode, sAuthCode
--, sAvsResponseCode, sCvv2ResponseCode, sCavvResponseCode, sStatusMsg
-- , sTransactionId, sTransactionIndex, iBabwResponseCode
-- , sDevErrorMessage, iExportStatus, dDateExported, sAWTransNo 
FROM BearWebDB.WebCart_Commerce.dbo.vwPT_Auth
where bIsProduction=1 and dTimeStamp > @DateCCWebServiceOnEachServer
and dtimestamp > @FirstDate
GROUP BY bIsApproved,sMessageType, iClientId, sGuestErrorMessage
order BY  count(*) DESC,iClientId, sMessageType, bIsApproved, sGuestErrorMessage
*/
```

