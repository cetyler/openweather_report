-- name: save_json_data!
-- Insert json data.
insert into temperature.raw_json_data (
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
