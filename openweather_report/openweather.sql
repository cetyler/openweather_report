-- name: save_json_data!
-- Insert json data.
insert into weather.raw_json_data (
         entry_date
        ,api_call
        ,raw_data
        ,software_version
)
values (
         :entry_date
        ,:api_call
        ,:raw_data
        ,:software_version
);

-- name: save_json_data_no_schema!
-- Insert json data.
insert into raw_json_data (
         entry_date
        ,api_call
        ,raw_data
        ,software_version
)
values (
         :entry_date
        ,:api_call
        ,:raw_data
        ,:software_version
);

-- name: create_raw_json_data_sqlite!
-- Create raw_json_data table
create table if not exists raw_json_data (
	     id integer primary key
	    ,entry_date text not null
	    ,api_call text no null
	    ,raw_data text null
	    ,software_version text null
);

-- name: create_raw_json_data_duckdb!
-- Create raw_json_data table
create table if not exists raw_json_data (
	     id integer
	    ,entry_date timestamp with time zone not null
	    ,api_call text not null
	    ,raw_data json null
	    ,software_version text null
	    ,primary key (id)
);

-- name: create_raw_json_data_postgresql!
-- Create raw_json_data table
create table if not exists weather.raw_json_data (
	     id bigserial not null
	    ,entry_date timestamp with time zone not null
	    ,api_call text no null
	    ,raw_data jsonb null
	    ,software_version text null
	    ,primary key (id)
);

-- name: create_weather_schema_postgresql!
-- Create weather schema
create schema if not exists weather;
