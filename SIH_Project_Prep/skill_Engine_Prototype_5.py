def analyze_skills(student_skills, job_requirements):

    results = []

    total_contribution = 0
    total_weight = 0

    for skill, requirement in job_requirements.items():

        current = student_skills.get(skill, 0)

        required = requirement["required"]
        weight = requirement["weight"]

        gap = max(required - current, 0)

        skill_ratio = min(current / required, 1)

        contribution = skill_ratio * weight

        total_contribution += contribution
        total_weight += weight

        priority = gap * weight

        results.append({
            "skill": skill,
            "current": current,
            "required": required,
            "gap": gap,
            "weight": weight,
            "priority": priority
        })

    if total_weight > 0:
        match_score = (
            total_contribution / total_weight
        ) * 100
    else:
        match_score = 0

    gaps = [
        skill for skill in results
        if skill["gap"] > 0
    ]

    gaps.sort(
        key=lambda x: x["priority"],
        reverse=True
    )

    return {
        "match_score": round(match_score, 2),
        "skills": results,
        "gaps": gaps
    }


# -------------------------
# STUDENT INPUT
# -------------------------

student_name = input("Student name: ")

student_skills = {}

n = int(input("Number of student skills: "))

for i in range(n):

    skill = input(f"Skill {i+1}: ")

    level = int(
        input("Proficiency (0-100): ")
    )

    student_skills[skill] = level


# -------------------------
# COMPANY INPUT
# -------------------------

company_name = input("Company name: ")

job_title = input("Job title: ")

job_requirements = {}

n = int(input("Number of required skills: "))

for i in range(n):

    skill = input(f"Required skill {i+1}: ")

    required = int(
        input("Required proficiency (0-100): ")
    )

    weight = int(
        input("Importance (1-5): ")
    )

    job_requirements[skill] = {
        "required": required,
        "weight": weight
    }


# -------------------------
# ANALYSIS
# -------------------------

result = analyze_skills(
    student_skills,
    job_requirements
)


# -------------------------
# DISPLAY
# -------------------------

print("\n==============================")
print("       SKILL BRIDGE AI")
print("==============================")

print("\nStudent:", student_name)
print("Company:", company_name)
print("Job:", job_title)

print(
    "\nMATCH SCORE:",
    result["match_score"],
    "%"
)

print("\nSKILL ANALYSIS")

for skill in result["skills"]:

    status = (
        "MATCHED"
        if skill["gap"] == 0
        else "GAP"
    )

    print(
        f"{skill['skill']}: "
        f"{skill['current']}/"
        f"{skill['required']} "
        f"→ {status}"
    )


print("\nPRIORITY SKILL GAPS")

for i, gap in enumerate(result["gaps"], 1):

    print(
        f"{i}. {gap['skill']} "
        f"(Gap: {gap['gap']}, "
        f"Priority: {gap['priority']})"
    )


print("\nLEARNING ROADMAP")

learning_paths = {

    "Python": [
        "Python Fundamentals",
        "OOP",
        "Advanced Python",
        "Python Project"
    ],

    "SQL": [
        "SQL Basics",
        "CRUD",
        "Joins",
        "Database Project"
    ],

    "Flask": [
        "Flask Basics",
        "Routing",
        "REST APIs",
        "Database Integ=ration",
        "Flask Project"
    ],

    "Git": [
        "Git Basics",
        "GitHub",
        "Branches",
        "Pull Requests"
    ]
}

for gap in result["gaps"]:

    skill = gap["skill"]

    print(f"\n{skill}:")

    for step in learning_paths.get(
        skill,
        ["Find appropriate learning resources"]
    ):
        print(" →", step)