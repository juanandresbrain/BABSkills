# dbo.pi_create_temp_tables_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.pi_create_temp_tables_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
/*
April 26, 2010		Feng		increase precision from (14,2) to (18,6) for cost fields
*/
create proc [dbo].[pi_create_temp_tables_$sp] 


AS

CREATE TABLE
	#tt_sku
		( [sku_id] [DECIMAL](13,0) NOT NULL )

CREATE TABLE
	#tt_pack
		( [pack_id] [DECIMAL](13,0) NOT NULL )

CREATE TABLE
	#tt_frozen_on_hand
		( [location_id] [SMALLINT] NOT NULL
		, [sku_id] [DECIMAL](13,0) NOT NULL
		, [inventory_status_id] [SMALLINT] NOT NULL
		, [on_hand_units] [INTEGER] NULL
		, [on_hand_cost] [DECIMAL](18,6) NULL
		, [on_hand_cost_local] [DECIMAL](18,6) NULL
		, [on_hand_valuation_retail] [DECIMAL](14,2) NULL
		, [on_hand_selling_retail] [DECIMAL](14,2) NULL
		, [average_cost] [DECIMAL](18,6) NULL 
		, [average_cost_local] [DECIMAL](18,6) NULL )

CREATE TABLE
	#tt_pack_frozen_on_hand
		( [location_id] [SMALLINT] NOT NULL
		, [pack_id] [DECIMAL](13,0) NOT NULL
		, [on_hand_units] [INTEGER] NULL )

CREATE TABLE 
	#tt_frozen_chain_on_hand
		( [style_id] [DECIMAL](13,0) NOT NULL
        , [chain_on_hand_units] [DECIMAL](14,2) NULL
        , [chain_on_hand_cost] [DECIMAL](18,6) NULL)

CREATE TABLE
	#tt_frozen_juris_on_hand
		( [style_id] [DECIMAL](13,0) NOT NULL
		, [jurisdiction_id] [SMALLINT] NOT NULL
		, [juris_on_hand_units] [INTEGER] NULL 
		, [juris_on_hand_cost] [DECIMAL](18,6) NULL
        , [juris_on_hand_cost_local] [DECIMAL](18,6) NULL)

CREATE TABLE
	#tt_future_on_hand
		( [location_id] [SMALLINT] NOT NULL
		, [sku_id] [DECIMAL](13,0) NOT NULL
		, [inventory_status_id] [SMALLINT] NOT NULL
		, [on_hand_units] [INTEGER] NULL
		, [on_hand_cost] [DECIMAL](18,6) NULL
		, [on_hand_cost_local] [DECIMAL](18,6) NULL
		, [on_hand_valuation_retail] [DECIMAL](14,2) NULL
		, [on_hand_selling_retail] [DECIMAL](14,2) NULL )

CREATE TABLE
	#tt_pack_future_on_hand
		( [location_id] [SMALLINT] NOT NULL
		, [pack_id] [DECIMAL](13,0) NOT NULL
		, [on_hand_units] [INTEGER] NULL )

CREATE TABLE 
	#tt_future_chain_on_hand
		( [style_id] [DECIMAL](13,0) NOT NULL
        , [chain_on_hand_units] [DECIMAL](14,2) NULL
        , [chain_on_hand_cost] [DECIMAL](18,6) NULL)

CREATE TABLE
	#tt_future_juris_on_hand
		( [style_id] [DECIMAL](13,0) NOT NULL
		, [jurisdiction_id] [SMALLINT] NOT NULL
		, [juris_on_hand_units] [INTEGER] NULL 
		, [juris_on_hand_cost] [DECIMAL](18,6) NULL
        , [juris_on_hand_cost_local] [DECIMAL](18,6) NULL)

CREATE TABLE
	#tt_frozen_retails
		( [id] [DECIMAL](13,0) IDENTITY(1,1) NOT NULL
		, [location_id] [SMALLINT] NOT NULL
		, [style_id] [DECIMAL](12,0) NOT NULL
		, [color_id] [SMALLINT] NOT NULL
		, [style_color_id] [DECIMAL](13,0) NOT NULL
		, [price_status_id] [SMALLINT] NULL
		, [valuation_unit_retail] [DECIMAL](14,2) NULL
		, [selling_unit_retail] [DECIMAL](14,2) NULL )

CREATE TABLE
	#tt_price_date
		( [location_id] [SMALLINT] NOT NULL
		, [jurisdiction_id] [SMALLINT] NOT NULL
		, [style_id] [DECIMAL](12,0) NOT NULL
		, [color_id] [SMALLINT] NOT NULL
		, [style_color_id] [DECIMAL](13,0) NOT NULL
		, [effective_date] [DATETIME] NOT NULL )

CREATE TABLE
	#tt_price_id
		( [location_id] [SMALLINT] NOT NULL
		, [jurisdiction_id] [SMALLINT] NOT NULL
		, [style_id] [DECIMAL](12,0) NOT NULL
		, [color_id] [SMALLINT] NOT NULL
		, [style_color_id] [DECIMAL](13,0) NOT NULL
		, [ib_price_id] [DECIMAL](13,0) NOT NULL )

CREATE TABLE
	#tt_price
		( [location_id] [SMALLINT] NOT NULL
		, [style_id] [DECIMAL](12,0) NOT NULL
		, [color_id] [SMALLINT] NOT NULL
		, [style_color_id] [DECIMAL](13,0) NOT NULL
		, [price_status_id] [SMALLINT] NOT NULL
		, [valuation_unit_retail] [DECIMAL](14,2) NOT NULL
		, [selling_unit_retail] [DECIMAL](14,2) NOT NULL )

ALTER TABLE
	#tt_frozen_on_hand
ADD PRIMARY KEY CLUSTERED
	( location_id
	, sku_id
	, inventory_status_id )

ALTER TABLE
	#tt_pack_frozen_on_hand
ADD PRIMARY KEY CLUSTERED
	( location_id
	, pack_id )

ALTER TABLE
	#tt_future_on_hand
ADD PRIMARY KEY CLUSTERED
	( location_id
	, sku_id
	, inventory_status_id )

ALTER TABLE
	#tt_pack_future_on_hand
ADD PRIMARY KEY CLUSTERED
	( location_id
	, pack_id )

ALTER TABLE
	#tt_frozen_retails
ADD PRIMARY KEY NONCLUSTERED
	( id )

ALTER TABLE
	#tt_frozen_retails
ADD UNIQUE CLUSTERED
	( location_id
	, style_id
	, color_id
	, style_color_id )

ALTER TABLE
	#tt_price_date
ADD PRIMARY KEY CLUSTERED
	( location_id
	, jurisdiction_id
	, style_id
	, color_id
	, style_color_id )

ALTER TABLE
	#tt_price_id
ADD PRIMARY KEY CLUSTERED
	( location_id
	, jurisdiction_id
	, style_id
	, color_id
	, style_color_id )

ALTER TABLE
	#tt_price
ADD PRIMARY KEY CLUSTERED
	( location_id
	, style_id
	, color_id
	, style_color_id )


ALTER TABLE 
	#tt_frozen_chain_on_hand 
ADD PRIMARY KEY NONCLUSTERED
	( style_id)

ALTER TABLE
	#tt_frozen_juris_on_hand 
ADD PRIMARY KEY NONCLUSTERED 
	( style_id
	, jurisdiction_id )

ALTER TABLE 
	#tt_future_chain_on_hand 
ADD PRIMARY KEY NONCLUSTERED 
	( style_id)

ALTER TABLE
	#tt_future_juris_on_hand 
ADD PRIMARY KEY NONCLUSTERED 
	( style_id
	, jurisdiction_id )
```

