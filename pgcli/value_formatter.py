from psycopg.abc import Dumper


def format_value_with_dumper(value, dumper: Dumper | None, escape_for_sql=False):
    if value is None:
        return "NULL"

    if dumper is None:
        return f"'{value}'"

    if escape_for_sql:
        res = dumper.quote(value)
    else:
        res = dumper.dump(value)

    try:
        return res.decode()
    except AttributeError:  # res may be memoryview
        return res.hex()
