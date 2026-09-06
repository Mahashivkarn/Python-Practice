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
    print("GAPS:", gaps)
    for gap in gaps:
                
        skill = gap["skills"]

        print("\nLearn:", skill)

        for step in learning_path.get(skill,[]):
            print(" →", step)
    return{
        "match_score" :match_score,
        "skill" : result
    }
students_skills ={
    "python" : 80,
    "c":70,
    "c++":5,
    "HTML":50
}
job_requirements= {
    "python":{
        "required" : 70,
        "score" : 5
    },
    "c" : {
        "required" :65,
        "score" : 4
    },
    "c++" : {
        "required" : 60,
        "score":4
    },
    "HTML" : {
        "required" : 80,
        "score" : 3,
    }
}

result = analyze_skills(
    students_skills,
    job_requirements
)   

print(result)
