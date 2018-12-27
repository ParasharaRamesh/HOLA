from django.apps import AppConfig


class RestConfig(AppConfig):
    name = 'rest'

    def ready(self):
        from rest.utils.tablesetup import TableSetup
        tableSetup = TableSetup(randomSeed=1)
        print("Clearing all tables...")
        tableSetup.clearAllTables()
        print("Populating all tables")
        tableSetup.initTables(tripTable=True)
