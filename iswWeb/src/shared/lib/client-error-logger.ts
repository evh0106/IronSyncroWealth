import { useUiStore } from "@/app/store/ui-store";

type ClientErrorPayload = {
  type: "error" | "unhandledrejection";
  message: string;
  stack?: string;
  url?: string;
  source?: string;
  line?: number;
  column?: number;
};

function postClientError(payload: ClientErrorPayload): void {
  const broker = useUiStore.getState().broker;
  const body = {
    ...payload,
    userAgent: navigator.userAgent,
    broker,
    occurredAt: new Date().toISOString(),
  };

  const endpoint = "/api/v1/client-error-log";

  fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
    keepalive: true,
  }).catch(() => {
    // Logging failure should not break the app.
  });
}

export function installGlobalClientErrorLogger(): void {
  window.addEventListener("error", (event) => {
    postClientError({
      type: "error",
      message: event.message || "Unknown client error",
      stack: event.error?.stack || "",
      url: window.location.href,
      source: event.filename || "",
      line: event.lineno || 0,
      column: event.colno || 0,
    });
  });

  window.addEventListener("unhandledrejection", (event) => {
    const reason = event.reason;
    const message = reason instanceof Error ? reason.message : String(reason ?? "Unhandled rejection");
    const stack = reason instanceof Error ? reason.stack || "" : "";

    postClientError({
      type: "unhandledrejection",
      message,
      stack,
      url: window.location.href,
    });
  });
}
