catalog = {
    "Algorithm Design": {"algorithms", "mathematics", "bellman-ford"},
    "Cloud Fundamentals": {"qwiklabs", "gcp", "projects"},
    "Database Management": {"sql", "union", "intersection", "queries"},
    "File System Admin": {"directories", "folders", "templates", "laptops"}
}

user_input = input("Enter your interests separated by commas: ").lower()
user_interests = set([x.strip() for x in user_input.split(",")])

recommendations = []
for item, tags in catalog.items():
    match_score = len(user_interests.intersection(tags))
    if match_score > 0:
        recommendations.append((match_score, item))

recommendations.sort(reverse=True)

if recommendations:
    print("Recommended items:")
    for score, item in recommendations:
        print(f"- {item} (Match score: {score})")
else:
    print("No recommendations found.")