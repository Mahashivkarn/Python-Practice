students_skills ={
    "pyhton" : 80,
    "c":70,
    "c++":5,
    "HTML":50
}
job_requirements= {
    "pyhton":{
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
    
    for skill, requirement in job_requirements.items():
        
        current = students_skills.get(skill,0)
        required = requirement["required"]  
        
        gap =max(required-current,0)
        
        result.append({
            "skills" :skill,
            "current" : current,
            "required" : required,
            "gap": gap
        })
    return result
print(analyze_skills(students_skills,job_requirements))

