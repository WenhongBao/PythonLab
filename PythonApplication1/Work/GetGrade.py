class Student(object):
    def _init_(self,name,score):
        self.name=name;
        self.score=score;

    def print_score(self):
        print('%s :%s' % (self.name,self.score));

    def get_grade(self):
        if self.score >= 90:
            return 'A';
        elif self.score >=60:
            return 'B';
        else:
            return 'C';

bart = Student('Bart Simposon',59);
lisa = Student('Lisa Simposon',87);

your_name = input('Please input your first name: ');
if your_name=='bart':
    bart.print_score;
    bart.get_grade;
else:
    lisa.print_score;
    lisa.get_grade;
