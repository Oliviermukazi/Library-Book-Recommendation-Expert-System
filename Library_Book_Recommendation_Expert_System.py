
recommendations = {
    ("AI", "beginner"): [
        "Artificial Intelligence: A Modern Approach",
        "AI Basics for Beginners",
        "Introduction to Artificial Intelligence"
    ],
    ("AI", "intermediate"): [
        "Machine Learning with Python",
        "Hands-On Machine Learning",
        "Deep Learning Fundamentals"
    ],
    ("AI", "advanced"): [
        "Deep Learning",
        "Reinforcement Learning: An Introduction",
        "Advanced AI Research Papers"
    ],

    ("Database", "beginner"): [
        "Database System Concepts",
        "Learning SQL",
        "Introduction to Databases"
    ],
    ("Database", "intermediate"): [
        "SQL Performance Explained",
        "Database Design for Mere Mortals",s
        "Practical Database Administration"
    ],
    ("Database", "advanced"): [
        "Distributed Database Systems",
        "Database Internals",
        "Advanced Database Management"
    ],

    ("Networking", "beginner"): [
        "Computer Networking Basics",
        "Networking for Beginners",
        "Introduction to Network Security"
    ],
    ("Networking", "advanced"): [
        "Computer Networks",
        "Advanced Network Security",
        "Network Protocol Analysis"
    ]
}


def recommend_books(subject, level):
    key = (subject, level)

    if key in recommendations:
        return recommendations[key]
    else:
        return ["No recommendation found for this combination."]


def main():
    print("=" * 50)
    print("LIBRARY BOOK RECOMMENDATION EXPERT SYSTEM")
    print("=" * 50)

    program = input("Enter Program of Study: ")
    subject = input("Enter Subject Interest (AI, Database, Networking): ")
    level = input("Enter Reading Level (beginner/intermediate/advanced): ")

    books = recommend_books(subject, level)

    print("\nRecommended Books:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book}")


if __name__ == "__main__":
    main()