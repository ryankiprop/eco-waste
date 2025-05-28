from lib.db.models import session, User, WasteEntry, DisposalMethod
from datetime import date

def seed_database():
    user = User(name="Eco User")
    entry = WasteEntry(
        date=date.today(),
        waste_type="Plastic",
        weight_kg=0.5,
        user=user
    )
    method = DisposalMethod(method="Recycled", waste_entry=entry)
    session.add_all([user, entry, method])
    session.commit()

if __name__ == "__main__":
    seed_database()