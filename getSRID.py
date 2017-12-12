subject = "hello world SRID: 12343324 I am not a bankster"
  
subjectSRIDIndex= subject.index('SRID')+6
subSubject = subject[subjectSRIDIndex:]
subSubjectIndex= len(subSubject) - subSubject.index(' ')+1
result = subSubject[0: subSubject.index(' ')+1: ]

print(subject)
print(subSubject)
print(result)
