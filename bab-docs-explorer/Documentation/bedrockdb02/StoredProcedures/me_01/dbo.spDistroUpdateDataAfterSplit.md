# dbo.spDistroUpdateDataAfterSplit

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spDistroUpdateDataAfterSplit"]
    dbo_distribution_split(["dbo.distribution_split"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.distribution_split |

## Stored Procedure Code

```sql
CREATE procEDURE [dbo].[spDistroUpdateDataAfterSplit]
-- =============================================================================================================
-- Name: spDistroUpdateDataAfterSplit
--
-- Description:	
--
-- Input:		@id
--
-- Output: 
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Missey	5/21/2010		added exported date
-- =============================================================================================================
	(
	@id bigint
	)
	
AS
	/* SET NOCOUNT ON */ 
	UPDATE distribution_split set released = 1, exported_date = GetDate() where id = @id
```

