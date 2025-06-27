from config import app, db
from reserva.reserva_route import reservas_bp

app.register_blueprint(reservas_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(
            host=app.config["HOST"],
            port=app.config["PORT"],
            debug=app.config["DEBUG"]
        )