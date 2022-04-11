import ampalibe
from view import UserView
from model import UserModel
from conf import Configuration

userView = UserView()
userModel = UserModel(Configuration())


@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    userView.greeting(sender_id)


@ampalibe.command('/users')
def main(**extends):
    userView.send_list_user(sender_id, userModel.list_users())