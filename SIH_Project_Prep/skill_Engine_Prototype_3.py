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
        
    return{
        "match_score" :match_score,
        "skill" : result
    }

result = analyze_skills(
    students_skills,
    job_requirements
)
result = analyze_skills(
    students_skills,
    job_requirements
)

print(result)
