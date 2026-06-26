An Apache-style access log is available at /app/access.log. Parse it and write a JSON summary report to /app/report.json.

/app/report.json must be a valid JSON object with exactly these three keys:

  total_requests  — integer, exact count of non-blank lines in the log
  unique_ips      — integer, exact count of distinct IP addresses (first whitespace-delimited field on each line)
  top_path        — string, the URL path with the highest request count (extracted from the quoted request field, e.g. "GET /index.html HTTP/1.1" -> /index.html); if two paths tie, either is acceptable

The file must contain no additional top-level keys.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
