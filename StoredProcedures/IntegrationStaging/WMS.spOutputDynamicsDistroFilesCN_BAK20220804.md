# WMS.spOutputDynamicsDistroFilesCN_BAK20220804

**Database:** IntegrationStaging  

## Architecture Diagram

```mermaid
flowchart LR
    SP["WMS.spOutputDynamicsDistroFilesCN_BAK20220804"]
    WMS_DynamicsTo3PLOrderExport(["WMS.DynamicsTo3PLOrderExport"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| WMS.DynamicsTo3PLOrderExport |

## Stored Procedure Code

```sql
CREATE proc [WMS].[spOutputDynamicsDistroFilesCN_BAK20220804]

as

set nocount on

IF (Object_ID('tempdb..##CNDistros3970') IS NOT NULL) DROP TABLE ##CNDistros3970
select *
into ##CNDistros3970
from WMS.DynamicsTo3PLOrderExport 
where ExportDate is null 
and SourceID in ('3970')

IF (Object_ID('tempdb..##CNDistros8502') IS NOT NULL) DROP TABLE ##CNDistros8502
select *
into ##CNDistros8502
from WMS.DynamicsTo3PLOrderExport 
where ExportDate is null 
and SourceID in ('8502')

IF (Object_ID('tempdb..##CNDistros8505') IS NOT NULL) DROP TABLE ##CNDistros8505
select *
into ##CNDistros8505
from WMS.DynamicsTo3PLOrderExport 
where ExportDate is null 
and SourceID in ('8505')

IF (Object_ID('tempdb..##CNDistros3980') IS NOT NULL) DROP TABLE ##CNDistros3980
select *
into ##CNDistros3980
from WMS.DynamicsTo3PLOrderExport 
where ExportDate is null 
and SourceID in ('3980')

if (select count(*) from ##CNDistros3970) > 0

BEGIN
	--OUTPUT CSV FILE 
	declare @A_counter int,
			@A_shipment varchar(20),
			@A_location varchar(4),
			@A_rectype int,
			@A_query varchar(1000),
			@A_date varchar(52),
			@A_file_name varchar(100),
			@A_file_location varchar(100),
			@A_server varchar(20),
			@A_database varchar(20),
			@A_bcp varchar(1000)

	select @A_counter = count(distinct document_number) from ##CNDistros3970

	while @A_counter > 0

		begin
			select @A_shipment = max(document_number) from ##CNDistros3970
			select @A_location = max(destid) from ##CNDistros3970 where document_number = @A_shipment
			select @A_rectype = max(rec_type) from ##CNDistros3970 where document_number = @A_shipment

			set @A_query = 'set nocount on select document_number, destid, rec_type, message, style_code, quantity, convert(varchar, getdate(), 101) release_date, distribution_number, ref_field_1, convert(varchar, expected_ship_date, 101) expected_ship_date from ##CNDistros3970 where document_number = ' + @A_shipment + 'order by style_code'
			select @A_date = replace(replace(replace(replace(convert(varchar, getdate(), 121), ' ', ''), '-', ''), ':', ''), '.', '')
			set @A_file_location = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\Distros\'
			set @A_file_name = 'DISTRIBUTION_CN_3970' + cast(@A_rectype as varchar) + '-' + @A_location + '.' + @A_date + '.csv'
			set @A_server = 'stl-ssis-p-01'
			set @A_bcp = 'bcp "' + @A_query + '" queryout "' + @A_file_location + @A_file_name + '"  -T -t, -c -S' + @A_server 

			exec master..xp_cmdshell @A_bcp

			--Set ExportDate
			update d
			set d.ExportDate = getdate()
			from WMS.DynamicsTo3PLOrderExport d
			join ##CNDistros3970 e 
				on d.RecID=e.RecID
			where e.document_number=@A_shipment

			delete from ##CNDistros3970 where document_number = @A_shipment
			select @A_counter = count(distinct document_number) from ##CNDistros3970

			if @A_counter < 1

			break
		else
			continue

		end


END


--===============================================================================================
--EXPORT DISTROS FOR WHSE 8502
--===============================================================================================
		

if (select count(*) from ##CNDistros8502) > 0

BEGIN
		--OUTPUT CSV FILE 
		declare @C_counter int,
				@C_shipment varchar(20),
				@C_location varchar(4),
				@C_rectype int,
				@C_query varchar(1000),
				@C_date varchar(52),
				@C_file_name varchar(100),
				@C_file_location varchar(100),
				@C_server varchar(20),
				@C_bcp varchar(1000)

		select @C_counter = count(distinct document_number) from ##CNDistros8502

		while @C_counter > 0

			begin
				select @C_shipment = max(document_number) from ##CNDistros8502
				select @C_location = max(destid) from ##CNDistros8502 where document_number = @C_shipment
				select @C_rectype = max(rec_type) from ##CNDistros8502 where document_number = @C_shipment

				set @C_query = 'set nocount on select document_number, destid, rec_type, message, style_code, quantity, convert(varchar, getdate(), 101) release_date, distribution_number, ref_field_1, convert(varchar, expected_ship_date, 101) expected_ship_date from ##CNDistros8502 where document_number = ' + @C_shipment + 'order by style_code'
				select @C_date = replace(replace(replace(replace(convert(varchar, getdate(), 121), ' ', ''), '-', ''), ':', ''), '.', '')
				set @C_file_location = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\Distros\'
				set @C_file_name = 'DISTRIBUTION_CN_8502' + cast(@C_rectype as varchar) + '-' + @C_location + '.' + @C_date + '.csv'
				set @C_server = 'stl-ssis-p-01'
				set @C_bcp = 'bcp "' + @C_query + '" queryout "' + @C_file_location + @C_file_name + '"  -T -t, -c -S' + @C_server 

				exec master..xp_cmdshell @C_bcp

				update d
				set d.ExportDate = getdate()
				from WMS.DynamicsTo3PLOrderExport d
				join ##CNDistros8502 e 
					on d.RecID=e.RecID
				where e.document_number=@C_shipment

				delete from ##CNDistros8502 where document_number = @C_shipment
				select @C_counter = count(distinct document_number) from ##CNDistros8502

				if @C_counter < 1

				break
			else
				continue

			end


END


--===============================================================================================
--EXPORT DISTROS FOR WHSE 8505
--===============================================================================================

if (select count(*) from ##CNDistros8505) > 0

BEGIN

	--OUTPUT CSV FILE 
	declare @D_counter int,
			@D_shipment varchar(20),
			@D_location varchar(4),
			@D_rectype int,
			@D_query varchar(1000),
			@D_date varchar(52),
			@D_file_name varchar(100),
			@D_file_location varchar(100),
			@D_server varchar(20),
			@D_bcp varchar(1000)

	select @D_counter = count(distinct document_number) from ##CNDistros8505

	while @D_counter > 0

		begin
			select @D_shipment = max(document_number) from ##CNDistros8505
			select @D_location = max(destid) from ##CNDistros8505 where document_number = @D_shipment
			select @D_rectype = max(rec_type) from ##CNDistros8505 where document_number = @D_shipment

			set @D_query = 'set nocount on select document_number, destid, rec_type, message, style_code, quantity, convert(varchar, getdate(), 101) release_date, distribution_number, ref_field_1, convert(varchar, expected_ship_date, 101) expected_ship_date from ##CNDistros8505 where document_number = ' + @D_shipment + 'order by style_code'
			select @D_date = replace(replace(replace(replace(convert(varchar, getdate(), 121), ' ', ''), '-', ''), ':', ''), '.', '')
			set @D_file_location = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\Distros\'
			set @D_file_name = 'DISTRIBUTION_CN_8505' + cast(@D_rectype as varchar) + '-' + @D_location + '.' + @D_date + '.csv'
			set @D_server = 'stl-ssis-p-01'
			set @D_bcp = 'bcp "' + @D_query + '" queryout "' + @D_file_location + @D_file_name + '"  -T -t, -c -S' + @D_server 

			exec master..xp_cmdshell @D_bcp

			update d
			set d.ExportDate = getdate()
			from WMS.DynamicsTo3PLOrderExport d
			join ##CNDistros8505 e 
				on d.RecID=e.RecID
			where e.document_number=@D_shipment

			delete from ##CNDistros8505 where document_number = @D_shipment
			select @D_counter = count(distinct document_number) from ##CNDistros8505

			if @D_counter < 1

			break
		else
			continue

		end


END

---========================
--	 3980
--=============================


if (select count(*) from ##CNDistros3980) > 0

BEGIN
	--OUTPUT CSV FILE 
	declare @B_counter int,
			@B_shipment varchar(20),
			@B_location varchar(4),
			@B_rectype int,
			@B_query varchar(1000),
			@B_date varchar(52),
			@B_file_name varchar(100),
			@B_file_location varchar(100),
			@B_server varchar(20),
			@B_database varchar(20),
			@B_bcp varchar(1000)

	select @B_counter = count(distinct document_number) from ##CNDistros3980

	while @B_counter > 0

		begin
			select @B_shipment = max(document_number) from ##CNDistros3980
			select @B_location = max(destid) from ##CNDistros3980 where document_number = @B_shipment
			select @B_rectype = max(rec_type) from ##CNDistros3980 where document_number = @B_shipment

			set @B_query = 'set nocount on select document_number, destid, rec_type, message, style_code, quantity, convert(varchar, getdate(), 101) release_date, distribution_number, ref_field_1, convert(varchar, expected_ship_date, 101) expected_ship_date from ##CNDistros3980 where document_number = ' + @B_shipment + 'order by style_code'
			select @B_date = replace(replace(replace(replace(convert(varchar, getdate(), 121), ' ', ''), '-', ''), ':', ''), '.', '')
			set @B_file_location = '\\kermode\FileRepository\MERCHANDISING\CN_Distro\OUTBOUND\Distros\'
			set @B_file_name = 'DISTRIBUTION_CN_3980' + cast(@B_rectype as varchar) + '-' + @B_location + '.' + @B_date + '.csv'
			set @B_server = 'stl-ssis-p-01'
			set @B_bcp = 'bcp "' + @B_query + '" queryout "' + @B_file_location + @B_file_name + '"  -T -t, -c -S' + @B_server 

			exec master..xp_cmdshell @B_bcp

			--Set ExportDate
			update d
			set d.ExportDate = getdate()
			from WMS.DynamicsTo3PLOrderExport d
			join ##CNDistros3980 e 
				on d.RecID=e.RecID
			where e.document_number=@B_shipment

			delete from ##CNDistros3980 where document_number = @B_shipment
			select @B_counter = count(distinct document_number) from ##CNDistros3980

			if @B_counter < 1

			break
		else
			continue

		end


END
```

