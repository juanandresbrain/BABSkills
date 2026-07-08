# dbo.spCheckToSeeIfCLIPRefNoAlreadyExists

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCheckToSeeIfCLIPRefNoAlreadyExists"]
    SUPPORT_VoucherImportProgramLiabilityNumbers(["SUPPORT.VoucherImportProgramLiabilityNumbers"]) --> SP
    cust_liability(["cust_liability"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| SUPPORT.VoucherImportProgramLiabilityNumbers |
| cust_liability |

## Stored Procedure Code

```sql
CREATE    proc [dbo].[spCheckToSeeIfCLIPRefNoAlreadyExists]
    @ReferenceNumber		varchar(20) ,
   @ReferenceType                    smallint,
    @ReturnValue		int OUTPUT

AS
-- =====================================================================================================
-- Name: spCheckToSeeIfCLIPRefNoAlreadyExists
--
-- Description:	Checks for existence of liability.
--
-- Input:	
--			voucher identifiers
--
-- Output: Resultset with the following columns:
--			Validation flag
--
-- Dependencies: None
--
-- Revision History
--		Name:			Date:			Comments:
--		?				08/24/2010		Initial version source control
-- exec spCheckToSeeIfCLIPRefNoAlreadyExists 64953192523961066, 35, 0 
-- =====================================================================================================

    SET @ReturnValue = 0
    /* check if the store exists first. else increment store number. */
    SELECT @ReturnValue= count(reference_no)
      FROM auditworks.SUPPORT.VoucherImportProgramLiabilityNumbers WITH (NOLOCK)
     WHERE reference_no = @ReferenceNumber
	AND reference_type = @ReferenceType 
	AND key_store_no = -1	
    
    if @ReturnValue > 0 return @ReturnValue

    SELECT @ReturnValue= count(reference_no)
      FROM cust_liability WITH (NOLOCK)
     WHERE reference_no = @ReferenceNumber
	AND reference_type = @ReferenceType 
	AND key_store_no = -1

    if @ReturnValue > 0 return @ReturnValue
```

