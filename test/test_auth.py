from ai_notes_generator.auth_service import login_user, register_user

username = "test_user"
password = "test123"

print("Testing registration...")

try:
    register_user(username, password)
    print("✅ User registered successfully.")
except Exception as exc:
    print("⚠️ Registration error:", exc)

print("\nTesting login...")

try:
    user = login_user(username, password)
    if user:
        print("✅ Login successful:", user)
    else:
        print("❌ Login failed.")
except Exception as exc:
    print("❌ Login error:", exc)