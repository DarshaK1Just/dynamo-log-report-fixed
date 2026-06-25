# Task: Parse Access Log into JSON Report

An Apache-style access log is available at `/app/access.log`.

Your job is to parse it and write a JSON summary report to `/app/report.json`.

## Required output format

The file `/app/report.json` must be valid JSON with exactly these three fields:

```json
{
  "total_requests": <integer — total number of log lines>,
  "unique_ips":     <integer — number of distinct client IP addresses>,
  "top_path":       <string  — the URL path that appears most often in requests>
}
```

## Success criteria

1. `/app/report.json` exists when your work is complete.
2. `total_requests` is the exact count of non-blank lines in the log.
3. `unique_ips` is the exact count of distinct IP addresses (first field of each log line).
4. `top_path` is the URL path (e.g. `/index.html`) with the highest request count; if there is a tie, any one of the tied paths is acceptable.
5. The file contains no additional top-level keys beyond the three listed above.
