"""
ogrencileri sinav puanlarina gore
dersi gecip gecmediklerini hesaplayan
bir program yaziniz
"""

from typing import Dict


student1 = { "exam1": 50, "exam2": 10 }
student2 = { "exam1": 90, "exam2": 70 }
student3 = { "exam1": 50, "exam2": 70 }

students = { 
    "ahmet": { "exam1": 50, "exam2": 10 }, 
    "ali": { "exam1": 90, "exam2": 70 }, 
    "ayse": { "exam1": 50, "exam2": 70 }
}


result = {}

for student in students.items():
    studentName = student[0]
    studentExams = student[1]
    exam1 = studentExams["exam1"]
    exam2 = studentExams["exam2"]

    ortalama = (exam1 + exam2) / 2

    if ortalama >= 50:
        result[studentName] = "GECTI"
    else:
        result[studentName] = "KALDI"


print(result)
