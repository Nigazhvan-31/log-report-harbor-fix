# Log Report

An Apache-style access log is available at:

/app/access.log

Your task is to analyze the log and generate a JSON report.

Write the output to:

/app/report.json

The JSON report must contain exactly the following fields:

- total_requests: Total number of requests in the log.
- unique_ips: Number of unique client IP addresses.
- top_path: The request path that appears most frequently.

## Success Criteria

1. The output file is created at `/app/report.json`.
2. The output is valid JSON.
3. The JSON contains exactly these keys:
   - total_requests
   - unique_ips
   - top_path
4. The values are correct based on the contents of `/app/access.log`.