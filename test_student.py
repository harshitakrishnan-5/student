import subprocess
import sys
# ----------- UNIT TESTS FOR calculate_grade -----------
def test_grade_S():
    from student import calculate_grade
    assert calculate_grade(95) == "S"

def test_grade_A():
    from student import calculate_grade
    assert calculate_grade(85) == "A"

def test_grade_B():
    from student import calculate_grade
    assert calculate_grade(70) == "B"

def test_grade_C():
    from student import calculate_grade
    assert calculate_grade(55) == "C"

def test_grade_D():
    from student import calculate_grade
    assert calculate_grade(45) == "D"

def test_grade_F():
    from student import calculate_grade
    assert calculate_grade(30) == "F"
# ----------- INTEGRATION TEST (FULL SCRIPT RUN) -----------
def test_student_program_execution():
    result = subprocess.run(
        [
            sys.executable,
            "student.py",
            "Harshita",
            "Integrated",
            "MCA",
            "3",
            "80",
            "98",
            "70",
        ],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Harshita" in result.stdout
    assert "Integrated MCA" in result.stdout
    assert "Average" in result.stdout
    assert "Grade" in result.stdout
