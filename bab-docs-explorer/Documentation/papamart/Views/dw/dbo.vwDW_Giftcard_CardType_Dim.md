# dbo.vwDW_Giftcard_CardType_Dim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Giftcard_CardType_Dim"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Giftcard_CardType_Dim]
-- =============================================================================================================
-- Name: [dbo].[vwDW_Giftcard_CardType_Dim]
--
-- Description: Selects the Types of Giftcards
--
-- Dependencies: 
--
-- Revision History

--		Name:			Date:			Comments:
--		Gary Murrish	9/18/2013		Initial
-- =============================================================================================================

AS



SELECT
	'Regular' AS GiftcardType
UNION ALL
SELECT
	'Upsell' AS GiftcardType
```

