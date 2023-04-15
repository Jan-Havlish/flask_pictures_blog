import pickledb

class PickleDBHandler:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = pickledb.load(self.db_path, False)

    def get(self, key):
        """
        Return value of record with a specific key.
        """
        return self.db.get(key)

    def set(self, key, value):
        """
        Save value to specific key.
        """
        self.db.set(key, value)
        self.db.dump()

    def delete(self, key):
        """
        Delate record with specific key.
        """
        self.db.rem(key)
        self.db.dump()

    def get_all(self):
        """
        Return all records in db.
        """
        return list(self.db.getall())