from streamsets.sdk import ControlHub


# cred id: eea2903f-eae8-44ea-9690-1955aa2ae746
# Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzIjoiOWViZGY5MTBlNjM1ZTdkOGYxNzE4MjhhZjQ4Y2JlNjZkOTJmZDgxYzA1NjkwZTA4N2FkNDUxOTc2M2FjMmNjMjVmNmMyYjE4OTY0ODJiNjM0MTcyNmZiYmQ0MjJjMzUyMzQ2MTZjN2ZlMGNlZjRkYmY4OGNiYTUxODBhMTljMDMiLCJ2IjoxLCJpc3MiOiJldTAxIiwianRpIjoiZWVhMjkwM2YtZWFlOC00NGVhLTk2OTAtMTk1NWFhMmFlNzQ2IiwibyI6IjA5N2YyYmI3LTMwMGQtMTFlYy04NWYxLTI5NDAxNTNkODM3NiJ9.


def connect():
    sch = ControlHub(credential_id="eea2903f-eae8-44ea-9690-1955aa2ae746",
                             token="eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzIjoiOWViZGY5MTBlNjM1ZTdkOGYxNzE4MjhhZjQ4Y2JlNjZkOTJmZDgxYzA1NjkwZTA4N2FkNDUxOTc2M2FjMmNjMjVmNmMyYjE4OTY0ODJiNjM0MTcyNmZiYmQ0MjJjMzUyMzQ2MTZjN2ZlMGNlZjRkYmY4OGNiYTUxODBhMTljMDMiLCJ2IjoxLCJpc3MiOiJldTAxIiwianRpIjoiZWVhMjkwM2YtZWFlOC00NGVhLTk2OTAtMTk1NWFhMmFlNzQ2IiwibyI6IjA5N2YyYmI3LTMwMGQtMTFlYy04NWYxLTI5NDAxNTNkODM3NiJ9.")
    return sch