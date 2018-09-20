from app import create_app,db
from flask_script import Manager, Server
from app.models import User,OAuth,Follow
from  flask_migrate import Migrate, MigrateCommand

# instances for the create_app
app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)


migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, User=User,Follow=Follow,OAuth = OAuth)


if __name__ == '__main__':
    manager.run()
