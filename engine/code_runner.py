"""
Code Runner & Test Case Execution Engine
LabPilot AI — Software Engineering Virtual Lab

Executes student or experiment code (C, C++, or Python) against test cases
using local compilers (MinGW GCC/G++) and runtime interpreters.
"""

import os
import subprocess
import tempfile
import time
import shutil

# Locate GCC/G++ or fallback
DEFAULT_GCC_PATHS = [
    r"C:\MinGW\bin\gcc.exe",
    r"C:\Program Files\MinGW\bin\gcc.exe",
    "gcc"
]

def get_gcc_path():
    for p in DEFAULT_GCC_PATHS:
        if os.path.isabs(p) and os.path.exists(p):
            return p
        which_p = shutil.which(p)
        if which_p:
            return which_p
    return None

def compile_c_code(source_code, output_exe_path):
    """
    Compiles C source code to an executable using MinGW gcc.
    Returns (success: bool, error_message: str)
    """
    gcc = get_gcc_path()
    if not gcc:
        return False, "MinGW GCC compiler not found in standard paths. Fallback to Python runner recommended."

    temp_c = output_exe_path + ".c"
    try:
        with open(temp_c, "w", encoding="utf-8") as f:
            f.write(source_code)

        cmd = [gcc, temp_c, "-o", output_exe_path]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
        
        if proc.returncode != 0:
            return False, f"Compilation Error:\n{proc.stderr}"
        return True, ""
    except subprocess.TimeoutExpired:
        return False, "Compilation timed out after 10 seconds."
    except Exception as e:
        return False, f"Compiler execution error: {str(e)}"
    finally:
        if os.path.exists(temp_c):
            try:
                os.remove(temp_c)
            except Exception:
                pass

def execute_program(command_list, test_input, timeout_sec=3):
    """
    Executes a compiled binary or python script with test_input piped into stdin.
    Returns (return_code, stdout, stderr, execution_time_ms)
    """
    start_time = time.time()
    try:
        proc = subprocess.run(
            command_list,
            input=test_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout_sec
        )
        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip(), elapsed_ms
    except subprocess.TimeoutExpired:
        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        return -1, "", "Execution Timed Out (Infinite loop or waiting for input)", elapsed_ms
    except Exception as e:
        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        return -2, "", str(e), elapsed_ms

def run_test_suite(language, code, test_cases):
    """
    Runs a list of test cases against the code.
    test_cases is a list of dicts: [
      {"id": "TC-01", "name": "Equilateral Triangle", "input": "5 5 5", "expected": "EQUILATERAL"}, ...
    ]
    """
    results = []
    passed_count = 0
    total_count = len(test_cases)
    temp_dir = tempfile.mkdtemp(prefix="labpilot_test_")

    try:
        if language.lower() in ["c", "cpp", "c++"]:
            exe_path = os.path.join(temp_dir, "solution.exe")
            ok, err = compile_c_code(code, exe_path)
            if not ok:
                return {
                    "success": False,
                    "compilation_error": err,
                    "results": [],
                    "passed": 0,
                    "total": total_count,
                    "coverage_percent": 0
                }
            run_cmd = [exe_path]
        else: # Python
            py_file = os.path.join(temp_dir, "solution.py")
            with open(py_file, "w", encoding="utf-8") as f:
                f.write(code)
            # Use sys.executable or python
            import sys
            run_cmd = [sys.executable, py_file]

        for tc in test_cases:
            tc_id = tc.get("id", "TC")
            tc_name = tc.get("name", "Unnamed Test")
            inp = tc.get("input", "").strip()
            exp = tc.get("expected", "").strip()

            rc, stdout, stderr, elapsed = execute_program(run_cmd, inp)

            # Compare stdout with expected
            if rc == -1:
                status = "TIMEOUT"
                passed = False
            elif rc != 0:
                status = "RUNTIME_ERROR"
                passed = False
            else:
                passed = (stdout == exp)
                status = "PASS" if passed else "FAIL"

            if passed:
                passed_count += 1

            results.append({
                "id": tc_id,
                "name": tc_name,
                "input": inp,
                "expected": exp,
                "actual": stdout if rc == 0 else f"Error: {stderr}",
                "status": status,
                "passed": passed,
                "execution_time_ms": elapsed
            })

        coverage = round((passed_count / total_count * 100), 1) if total_count > 0 else 0
        return {
            "success": True,
            "compilation_error": "",
            "results": results,
            "passed": passed_count,
            "total": total_count,
            "coverage_percent": coverage
        }

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
