# dbo.sp_VoucherLookup

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_VoucherLookup"]
    cust_liability(["cust_liability"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| cust_liability |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Tim Paschedag
-- ALTER  date: 9/17/2008
-- Description:	Modified to add lookup by Voucher Voucher Number & Customer Number
--		Name:			Date:			Comments:
--		Garyd			08/30/2010		Initial version in source control
--		Keith Missey	01/11/2011		added case statement
--exec sp_VoucherLookup '721838780', '0107431345840679'
-- =============================================
CREATE PROCEDURE [dbo].[sp_VoucherLookup]
	-- Add the parameters for the stored procedure here
	@sfs_Number varchar(20) = 'NoData',
	@voucher_number varchar(20) = 'NoData'
AS
BEGIN

	SET NOCOUNT ON;

IF @sfs_Number != 'NoData'
BEGIN
	select reference_no as VoucherNumber, 
		   date_issued as [Date], 
		   CASE 
			WHEN expiry_date < GETDATE() THEN '0.00'
			ELSE liability_amount
			END as Balance, 
		   first_name as FirstName, 
		   last_name as LastName,
	       address_1 as Address, 
		   address_2 as Address2, 
		   city as City, 
		   state as State, 
		   post_code as ZipCode, 
		   customer_no as GuestNumber
from cust_liability with (nolock)
where reference_type=31 AND customer_no = @sfs_Number
END

IF @voucher_number != 'NoData'
BEGIN
	select reference_no as VoucherNumber, 
		date_issued as [Date], 
		CASE 
			WHEN expiry_date < GETDATE() THEN '0.00'
			ELSE liability_amount
			END as Balance,
		first_name as FirstName, 
		last_name as LastName,address_1 as Address, 
		address_2 as Address2, 
		city as City, 
		state as State, 
		post_code as ZipCode, 
		customer_no as GuestNumber
	from cust_liability with (nolock)
	where reference_type=31 AND (reference_no LIKE @voucher_number)
END

END
```

