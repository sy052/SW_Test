# tests/test_markers.py
import pytest
import sys
import time


@pytest.mark.skip(reason="이 기능은 아직 개발 중입니다. 테스트를 건너뜁니다.")
def test_wip_feature():
    """Work-In-Progress 기능 테스트 (항상 스킵됨)."""
    print("\n이 메시지는 출력되지 않습니다 (스킵됨).")
    assert False

is_windows = sys.platform == "win32"
reason_for_skip = "Windows 환경에서만 실행 가능한 테스트입니다."

@pytest.mark.skipif(not is_windows, reason=reason_for_skip)
def test_windows_only_functionality():
    """Windows 특정 기능을 테스트합니다."""
    print("\nWindows에서만 이 메시지가 보입니다!")
    assert True

@pytest.mark.skipif(sys.version_info < (3, 9), reason="Python 3.9 이상 버전이 필요합니다.")
def test_requires_newer_python():
    """최신 파이썬 기능에 의존하는 테스트."""
    print(f"\n이 테스트는 Python {sys.version_info.major}.{sys.version_info.minor} 에서 실행 중입니다.")
    assert True

@pytest.mark.xfail(reason="알려진 버그 #456. 현재는 실패가 정상입니다.")
def test_known_bug_in_calculation():
    """현재 버그로 인해 실패할 것으로 예상되는 테스트."""
    print("\n실행은 되지만, 결과는 XFAIL 또는 XPASS 입니다.")
    assert 0.1 + 0.7 == 0.8 # 부동소수점 문제로 실패 가능성

@pytest.mark.xfail(strict=True, reason="버그가 수정되어 이제 통과하면 안 됩니다!")
def test_fixed_bug_should_now_pass_but_marked_xfail():
     """xfail(strict=True)로 표시했지만, 버그 수정 후 통과 시 최종 결과 FAILED."""
     print("\n이 테스트는 이제 통과하지만, xfail(strict=True) 이므로 최종 결과는 FAILED.")
     assert True

@pytest.mark.smoke
def test_quick_smoke_check():
    """빠르게 핵심 기능을 확인하는 스모크 테스트."""
    print("\nRunning Smoke test...")
    assert True

@pytest.mark.regression
def test_bug_fix_verification():
    """과거 버그가 수정되었는지 확인하는 회귀 테스트."""
    print("\nRunning Regression test...")
    assert True

@pytest.mark.slow
def test_time_consuming_operation():
    """실행 시간이 오래 걸리는 테스트."""
    print("\nRunning Slow test (1초 대기)...")
    time.sleep(1)
    assert True

@pytest.mark.smoke
@pytest.mark.ui
def test_login_ui_smoke():
    """로그인 UI의 스모크 테스트."""
    print("\nRunning UI Smoke test...")
    assert True




