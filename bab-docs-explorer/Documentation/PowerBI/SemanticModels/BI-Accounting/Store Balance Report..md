# Store Balance Report.

**Workspace:** BI-Accounting  
**Dataset ID:** a856df4a-ad38-48d8-8962-23ab0777dcb4  

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
| Store_Balance | 11 | 0 |  |

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
    #"Changed Type" = Table.TransformColumnTypes(#"Reordered Columns",{{"Fiscal Month (Name)", type text}, {"Fiscal Year (Header)", type text}, {"Fiscal Quarter (Header)", type text}, {"Fiscal Month (Header)", type text}, {"Fiscal Week (Header)", type text}, {"Calendar Year (Header)", type text}, {"Calendar Quarter (Header)", type text}, {"Calendar Month (Header)", type text}, {"Calendar Week (Header)", type text}}),
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each [Actual Datetime] > #datetime(2024, 7, 31, 0, 0, 0)),
    #"Changed Type1" = Table.TransformColumnTypes(#"Filtered Rows",{{"Actual Datetime", type date}})
in
    #"Changed Type1"
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

### Store_Balance

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source", [CreateNavigationProperties=false, Query="select * from rpt_store_balance_ya_tst_6"]),
    #"Changed Type" = Table.TransformColumnTypes(Source,{{"Posting Date", type date}})
in
    #"Changed Type"
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Mart | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Mart](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Mart/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
