from ai_notes_generator.ai_service import generate_notes


sample_text = """
Artificial Intelligence is the simulation of human intelligence in machines.
It enables systems to learn, reason, and make decisions.
"""

try:
    result = generate_notes(sample_text)
    print("✅ AI response:")
    print(result)
except Exception as exc:
    print("❌ AI test failed:")
    print(exc)