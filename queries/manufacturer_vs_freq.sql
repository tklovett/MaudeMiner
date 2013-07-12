SELECT count(report_key), contacts.name, contacts.street_1 FROM events, contacts WHERE events.manufacturer_id = contacts.id GROUP BY contacts.name HAVING count(report_key) > 1;
SELECT count(report_key), contacts.name, contacts.street_1 FROM events, contacts WHERE events.manufacturer_id = contacts.id GROUP BY contacts.street_1 HAVING count(report_key) > 1;