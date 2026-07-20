# Store Balance Report

**Workspace:** BI-Accounting  
**Dataset ID:** 0d396952-75ca-4538-bbe2-c8e839e689f3  

## Tables

| Table | Columns | Measures | Hidden |
|---|---|---|---|
| Transactions | 19 | 0 |  |
| DateTableTemplate_b6814105-aadb-4fa7-b980-25d97abf98b3 | 8 | 0 | Yes |
| Calendar | 39 | 0 |  |
| LocalDateTable_0af06871-dcc3-4102-b805-8706ba2d636e | 8 | 0 | Yes |
| LocalDateTable_261c3579-1319-40d0-83b0-050aab355d89 | 8 | 0 | Yes |
| Locations (Store MDM) | 42 | 0 |  |
| LocalDateTable_055586fe-cc31-448a-8096-ad765664c40a | 8 | 0 | Yes |
| LocalDateTable_64c9f10f-dc16-466f-bff8-2c507f4308b7 | 8 | 0 | Yes |
| LocalDateTable_f21e200a-2634-4aa9-af9e-ee5d7b78d0a9 | 8 | 0 | Yes |
| Products (PLM) | 147 | 0 |  |
| LocalDateTable_d9f9e357-cfef-42d1-91f8-f65596fc556b | 8 | 0 | Yes |
| LocalDateTable_4eb5094a-0fd4-48e6-88b8-ace75db5cf03 | 8 | 0 | Yes |
| LocalDateTable_2a025452-63d1-4b09-b2f1-d4a26a46a764 | 8 | 0 | Yes |
| LocalDateTable_8b8eb212-86b9-42d4-8887-9ddad4537199 | 8 | 0 | Yes |
| LocalDateTable_09d25f19-a5a5-4b40-bde0-7139caa3eb08 | 8 | 0 | Yes |
| LocalDateTable_1809ee2f-dbf4-4cf3-9f5f-28f6f329f073 | 8 | 0 | Yes |
| LocalDateTable_e74b83a1-fd0b-4374-8045-39cbf97fde81 | 8 | 0 | Yes |
| Retail Lines | 23 | 0 |  |
| LocalDateTable_f3d81868-4722-4bef-b677-8954033d1dcb | 8 | 0 | Yes |
| Orders | 18 | 0 |  |
| LocalDateTable_ad47e57a-089b-427e-b22b-36a4a2828856 | 8 | 0 | Yes |
| Tender Lines | 18 | 0 |  |
| LocalDateTable_7940c596-6fe1-44c0-b05b-acc7e96f4d2a | 8 | 0 | Yes |
| Expenses | 18 | 0 |  |
| LocalDateTable_59a8a497-acd3-444d-b818-b13387c0d863 | 8 | 0 | Yes |

## Measures

_No measures detected._

## Power Query Source (per table)

### Transactions

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source",[
    Query="SELECT
	sli.device_id, 
	sli.business_date, 
	sli.sequence_number, 
	sli.line_sequence_number, 
    sli.create_time,
    CAST(sli.create_time AS DATE) AS create_date,
	sli.session_id, 
	sli.till_id, 
	sli.store_bank_id, 
	T.trans_type,
	sli.tender_type_code, 
	sli.tender_code, 
	sli.iso_currency_code, 
	sli.open_session_amount, 
	sli.close_session_amount, 
	sli.counted_session_amount, 
    sli.counted_session_amount - sli.close_session_amount as over_under_session_amount
  FROM dbo.jumpmind_sls_tender_settlement_line_itm sli
  JOIN dbo.jumpmind_sls_trans T
    ON T.business_date = sli.business_date
    AND T.sequence_number = sli.sequence_number
    AND T.device_id = sli.device_id
  WHERE 1=1
	AND T.trans_type IN ('OPEN_STORE_BANK','CLOSE_STORE_BANK') AND T.create_time > DATEADD(MONTH, -6, GETDATE());"
]),
    #"Added Conditional Column" = Table.AddColumn(Source, "TenderPaymentType", each if Text.Contains([tender_type_code], "CASH") then "Safe Float Amount" else if Text.Contains([tender_type_code], "LOCAL") then "Safe Float Amount" else null)
in
    #"Added Conditional Column"
```

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
    #"Filtered Rows" = Table.SelectRows(#"Changed Type", each [Actual Datetime] > #datetime(2024, 7, 31, 0, 0, 0))
in
    #"Filtered Rows"
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

### Products (PLM)

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Mart", [Query="SELECT DISTINCT#(lf)#(lf)       products.[product_key] AS [ProductKey]#(lf)      ,products.[BaseID] AS [BaseID]#(lf)      ,products.[style_code] AS [Style Code]#(lf)      ,products.[INLINE_CD] AS [Inline CD]#(lf)      ,products.[style_desc] AS [Style Description]#(lf)      ,products.[jurisdiction_code] AS [Jurisdiction Code]#(lf)      ,attributes.[ProductSellingGeography] AS [Product Selling Geography]#(lf)      ,products.[jurisdiction_id] AS [Jurisdiction Id]#(lf)      ,attributes.[ProductCountry] AS [Product Country]#(lf)      ,products.[original_retail] AS [Original Retail]#(lf)      ,products.[current_retail] AS [Current Retail]#(lf)      ,products.[current_selling_retail_home] AS [Current Selling Retail Home]#(lf)      ,products.[cdn_value] AS [CDN Value]#(lf)      ,products.[euro_value] AS [Euro Value]#(lf)      ,products.[price_with_vat] AS [Price with VAT]#(lf)      ,products.[priceline_code] AS [Priceline Code]#(lf)      ,products.[ScorecardCategory] AS [Scorecard Category]#(lf)      ,products.[department] AS [Department]#(lf)      ,products.[department_code] AS [Department Code]#(lf)      ,attributes.[DepartmentHierarchyGroupID] AS [Department Hierarchy Group ID]#(lf)      ,products.[class] AS [Class]#(lf)      ,products.[class_code] AS [Class Code]#(lf)      ,attributes.[ClassHierarchyGroupID] AS [Class Hierarchy Group ID]#(lf)      ,attributes.[ClassParentGroupID] AS [Class Parent Group ID]#(lf)      ,products.[subclass] AS [Subclass]#(lf)      ,products.[subclass_code] AS [Subclass Code]#(lf)      ,attributes.[SubClassHierarchyGroupID] AS [Subclass Hierarchy Group ID]#(lf)      ,attributes.[SubClassParentGroupID] AS [Subclass Parent Group ID]#(lf)      ,attributes.[StyleParentGroupID] AS [Style Parent Group ID]#(lf)      ,products.[division] AS [Division]#(lf)      ,attributes.[DivisionCode] AS [Division Code]#(lf)      ,attributes.[ConsumerGroup] AS [Consumer Group]#(lf)      ,products.[concept] AS [Concept]#(lf)      ,products.[chain] AS [Chain]#(lf)      ,attributes.[ChainCode] AS [Chain Code]#(lf)      ,attributes.[ItemType] AS [Item Type]#(lf)      ,attributes.[isBundleSKU] AS [Is Bundle SKU]#(lf)      ,attributes.[WebExclusive] AS [Web Exclusive]#(lf)      ,attributes.[Web] AS [Web]#(lf)      ,attributes.[KeyStory] AS [Key Story]#(lf)      ,attributes.[LICEN] AS [Licensed]#(lf)      ,attributes.[LicensedCollection] AS [Licensed Collection]#(lf)      ,attributes.[occasion] AS [Occasion]#(lf)      ,attributes.[OccasionCode] AS [Occasion Code]#(lf)      ,attributes.[Sound] AS [Sound]#(lf)      ,products.[color_code] AS [Color Code]#(lf)      ,products.[color_desc] AS [Color Description]#(lf)      ,products.[color_id] AS [Color Id]#(lf)      ,attributes.[sportsTeam] AS [Sports Team]#(lf)      ,products.[merch_status] AS [Merch Status]#(lf)      ,attributes.[SellingStatus] AS [Selling Status]#(lf)      ,attributes.[AvailB] AS [AvailB]#(lf)      ,products.[activation_date] AS [Activation Date]#(lf)      ,attributes.[MerchInDate] AS [Merch In Date]#(lf)      ,attributes.[merchOutDate] AS [Merch Out Date]#(lf)      ,attributes.[ODATE] AS [ODate]#(lf)      ,attributes.[ONOTE] AS [Out Date Note]#(lf)      ,attributes.[isOutOfStock] AS [Is Out Of Stock]#(lf)      ,products.[reorder_flag] AS [Reorder Flag]#(lf)      ,attributes.[OnOrderFlag] AS [On Order Flag]#(lf)      ,attributes.[isWebEligible] AS [Is Web Eligible]#(lf)      ,attributes.[WMSTAT] AS [WMSTAT]#(lf)      ,attributes.[OMSTAT] AS [OMSTAT]#(lf)      ,attributes.[OrderMultiple] AS [Order Multiple]#(lf)      ,attributes.[DistributionMultiple] AS [Distribution Multiple]#(lf)      ,attributes.[InnerCasePack] AS [Inner Case Pack]#(lf)      ,attributes.[ManufacturerCountry] AS [Manufacturer Country]#(lf)      ,products.[primary_vendor_name] AS [Primary Vendor Name]#(lf)      ,products.[primary_vendor_code] AS [Primary Vendor Code]#(lf)      ,products.[alt_primary_vendor_code] AS [Alt Primary Vendor Code]#(lf)      ,attributes.[InventoryBuffer] AS [Inventory Buffer]#(lf)      ,attributes.[CommodityCode] AS [Commodity Code]#(lf)      ,attributes.[QuantityRestriction] AS [Quantity Restriction]#(lf)      ,attributes.[AccessoryEligible] AS [Accessory Eligible]#(lf)      ,attributes.[AccessoryType] AS [Accessory Type]#(lf)      ,attributes.[AnimalSoldSeparately] AS [Animal Sold Separately]#(lf)      ,attributes.[AsthmaFriendly] AS [Asthma Friendly]#(lf)      ,attributes.[BirthCertificateRequired] AS [Birth Certificate Required]#(lf)      ,attributes.[BodyType] AS [Body Type]#(lf)      ,attributes.[Bottoms] AS [Bottoms]#(lf)      ,attributes.[Boy] AS [Boy]#(lf)      ,attributes.[BRF] AS [Back Room Fulfillment]#(lf)      ,attributes.[CompSetName] AS [Comp Set Name]#(lf)      ,products.[CORE_FASH_CD] AS [Core Fashion CD]#(lf)      ,attributes.[DisplayOnAmazon] AS [Display On Amazon]#(lf)      ,attributes.[EmbroideryProductList] AS [Embroidery Product List]#(lf)      ,attributes.[EyeColor] AS [Eye Color]#(lf)      ,attributes.[fourLeggedAnimal] AS [Four Legged Animal]#(lf)      ,attributes.[FriendHeight] AS [Friend Height]#(lf)      ,attributes.[FriendWeight] AS [Friend Weight]#(lf)      ,products.[GENDER] AS [Gender]#(lf)      ,attributes.[GiftBoxType] AS [Gift Box Type]#(lf)      ,attributes.[giftCardType] AS [Gift Card Type]#(lf)      ,attributes.[Girl] AS [Girl]#(lf)      ,attributes.[isCashierEnterQty] AS [Is Cashier Enters Quantity]#(lf)      ,attributes.[isCashierEntersPrice] AS [Is Cashier Enters Price]#(lf)      ,attributes.[isCouponEligible] AS [Is Coupon Eligible]#(lf)      ,attributes.[isEmployeeDiscountEligible] AS [Is Employee Discount Eligible]#(lf)      ,attributes.[isEndlessAisleEligible] AS [Is Endless Aisle Eligible]#(lf)      ,attributes.[isLoyaltyRewardsDiscountEligible] AS [Is Loyalty Rewards Discount Eligible]#(lf)      ,attributes.[isQtyRestricted] AS [Is Quantity Restricted]#(lf)      ,attributes.[isReturnEligible] AS [Is Return Eligible]#(lf)      ,attributes.[isTaxExempt] AS [Is Tax Exempt]#(lf)      ,attributes.[Mini] AS [Mini]#(lf)      ,attributes.[MLBTeams] AS [MLB Teams]#(lf)      ,attributes.[Music] AS [Music]#(lf)      ,attributes.[NBATeams] AS [NBA Teams]#(lf)      ,attributes.[Neutral] AS [Neutral]#(lf)      ,attributes.[NFLTeams] AS [NFL Teams]#(lf)      ,attributes.[NHLTeams] AS [NHL Teams]#(lf)      ,attributes.[NoInternationalShipping] AS [No International Shipping]#(lf)      ,attributes.[Outfits] AS [Outfits]#(lf)      ,attributes.[Outlet] AS [Outlet]#(lf)      ,attributes.[PackageOption] AS [Package Option]#(lf)      ,attributes.[ProductCanBeEmbroidered] AS [Product Can Be Embroidered]#(lf)      ,attributes.[ProductMustBeEmbroidered] AS [Product Must Be Embroidered]#(lf)      ,attributes.[Purses] AS [Purses]#(lf)      ,attributes.[RefundEligible] AS [Refund Eligible]#(lf)      ,attributes.[Seasonal] AS [Seasonal]#(lf)      ,attributes.[ShippingClass] AS [Shipping Class]#(lf)      ,attributes.[Shoes] AS [Shoes]#(lf)      ,attributes.[SkinType] AS [Skin Type]#(lf)      ,attributes.[SoundEligible] AS [Sound Eligible]#(lf)      ,attributes.[StoreFrontEligible] AS [Store Front Eligible]#(lf)      ,attributes.[Stuffable] AS [Stuffable]#(lf)      ,attributes.[SAC] AS [Stuffed-And-Closed]#(lf)      ,attributes.[SNC] AS [Stuffed-Not-Closed]#(lf)      ,attributes.[ThirdPartySiteEligible] AS [Third Party Site Eligible]#(lf)      ,attributes.[Tops] AS [Tops]#(lf)      ,attributes.[UKFootball] AS [UK Football]#(lf)      ,attributes.[UPC] AS [UPC]#(lf)      ,attributes.[WarningLabel] AS [Warning Label]#(lf)      ,products.[wss_reportable] AS [WSS Reportable]#(lf)      ,products.[UPDT_DT] AS [Last Update Datetime]#(lf)      ,products.[TotalFOB] AS [LastPOCost]#(lf)#(lf)#(lf)  FROM#(tab)#(tab)#(tab)[dbo].[product_dim] products#(lf)#(lf)  LEFT JOIN#(tab)#(tab)[dbo].[productcatalogmasterattributes] attributes#(lf)  ON#(tab)#(tab)#(tab)products.[jurisdiction_code] = attributes.[ProductSellingGeography]#(lf)  AND#(tab)#(tab)#(tab)products.[style_code] = attributes.[StyleCode]#(tab)#(lf)#(lf)  WHERE#(tab)#(tab)#(tab)products.[style_code] IS NOT NULL#(lf)  AND#(tab)#(tab)#(tab)products.[product_key] > 0#(lf)#(lf)  ORDER BY#(tab)#(tab)products.[style_code] ASC", CreateNavigationProperties=false]),
    #"Added Custom | Core SKU" = Table.AddColumn(Source, "Core SKU", each Text.End([Style Code],5)),
    #"Added Custom | Item Line" = Table.AddColumn(#"Added Custom | Core SKU", "Item Line", each [Style Code] & " - " & [Style Description]),
    #"Added Conditional | Primary Selling Currency" = Table.AddColumn(#"Added Custom | Item Line", "Primary Selling Currency", each if [Jurisdiction Code] = "CA" then "CAD" else if [Jurisdiction Code] = "IE" then "EUR" else if [Jurisdiction Code] = "UK" then "GBP" else if [Jurisdiction Code] = "US" then "USD" else [Jurisdiction Code]),
    #"Added Custom | CurrencyItemKey" = Table.AddColumn(#"Added Conditional | Primary Selling Currency", "CurrencyItemKey", each [Primary Selling Currency] & [Style Code]),
    #"Added Conditional Column | Web Eligible" = Table.AddColumn(#"Added Custom | CurrencyItemKey", "Web Eligible", each if [Web] = "WEBYES" then true else if [Web] = "WEBNO" then false else if [Web] = "WEBNYC" then true else null),
    #"Added Conditional Column | Web Eligible NYC Only" = Table.AddColumn(#"Added Conditional Column | Web Eligible", "Web Eligible - NYC Only", each if [Web] = "WEBNYC" then true else false),
    #"Inserted Date | Out Date" = Table.AddColumn(#"Added Conditional Column | Web Eligible NYC Only", "Out Date", each Date.From([ODate]), type date),
    #"Replaced Errors | Out Date" = Table.ReplaceErrorValues(#"Inserted Date | Out Date", {{"Out Date", null}}),
    #"Added Conditional Column | Merch Out Date" = Table.AddColumn(#"Replaced Errors | Out Date", "Merchandise Out Date", each if [Merch Out Date] <> null then [Merch Out Date] else [Out Date]),
    #"Added Custom | Item Line Core SKU" = Table.AddColumn(#"Added Conditional Column | Merch Out Date", "Item Line (Core SKU)", each [Core SKU] & " - " & [Style Description]),
    #"Replaced Value | Y > TRUE" = Table.ReplaceValue(#"Added Custom | Item Line Core SKU","Y","true",Replacer.ReplaceText,{"WSS Reportable","Outlet"}),
    #"Replaced Value | N > FALSE" = Table.ReplaceValue(#"Replaced Value | Y > TRUE","N","false",Replacer.ReplaceText,{"WSS Reportable","Outlet"}),
    #"Replaced Value | NULL > null" = Table.ReplaceValue(#"Replaced Value | N > FALSE","NULL",null,Replacer.ReplaceValue,{"Alt Primary Vendor Code"}),
    #"Replaced Value | NO > FALSE" = Table.ReplaceValue(#"Replaced Value | NULL > null","NO","false",Replacer.ReplaceText,{"Licensed"}),
    #"Replaced Value | 0 > FALSE" = Table.ReplaceValue(#"Replaced Value | NO > FALSE","0","false",Replacer.ReplaceText,{"Is Cashier Enters Quantity", "Is Cashier Enters Price", "Is Quantity Restricted", "Is Return Eligible", "Outlet"}),
    #"Replaced Value | 1 > TRUE" = Table.ReplaceValue(#"Replaced Value | 0 > FALSE","1","true",Replacer.ReplaceText,{"Is Cashier Enters Quantity", "Is Cashier Enters Price", "Is Quantity Restricted", "Is Return Eligible", "Outlet"}),
    #"Added Conditional Column | D365 Legal Entity" = Table.AddColumn(#"Replaced Value | 1 > TRUE", "D365 Legal Entity", each if [CurrencyItemKey] = "USD8" then 1200 else if [CurrencyItemKey] = "USD9" then 3001 else if [Primary Selling Currency] = "CAD" then 1700 else if [Primary Selling Currency] = "EUR" then 2110 else if [Primary Selling Currency] = "GBP" then 2110 else if [Primary Selling Currency] = "USD" then 1100 else null),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Conditional Column | D365 Legal Entity",{{"Embroidery Product List", type logical}, {"Product Can Be Embroidered", type logical}, {"Product Must Be Embroidered", type logical}, {"Asthma Friendly", type logical}, {"Back Room Fulfillment", type logical}, {"Music", type logical}, {"Animal Sold Separately", type logical}, {"Stuffed-And-Closed", type logical}, {"Bottoms", type logical}, {"Outfits", type logical}, {"Mini", type logical}, {"Tops", type logical}, {"Purses", type logical}, {"Stuffed-Not-Closed", type logical}, {"Boy", type logical}, {"Girl", type logical}, {"Neutral", type logical}, {"Birth Certificate Required", type logical}, {"Refund Eligible", type logical}, {"Third Party Site Eligible", type logical}, {"AvailB", type logical}, {"Stuffable", type logical}, {"No International Shipping", type logical}, {"Display On Amazon", type logical}, {"Web Exclusive", type logical}, {"Accessory Eligible", type logical}, {"Sound Eligible", type logical}, {"Store Front Eligible", type logical}, {"Merch Out Date", type date}, {"On Order Flag", type logical}, {"Shoes", type logical}, {"Sound", type logical}, {"Four Legged Animal", type logical}, {"Merch In Date", type date}, {"Activation Date", type date}, {"Item Line", type text}, {"Primary Selling Currency", type text}, {"CurrencyItemKey", type text}, {"Core SKU", type text}, {"ProductKey", type text}, {"Is Bundle SKU", type logical}, {"Web Eligible", type logical}, {"Web Eligible - NYC Only", type logical}, {"Licensed", type logical}, {"Is Out Of Stock", type logical}, {"Is Web Eligible", type logical}, {"Is Cashier Enters Quantity", type logical}, {"Is Cashier Enters Price", type logical}, {"Is Coupon Eligible", type logical}, {"Is Employee Discount Eligible", type logical}, {"Is Loyalty Rewards Discount Eligible", type logical}, {"Is Quantity Restricted", type logical}, {"Is Return Eligible", type logical}, {"Is Tax Exempt", type logical}, {"WSS Reportable", type logical}, {"Outlet", type logical}, {"Merchandise Out Date", type date}, {"Item Line (Core SKU)", type text}, {"D365 Legal Entity", type text}}),
    #"Added Custom | ItemKey" = Table.AddColumn(#"Changed Type", "ItemKey", each [D365 Legal Entity] & "-" & [Style Code]),
    #"Changed Type | ItemKey" = Table.TransformColumnTypes(#"Added Custom | ItemKey",{{"ItemKey", type text}}),
    #"Renamed Columns" = Table.RenameColumns(#"Changed Type | ItemKey",{{"Merch Out Date", "Out Date 1"}, {"Out Date", "Out Date 2"}, {"Merchandise Out Date", "Merch Out Date"}}),
    #"Sorted Rows | Last Update Datetime DESC" = Table.Sort(#"Renamed Columns",{{"Last Update Datetime", Order.Descending}}),
    #"Removed Duplicates | CurrencyItemKey" = Table.Distinct(#"Sorted Rows | Last Update Datetime DESC", {"CurrencyItemKey"}),
    #"Filtered Rows | Primary Selling Currency {CAD,EUR,GBP,USD}" = Table.SelectRows(#"Removed Duplicates | CurrencyItemKey", each ([Primary Selling Currency] <> "CN" and [Primary Selling Currency] <> "DK" and [Primary Selling Currency] <> "FR")),
    #"Sorted Rows | Primary Selling Currrency DESC" = Table.Sort(#"Filtered Rows | Primary Selling Currency {CAD,EUR,GBP,USD}",{{"Primary Selling Currency", Order.Descending}}),
    #"Removed Duplicates | ItemKey" = Table.Distinct(#"Sorted Rows | Primary Selling Currrency DESC", {"ItemKey"}),
    #"Sorted Rows | Style Code ASC" = Table.Sort(#"Removed Duplicates | ItemKey",{{"Style Code", Order.Ascending}}),
    #"Renamed Columns1" = Table.RenameColumns(#"Sorted Rows | Style Code ASC",{{"LastPOCost", "Last PO Cost"}})
in
    #"Renamed Columns1"
```

### LocalDateTable_d9f9e357-cfef-42d1-91f8-f65596fc556b

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Activation Date])), 1, 1), Date(Year(MAX('Products (PLM)'[Activation Date])), 12, 31))
```

### LocalDateTable_4eb5094a-0fd4-48e6-88b8-ace75db5cf03

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Merch In Date])), 1, 1), Date(Year(MAX('Products (PLM)'[Merch In Date])), 12, 31))
```

### LocalDateTable_2a025452-63d1-4b09-b2f1-d4a26a46a764

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Out Date 1])), 1, 1), Date(Year(MAX('Products (PLM)'[Out Date 1])), 12, 31))
```

### LocalDateTable_8b8eb212-86b9-42d4-8887-9ddad4537199

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Last Update Datetime])), 1, 1), Date(Year(MAX('Products (PLM)'[Last Update Datetime])), 12, 31))
```

### LocalDateTable_09d25f19-a5a5-4b40-bde0-7139caa3eb08

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Out Date 2])), 1, 1), Date(Year(MAX('Products (PLM)'[Out Date 2])), 12, 31))
```

### LocalDateTable_1809ee2f-dbf4-4cf3-9f5f-28f6f329f073

```sql
Calendar(Date(Year(MIN('Products (PLM)'[Merch Out Date])), 1, 1), Date(Year(MAX('Products (PLM)'[Merch Out Date])), 12, 31))
```

### LocalDateTable_e74b83a1-fd0b-4374-8045-39cbf97fde81

```sql
Calendar(Date(Year(MIN('Transactions'[create_time])), 1, 1), Date(Year(MAX('Transactions'[create_time])), 12, 31))
```

### Retail Lines

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source",[
    Query="WITH sales AS (
    SELECT 'SALES' AS report,
    'Merchandise' AS tender_payment_type,
    CASE WHEN LI.item_type = 'DONATION' THEN 'Charity Donation'
            WHEN LI.item_type = 'STORE_ORDER_SHIPPING' THEN 'Shipping Web Fees'
            ELSE LI.item_type END AS fees,
    T.business_unit_id, 
    T.business_date, 
    T.sequence_number, 
    T.create_time,
    CAST(T.create_time AS DATE) AS transaction_date,
    T.trans_type,
    LI.device_id, 
    LI.item_description, 
    LI.item_id, 
    LI.item_type, 
    LI.extended_amount,
    CASE WHEN trans_type = 'SALE' THEN LI.extended_amount ELSE NULL END AS sales,
    CASE WHEN trans_type = 'RETURN' THEN LI.extended_amount ELSE NULL END AS returns,
    CASE WHEN trans_type = 'SALE' THEN LI.extended_amount ELSE 0 END - CASE WHEN trans_type = 'RETURN' THEN LI.extended_amount ELSE 0 END AS net,
    LIPM.promotion_type,
    LIPM.description, 
    LIPM.promo_code_id, -- when not NULL, indicates a serialized coupon
    LIPM.modification_total
FROM jumpmind_sls_retail_line_item LI
JOIN jumpmind_sls_trans T 
    ON T.business_date = LI.business_date
    AND T.sequence_number = LI.sequence_number
    AND T.device_id = LI.device_id
LEFT JOIN jumpmind_sls_retail_line_item_price_mod LIPM
    ON LI.business_date = LIPM.business_date
    AND LI.sequence_number = LIPM.sequence_number
    AND LI.line_sequence_number = LIPM.line_sequence_number
    AND LI.device_id = LIPM.device_id
WHERE T.trans_status = 'COMPLETED'
    AND LI.voided = 0
    AND T.create_time >= DATEADD(MONTH, -2, GETDATE())
),
discounts as (
    SELECT 'DISCOUNTS' AS report,
    CASE WHEN LIPM.promo_code_id IS NOT NULL THEN 'Serialized Coupon'
        WHEN LIPM.promotion_type = 'EMPLOYEE_DISCOUNT' THEN 'Subtotal Employee Discount'
        ELSE 'Promotions Markdown' END AS tender_payment_type,
    CASE WHEN LI.item_type = 'DONATION' THEN 'Charity Donation'
            WHEN LI.item_type = 'STORE_ORDER_SHIPPING' THEN 'Shipping Web Fees'
            ELSE LI.item_type END AS fees,
    T.business_unit_id, 
    T.business_date, 
    T.sequence_number, 
    T.create_time,
    CAST(T.create_time AS DATE) AS transaction_date,
    T.trans_type,
    LI.device_id, 
    LI.item_description, 
    LI.item_id, 
    LI.item_type, 
    LI.extended_amount,
    CASE WHEN trans_type = 'SALE' THEN -LIPM.modification_total ELSE NULL END AS sales,
    CASE WHEN trans_type = 'RETURN' THEN -LIPM.modification_total ELSE NULL END AS returns,
    CASE WHEN trans_type = 'SALE' THEN -LIPM.modification_total ELSE 0 END - CASE WHEN trans_type = 'RETURN' THEN -LIPM.modification_total ELSE 0 END AS net,
    LIPM.promotion_type,
    LIPM.description, 
    LIPM.promo_code_id, -- when not NULL, indicates a serialized coupon
    LIPM.modification_total
FROM jumpmind_sls_retail_line_item LI
JOIN jumpmind_sls_trans T 
    ON T.business_date = LI.business_date
    AND T.sequence_number = LI.sequence_number
    AND T.device_id = LI.device_id
JOIN jumpmind_sls_retail_line_item_price_mod LIPM
    ON LI.business_date = LIPM.business_date
    AND LI.sequence_number = LIPM.sequence_number
    AND LI.line_sequence_number = LIPM.line_sequence_number
    AND LI.device_id = LIPM.device_id
WHERE T.trans_status = 'COMPLETED'
    AND LI.voided = 0
    AND T.create_time >= DATEADD(MONTH, -2, GETDATE())
),
taxes AS (
    select 'SALES TAXES' AS report
, tli.tax_type AS tender_payment_type
, NULL AS fees
, t.business_unit_id
, t.business_date
, t.sequence_number
, t.create_time
, CAST(t.create_time AS DATE) AS transaction_date
, t.trans_type
, tli.device_id
, rl.item_description
, rl.item_id
, rl.item_type
, rl.extended_amount
, CASE WHEN t.trans_type = 'SALE' THEN tli.tax_amount ELSE NULL END AS sales
, CASE WHEN t.trans_type = 'RETURNS' THEN tli.tax_amount ELSE NULL END AS returns
, CASE WHEN t.trans_type = 'SALE' THEN tli.tax_amount ELSE 0 END
- CASE WHEN t.trans_type = 'RETURNS' THEN tli.tax_amount ELSE 0 END AS net
, NULL as promotion_type
, NULL as description
, NULL as promo_code_id
, NULL as modification_total
from dbo.jumpmind_sls_retail_line_item rl
join dbo.jumpmind_sls_tax_retail_line_item tli
    on rl.device_id = tli.device_id
    and rl.business_date = tli.business_date
    and rl.sequence_number = tli.sequence_number
    and rl.line_sequence_number = tli.line_sequence_number
join dbo.jumpmind_sls_trans t 
    on rl.device_id = t.device_id
    and rl.business_date = t.business_date
    and rl.sequence_number = t.sequence_number
WHERE t.trans_status = 'COMPLETED'
    AND rl.voided = 0
    AND t.create_time >= DATEADD(MONTH, -2, GETDATE())
)
    SELECT *
    FROM sales
    UNION
    SELECT *
    FROM discounts
    UNION
    SELECT *
    FROM taxes"
]),
    #"Added Custom" = Table.AddColumn(Source, "gift_cards", each if [tender_payment_type] = "Merchandise" and [item_type] = "GIFTCARD" then "BAB Gift Cards"
    else if [tender_payment_type] <> "Merchandise" and [item_type] = "GIFTCARD" then "BAB Gift Cards Discount"
    else null)
in
    #"Added Custom"
```

### LocalDateTable_f3d81868-4722-4bef-b677-8954033d1dcb

```sql
Calendar(Date(Year(MIN('Retail Lines'[create_time])), 1, 1), Date(Year(MAX('Retail Lines'[create_time])), 12, 31))
```

### Orders

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source",[
    Query="WITH endless_aisle_sales AS (
	SELECT
		'Endless Aisle' as endless_aisle
		,so.business_unit_id
		,so.order_id
		,soli.orig_sequence_number
		,soli.orig_line_sequence_number
		,so.business_date
		,so.device_id
		,t.trans_type
		,t.create_time
		,CAST(t.create_time AS DATE) AS transaction_date
		,so.total
		,CASE WHEN trans_type = 'SALE' THEN so.total ELSE NULL END AS receipts
		,CASE WHEN trans_type = 'RETURN' THEN so.total ELSE NULL END AS returns
		,CASE WHEN trans_type = 'SALE' THEN so.total ELSE 0 END 
			- CASE WHEN trans_type = 'RETURN' THEN so.total ELSE 0 END AS net
		,NULL AS promotion_type
		,NULL AS promotion_description
		,NULL AS promo_code_id
	FROM dbo.jumpmind_sls_order so
	JOIN dbo.jumpmind_sls_order_line_item soli ON so.order_id = soli.order_id
	JOIN dbo.jumpmind_sls_retail_trans rt ON rt.order_id = soli.order_id
		AND rt.business_date = soli.orig_business_date
		AND rt.sequence_number = soli.orig_sequence_number
	JOIN dbo.jumpmind_sls_trans t ON t.device_id = rt.device_id
		AND t.business_date = rt.business_date
		AND t.sequence_number = rt.sequence_number	
	WHERE t.trans_status = 'COMPLETED'
	AND t.create_time >= DATEADD(MONTH, -6, GETDATE())
	),
	endless_aisle_deferrals AS (
	SELECT 
		CASE WHEN lipm.promo_code_id IS NOT NULL THEN 'Subtotal $ Off Promotions Discount Prorated'
			ELSE 'Item $ Off Promotions Markdown' END as endless_aisle
		,so.business_unit_id
		,so.order_id
		,soli.orig_sequence_number
		,soli.orig_line_sequence_number
		,so.business_date
		,so.device_id
		,t.trans_type
		,t.create_time
		,CAST(t.create_time AS DATE) AS transaction_date
		,so.total
		,CASE WHEN trans_type = 'SALE' THEN lipm.modification_total ELSE NULL END AS receipts
		,CASE WHEN trans_type = 'RETURN' THEN lipm.modification_total ELSE NULL END AS returns
		,CASE WHEN trans_type = 'SALE' THEN lipm.modification_total ELSE 0 END
		- CASE WHEN trans_type = 'RETURN' THEN lipm.modification_total ELSE 0 END AS net
		,lipm.promotion_type
		,lipm.description
		,lipm.promo_code_id
	FROM dbo.jumpmind_sls_order so
	JOIN dbo.jumpmind_sls_order_line_item soli ON so.order_id = soli.order_id
	JOIN dbo.jumpmind_sls_retail_trans rt ON rt.order_id = soli.order_id
		AND rt.business_date = soli.orig_business_date
		AND rt.sequence_number = soli.orig_sequence_number
	JOIN dbo.jumpmind_sls_trans t ON t.device_id = rt.device_id
		AND t.business_date = rt.business_date
		AND t.sequence_number = rt.sequence_number	
	join dbo.jumpmind_sls_retail_line_item_price_mod lipm
		ON rt.device_id = lipm.device_id
		AND rt.business_date = lipm.business_date
		AND rt.sequence_number = lipm.sequence_number
		and soli.orig_line_sequence_number = lipm.line_sequence_number
	WHERE t.trans_status = 'COMPLETED'
	AND t.create_time >= DATEADD(MONTH, -6, GETDATE())
	)
	select *
	from endless_aisle_sales
	union 
	select *
	from endless_aisle_deferrals
"
])
in
    Source
```

### LocalDateTable_ad47e57a-089b-427e-b22b-36a4a2828856

```sql
Calendar(Date(Year(MIN('Orders'[create_time])), 1, 1), Date(Year(MAX('Orders'[create_time])), 12, 31))
```

### Tender Lines

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source",[
    Query="SELECT 
    T.business_unit_id, 
    T.business_date, 
    T.sequence_number, 
    T.create_time,
    CAST(T.create_time AS DATE) AS transaction_date,
    tl.line_sequence_number,
    tl.device_id,
    ct.reason_code,
    --ct.paid_to,
    tl.tender_type_code,
    CASE WHEN tl.tender_code LIKE 'AMEX%' THEN 'AMEX'
        WHEN tl.tender_code LIKE 'MASTER%' THEN 'MASTERCARD'
        WHEN tl.tender_code LIKE 'VISA%' THEN 'VISA'
        ELSE tl.tender_code END AS tender_code,
    tl.iso_currency_code,
    tl.tender_amount,
    CASE WHEN tl.change_flag = 0 THEN tl.tender_amount ELSE NULL END AS receipts,
    CASE WHEN tl.change_flag = 1 THEN tl.tender_amount ELSE NULL END AS disbursements,
    CASE WHEN tl.change_flag = 0 THEN tl.tender_amount ELSE 0 END + CASE WHEN tl.change_flag = 1 THEN tl.tender_amount ELSE 0 END AS net
FROM dbo.jumpmind_sls_tender_line_item tl
JOIN dbo.jumpmind_sls_trans T
    ON T.business_date = tl.business_date
    AND T.sequence_number = tl.sequence_number
    AND T.device_id = tl.device_id
LEFT JOIN dbo.jumpmind_sls_tender_control_trans ct  
	ON T.business_date = ct.business_date
    AND T.sequence_number = ct.sequence_number
    AND T.device_id = ct.device_id
WHERE T.create_time >= DATEADD(MONTH, -6, GETDATE());"
]),
    #"Added Conditional Column" = Table.AddColumn(Source, "Expenses", each if [reason_code] = "10" then "Supplies" else if [reason_code] = "20" then "Supplies" else if [reason_code] = "30" then "Supplies" else if [reason_code] = "40" then "Supplies" else if [reason_code] = "50" then "Supplies" else if [tender_type_code] = "ROUNDING_ADJUSTMENT" then "Nickel Rounding Expense" else null)
in
    #"Added Conditional Column"
```

### LocalDateTable_7940c596-6fe1-44c0-b05b-acc7e96f4d2a

```sql
Calendar(Date(Year(MIN('Tender Lines'[create_time])), 1, 1), Date(Year(MAX('Tender Lines'[create_time])), 12, 31))
```

### Expenses

```sql
let
    Source = Sql.Database("4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com", "LH_Source",[
    Query="WITH supplies AS (
    SELECT 
        'Supplies' AS expenses,
        T.business_unit_id, 
        T.business_date, 
        T.sequence_number, 
        tl.line_sequence_number,
        T.create_time,
        CAST(T.create_time AS DATE) AS transaction_date,
        T.trans_type,
        tl.device_id,
        ct.reason_code,
        --ct.paid_to,
        tl.tender_type_code,
        tl.tender_code,
        tl.iso_currency_code,
        tl.tender_amount,
        CASE WHEN T.trans_type = 'PAY_IN' THEN tl.tender_amount ELSE NULL END AS recoveries,
        CASE WHEN T.trans_type = 'PAY_OUT' THEN tl.tender_amount ELSE NULL END AS disbursement,
        CASE WHEN T.trans_type = 'PAY_IN' THEN tl.tender_amount ELSE 0 END
        + CASE WHEN T.trans_type = 'PAY_OUT' THEN tl.tender_amount ELSE NULL END AS net
    FROM dbo.jumpmind_sls_tender_line_item tl
    JOIN dbo.jumpmind_sls_trans T
        ON T.business_date = tl.business_date
        AND T.sequence_number = tl.sequence_number
        AND T.device_id = tl.device_id
    LEFT JOIN dbo.jumpmind_sls_tender_control_trans ct  
	    ON T.business_date = ct.business_date
        AND T.sequence_number = ct.sequence_number
        AND T.device_id = ct.device_id
    WHERE T.create_time >= DATEADD(MONTH, -6, GETDATE())
	    AND ct.reason_code IN ('10','20','30','40','50')  -- reason_codes mapped as supplies
	    AND T.trans_type IN ('PAY_IN','PAY_OUT')
), nickel_rounding AS (
    SELECT 
        'Nickel Rounding Expense' as expenses,
        T.business_unit_id, 
        T.business_date, 
        T.sequence_number, 
        tl.line_sequence_number,
        T.create_time,
        CAST(T.create_time AS DATE) AS transaction_date,
        T.trans_type,
        tl.device_id,
        NULL AS reason_code,
        tl.tender_type_code,
        tl.tender_code,
        tl.iso_currency_code,
        tl.tender_amount,
        CASE WHEN T.trans_type = 'SALE' THEN tl.tender_amount ELSE NULL END AS recoveries,
        CASE WHEN T.trans_type = 'RETURN' THEN tl.tender_amount ELSE NULL END AS disbursement,
        CASE WHEN T.trans_type = 'SALE' THEN tl.tender_amount ELSE 0 END
        + CASE WHEN T.trans_type = 'RETURN' THEN tl.tender_amount ELSE 0 END AS net
    FROM jumpmind_sls_tender_line_item tl
    JOIN jumpmind_sls_trans T
        ON T.business_date = tl.business_date
        AND T.sequence_number = tl.sequence_number
        AND T.device_id = tl.device_id
    where tl.tender_type_code = 'ROUNDING_ADJUSTMENT'
    AND tl.create_time >= DATEADD(MONTH, -6, GETDATE())
)
select *
from supplies 
union
select *
from nickel_rounding
"
])
in
    Source
```

### LocalDateTable_59a8a497-acd3-444d-b818-b13387c0d863

```sql
Calendar(Date(Year(MIN('Expenses'[create_time])), 1, 1), Date(Year(MAX('Expenses'[create_time])), 12, 31))
```

## Data Source Cross-References

| Server | Database | Linked SQL Documentation |
|---|---|---|
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Source | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Source](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Source/) |
| 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com | LH_Mart | [4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/LH_Mart](../../../4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com/DataDictionary/LH_Mart/) |
