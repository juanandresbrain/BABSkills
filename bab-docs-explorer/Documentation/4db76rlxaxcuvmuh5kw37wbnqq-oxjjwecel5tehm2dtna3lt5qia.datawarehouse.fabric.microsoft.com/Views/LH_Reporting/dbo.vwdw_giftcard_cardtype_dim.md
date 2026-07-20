# dbo.vwdw_giftcard_cardtype_dim

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-oxjjwecel5tehm2dtna3lt5qia.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwdw_giftcard_cardtype_dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW vwdw_giftcard_cardtype_dim
-- =============================================================================================================  
-- Name: [dbo].[vwDW_Giftcard_CardType_Dim]  
--  
-- Description: Selects the Types of Giftcards  
--  
-- Dependencies:   
--  
-- Revision History  
  
--  Name:   Date:   Comments:  
--  Gary Murrish 9/18/2013  Initial  
-- =============================================================================================================  
  
AS  
  
  
  
SELECT  
 'Regular' AS GiftcardType  
UNION ALL  
SELECT  
 'Upsell' AS GiftcardType
```

