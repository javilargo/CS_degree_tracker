class Course:
    def __init__(self, id, level, name, requirements, status, unlocks):
        self.id = id
        self.level = level
        self.name = name
        self.requirements = requirements
        self.status = status
        self.unlocks = unlocks
        
    def __repr__(self):
        return f"Course('{self.id}',{self.level},'{self.name}',{self.requirements},'{self.status}',{self.unlocks})"