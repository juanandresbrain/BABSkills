# dbo.spClubBABW_Select_SerializedCouponExists

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spClubBABW_Select_SerializedCouponExists"]
    cust_liability(["cust_liability"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| cust_liability |

## Stored Procedure Code

```sql
create PROCEDURE [dbo].[spClubBABW_Select_SerializedCouponExists] 
-- =====================================================================================================
-- Name: spClubBABW_Select_SerializedCouponExists
--
-- Description:	Returns Ridemarkerz booked parties broken out by store and booking method
--
-- Input:	
--			@CouponCode		Varchar(50)	Passed in from Club BABW web app to match against coupon
--										reference_no
--
-- Output: Resultset with the following columns:
--			reference_no
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		Matt Ludtke 	1/28/2011		Created using code from Ken Schlobohm of Oakwood Team
-- =====================================================================================================

      -- Add the parameters for the stored procedure here
      @CouponCode Varchar(50)
AS
BEGIN
      -- Insert statements for procedure here
      SELECT reference_no
      FROM cust_liability with (nolock)
      WHERE reference_no = @CouponCode;
END
```

