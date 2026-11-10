# Add more questions
# Add category field in each question
# Show category before each question
# Add a points field in each question
# Show in results percentage of correct answers

questions = [
    {
        "question": "Ποια είναι η πρωτεύουσα της Ελλάδας;",
        "options": ["Αθήνα", "Πάτρα", "Λάρισα"],
        "answer": "Αθήνα"
        
    },
    {
        "question": "Πόσο κάνει 5 * 5;",
        "options": ["20", "25", "30"],
        "answer": "25"
    },
    {
        "question": "Ποια γλώσσα μαθαίνουμε;",
        "options": ["Java", "Python", "C++"],
        "answer": "Python"
    }
]

print("==============================")
print("       QUIZ MASTER v0.2")
print("==============================")

while True:
    while True:
        player_name = input("Πώς σε λένε; ").strip()
        if not player_name:
            print ("Το όνομα δεν μπορεί να είναι κενό. Δοκιμάστε ξανά.")
        else:
            break

    score = 0

    print("\nΚαλώς ήρθες,", player_name)
    print("Απάντησε στις παρακάτω ερωτήσεις!\n")

    for index, question in enumerate(questions, start=1):

        print("\nΕρώτηση", index)
        print("------------------------------")

        print(question["question"])

        for option in question["options"]:
            print("-", option)

        answer = input("\nΗ απάντησή σου: ")

        if answer.strip().lower() == question["answer"].lower():
            print("ΣΩΣΤΑ! +1 βαθμός")
            score += 1
        
        else:
            print("ΛΑΘΟΣ!")
            print("Η σωστή απάντηση είναι:", question["answer"])

        print("Τρέχον σκορ:", score)

    print("\n==============================")
    print("       ΤΕΛΙΚΑ ΑΠΟΤΕΛΕΣΜΑΤΑ")
    print("==============================")

    print("Παίκτης:", player_name)
    print("Τελική βαθμολογία:", score, "/", len(questions))

    if score == 3:  
        print("Εξαιρετικά! Τα απάντησες όλα σωστά!")
    elif score == 2:
        print("Πολύ καλά!")
    elif score == 1:
        print("Καλή προσπάθεια!")
    else:
        print("Χρειάζεται λίγη ακόμη εξάσκηση!")

    print("\nΕυχαριστούμε που έπαιξες!")

    while True:
        tryagain = input("\nΠαίξετε ξανά; (Y/N): ").lower()
        if tryagain in ("y", "n"):
            break
        print ("Λάθος επιλογή!")

    if tryagain == "n":
        break



