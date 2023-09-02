class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

    def display_experience(self):
        print("company: ", self.company)
        print("Job Title", self.job_title)
        print("Start Date: ", self.start_date)
        print("Expire Date: ", self.end_date)


class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date

    def display_education(self):
        print("degree: ", self.degree)
        print("institution: ", self.institution)
        print("Expire Date: ", self.completion_date)


class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage

    def display_skill(self):
        print("Skill: ", self.skill)
        print("Level: ", self.percentage)


class CV:
    def __init__(self, name):
        self.name = name
        self.experiences = []
        self.education = []
        self.skills = []

    def add_experience(self):
        company = input("Company: ")
        job_title = input("Job Title: ")
        start_date = input("Start Date: ")
        end_date = input("Expire Date: ")

        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)

        answer = input("Do you want to add a new experience (yes/no): ")
        if answer == "yes":
            self.add_experience()

    def add_education(self):
        degree = input("degree: ")
        institution = input("institution: ")
        completion_date = input("Expire Date: ")

        education = Education(degree, institution, completion_date)
        self.education.append(education)

        answer = input("Do you want to add a new education (yes/no): ")
        if answer == "yes":
            self.add_education()

    def add_skill(self):
        skill = input("Skill: ")
        percentage = input("Level: ")

        skill = Skill(skill, percentage)
        self.skills.append(skill)

        answer = input("Do you want to add a new skill (yes/no): ")
        if answer == "yes":
            self.add_skill()

    def display_cv(self):
        print("CV Name: ", self.name)
        print()

        for experience in self.experiences:
            experience.display_experience()
            print()

        for education in self.education:
            education.display_education()
            print()

        for skill in self.skills:
            skill.display_skill()
            print()



name = input("Name: ")
cv = CV(name)
cv.add_skill()
cv.add_education()
cv.add_experience()
cv.display_cv()

