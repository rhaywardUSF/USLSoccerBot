def init_tables():
    global conn
    global c
    conn = sqlite3.connect(location)
    c = conn.cursor()
    create_structureStatuses_table()
    populate_structureStatuses_table()
    create_flairs_table()
    populate_flairs_table()
    create_leagues_table()
    populate_leagues_table()
    create_regions_table()
    populate_regions_table()
    create_conferences_table()
    populate_conferences_table()
    create_divisions_table()
    create_teams_table()
    populate_teams_table()

def create_structureStatuses_table():
    tPrint("Create structureStatuses table")
    sql = "CREATE TABLE IF NOT EXISTS structureStatuses " \
    "(" \
    "id INTEGER, " \
    "status TEXT UNIQUE NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id) " \
    ")"
    c.execute(sql)

def populate_structureStatuses_table():
    tPrint("Populate structureStatuses table")
    for structureStatus in structureStatuses:
        tPrint("add Status " + str(structureStatus['status']))
        sql = "INSERT OR IGNORE INTO structureStatuses (id, status) " \
        "VALUES "\
        "(" \
        "?" \
        ", " \
        "?" \
        ")"
        c.execute(sql, (structureStatus['id'], structureStatus['status']))
        sql = "UPDATE structureStatuses " \
        "SET id = ?, " \
        "status = ? " \
        "WHERE id = ?"
        c.execute(sql, (structureStatus['id'], structureStatus['status'], structureStatus['id']))

def create_flairs_table():
    tPrint("Create flairs table")
    sql = "CREATE TABLE IF NOT EXISTS flairs " \
    "(" \
    "id INTEGER, " \
    "flairLabel TEXT DEFAULT(''), " \
    "flairClass TEXT UNIQUE NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id) " \
    ")"
    c.execute(sql)

def populate_flairs_table():
    tPrint("Populate flairs table")
    for flair in flairs:
        tPrint("add Flair " + str(flair['flairLabel']))
        sql = "INSERT OR IGNORE INTO flairs (flairLabel, flairClass) " \
        "VALUES "\
        "(" \
        "?, ?" \
        ")"
        c.execute(sql, (flair['flairLabel'], flair['flairClass']))
        sql = "UPDATE flairs " \
        "SET " \
        "flairLabel = ?, " \
        "flairClass = ? " \
        "WHERE flairClass = ?"
        c.execute(sql, (flair['flairLabel'], flair['flairClass'], flair['flairClass']))

def create_leagues_table():
    tPrint("Create leagues table")
    sql = "CREATE TABLE IF NOT EXISTS leagues " \
    "(" \
    "id INTEGER, " \
    "name TEXT NOT NULL, " \
    "abbreviation TEXT NOT NULL, " \
    "flairId INTEGER, " \
    "statusId INTEGER NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id), " \
    "FOREIGN KEY(statusId) REFERENCES structureStatuses(id), " \
    "FOREIGN KEY(flairId) REFERENCES flairs(id)" \
    ")"
    c.execute(sql)

def populate_leagues_table():
    tPrint("Populate leagues table")
    for league in leagues:
        tPrint("add League " + str(league['name']))
        sql = "INSERT OR IGNORE INTO leagues (id, name, abbreviation, flairId, statusId) " \
        "VALUES "\
        "(" \
        "?, ?, ?, ?, ?" \
        ")"
        c.execute(sql, (league['id'], league['name'], league['abbreviation'], league['flairClass'], league['statusId']))
        sql = "UPDATE leagues " \
        "SET id = ?, " \
        "name = ?, " \
        "abbreviation = ?, "\
        "flairId = (SELECT id FROM flairs WHERE flairClass = ?), " \
        "statusId = ? " \
        "WHERE id = ?"
        c.execute(sql, (league['id'], league['name'], league['abbreviation'], league['flairClass'], league['statusId'], league['id']))

def create_regions_table():
    tPrint("Create regions table")
    sql = "CREATE TABLE IF NOT EXISTS regions " \
    "(" \
    "id INTEGER, " \
    "name TEXT NOT NULL, " \
    "abbreviation TEXT NOT NULL, " \
    "flairId INTEGER, " \
    "leagueId INTEGER NOT NULL, " \
    "statusId INTEGER NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id), " \
    "FOREIGN KEY(statusId) REFERENCES structureStatuses(id)," \
    "FOREIGN KEY(flairId) REFERENCES flairs(id), " \
    "FOREIGN KEY(leagueId) REFERENCES leagues(id)" \
    ")"
    c.execute(sql)

def populate_regions_table():
    tPrint("Populate regions table")
    for region in regions:
        tPrint("add Region " + str(region['name']))
        sql = "INSERT OR IGNORE INTO regions (id, name, abbreviation, flairId, leagueId, statusId) " \
        "VALUES "\
        "(" \
        "?, ?, ?, (SELECT id FROM flairs WHERE flairClass = ?), ?, ?" \
        ")"
        c.execute(sql, (region['id'], region['name'], region['abbreviation'], region['flairClass'], region['leagueId'], region['statusId']))
        sql = "UPDATE regions " \
        "SET id = ?, " \
        "name = ?, " \
        "abbreviation = ?, "\
        "flairId = (SELECT id FROM flairs WHERE flairClass = ?), " \
        "leagueId = ?, " \
        "statusId = ? " \
        "WHERE id = ?"
        c.execute(sql, (region['id'], region['name'], region['abbreviation'], region['flairClass'], region['leagueId'], region['statusId'], region['id']))


def create_conferences_table():
    tPrint("Create conferences table")
    sql = "CREATE TABLE IF NOT EXISTS conferences " \
    "(" \
    "id INTEGER, " \
    "name TEXT NOT NULL, " \
    "abbreviation TEXT NOT NULL, " \
    "flairId INTEGER, " \
    "leagueId INTEGER NOT NULL, " \
    "regionId INTEGER DEFAULT -1, " \
    "statusId INTEGER NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id), " \
    "FOREIGN KEY(statusId) REFERENCES structureStatuses(id), " \
    "FOREIGN KEY(flairId) REFERENCES flairs(id), " \
    "FOREIGN KEY(leagueId) REFERENCES leagues(id), " \
    "FOREIGN KEY(regionId) REFERENCES regions(id)" \
    ")"
    c.execute(sql)

def populate_conferences_table():
    tPrint("Populate conferences table")
    for conference in conferences:
        tPrint("add Conference " + str(conference['name']))
        sql = "INSERT OR IGNORE INTO conferences (id, name, abbreviation, flairId, leagueId, regionId, statusId) " \
        "VALUES "\
        "(" \
        "?, ?, ?, (SELECT id FROM flairs WHERE flairClass = ?), ?, ?, ?" \
        ")"
        c.execute(sql, (conference['id'], conference['name'], conference['abbreviation'], conference['flairClass'], conference['leagueId'], conference['regionId'], conference['statusId']))
        sql = "UPDATE conferences " \
        "SET id = ?, " \
        "name = ?, " \
        "abbreviation = ?, "\
        "flairId = (SELECT id FROM flairs WHERE flairClass = ?), " \
        "leagueId = ?, " \
        "regionId = ?, " \
        "statusId = ? " \
        "WHERE id = ?"
        c.execute(sql, (conference['id'], conference['name'], conference['abbreviation'], conference['flairClass'], conference['leagueId'], conference['regionId'], conference['statusId'], conference['id']))



def create_divisions_table():
    tPrint("Create divisions table")
    sql = "CREATE TABLE IF NOT EXISTS divisions " \
    "(" \
    "id INTEGER, " \
    "name TEXT NOT NULL, " \
    "abbreviation TEXT NOT NULL, " \
    "flairId INTEGER, " \
    "leagueId INTEGER NOT NULL, " \
    "regionId INTEGER DEFAULT -1, " \
    "conferenceId INTEGER DEFAULT -1, " \
    "statusId INTEGER NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id), " \
    "FOREIGN KEY(statusId) REFERENCES structureStatuses(id), " \
    "FOREIGN KEY(flairId) REFERENCES flairs(id), " \
    "FOREIGN KEY(leagueId) REFERENCES leagues(id), " \
    "FOREIGN KEY(regionId) REFERENCES regions(id), " \
    "FOREIGN KEY(conferenceId) REFERENCES conferences(id)" \
    ")"
    c.execute(sql)

def create_teams_table():
    tPrint("Create teams table")
    sql = "CREATE TABLE IF NOT EXISTS teams " \
    "(" \
    "id INTEGER, " \
    "name TEXT NOT NULL, " \
    "abbreviation TEXT NOT NULL, " \
    "leagueId INTEGER NOT NULL, " \
    "regionId INTEGER DEFAULT -1," \
    "conferenceId INTEGER DEFAULT -1, " \
    "divisionId INTEGER DEFAULT -1, " \
    "flairId INTEGER, " \
    "statusId INTEGER NOT NULL, " \
    "createdOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "updatedOn DATETIME NOT NULL DEFAULT (datetime(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))), " \
    "PRIMARY KEY(id), " \
    "FOREIGN KEY(leagueId) REFERENCES leagues(id), " \
    "FOREIGN KEY(regionId) REFERENCES regions(id), " \
    "FOREIGN KEY(conferenceId) REFERENCES conferences(id), " \
    "FOREIGN KEY(divisionId) REFERENCES divisions(id), " \
    "FOREIGN KEY(flairId) REFERENCES flairs(id), " \
    "FOREIGN KEY(statusId) REFERENCES structureStatuses(id)" \
    ")"
    c.execute(sql)

def populate_teams_table():
    tPrint("Populate teams table")
    for team in teams:
        tPrint("add team " + str(team['name']))
        sql = "INSERT INTO teams (name, abbreviation, leagueId, regionId, conferenceId, divisionId, flairId, statusId) " \
        "VALUES "\
        "(" \
        "?, ?, ?, ?, ?, ?, (SELECT id FROM flairs WHERE flairClass = ?), ?" \
        ")"
        c.execute(sql, (team['name'], team['abbreviation'], team['leagueId'], team['regionId'], team['conferenceId'], team['divisionId'], team['flairClass'], team['statusId']))
        sql = "UPDATE teams " \
        "SET " \
        "name = ?, " \
        "abbreviation = ?, " \
        "leagueId = ?, " \
        "regionId = ?, " \
        "conferenceId = ?, " \
        "divisionId = ?, " \
        "flairId = (SELECT id FROM flairs WHERE flairClass = ?), " \
        "statusId = ? " \
        "WHERE flairId = (SELECT id FROM flairs WHERE flairClass = ?)"
        c.execute(sql, (team['name'], team['abbreviation'], team['leagueId'], team['regionId'], team['conferenceId'], team['divisionId'], team['flairClass'], team['statusId'], team['flairClass']))

init_tables()