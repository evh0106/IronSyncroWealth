"""호환용 래퍼: 기존 websocket.main 경로를 src/websocket.py로 연결합니다."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

_MODULE_KEY = '_kiwoom_websocket_entry'


def _load_entry_module():
    mod = sys.modules.get(_MODULE_KEY)
    if mod is not None:
        return mod

    entry_path = Path(__file__).resolve().parents[1] / 'websocket.py'
    spec = spec_from_file_location(_MODULE_KEY, entry_path)
    if spec is None or spec.loader is None:
        raise ImportError(f'Cannot load websocket entry module: {entry_path}')

    mod = module_from_spec(spec)
    sys.modules[_MODULE_KEY] = mod
    spec.loader.exec_module(mod)
    return mod


_entry = _load_entry_module()

run_realtime_quote = _entry.run_realtime_quote
run_account_realtime = _entry.run_account_realtime
run_condition_search = _entry.run_condition_search

# 백그라운드 WebSocket (REST API와 동시 사용)
run_realtime_quote_bg = _entry.run_realtime_quote_bg
run_account_realtime_bg = _entry.run_account_realtime_bg
stop_realtime_background = _entry.stop_realtime_background
is_realtime_running = _entry.is_realtime_running

main = _entry.main


if __name__ == '__main__':
    main()
