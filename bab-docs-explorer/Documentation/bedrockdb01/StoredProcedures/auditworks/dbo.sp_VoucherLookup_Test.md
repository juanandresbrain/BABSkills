# dbo.sp_VoucherLookup_Test

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_VoucherLookup_Test"]
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
-- Create date: 5/19/2008
-- Description:	SP for VoucherLookup Application
-- =============================================
CREATE PROCEDURE [dbo].[sp_VoucherLookup_Test]
	-- Add the parameters for the stored procedure here
	@customer_number varchar(20) = 'NoData',
	@voucher_number varchar(20) = 'NoData',
	@refType int
AS
BEGIN

	SET NOCOUNT ON;

IF @customer_number != 'NoData'
BEGIN
	select reference_no as VoucherNumber, 
		   date_issued as [Date], 
		   liability_amount as Balance, 
		   first_name as FirstName, 
		   last_name as LastName,
	       address_1 as Address, 
		   address_2 as Address2, 
		   city as City, 
		   state as State, 
		   post_code as ZipCode, 
		   customer_no as GuestNumber,
		   expiry_date as ExpiryDate,
		   email_address as email,
		   forfeited_flag as ForfeitedFlag
from cust_liability with (nolock)
where reference_type=@refType AND customer_no = @customer_number
END

IF @voucher_number != 'NoData'
BEGIN
	select reference_no as VoucherNumber, 
		date_issued as [Date], 
		liability_amount as Balance, 
		first_name as FirstName, 
		last_name as LastName,address_1 as Address, 
		address_2 as Address2, 
		city as City, 
		state as State, 
		post_code as ZipCode, 
		customer_no as GuestNumber,
		expiry_date as ExpiryDate,
		email_address as email,
		forfeited_flag as ForfeitedFlag
	from cust_liability with (nolock)
	where reference_type=@refType AND (reference_no LIKE @voucher_number)

END

END
```

