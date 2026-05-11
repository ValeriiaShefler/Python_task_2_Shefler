# Задача 4: Студенты и аспиранты
# Создаем классы, которые будут связаны друг с другом (аспирант - особый вид студента)

class Student:
    # базовый класс студент
    
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float):
        # у студента есть ФИО, возраст, номер группы и средний балл
        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade
    
    def get_info(self) -> str:
        #возвращает информацию о человеке
        return f"ФИО: {self.full_name}, Возраст: {self.age} лет, Номер группы: {self.group_number}, Средний балл: {self.average_grade}"
    
    def get_scholarship(self) -> int:
        #буду считать, что без стипендии студент остается, если средний балл 4 и больше
        if self.average_grade == 5.0:
            return 6000
        elif self.average_grade < 5.0 and self.average_grade >= 4.0:
            return 4000
        else:
            # Если балл ниже 3.0 или например отрицательный
            return 0
    
    def compare_scholarship(self, other) -> str:
        # сравниваем стипендии студентов как это делали с параметрами фигур
        my_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()
        
        if my_scholarship > other_scholarship:
            return f"Стипендия {self.full_name} ({my_scholarship}р) > стипендии {other.full_name} ({other_scholarship}р)"
        elif my_scholarship < other_scholarship:
            return f"Стипендия {self.full_name} ({my_scholarship}р) < стипендии {other.full_name} ({other_scholarship}р)"
        else:
            return f"Стипендии равны: {my_scholarship}р у {self.full_name} и {other.full_name}"
    
    
class GraduateStudent(Student):
    # класс аспирант с научной работой
    
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float, research_topic: str):
        #вызываем метод родителя через super() чтобы задать параметры студента, а затем добавляем науч работу
        super().__init__(full_name, age, group_number, average_grade)
        self.research_topic = research_topic  # добавляем новое свойство - тему научной работы
    
    def get_info(self) -> str:
        #дополняем также метод вывода научной работой
        base_info = super().get_info()  # берем родительскую инфу (ФИО и возраст)
        return f"{base_info}, Научная работа: '{self.research_topic}'"
    
    def get_scholarship(self) -> int:
        #переопределяем метод расчета стипендии, потому что у аспирантов она больше
        if self.average_grade == 5.0:
            return 8000
        elif self.average_grade < 5.0 and self.average_grade >= 4.0:
            return 6000
        else:
            return 0

def main():
    #Тестируем
    print("=" * 60)
    print("СОЗДАНИЕ СТУДЕНТОВ И АСПИРАНТОВ")
    print("=" * 60)
    
    # Создаем обычных студентов
    student1 = Student("Сычева Лина Игоревна", 20, "5142704/50801", 5.0)
    student2 = Student("Петров Иван Иванович", 20, "5142704/50701", 3.2)
    student3 = Student("Шефлер Валерия Александровна", 22, "5142704/50801", 4.8)  # плохая успеваемость
    
    # Создаем аспирантов
    grad1 = GraduateStudent("Иванов Петр Петрович", 24, "5144704/53301", 5.0, "Искусственный интеллект и промышленные вентиляторы")
    grad2 = GraduateStudent("Викторов Виктор Викторович", 24, "5174704/53321", 4.5, "Интернет вещей как инновация")
    
    print("\nИНФОРМАЦИЯ О ЛЮДЯХ:")
    print("-" * 40)
    print(student1.get_info())
    print(student2.get_info())
    print(grad1.get_info())
    print(grad2.get_info())
    
    print("\n" + "=" * 60)
    print("СТИПЕНДИИ:")
    print("=" * 60)
    print(f"{student1.full_name}: {student1.get_scholarship()}р (средний балл {student1.average_grade})")
    print(f"{student2.full_name}: {student2.get_scholarship()}р (средний балл {student2.average_grade})")
    print(f"{student3.full_name}: {student3.get_scholarship()}р (средний балл {student3.average_grade})")
    print(f"{grad1.full_name}: {grad1.get_scholarship()}р (средний балл {grad1.average_grade})")
    print(f"{grad2.full_name}: {grad2.get_scholarship()}р (средний балл {grad2.average_grade})")
    
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ СТИПЕНДИЙ:")
    print("=" * 60)
    print(student1.compare_scholarship(student2))
    print(student2.compare_scholarship(grad1))
    print(grad1.compare_scholarship(grad2))
    print(student3.compare_scholarship(student1))
    print(grad2.compare_scholarship(student2))

if __name__ == "__main__":
    main()