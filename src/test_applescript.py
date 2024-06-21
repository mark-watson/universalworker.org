from applescript_lib import *

def test(path):
    print(f"\nTesting AppleScript at {path} ")
    output = applescript_to_text(path)
    print(output)

if __name__ == "__main__":
    test("scripts/calendar_today.sctp")
    test("scripts/email_subjects.sctp")
    test("scripts/notes.sctp")
