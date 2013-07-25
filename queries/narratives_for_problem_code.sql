select narratives.text from narratives, deviceproblems where deviceproblems.report_key = narratives.report_key and deviceproblems.code = 1317;


SELECT T.*, narratives.text FROM (SELECT report_key, code FROM deviceproblems WHERE code = 2882 OR code = 2899 OR code = 3025 ) as T INNER JOIN narratives ON narratives.report_key = T.report_key;

SELECT distinct report_key FROM deviceproblems WHERE code = 2882 OR code = 2899 OR code = 3025 OR code = 1111 OR code = 1112 OR code = 1138 OR code = 1189 OR code = 1449 OR code = 1473 OR code = 1495 OR code = 2581 OR code = 2582 OR code = 2879 OR code = 2880 OR code = 2881 OR code = 2898 OR code = 2996 OR code = 2997 OR code = 3013 OR code = 3014 OR code = 1497 OR code = 2902 OR code = 2903 OR code = 2591; 
