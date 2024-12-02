from app.models import db, Echo

def create_echo(user_id, content, expires_at):
    """Logic to create a new echo."""
    new_echo = Echo(user_id=user_id, content=content, expires_at=expires_at)
    db.session.add(new_echo)
    db.session.commit()
    return new_echo

def get_user_echos(user_id):
    """Retrieve all echoes for a specific user."""
    return Echo.query.filter_by(user_id=user_id).all()
