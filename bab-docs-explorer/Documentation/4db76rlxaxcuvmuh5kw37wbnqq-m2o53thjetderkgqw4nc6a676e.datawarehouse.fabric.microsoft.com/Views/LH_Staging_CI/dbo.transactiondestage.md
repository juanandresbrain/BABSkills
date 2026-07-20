# dbo.transactiondestage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.transactiondestage"]
    dbo_transactiondestage(["dbo.transactiondestage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.transactiondestage |

## View Code

```sql
CREATE   VIEW [dbo].[transactiondestage]
AS
    SELECT [Units], [SKU] COLLATE Latin1_General_CI_AS AS [SKU], [Department] COLLATE Latin1_General_CI_AS AS [Department], [ShippingAmount], [OrderReference] COLLATE Latin1_General_CI_AS AS [OrderReference], [SubClass] COLLATE Latin1_General_CI_AS AS [SubClass], [LicensedOrNot], [SportsTeams] COLLATE Latin1_General_CI_AS AS [SportsTeams], [TransactionLineNumber], [UnitDiscountAmount], [GroupedTendersAmazon], [CurrencyType] COLLATE Latin1_General_CI_AS AS [CurrencyType], [MatchedByEmail] COLLATE Latin1_General_CI_AS AS [MatchedByEmail], [FulfillmentDate], [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [KeyStory] COLLATE Latin1_General_CI_AS AS [KeyStory], [MSTAT] COLLATE Latin1_General_CI_AS AS [MSTAT], [inDiscountFacts], [EmbroideryType] COLLATE Latin1_General_CI_AS AS [EmbroideryType], [ShippingType] COLLATE Latin1_General_CI_AS AS [ShippingType], [GroupedTendersPOParty], [SoundEligible], [GroupedTendersGiftCard], [EmployeeID], [isBundleOrSet], [isWebGift], [LifetimeVisitNumber], [IsBundle], [ProductHierarchyCode] COLLATE Latin1_General_CI_AS AS [ProductHierarchyCode], [GAAPSalesAmount], [TransactionDate], [SkinType] COLLATE Latin1_General_CI_AS AS [SkinType], [GroupedTendersKlarna], [GroupedTendersWeChatPay], [TransactionID] COLLATE Latin1_General_CI_AS AS [TransactionID], [Country] COLLATE Latin1_General_CI_AS AS [Country], [StoreNumber] COLLATE Latin1_General_CI_AS AS [StoreNumber], [ConsumerGroup] COLLATE Latin1_General_CI_AS AS [ConsumerGroup], [GroupedTendersOther], [GroupedTendersPartyDeposit], [OnlineExclusive], [Occasions] COLLATE Latin1_General_CI_AS AS [Occasions], [TransactionMonth], [Class] COLLATE Latin1_General_CI_AS AS [Class], [GroupedTendersCash], [StoreConcept] COLLATE Latin1_General_CI_AS AS [StoreConcept], [UpdatedTransaction], [CategoryType] COLLATE Latin1_General_CI_AS AS [CategoryType], [GroupedTendersAliPay], [TransactionYear] COLLATE Latin1_General_CI_AS AS [TransactionYear], [BasePointsEarned], [GroupedTendersFacebook], [GroupedTendersCreditDebit], [GroupedTendersPayPal], [NetRetailAmountwVAT], [IsSet]
    FROM LH_Staging.[dbo].[transactiondestage]
```

