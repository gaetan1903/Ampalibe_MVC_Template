from ampalibe import Model


class UserModel(Model):

    def __init__(self, conf):
        super().__init__(conf)
    

    @Model.verif_db
    def list_users(self):
        self.cursor.execute("SELECT * FROM amp_user")
        res = self.cursor.fetchall()
        self.db.commit()
        return res