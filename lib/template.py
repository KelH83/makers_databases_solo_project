class Template:
    def __init__(self, full_name, cohort):
        self.full_name = full_name
        self.cohort = cohort

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Name:{self.full_name},Cohort:{self.cohort}"
