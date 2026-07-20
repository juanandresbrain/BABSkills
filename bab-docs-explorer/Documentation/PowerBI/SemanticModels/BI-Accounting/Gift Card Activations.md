# Gift Card Activations

**Workspace:** BI-Accounting  
**Dataset ID:** 5082c839-b2bf-41a1-8aed-346dbee2a96a  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| DateTableTemplate_b6814105-aadb-4fa7-b980-25d97abf98b3 | 8 | 0 | Yes |
| Calendar | 36 | 0 |  |
| LocalDateTable_0af06871-dcc3-4102-b805-8706ba2d636e | 8 | 0 | Yes |
| LocalDateTable_261c3579-1319-40d0-83b0-050aab355d89 | 8 | 0 | Yes |
| Locations (Store MDM) | 42 | 0 |  |
| LocalDateTable_055586fe-cc31-448a-8096-ad765664c40a | 8 | 0 | Yes |
| LocalDateTable_64c9f10f-dc16-466f-bff8-2c507f4308b7 | 8 | 0 | Yes |
| LocalDateTable_f21e200a-2634-4aa9-af9e-ee5d7b78d0a9 | 8 | 0 | Yes |
| Business Units | 10 | 0 |  |
| LocalDateTable_4c9b482a-789f-493c-b8d9-90d97e039cc2 | 8 | 0 | Yes |
| LocalDateTable_69a82fc8-c1c8-40e8-91d7-00b3fae0e920 | 8 | 0 | Yes |
| Gift Card | 18 | 0 |  |

## Measures

_No measures detected._

## Power Query Source (per table)

### DateTableTemplate_b6814105-aadb-4fa7-b980-25d97abf98b3

```sql
Calendar(Date(2015,1,1), Date(2015,1,1))
```

### Calendar

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [CreateNavigationProperties=false]),
    dbo_date_dim = Source{[Schema="dbo",Item="date_dim"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(dbo_date_dim,{{"actual_date", "Actual Datetime"}, {"fiscal_year", "Fiscal Year"}, {"season", "Season"}, {"fiscal_quarter", "Fiscal Quarter"}, {"fiscal_period", "Fiscal Month"}, {"fiscal_week", "Fiscal Week"}, {"month", "Calendar Month Id"}, {"year", "Calendar Year"}, {"month_name", "Calendar Month Name"}, {"day_of_month", "Day of Calendar Month"}, {"day_of_year", "Day of Calendar Year"}, {"day_name", "Day Name"}, {"weekend_y_n", "Is Weekend"}, {"day_of_week", "Day of Week"}, {"day_id", "Running Fiscal Day Id"}, {"week_of_period", "Week of Fiscal Month"}, {"week_of_quarter", "Week of Fiscal Quarter"}, {"period_of_quarter", "Month of Fiscal Quarter"}, {"holiday_period_code", "Holiday Period Code"}, {"week_id", "Running Fiscal Week Id"}, {"period_id", "Running Fiscal Month Id"}, {"quarter_id", "Running Fiscal Quarter Id"}, {"org_fiscal_quarter", "Fiscal Quarter 2"}, {"org_fiscal_period", "Fiscal Month 2"}, {"org_fiscal_week", "Fiscal Week 2"}, {"org_week_of_period", "Week of Fiscal Month 2"}, {"org_week_of_quarter", "Week of Fiscal Quarter 2"}, {"org_period_of_quarter", "Month of Fiscal Quarter 2"}}),
    #"Filtered Rows | Fiscal Year > 2018" = Table.SelectRows(#"Renamed Columns", each ([Fiscal Year] > 2018)),
    #"Inserted Date | Actual Date" = Table.AddColumn(#"Filtered Rows | Fiscal Year > 2018", "Actual Date", each Date.From([Actual Datetime]), type date),
    #"Removed Columns | Duplicates" = Table.RemoveColumns(#"Inserted Date | Actual Date",{"Fiscal Quarter 2", "Fiscal Month 2", "Fiscal Week 2", "Week of Fiscal Month 2", "Week of Fiscal Quarter 2", "Month of Fiscal Quarter 2", "Calendar Month Name", "Calendar Month Id"}),
    #"Sorted Rows | Actual Datetime ASC" = Table.Sort(#"Removed Columns | Duplicates",{{"Actual Datetime", Order.Ascending}}),
    #"Added Custom | Fiscal Year (Header)" = Table.AddColumn(#"Sorted Rows | Actual Datetime ASC", "Fiscal Year (Header)", each "FY" & Text.From([Fiscal Year])),
    #"Added Custom | Fiscal Quarter (Header)" = Table.AddColumn(#"Added Custom | Fiscal Year (Header)", "Fiscal Quarter (Header)", each "FQ" & Text.From([Fiscal Quarter])),
    #"Added Conditional Column | Fiscal Month (Name)" = Table.AddColumn(#"Added Custom | Fiscal Quarter (Header)", "Fiscal Month (Name)", each if [Fiscal Month] = 1 then "Febuary" else if [Fiscal Month] = 2 then "March" else if [Fiscal Month] = 3 then "April" else if [Fiscal Month] = 4 then "May" else if [Fiscal Month] = 5 then "June" else if [Fiscal Month] = 6 then "July" else if [Fiscal Month] = 7 then "August" else if [Fiscal Month] = 8 then "September" else if [Fiscal Month] = 9 then "October" else if [Fiscal Month] = 10 then "November" else if [Fiscal Month] = 11 then "December" else if [Fiscal Month] = 12 then "January" else null),
    #"Inserted Month Name | Calendar Month (Name)" = Table.AddColumn(#"Added Conditional Column | Fiscal Month (Name)", "Calendar Month (Name)", each Date.MonthName([Actual Datetime]), type text),
    #"Inserted Month | Calendar Month INT" = Table.AddColumn(#"Inserted Month Name | Calendar Month (Name)", "Calendar Month", each Date.Month([Actual Datetime]), Int64.Type),
    #"Added Custom | Fiscal Month (Header)" = Table.AddColumn(#"Inserted Month | Calendar Month INT", "Fiscal Month (Header)", each Text.PadStart(Text.From([Fiscal Month]),2,"0") & "-" & [#"Fiscal Month (Name)"]),
    #"Added Custom | Calendar Month (Header)" = Table.AddColumn(#"Added Custom | Fiscal Month (Header)", "Calendar Month (Header)", each Text.PadStart(Text.From([#"Calendar Month"]),2,"0") & "-" & [#"Calendar Month (Name)"]),
    #"Added Custom | Fiscal Week (Header)" = Table.AddColumn(#"Added Custom | Calendar Month (Header)", "Fiscal Week (Header)", each "FW" & Text.PadStart(Text.From([Fiscal Week]),2,"0")),
    #"Inserted Quarter | Calendar Quarter INT" = Table.AddColumn(#"Added Custom | Fiscal Week (Header)", "Calendar Quarter", each Date.QuarterOfYear([Actual Datetime]), Int64.Type),
    #"Added Custom | Calendar Quarter (Header)" = Table.AddColumn(#"Inserted Quarter | Calendar Quarter INT", "Calendar Quarter (Header)", each "CQ" & Text.From([#"Calendar Quarter"])),
    #"Added Custom | Calendar Year (Header)" = Table.AddColumn(#"Added Custom | Calendar Quarter (Header)", "Calendar Year (Header)", each "CY" & Text.From([Calendar Year])),
    #"Inserted Week of Year | Calendar Week INT" = Table.AddColumn(#"Added Custom | Calendar Year (Header)", "Calendar Week", each Date.WeekOfYear([Actual Datetime]), Int64.Type),
    #"Added Custom | Calendar Week (Header)" = Table.AddColumn(#"Inserted Week of Year | Calendar Week INT", "Calendar Week (Header)", each "CW" & Text.PadStart(Text.From([Calendar Week]),2,"0")),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Added Custom | Calendar Week (Header)","",null,Replacer.ReplaceValue,{"Holiday Period Code"}),
    #"Reordered Columns" = Table.ReorderColumns(#"Replaced Value | """" with NULL",{"date_key", "Actual Datetime", "Actual Date", "Fiscal Year", "Fiscal Quarter", "Fiscal Month", "Fiscal Month (Name)", "Fiscal Week", "Calendar Year", "Calendar Quarter", "Calendar Month", "Calendar Month (Name)", "Calendar Week", "Day Name", "Is Weekend", "Holiday Period Code", "Season", "Day of Week", "Day of Calendar Month", "Day of Calendar Year", "Week of Fiscal Month", "Week of Fiscal Quarter", "Month of Fiscal Quarter", "Running Fiscal Day Id", "Running Fiscal Week Id", "Running Fiscal Month Id", "Running Fiscal Quarter Id", "Fiscal Year (Header)", "Fiscal Quarter (Header)",  "Fiscal Month (Header)", "Fiscal Week (Header)", "Calendar Year (Header)", "Calendar Quarter (Header)", "Calendar Month (Header)", "Calendar Week (Header)"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Reordered Columns",{{"Fiscal Month (Name)", type text}, {"Fiscal Year (Header)", type text}, {"Fiscal Quarter (Header)", type text}, {"Fiscal Month (Header)", type text}, {"Fiscal Week (Header)", type text}, {"Calendar Year (Header)", type text}, {"Calendar Quarter (Header)", type text}, {"Calendar Month (Header)", type text}, {"Calendar Week (Header)", type text}})
in
    #"Changed Type"
```

### LocalDateTable_0af06871-dcc3-4102-b805-8706ba2d636e

```sql
Calendar(Date(Year(MIN('Calendar'[Actual Datetime])), 1, 1), Date(Year(MAX('Calendar'[Actual Datetime])), 12, 31))
```

### LocalDateTable_261c3579-1319-40d0-83b0-050aab355d89

```sql
Calendar(Date(Year(MIN('Calendar'[Actual Date])), 1, 1), Date(Year(MAX('Calendar'[Actual Date])), 12, 31))
```

### Locations (Store MDM)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [CreateNavigationProperties=false]),
    dbo_store_dim = Source{[Schema="dbo",Item="store_dim"]}[Data],
    #"Renamed Columns" = Table.RenameColumns(dbo_store_dim,{{"store_id", "Location Number"}, {"bearea", "Bearea"}, {"store_name", "Location Name"}, {"bearritory", "District"}, {"address1", "Address line 1"}, {"store_name_abbrv", "Abbrev"}, {"region", "Region"}, {"zone", "Zone"}, {"address2", "Address line 2"}, {"state_province_name", "State/Province name"}, {"business_type", "Business type"}, {"city", "City"}, {"division", "Division"}, {"state_province", "State/Province"}, {"county", "County"}, {"business_unit", "Business unit"}, {"country", "Country"}, {"country_name", "Country name"}, {"postal_code", "Postal code"}, {"phone", "Phone"}, {"email", "Email"}, {"opening_date", "Opening date"}, {"active", "Active"}, {"latitude", "Latitude"}, {"longitude", "Longitude"}, {"volume_group", "Volume group"}, {"store_mgr", "Store manager"}, {"bearea_mgr", "Bearea manager"}, {"bearitory_mgr", "Bearritory manager"}, {"region_mgr", "Region manager"}, {"store_type", "Store type"}, {"closing_date", "Closing date"}, {"comp_date", "Comp date"}, {"store_group_id", "Store group Id"}, {"address3", "Address line 3"}, {"address4", "Address line 4"}, {"square_feet", "Square feet"}, {"num_of_pos", "POS count"}, {"num_of_kiosks", "Kiosk count"}, {"postal_plus4", "Postal +4"}, {"Legal_Description", "Legal description"}, {"comp_week_id", "Comp week Id"}, {"bearea_id", "Bearea Id"}, {"bearitory_id", "Bearittory Id"}, {"region_id", "Region Id"}, {"division_code", "Division code"}, {"language", "Language"}, {"demographics_bg_key", "Demographics key"}, {"fax", "Fax"}}),
    #"Filtered Rows | ETL_LOG_ID <> -1" = Table.SelectRows(#"Renamed Columns", each ([ETL_LOG_ID] <> -1)),
    #"Filtered Rows | Store Key > 0" = Table.SelectRows(#"Filtered Rows | ETL_LOG_ID <> -1", each [store_key] > 0),
    #"Removed Columns | System Fields" = Table.RemoveColumns(#"Filtered Rows | Store Key > 0",{"INS_DT", "UPDT_DT", "ETL_LOG_ID", "ETL_EVNT_ID"}),
    #"Removed Columns | Empty Columns" = Table.RemoveColumns(#"Removed Columns | System Fields",{"Zone", "Business type", "County", "Business unit", "Fax", "Address line 3", "Address line 4", "Kiosk count", "Postal +4", "Bearea Id", "Bearittory Id", "Region Id", "Division code", "Language"}),
    #"Filtered Rows | Remove DC Bypass, Locked-Held, Transfer" = Table.SelectRows(#"Removed Columns | Empty Columns", each not Text.Contains([Location Name], "DC Bypass") and not Text.Contains([Location Name], "Locked-Held") and not Text.Contains([Location Name], "Transfer") and not Text.Contains([Location Name], "RZ") and not Text.Contains([Location Name], "Ridemakerz")),
    #"Filtered Rows | Address line 1 IS NOT NULL" = Table.SelectRows(#"Filtered Rows | Remove DC Bypass, Locked-Held, Transfer", each ([Address line 1] <> null)),
    #"Replaced Value | 980 with 9980" = Table.ReplaceValue(#"Filtered Rows | Address line 1 IS NOT NULL",980,9980,Replacer.ReplaceValue,{"Location Number"}),
    #"Replaced Value | 960 with 9960" = Table.ReplaceValue(#"Replaced Value | 980 with 9980",960,9960,Replacer.ReplaceValue,{"Location Number"}),
    #"Filtered Rows | Toys R US" = Table.SelectRows(#"Replaced Value | 960 with 9960", each not Text.Contains([Location Name], "Toys R US")),
    #"Added Custom | Location Number (Standard)" = Table.AddColumn(#"Filtered Rows | Toys R US", "Location Number (Standard)", each Text.PadStart(Text.PadStart(Number.ToText([Location Number]),3,"0"),4,"1")),
    #"Added Custom | Location Line" = Table.AddColumn(#"Added Custom | Location Number (Standard)", "Location Line", each [#"Location Number (Standard)"] & " | " & [Location Name]),
    #"Added Conditional Column | Legal Entity (D365)" = Table.AddColumn(#"Added Custom | Location Line", "Legal Entity (D365)", each if [Country] = "US" then 1100 else if [Country] = "CA" then 1700 else if [Country] = "IE" then 2110 else if [Country] = "UK" then 2110 else null),
    #"Cleaned Text" = Table.TransformColumns(#"Added Conditional Column | Legal Entity (D365)",{{"Location Name", Text.Clean, type text}, {"Abbrev", Text.Clean, type text}, {"District", Text.Clean, type text}, {"Address line 1", Text.Clean, type text}, {"Bearea", Text.Clean, type text}, {"Region", Text.Clean, type text}, {"Address line 2", Text.Clean, type text}, {"State/Province name", Text.Clean, type text}, {"City", Text.Clean, type text}, {"Division", Text.Clean, type text}, {"State/Province", Text.Clean, type text}, {"Country", Text.Clean, type text}, {"Country name", Text.Clean, type text}, {"Postal code", Text.Clean, type text}, {"Phone", Text.Clean, type text}, {"Email", Text.Clean, type text}, {"Store manager", Text.Clean, type text}, {"Bearea manager", Text.Clean, type text}, {"Bearritory manager", Text.Clean, type text}, {"Region manager", Text.Clean, type text}, {"Store type", Text.Clean, type text}, {"Abbreviation", Text.Clean, type text}, {"Legal description", Text.Clean, type text}}),
    #"Trimmed Text" = Table.TransformColumns(#"Cleaned Text",{{"Location Name", Text.Trim, type text}, {"Abbrev", Text.Trim, type text}, {"District", Text.Trim, type text}, {"Address line 1", Text.Trim, type text}, {"Bearea", Text.Trim, type text}, {"Region", Text.Trim, type text}, {"Address line 2", Text.Trim, type text}, {"State/Province name", Text.Trim, type text}, {"City", Text.Trim, type text}, {"Division", Text.Trim, type text}, {"State/Province", Text.Trim, type text}, {"Country", Text.Trim, type text}, {"Country name", Text.Trim, type text}, {"Postal code", Text.Trim, type text}, {"Phone", Text.Trim, type text}, {"Email", Text.Trim, type text}, {"Store manager", Text.Trim, type text}, {"Bearea manager", Text.Trim, type text}, {"Bearritory manager", Text.Trim, type text}, {"Region manager", Text.Trim, type text}, {"Store type", Text.Trim, type text}, {"Abbreviation", Text.Trim, type text}, {"Legal description", Text.Trim, type text}}),
    #"Capitalized Each Word" = Table.TransformColumns(#"Trimmed Text",{{"State/Province name", Text.Proper, type text}}),
    #"Added Custom | City State" = Table.AddColumn(#"Capitalized Each Word", "City, State", each [City] & ", " & [#"State/Province name"]),
    #"Replaced Value | ? with NULL" = Table.ReplaceValue(#"Added Custom | City State","?","",Replacer.ReplaceText,{"State/Province name"}),
    #"Replaced Value | """" with NULL" = Table.ReplaceValue(#"Replaced Value | ? with NULL","",null,Replacer.ReplaceValue,{"Address line 2", "Legal description", "Demographics key","State/Province name"}),
    #"Replaced Value | ( with NULL" = Table.ReplaceValue(#"Replaced Value | """" with NULL","(","",Replacer.ReplaceText,{"Phone"}),
    #"Replaced Value | ) with NULL" = Table.ReplaceValue(#"Replaced Value | ( with NULL",")","",Replacer.ReplaceText,{"Phone"}),
    #"Replaced Value | - with NULL" = Table.ReplaceValue(#"Replaced Value | ) with NULL","-","",Replacer.ReplaceText,{"Phone"}),
    #"Changed Type" = Table.TransformColumnTypes(#"Replaced Value | - with NULL",{{"Legal Entity (D365)", type text}, {"Active", type logical}, {"Location Number (Standard)", type text}, {"Location Line", type text}, {"City, State", type text}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Changed Type",{{"Location Number", "Location Number (MDM)"}, {"Location Number (Standard)", "Location Number (D365)"}}),
    #"Sorted Rows" = Table.Sort(#"Renamed Columns1",{{"District", Order.Descending}}),
    #"Removed Duplicates" = Table.Distinct(#"Sorted Rows", {"Location Number (D365)"}),
    #"Sorted Rows1" = Table.Sort(#"Removed Duplicates",{{"Location Number (D365)", Order.Ascending}})
in
    #"Sorted Rows1"
```

### LocalDateTable_055586fe-cc31-448a-8096-ad765664c40a

```sql
Calendar(Date(Year(MIN('Locations (Store MDM)'[Opening date])), 1, 1), Date(Year(MAX('Locations (Store MDM)'[Opening date])), 12, 31))
```

### LocalDateTable_64c9f10f-dc16-466f-bff8-2c507f4308b7

```sql
Calendar(Date(Year(MIN('Locations (Store MDM)'[Closing date])), 1, 1), Date(Year(MAX('Locations (Store MDM)'[Closing date])), 12, 31))
```

### LocalDateTable_f21e200a-2634-4aa9-af9e-ee5d7b78d0a9

```sql
Calendar(Date(Year(MIN('Locations (Store MDM)'[Comp date])), 1, 1), Date(Year(MAX('Locations (Store MDM)'[Comp date])), 12, 31))
```

### Business Units

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="WITH oms_codes AS (#(lf)    SELECT#(lf)        NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), '') AS code,#(lf)        MIN(COALESCE(r.DateCreatedUTC, r.OrderDateUTC, r.OrderStatusChangeDateUTC, r.ExportCreatedUTC)) AS create_time,#(lf)        MAX(COALESCE(r.UpdateDate,     r.OrderStatusChangeDateUTC, r.OrderDateUTC,     r.ExportCreatedUTC)) AS last_update_time#(lf)    FROM [dbo].[mulesoft_dynamicstargettrans] AS dtt#(lf)    LEFT JOIN [dbo].[mulesoft_deckjsonraw_root] AS r#(lf)           ON r.OrderID = dtt.OrderId#(lf)    WHERE NULLIF(dtt.MaxWarehouseCode, '') IS NOT NULL#(lf)    GROUP BY NULLIF(CONVERT(varchar(64), dtt.MaxWarehouseCode), '')#(lf)),#(lf)oms_bu AS (#(lf)    SELECT#(lf)        CASE#(lf)          WHEN code = 'BAB'   THEN 1013#(lf)          WHEN code = 'BABUK' THEN 2013#(lf)          WHEN TRY_CONVERT(int, code) IS NOT NULL THEN TRY_CONVERT(int, code)#(lf)          ELSE 9999#(lf)        END                                                      AS business_unit_id,#(lf)        CASE#(lf)          WHEN code = 'BAB'   THEN '1013'#(lf)          WHEN code = 'BABUK' THEN '2013'#(lf)          WHEN TRY_CONVERT(int, code) IS NOT NULL THEN CONVERT(varchar(32), TRY_CONVERT(int, code))#(lf)          ELSE '9999'#(lf)        END                                                      AS geo_code,#(lf)        code                                                      AS business_unit_name,#(lf)        CAST(NULL AS varchar(64))                                 AS government_id,#(lf)        create_time,#(lf)        CAST('sp_bab_oms_merge_business_units' AS varchar(128))   AS create_by,#(lf)        last_update_time,#(lf)        CAST('sp_bab_oms_merge_business_units' AS varchar(128))   AS last_update_by#(lf)    FROM oms_codes#(lf))#(lf)#(lf)SELECT#(lf)    bu.business_unit_id,#(lf)    bu.geo_code,#(lf)    bu.business_unit_name,#(lf)    bu.government_id,#(lf)    bu.create_time,#(lf)    bu.create_by,#(lf)    bu.last_update_time,#(lf)    bu.last_update_by#(lf)FROM [dbo].[jumpmind_ctx_business_unit] AS bu#(lf)#(lf)UNION ALL#(lf)#(lf)SELECT#(lf)    o.business_unit_id,#(lf)    o.geo_code,#(lf)    o.business_unit_name,#(lf)    o.government_id,#(lf)    o.create_time,#(lf)    o.create_by,#(lf)    o.last_update_time,#(lf)    o.last_update_by#(lf)FROM oms_bu AS o#(lf)LEFT JOIN [dbo].[jumpmind_ctx_business_unit] AS bu#(lf)       ON bu.geo_code = o.geo_code   -- avoid duplicates where POS already defines this code#(lf)WHERE bu.geo_code IS NULL;", CreateNavigationProperties=false]),
    #"Renamed Columns" = Table.RenameColumns(Source,{{"business_unit_id", "Business Unit Id"}, {"business_unit_name", "Business Unit Name"}}),
    #"Added Custom | Location Line" = Table.AddColumn(#"Renamed Columns", "Location Line", each Text.From([Business Unit Id]) & " | " & [Business Unit Name]),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Custom | Location Line",{{"Location Line", type text}})
in
    #"Changed Type"
```

### LocalDateTable_4c9b482a-789f-493c-b8d9-90d97e039cc2

```sql
Calendar(Date(Year(MIN('Business Units'[create_time])), 1, 1), Date(Year(MAX('Business Units'[create_time])), 12, 31))
```

### LocalDateTable_69a82fc8-c1c8-40e8-91d7-00b3fae0e920

```sql
Calendar(Date(Year(MIN('Business Units'[last_update_time])), 1, 1), Date(Year(MAX('Business Units'[last_update_time])), 12, 31))
```

### Gift Card

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [Query="use LH_Source;#(lf)#(lf)WITH pos_data AS (#(lf)    SELECT#(lf)        CAST(CASE#(lf)            WHEN sd.country = 'US' THEN '1100'#(lf)            WHEN sd.country = 'CA' THEN '1700'#(lf)            WHEN sd.country = 'IE' THEN '2110'#(lf)            WHEN sd.country = 'UK' THEN '2110'#(lf)            ELSE NULL#(lf)        END AS varchar(10)) AS Legal_Entity,#(lf)        TRY_CONVERT(int, t.business_unit_id) AS Store_Number,#(lf)        CAST(RIGHT(CAST(t.till_id AS varchar(64)), 3) AS varchar(64)) AS Register_Number,#(lf)        CAST(#(lf)            TRY_CONVERT(datetime2(6), t.create_time)#(lf)            AT TIME ZONE 'UTC'#(lf)            AT TIME ZONE 'UTC-02'#(lf)            AS date#(lf)        ) AS Transaction_Date,#(lf)#(lf)        CAST(t.username AS varchar(64)) AS Cashier_Number,#(lf)        CAST(CONCAT(t.device_id, '-', t.business_date, '-', t.sequence_number) AS varchar(100)) AS Transaction_Key,#(lf)        dh.RetailTransactionId,#(lf)        CAST(cli.card_number AS varchar(64)) AS Card_Number,#(lf)        CAST(TRY_CONVERT(datetime2(6), t.create_time) AS time) AS Entry_time,#(lf)        CAST(rli.quantity AS decimal(18,2)) AS Activated_Gift_Card_units,#(lf)        CAST(rli.extended_amount AS decimal(18,2)) AS Activated_Gift_Card_gross_amount_TE,#(lf)        CAST(rli.extended_discounted_amount AS decimal(18,2)) AS Activated_Gift_Card_netamount_TE,#(lf)        CAST(rt.iso_currency_code AS varchar(3)) AS Currency,#(lf)        CAST(NULL AS int) AS ItemTypeID,#(lf)        CAST(NULL AS varchar(100)) AS PaymentSubType,#(lf)        CAST(NULL AS int) AS PaymentTransactionTypeId,#(lf)        CAST(NULL AS varchar(255)) AS RefundReference#(lf)#(lf)    FROM dbo.jumpmind_sls_trans t#(lf)    JOIN dbo.jumpmind_sls_retail_line_item rli#(lf)        ON t.device_id = rli.device_id#(lf)        AND t.business_date = rli.business_date#(lf)        AND t.sequence_number = rli.sequence_number#(lf)    JOIN dbo.jumpmind_sls_card_line_item cli#(lf)        ON rli.device_id = cli.device_id#(lf)        AND rli.business_date = cli.business_date#(lf)        AND rli.sequence_number = cli.sequence_number#(lf)        AND rli.line_sequence_number = cli.ref_line_sequence_number#(lf)    LEFT JOIN dbo.jumpmind_sls_retail_trans rt#(lf)        ON t.device_id = rt.device_id#(lf)        AND t.business_date = rt.business_date#(lf)        AND t.sequence_number = rt.sequence_number#(lf)    LEFT JOIN dbo.mulesoft_dynamicsheader dh#(lf)        ON CAST(CONCAT(t.device_id, '-', t.business_date, '-', t.sequence_number) AS varchar(100)) = dh.TransactionKey#(lf)    LEFT JOIN LH_Mart.dbo.store_dim sd#(lf)        ON TRY_CONVERT(int, t.business_unit_id) = TRY_CONVERT(int, sd.store_id)#(lf)    WHERE t.create_by = 'openpos-sls'#(lf)        AND voided <> 1#(lf)        AND TRY_CONVERT(date, t.business_date, 112) >= DATEADD(month, -4, CAST(GETDATE() AS date))#(lf)        AND rli.item_type = 'GIFTCARD'#(lf)        AND rli.line_item_type = 'STORE_SALE'#(lf)        AND t.training_mode = 0#(lf)        AND t.trans_status = 'COMPLETED'#(lf)        AND cli.card_number IS NOT NULL#(lf)),#(lf)oms_data AS (#(lf)    SELECT#(lf)        CAST(CASE#(lf)            WHEN sd.country = 'US' THEN '1100'#(lf)            WHEN sd.country = 'CA' THEN '1700'#(lf)            WHEN sd.country = 'IE' THEN '2110'#(lf)            WHEN sd.country = 'UK' THEN '2110'#(lf)            ELSE NULL#(lf)        END AS varchar(10)) AS Legal_Entity,#(lf)#(lf)        CASE#(lf)            WHEN r.SiteCode = 'BAB' THEN '1013'#(lf)            WHEN r.SiteCode = 'BABUK' THEN '2013'#(lf)            ELSE '9999'#(lf)        END AS Store_Number,#(lf)#(lf)        CAST(#(lf)            CASE#(lf)                WHEN r.SiteCode = 'BABUK' THEN#(lf)                    TRY_CONVERT(datetime2(6),#(lf)                        CASE#(lf)                            WHEN pt_match.PaymentTransactionTypeId = 13 THEN th.EarlyCaptureDateTime#(lf)                            WHEN pt_match.PaymentTransactionTypeId = 1 THEN COALESCE(th.EarlyCaptureDateTime, th.CaptureDateTime)#(lf)                            WHEN pt_match.PaymentTransactionTypeId IN (10, 14) THEN th.CaptureFromEarlyDatetime#(lf)                            ELSE COALESCE(th.EarlyCaptureDateTime, th.AuthorizationDateTime, th.CaptureDateTime)#(lf)                        END#(lf)                    ) AT TIME ZONE 'UTC' AT TIME ZONE 'GMT Standard Time'#(lf)                ELSE#(lf)                    TRY_CONVERT(datetime2(6),#(lf)                        CASE#(lf)                            WHEN pt_match.PaymentTransactionTypeId = 13 THEN th.EarlyCaptureDateTime#(lf)                            WHEN pt_match.PaymentTransactionTypeId = 1 THEN COALESCE(th.EarlyCaptureDateTime, th.CaptureDateTime)#(lf)                            WHEN pt_match.PaymentTransactionTypeId IN (10, 14) THEN th.CaptureFromEarlyDatetime#(lf)                            ELSE COALESCE(th.EarlyCaptureDateTime, th.AuthorizationDateTime, th.CaptureDateTime)#(lf)                        END#(lf)                    ) AT TIME ZONE 'UTC' AT TIME ZONE 'Central Standard Time'#(lf)            END AS datetime2(6)#(lf)        ) AS Sale_Transaction_Date,#(lf)#(lf)        CAST(#(lf)            CASE#(lf)                WHEN r.SiteCode = 'BABUK' THEN TRY_CONVERT(datetime2(6), th_ref.RefundDateTime) AT TIME ZONE 'UTC' AT TIME ZONE 'GMT Standard Time'#(lf)                ELSE TRY_CONVERT(datetime2(6), th_ref.RefundDateTime) AT TIME ZONE 'UTC' AT TIME ZONE 'Central Standard Time'#(lf)            END AS datetime2(6)#(lf)        ) AS Refund_Transaction_Date,#(lf)#(lf)        COALESCE(TRY_CONVERT(varchar(50), r.OrderNumber), TRY_CONVERT(varchar(50), r.OrderID)) AS Calc_Order_ID,#(lf)#(lf)        r.UserID AS Cashier_Number,#(lf)        gc.GiftCardNumber,#(lf)        oi.ItemTypeID,#(lf)#(lf)        pt_match.PaymentSubType,#(lf)        pt_match.PaymentTransactionTypeId,#(lf)        ref_match.RefundReference,#(lf)#(lf)        oi.GrossPrice AS SaleGrossPrice,#(lf)        oi.NetPrice AS SaleNetPrice,#(lf)#(lf)        CASE WHEN ia_agg.OrderItemID IS NOT NULL OR th_ref.RefundDateTime IS NOT NULL THEN 1 ELSE 0 END AS HasRefundFlag,#(lf)#(lf)        ia_agg.RefundCount,#(lf)        ia_agg.RefundGrossAmount,#(lf)        ia_agg.RefundNetAmount#(lf)#(lf)    FROM dbo.mulesoft_deckjsonraw_root r#(lf)    JOIN dbo.mulesoft_deckjsonraw_orderitems oi ON r.OrderID = oi._ParentKeyField#(lf)    JOIN dbo.mulesoft_deckjsonraw_giftcards gc ON oi.ID = gc.OrderItemID#(lf)    LEFT JOIN (#(lf)        SELECT#(lf)            _ParentKeyField,#(lf)            OrderItemID,#(lf)            COUNT(*) AS RefundCount,#(lf)            SUM(GrossPrice) AS RefundGrossAmount,#(lf)            SUM(NetPrice) AS RefundNetAmount#(lf)        FROM dbo.mulesoft_deckjsonraw_orderitemadjustments#(lf)        WHERE AdjustmentType NOT IN (1, 12)#(lf)        GROUP BY _ParentKeyField, OrderItemID#(lf)    ) ia_agg#(lf)        ON oi._ParentKeyField = ia_agg._ParentKeyField#(lf)        AND oi.ID = ia_agg.OrderItemID#(lf)#(lf)    OUTER APPLY (#(lf)        SELECT TOP 1#(lf)            op_sale.PaymentSubType,#(lf)            pt_sale.TransactionDateUTC,#(lf)            pt_sale.PaymentTransactionTypeId#(lf)        FROM dbo.mulesoft_deckjsonraw_orderpayments op_sale#(lf)        JOIN dbo.mulesoft_deckjsonraw_paymenttransactions pt_sale#(lf)            ON CAST(op_sale.ID AS varchar(64)) = CAST(pt_sale.OrderPaymentId AS varchar(64))#(lf)        WHERE op_sale._ParentKeyField = r.OrderID#(lf)            AND (#(lf)                (oi.ItemTypeID = 24 AND op_sale.PaymentSubType = 'Adyen_PayPal' AND pt_sale.PaymentTransactionTypeId = 13)#(lf)                OR#(lf)                (oi.ItemTypeID = 24 AND ISNULL(op_sale.PaymentSubType, '') <> 'Adyen_PayPal' AND pt_sale.PaymentTransactionTypeId = 1)#(lf)                OR#(lf)                (oi.ItemTypeID <> 24 AND pt_sale.PaymentTransactionTypeId IN (10, 14))#(lf)            )#(lf)        ORDER BY#(lf)            CASE#(lf)                WHEN oi.ItemTypeID = 24 AND op_sale.PaymentSubType = 'Adyen_PayPal' AND pt_sale.PaymentTransactionTypeId = 13 THEN 1#(lf)                WHEN oi.ItemTypeID = 24 AND ISNULL(op_sale.PaymentSubType, '') <> 'Adyen_PayPal' AND pt_sale.PaymentTransactionTypeId = 1 THEN 2#(lf)                WHEN oi.ItemTypeID <> 24 AND pt_sale.PaymentTransactionTypeId IN (10, 14) THEN 3#(lf)                ELSE 99#(lf)            END,#(lf)            TRY_CONVERT(datetime2(6), pt_sale.TransactionDateUTC) DESC#(lf)    ) pt_match#(lf)#(lf)    OUTER APPLY (#(lf)        SELECT TOP 1 pt_ref.Generic1 AS RefundReference#(lf)        FROM dbo.mulesoft_deckjsonraw_orderpayments op_ref#(lf)        JOIN dbo.mulesoft_deckjsonraw_paymenttransactions pt_ref#(lf)            ON CAST(op_ref.ID AS varchar(64)) = CAST(pt_ref.OrderPaymentId AS varchar(64))#(lf)        WHERE op_ref._ParentKeyField = r.OrderID#(lf)            AND pt_ref.Generic1 IS NOT NULL#(lf)    ) ref_match#(lf)#(lf)    INNER JOIN [LH_Source].[dbo].[vwOrderTransactionHistory_v1_4] th#(lf)        ON r.OrderID = th.OrderID#(lf)#(lf)    LEFT JOIN [LH_Source].[dbo].[vwOrderTransactionHistory_v1_4] th_ref#(lf)        ON r.OrderID = th_ref.OrderID#(lf)        AND ref_match.RefundReference = th_ref.RefundReference#(lf)#(lf)    LEFT JOIN LH_Mart.dbo.store_dim sd#(lf)        ON sd.store_id = CAST(CASE WHEN r.SiteCode = 'BAB' THEN '1013' WHEN r.SiteCode = 'BABUK' THEN '2013' ELSE '9999' END AS varchar(64))#(lf)#(lf)    WHERE r.OrderStatus IN (6, 10)#(lf)    AND (pt_match.TransactionDateUTC IS NULL OR TRY_CONVERT(date, pt_match.TransactionDateUTC) >= DATEADD(month, -4, CAST(GETDATE() AS date)))#(lf)),#(lf)#(lf)oms AS (#(lf)    SELECT DISTINCT#(lf)        bd.Legal_Entity AS Legal_Entity,#(lf)        bd.Store_Number AS Store_Number,#(lf)        CAST('052' AS varchar(64)) AS Register_Number,#(lf)#(lf)        CAST(CASE#(lf)            WHEN v.TxType = 'Sale' THEN bd.Sale_Transaction_Date#(lf)            WHEN v.TxType = 'Refund' THEN bd.Refund_Transaction_Date#(lf)        END AS date) AS Transaction_Date,#(lf)#(lf)        CAST(bd.Cashier_Number AS varchar(64)) AS Cashier_Number,#(lf)#(lf)        CAST(CONCAT(bd.Store_Number, '-052-', CONVERT(varchar(8),#(lf)            CASE#(lf)                WHEN v.TxType = 'Sale' THEN bd.Sale_Transaction_Date#(lf)                WHEN v.TxType = 'Refund' THEN bd.Refund_Transaction_Date#(lf)            END#(lf)        , 112), '-', bd.Calc_Order_ID) AS varchar(100)) AS Transaction_Key,#(lf)#(lf)        dh.RetailTransactionId,#(lf)        CAST(bd.GiftCardNumber AS varchar(64)) AS Card_Number,#(lf)#(lf)        CAST(CASE#(lf)            WHEN v.TxType = 'Sale' THEN bd.Sale_Transaction_Date#(lf)            WHEN v.TxType = 'Refund' THEN bd.Refund_Transaction_Date#(lf)        END AS time) AS Entry_time,#(lf)#(lf)        CAST(CASE#(lf)            WHEN v.TxType = 'Sale' THEN 1#(lf)            WHEN v.TxType = 'Refund' THEN -1 * ISNULL(bd.RefundCount, 1)#(lf)        END AS decimal(18,2)) AS Activated_Gift_Card_units,#(lf)#(lf)        CAST(CASE#(lf)            WHEN v.TxType = 'Sale' THEN bd.SaleGrossPrice#(lf)            WHEN v.TxType = 'Refund' THEN -1 * COALESCE(bd.RefundGrossAmount, bd.SaleGrossPrice)#(lf)        END AS decimal(18,2)) AS Activated_Gift_Card_gross_amount_TE,#(lf)#(lf)        CAST(CASE#(lf)            WHEN v.TxType = 'Sale' THEN bd.SaleNetPrice#(lf)            WHEN v.TxType = 'Refund' THEN -1 * COALESCE(bd.RefundNetAmount, bd.SaleNetPrice)#(lf)        END AS decimal(18,2)) AS Activated_Gift_Card_netamount_TE,#(lf)#(lf)        CAST('USD' AS varchar(3)) AS Currency,#(lf)        CAST(bd.ItemTypeID AS int) AS ItemTypeID,#(lf)        CAST(bd.PaymentSubType AS varchar(100)) AS PaymentSubType,#(lf)        CAST(bd.PaymentTransactionTypeId AS int) AS PaymentTransactionTypeId,#(lf)#(lf)        CAST(CASE#(lf)            WHEN v.TxType = 'Refund' THEN bd.RefundReference#(lf)            ELSE NULL#(lf)        END AS varchar(255)) AS RefundReference#(lf)#(lf)    FROM oms_data bd#(lf)    CROSS APPLY (#(lf)        SELECT 'Sale' AS TxType#(lf)        UNION ALL#(lf)        SELECT 'Refund'#(lf)        WHERE bd.HasRefundFlag = 1#(lf)    ) v#(lf)#(lf)    LEFT JOIN dbo.mulesoft_dynamicsheaderoms dh#(lf)        ON dh.TransactionKey = CAST(CONCAT(bd.Store_Number, '-052-', CONVERT(varchar(8),#(lf)            CASE#(lf)                WHEN v.TxType = 'Sale' THEN bd.Sale_Transaction_Date#(lf)                WHEN v.TxType = 'Refund' THEN bd.Refund_Transaction_Date#(lf)            END#(lf)        , 112), '-', bd.Calc_Order_ID) AS varchar(100))#(lf))#(lf)#(lf)SELECT DISTINCT * FROM pos_data#(lf)UNION ALL#(lf)SELECT DISTINCT * FROM oms", CreateNavigationProperties=false]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Transaction_Date", type date}})
in
    #"Changed Type"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Mart | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Mart](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Mart/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
