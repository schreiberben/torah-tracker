if __name__ == "__main__":
    from flask import Flask
    from flask_restful import Api

    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    
    from models import db
    db.init_app(app)

    # api.add_resource()  # TODO


    app.run(debug=True)
