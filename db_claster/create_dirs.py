from os import mkdir
from os import path
from pathlib import Path

file = Path(__file__).parent.absolute()


def check(name):
    if not path.exists(f"{file}\\{name}"):
        mkdir(f"{file}\\{name}")
    return


check("pg_replslot")
check("pg_tblspc")
check("pg_notify")
check("pg_twophase")
check("pg_commit_ts")
check("pg_stat_tmp")
check("pg_snapshots")
check("pg_logical")
check("pg_logical\\snapshots")
check("pg_logical\\mappings")
