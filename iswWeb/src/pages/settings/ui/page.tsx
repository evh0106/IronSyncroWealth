import { useUiStore } from "@/app/store/ui-store";

export function SettingsPage() {
  const theme = useUiStore((state) => state.theme);
  const setTheme = useUiStore((state) => state.setTheme);

  return (
    <div className="page-stack">
      <h1>Settings</h1>
      <p className="lead">브로커 연동 및 앱 테마 같은 전역 설정을 관리합니다.</p>
      <section className="panel">
        <h3>Theme</h3>
        <div className="broker-switch">
          <button className={theme === "sunrise" ? "active" : ""} onClick={() => setTheme("sunrise")} type="button">
            Sunrise
          </button>
          <button className={theme === "midnight" ? "active" : ""} onClick={() => setTheme("midnight")} type="button">
            Midnight
          </button>
        </div>
      </section>
    </div>
  );
}