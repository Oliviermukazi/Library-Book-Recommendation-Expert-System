from flask import Flask, request, render_template_string

app = Flask(__name__)

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
        "Database Design for Mere Mortals",
        "Practical Database Administration"
    ],
    ("Database", "advanced"): [
        "Distributed Database Systems",
        "Database Internals",
        "Advanced Database Management"
    ]
}


@app.route("/", methods=["GET", "POST"])
def home():

    books = []

    if request.method == "POST":
        subject = request.form.get("subject")
        level = request.form.get("level")

        books = recommendations.get(
            (subject, level),
            ["No recommendations found for this selection."]
        )

    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Smart Library Recommendation System</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
body{
    background: linear-gradient(135deg,#0f172a,#1e293b);
    min-height:100vh;
    color:white;
    font-family:Segoe UI,sans-serif;
}

.container-box{
    max-width:900px;
    margin:auto;
    margin-top:50px;
    background:rgba(255,255,255,0.08);
    padding:40px;
    border-radius:20px;
    backdrop-filter:blur(10px);
}

.title{
    text-align:center;
    margin-bottom:30px;
    font-weight:bold;
}

.btn-custom{
    background:#6366f1;
    border:none;
}

.book{
    background:#1e293b;
    padding:12px;
    border-radius:10px;
    margin-top:10px;
}
</style>

</head>
<body>

<div class="container-box">

<h1 class="title">📚 Smart Library Expert System</h1>

<form method="POST">

<div class="mb-3">
<label>Program of Study</label>
<input type="text" class="form-control" name="program">
</div>

<div class="mb-3">
<label>Subject Interest</label>
<select class="form-select" name="subject">
<option value="AI">AI</option>
<option value="Database">Database</option>
</select>
</div>

<div class="mb-3">
<label>Reading Level</label>
<select class="form-select" name="level">
<option value="beginner">Beginner</option>
<option value="intermediate">Intermediate</option>
<option value="advanced">Advanced</option>
</select>
</div>

<button type="submit" class="btn btn-custom text-white">
Recommend Books
</button>

</form>

{% if books %}
<hr>
<h3>Recommended Books</h3>

{% for book in books %}
<div class="book">
    {{ book }}
</div>
{% endfor %}

{% endif %}

</div>

</body>
</html>
""", books=books)


if __name__ == "__main__":
    app.run(debug=True)