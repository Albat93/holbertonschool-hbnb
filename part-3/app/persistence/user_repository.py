from app.models.user import User
from app.persistence.repository import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        """Retourne un utilisateur dont l'email correspond à celui passé en paramètre."""
        return self.model.query.filter_by(email=email).first()
