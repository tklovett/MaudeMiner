select narratives.report_key, deviceproblems.device_problem_code, narratives.text
from narratives, deviceproblems
where deviceproblems.device_problem_code=2882 or deviceproblems.device_problem_code=2899 and narratives.report_key=deviceproblems.report_key;



1590846
1600490
1745795
2307574

select report_key, text from narratives where report_key=1590846 or report_key=1600490 or report_key=1745795 or report_key=2307574;
