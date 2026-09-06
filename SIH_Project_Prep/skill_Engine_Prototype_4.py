def analyze_skills(students_skills,job_requirements):
    result =[]
    
    total_contribution = 0
    total_score = 0
    
    for skill, requirement in job_requirements.items():
        
        current = students_skills.get(skill,0)
        required = requirement["required"] 
        score = requirement["score"]
         
        
        gap =max(required-current,0)
        
        skill_ratio =min(current/required,1)
        
        contribution =skill_ratio*score
        
        total_contribution += contribution
        total_score += score
        
        
        
        priority_score = gap * score
        
        result.append({
            "skills" :skill,
            "current" : current,
            "required" : required,
            "gap": gap,
            "score" : score,
            "priority" : priority_score
        })
        match_score = (
            total_contribution / total_score
        )*100
        
        gaps = [
            skill for skill in result
            if skill["gap"] > 0
        ]
        
        gaps.sort(
            key =lambda x : x["priority"],
            reverse = True
        )
        learning_path = {
            
            "python" : [
                "Python Fundamentals",
                "OOP",
                "Advanced Python",
                "Python Projects"
            ],
            "c" : [
                "C Fundamentals",
                "Pointers",
                "Array",
            ],
            "c++" : [
                "C++ Fundamentals",
                "OOP",
                "STL"
            ],
            "HTML" : [
                "HTML Basics",
                "HTML Forms",
                "HTML Projects"
            ]
                
        }
    
    for gap in gaps:
                
        skill = gap["skills"]

        print("\nLearn:", skill)

        for step in learning_path.get(skill,[]):
            print(" →", step)
    return{
        "match_score" :match_score,
        "skill" : result
    }

    
#Input From The Students


students_name =input("Enter Your Name:")

students_skills ={}

number_of_skills = int(input("How many skills do you have?"))

for i in range(number_of_skills) :
    
    skill = input("Enter Skill Name:")
    
    level=int(input("Enter Proefficiency (0-100):"))
    
    students_skills[skill] = level
    
    
#Input From The Companys    


company_name =input("Enter Company's Name:")

job_titles = input("Enter job title:")

job_requirements = {}

number_of_requirements = int(input("How Many Required Skills?"))

for i in range(number_of_requirements):
    
    skill = input("Enter Required Skill:")
    
    required = int(input("Required Proefficiency (0-100)"))
    
    score = int(input("Importance (1-5):"))
    
    job_requirements[skill] ={
        "required" : required,
        "score" : score
    }

result = analyze_skills(
    students_skills,
    job_requirements
)   

print(result)
