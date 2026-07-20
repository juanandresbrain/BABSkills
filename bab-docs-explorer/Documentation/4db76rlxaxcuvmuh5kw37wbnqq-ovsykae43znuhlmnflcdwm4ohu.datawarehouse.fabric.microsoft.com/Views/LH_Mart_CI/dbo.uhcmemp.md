# dbo.uhcmemp

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.uhcmemp"]
    dbo_uhcmemp(["dbo.uhcmemp"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.uhcmemp |

## View Code

```sql
; CREATE   VIEW [dbo].[uhcmemp] AS     SELECT [efoPhoneExtension] COLLATE Latin1_General_CI_AS AS [efoPhoneExtension], [EepNameFirst] COLLATE Latin1_General_CI_AS AS [EepNameFirst], [EecLocation] COLLATE Latin1_General_CI_AS AS [EecLocation], [EecSalaryOrHourly] COLLATE Latin1_General_CI_AS AS [EecSalaryOrHourly], [TerminatedEnteredDate] COLLATE Latin1_General_CI_AS AS [TerminatedEnteredDate], [EecEmplStatus] COLLATE Latin1_General_CI_AS AS [EecEmplStatus], [EecDateOfOriginalHire] COLLATE Latin1_General_CI_AS AS [EecDateOfOriginalHire], [EepNameMiddle] COLLATE Latin1_General_CI_AS AS [EepNameMiddle], [Country] COLLATE Latin1_General_CI_AS AS [Country], [FullName] COLLATE Latin1_General_CI_AS AS [FullName], [City] COLLATE Latin1_General_CI_AS AS [City], [EepNameLast] COLLATE Latin1_General_CI_AS AS [EepNameLast], [EepNamePreferred] COLLATE Latin1_General_CI_AS AS [EepNamePreferred], [Postal Code] COLLATE Latin1_General_CI_AS AS [Postal Code], [WorkPhoneNumber] COLLATE Latin1_General_CI_AS AS [WorkPhoneNumber], [LocDesc] COLLATE Latin1_General_CI_AS AS [LocDesc], [TermEmailSentFlag], [PhoneNumber] COLLATE Latin1_General_CI_AS AS [PhoneNumber], [DateOfBirth] COLLATE Latin1_General_CI_AS AS [DateOfBirth], [EepAddressEMail2] COLLATE Latin1_General_CI_AS AS [EepAddressEMail2], [SupervisorPosition] COLLATE Latin1_General_CI_AS AS [SupervisorPosition], [HireSentFlag], [SupervisorID] COLLATE Latin1_General_CI_AS AS [SupervisorID], [UpdateDate], [JbcJobCode] COLLATE Latin1_General_CI_AS AS [JbcJobCode], [EepEEID] COLLATE Latin1_General_CI_AS AS [EepEEID], [TerminatedEffectiveDate] COLLATE Latin1_General_CI_AS AS [TerminatedEffectiveDate], [EecDateOfLastHire] COLLATE Latin1_General_CI_AS AS [EecDateOfLastHire], [EecOrgLvl1Description] COLLATE Latin1_General_CI_AS AS [EecOrgLvl1Description], [LocationName] COLLATE Latin1_General_CI_AS AS [LocationName], [EecOrgLvl1Code] COLLATE Latin1_General_CI_AS AS [EecOrgLvl1Code], [EepAddressEMail] COLLATE Latin1_General_CI_AS AS [EepAddressEMail], [SupervisorName] COLLATE Latin1_General_CI_AS AS [SupervisorName], [Address] COLLATE Latin1_General_CI_AS AS [Address], [TerminatedFlag] COLLATE Latin1_General_CI_AS AS [TerminatedFlag], [SendUpdateFlag], [TerminationDate] COLLATE Latin1_General_CI_AS AS [TerminationDate], [sAMAccountName] COLLATE Latin1_General_CI_AS AS [sAMAccountName], [EfoPhoneNumber] COLLATE Latin1_General_CI_AS AS [EfoPhoneNumber], [InsertDate], [State/Province] COLLATE Latin1_General_CI_AS AS [State/Province], [FaxNumber] COLLATE Latin1_General_CI_AS AS [FaxNumber], [EepCompanyCode] COLLATE Latin1_General_CI_AS AS [EepCompanyCode], [JbcLongDesc] COLLATE Latin1_General_CI_AS AS [JbcLongDesc]     FROM [dbo].[uhcmemp]
```

