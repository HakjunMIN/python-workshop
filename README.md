# Python



## Github 가입
https://docs.github.com/ko/get-started/start-your-journey/creating-an-account-on-github

## Github Copilot 연동 
https://copilot.github.microsoft.com/

## VSCode 설치
https://code.visualstudio.com/download

### 익스텐션설치
https://marketplace.visualstudio.com/VSCode 혹은 VSCode내 Extensions
Github Copilot & Chat, Python, Jupyter

## 문제풀이

### Dict

##### 문제1: 학생 점수 관리
다음과 같은 학생들의 이름과 점수가 주어졌을 때,
	1.	학생 이름을 입력받아 해당 학생의 점수를 출력하는 프로그램을 작성하세요.
	2.	만약 입력한 이름이 존재하지 않으면 “해당 학생이 없습니다.“를 출력하세요.

```python
students = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지영": 90
}
```

출력

```
학생 이름을 입력하세요: 영희
영희의 점수는 92점입니다.

학생 이름을 입력하세요: 수진
해당 학생이 없습니다.
```

<details>
<summary>풀이</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
```python
students = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지영": 90
}

name = input("학생 이름을 입력하세요: ")

if name in students:
    print(f"{name}의 점수는 {students[name]}점입니다.")
else:
    print("해당 학생이 없습니다.")

```
</details>

#### 문제2: 반별 최고 점수 학생 찾기
여러 반의 학생 이름과 점수가 다음과 같이 딕셔너리로 주어집니다.
각 반에서 최고 점수를 받은 학생의 이름과 점수를 출력하는 프로그램을 작성하세요.
```python

classes = {
    "1반": {"철수": 85, "영희": 92, "민수": 78},
    "2반": {"지영": 90, "수진": 88, "현우": 95},
    "3반": {"민지": 91, "지수": 89, "준호": 87}
}
```
출력
```
1반: 영희 (92점)
2반: 현우 (95점)
3반: 민지 (91점)
```
<details>
<summary>풀이</summary>

```python
classes = {
    "1반": {"철수": 85, "영희": 92, "민수": 78},
    "2반": {"지영": 90, "수진": 88, "현우": 95},
    "3반": {"민지": 91, "지수": 89, "준호": 87}
}
for class_name, students in classes.items():
    max_score = max(students.values())
    top_student = [name for name, score in students.items() if score == max_score]
    print(f"{class_name}: {top_student[0]} ({max_score}점)")
```
</details>

#### 백준 문제 20291
문제: 파일 정리
문제 링크:https://www.acmicpc.net/problem/20291

### 함수

#### 문제3. 학생 점수 평균과 최고점수 반환 함수 만들기
학생들의 이름과 점수가 담긴 딕셔너리가 주어집니다.
이 딕셔너리를 인자로 받아,
	•	전체 학생의 평균 점수와
	•	최고 점수를 받은 학생의 이름과 점수
를 튜플로 반환하는 함수를 작성하세요.

```python
students = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지영": 90
}
```

함수 사용예시
```python
result = analyze_scores(students)
print(result)
# 출력 예시: (86.25, '영희', 92)
```

<details>
<summary>풀이</summary>

```python
def analyze_scores(students):
    total_score = sum(students.values())
    average_score = total_score / len(students)
    
    max_score = max(students.values())
    top_student = [name for name, score in students.items() if score == max_score]
    
    return (average_score, top_student[0], max_score)
students = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지영": 90
}
result = analyze_scores(students)
print(result)
# 출력 예시: (86.25, '영희', 92)
```
</details>

#### 문제4: 점수 기준으로 학생 정렬하기 (람다 함수 활용)
학생들의 이름과 점수가 담긴 리스트가 있습니다.
이 리스트를 점수를 기준으로 내림차순 정렬하는 프로그램을 작성하세요.
단, 정렬에는 람다(lambda) 함수를 사용해야 합니다.
```python
students = [
    ("철수", 85),
    ("영희", 92),
    ("민수", 78),
    ("지영", 90)
]

[('영희', 92), ('지영', 90), ('철수', 85), ('민수', 78)]

```

<details>
<summary>풀이</summary>

```python
students = [
    ("철수", 85),
    ("영희", 92),
    ("민수", 78),
    ("지영", 90)
]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
```
</details>

#### 문제5: 학생 점수 5점씩 올리기 (map 함수 활용)
학생들의 이름과 점수가 담긴 리스트가 있습니다.
모든 학생의 점수를 5점씩 올린 새로운 리스트를 만들어 출력하세요.
단, 점수 변환에는 map 함수를 사용해야 합니다.
```python
students = [
    ("철수", 85),
    ("영희", 92),
    ("민수", 78),
    ("지영", 90)
]
```
출력 예시
```
[('철수', 90), ('영희', 97), ('민수', 83), ('지영', 95)]
```

<details>
<summary>풀이</summary>

```python
students = [
    ("철수", 85),
    ("영희", 92),
    ("민수", 78),
    ("지영", 90)
]

# map 함수를 사용하여 점수 5점씩 올리기
new_students = list(map(lambda x: (x[0], x[1] + 5), students))

print(new_students)

```
</details>

#### 문제6: 학생(Student) 클래스 만들기
학생의 이름과 점수를 저장하는 Student 클래스를 만드세요.
이 클래스는 다음과 같은 기능을 가져야 합니다.
	1.	생성자에서 이름과 점수를 입력받아 저장한다.
	2.	학생 정보를 출력하는 `show_info()` 메서드를 가진다.
	3.	점수를 변경하는 `update_score(new_score)` 메서드를 가진다.
아래와 같이 클래스를 사용했을 때, 예시와 같은 결과가 나오도록 하세요.
예시 코드
```python
s1 = Student("철수", 85)
s2 = Student("영희", 92)

s1.show_info()      # 이름: 철수, 점수: 85
s2.show_info()      # 이름: 영희, 점수: 92

s1.update_score(90)
s1.show_info()      # 이름: 철수, 점수: 90
```

<details>
<summary>풀이</summary>

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")

    def update_score(self, new_score):
        self.score = new_score
s1 = Student("철수", 85)
s2 = Student("영희", 92)
s1.show_info()      # 이름: 철수, 점수: 85
s2.show_info()      # 이름: 영희, 점수: 92
s1.update_score(90)
s1.show_info()      # 이름: 철수, 점수: 90
```
</details>


#### 문제7: 학생과 대학생 클래스 만들기 (상속 활용)
	1.	Student 클래스를 만드세요.
	•	이름(name)과 점수(score)를 저장합니다.
	•	학생 정보를 출력하는 `show_info()` 메서드를 가집니다.
	2.	UniversityStudent 클래스를 만드세요.
	•	Student 클래스를 상속받습니다.
	•	추가로 전공(major) 정보를 저장합니다.
	•	학생 정보를 출력하는 `show_info()` 메서드를 오버라이드하여,
이름, 점수, 전공을 모두 출력하도록 하세요.

```python
s = Student("철수", 85)
u = UniversityStudent("영희", 92, "컴퓨터공학")

s.show_info()   # 이름: 철수, 점수: 85
u.show_info()   # 이름: 영희, 점수: 92, 전공: 컴퓨터공학
```

<details>
<summary>풀이</summary>

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")
class UniversityStudent(Student):
    def __init__(self, name, score, major):
        super().__init__(name, score)
        self.major = major

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}, 전공: {self.major}")
s = Student("철수", 85)
u = UniversityStudent("영희", 92, "컴퓨터공학")
s.show_info()   # 이름: 철수, 점수: 85
u.show_info()   # 이름: 영희, 점수: 92, 전공: 컴퓨터공학
```
</details>


#### 문제8: Pydantic BaseModel을 활용한 학생 정보 검증 및 JSON 변환
	1.	Student 클래스를 Pydantic의 `BaseModel`을 상속받아 만드세요.
	•	이름(name, str)과 점수(score, int)를 필드로 가집니다.
	•	점수는 0 이상 100 이하만 허용되도록 검증하세요.
	2.	여러 명의 학생 정보를 담은 딕셔너리 리스트가 있습니다.
이 리스트를 이용해 Student 인스턴스 리스트를 만드세요.
	3.	Student 인스턴스 리스트를 JSON 문자열로 변환하세요.
	4.	JSON 문자열을 다시 읽어와 Student 인스턴스 리스트로 복원하세요.
	5.	각 학생의 정보를 출력하세요.

```python
data = [
    {"name": "철수", "score": 85},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 78},
    {"name": "지영", "score": 90}
]

이름: 철수, 점수: 85
이름: 영희, 점수: 92
이름: 민수, 점수: 78
이름: 지영, 점수: 90

```

<details>
<summary>풀이</summary>

```python
from pydantic import BaseModel, Field, ValidationError
import json

class Student(BaseModel):
    name: str
    score: int = Field(..., ge=0, le=100)  # 0 이상 100 이하

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")

# 1. 딕셔너리 리스트로부터 Student 인스턴스 리스트 생성
data = [
    {"name": "철수", "score": 85},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 78},
    {"name": "지영", "score": 90}
]

students = [Student(**d) for d in data]

# 2. Student 인스턴스 리스트를 JSON 문자열로 변환
json_str = json.dumps([s.dict() for s in students], ensure_ascii=False, indent=2)

# 3. JSON 문자열을 다시 Student 인스턴스 리스트로 복원
loaded_data = json.loads(json_str)
loaded_students = [Student(**d) for d in loaded_data]

# 4. 학생 정보 출력
for s in loaded_students:
    s.show_info()
```
</details>

### 모듈화

#### 문제9: 학생 관리 시스템 모듈화
학생 정보를 관리하는 프로그램을 다음과 같이 **3개의 파일(모듈)**로 나누어 작성하세요.
1. `student.py`
	•	`Student` 클래스를 정의합니다.
	•	이름(name), 점수(score) 필드를 가집니다.
	•	점수는 0~100 사이만 허용하며, 범위를 벗어나면 예외를 발생시킵니다.
	•	학생 정보를 출력하는 `show_info()` 메서드를 가집니다.
2. `manager.py`
	•	`StudentManager` 클래스를 정의합니다.
	•	학생(Student) 인스턴스 리스트를 관리합니다.
	•	학생 추가, 전체 학생 정보 출력, 학생 정보를 파일로 저장/불러오기 기능을 메서드로 구현합니다.
	•	파일 저장/불러오기 시 JSON 형식을 사용합니다.
3. `main.py`
	•	사용자로부터 학생 정보를 입력받아 추가하고,
전체 학생 정보를 출력하며,
프로그램 종료 시 학생 정보를 파일로 저장하는 코드를 작성하세요.

```python
1. 학생 추가
2. 전체 학생 보기
3. 종료
메뉴 선택: 1
이름: 철수
점수: 105
점수는 0~100 사이여야 합니다.

메뉴 선택: 1
이름: 영희
점수: 92

메뉴 선택: 2
이름: 영희, 점수: 92

메뉴 선택: 3
학생 정보가 저장되었습니다.

```

<details>
<summary>풀이</summary>

1. `student.py`

```python
class ScoreError(Exception):
    pass

class Student:
    def __init__(self, name, score):
        if not (0 <= score <= 100):
            raise ScoreError("점수는 0~100 사이여야 합니다.")
        self.name = name
        self.score = score

    def show_info(self):
        print(f"이름: {self.name}, 점수: {self.score}")

    def to_dict(self):
        return {"name": self.name, "score": self.score}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["score"])
```

2. `manager.py`

```python
import json
from student import Student, ScoreError

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        try:
            student = Student(name, score)
            self.students.append(student)
        except ScoreError as e:
            print(e)

    def show_all(self):
        if not self.students:
            print("등록된 학생이 없습니다.")
        for s in self.students:
            s.show_info()

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f, ensure_ascii=False, indent=2)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.students = [Student.from_dict(d) for d in data]
        except FileNotFoundError:
            self.students = []

```
3. `main.py`

```python
from manager import StudentManager

def main():
    manager = StudentManager()
    manager.load_from_file("students.json")

    while True:
        print("\n1. 학생 추가")
        print("2. 전체 학생 보기")
        print("3. 종료")
        menu = input("메뉴 선택: ")

        if menu == "1":
            name = input("이름: ")
            try:
                score = int(input("점수: "))
            except ValueError:
                print("점수는 숫자로 입력하세요.")
                continue
            manager.add_student(name, score)
        elif menu == "2":
            manager.show_all()
        elif menu == "3":
            manager.save_to_file("students.json")
            print("학생 정보가 저장되었습니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()

```
</details>


### 기본 챗봇 만들기

https://docs.chainlit.io/integrations/openai

```sh
pip install -r requirements.txt

chainlit run app.py
```



