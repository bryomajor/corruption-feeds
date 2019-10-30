
from app import create_app
from flask_script import Manager,Server

app = create_app('production')
            
manager =  Manager(app)
manager.add_command('run',Server(use_debugger=True))

if __name__ == "__main__":
    manager.run()
