from flask_app import app
from flask_app.controllers import controllers_checklist
from flask_app.models.models_user import User






if __name__=='__main__':
    app.run(debug=True)