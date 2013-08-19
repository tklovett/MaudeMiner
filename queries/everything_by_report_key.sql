SELECT * FROM Events, Narratives, Devices, DeviceProblems, Patients LEFT JOIN (SELECT DISTINCT report_key as rk FROM events) AS T ON Events.report_key = T.rk, Narratives.report_key = T.rk, Devices.report_key = T.rk, DeviceProblems.report_key = T.rk, Patients.report_key = T.rk

SELECT Events.*, Narratives.*, Devices.*, DeviceProblems.*, Patients.* 
FROM Events 
LEFT JOIN Narratives ON Events.report_key = Narratives.report_key 
LEFT JOIN Devices ON Events.report_key = Devices.report_key 
LEFT JOIN DeviceProblems ON Events.report_key = DeviceProblems.report_key 
LEFT JOIN Patients ON Events.report_key = Patients.report_key 
ORDER BY Events.report_key;