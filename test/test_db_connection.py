from ai_notes_generator.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from ai_notes_generator.db import get_db

print("Loaded config:")
print("DB_HOST:", repr(DB_HOST))
print("DB_USER:", repr(DB_USER))
print("DB_PASSWORD:", repr(DB_PASSWORD))
print("DB_NAME:", repr(DB_NAME))

try:
    connection = get_db()
    print("✅ Database connected successfully.")
    connection.close()
except Exception as exc:
    print("❌ Database connection failed.")
    print("Error:", exc)