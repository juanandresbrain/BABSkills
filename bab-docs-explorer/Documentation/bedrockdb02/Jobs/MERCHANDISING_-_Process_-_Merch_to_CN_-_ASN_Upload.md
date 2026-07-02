# Job: MERCHANDISING - Process - Merch to CN - ASN Upload

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** No description available.

## Architecture Diagram

```mermaid
flowchart LR
    JOB["MERCHANDISING - Process - Merch to CN - ASN Upload"]
    JOB --> Generate_ASN_File_for_Aptos_POs_1["Step 1: Generate ASN File for Aptos POs [TSQL]"]`n    JOB --> Check_Directory_For_Aptos_or_D365_ASN_files_and_FTP_2["Step 2: Check Directory For Aptos or D365 ASN files and FTP [TSQL]"]`n```

## Steps

### Step 1: Generate ASN File for Aptos POs
**Subsystem:** TSQL  

```sql
exec spMerchandisingOutputAsnCN
```

### Step 2: Check Directory For Aptos or D365 ASN files and FTP
**Subsystem:** TSQL  

```sql
IF (Object_ID('tempdb..#ASNASNfiles') IS NOT NULL) DROP TABLE #ASNfiles
create table #ASNfiles (output varchar(1000))
insert #ASNfiles exec master..xp_cmdshell 'dir \\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\ASN\*.csv /B'
delete from #ASNfiles where output is null or output = 'File Not Found'

if (select count(*) from #ASNfiles) > 0

Begin

	exec spMerchandisingFtpCN_ASN

End 
```


