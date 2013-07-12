SELECT 
narratives.report_key,
devices.brand_name,
devices.generic_name,
devices.model_number,
contacts.name,
deviceproblemcodes.description,
narratives.text
FROM narratives, devices, contacts, deviceproblems, deviceproblemcodes
WHERE
narratives.text like '%blue screen%'
AND narratives.report_key = deviceproblems.report_key
AND deviceproblems.device_problem_code = deviceproblemcodes.code
AND devices.manufacturer_id = contacts.id;


select narratives.report_key, narratives.text from narratives where narratives.text like '%blue screen%';
select narratives.report_key, deviceproblems.device_problem_code, narratives.text from narratives, deviceproblems where narratives.text like '%blue screen%' and deviceproblems.report_key = narratives.report_key;
select narratives.report_key, deviceproblemcodes.description, narratives.text from narratives, deviceproblems, deviceproblemcodes where narratives.text like '%blue screen%' and deviceproblemcodes.code = deviceproblems.device_problem_code AND deviceproblems.report_key = narratives.report_key;


select narratives.report_key, devices.brand_name, devices.generic_name, devices.model_number, narratives.text from narratives, devices where narratives.text like '%blue screen%' and devices.report_key = narratives.report_key;