import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "node:path";
import fs from "node:fs";

function webClientErrorLogPlugin() {
  const logDir = path.resolve(__dirname, "log");
  const logFile = path.join(logDir, "webapp_error.log");

  return {
    name: "web-client-error-log-plugin",
    configureServer(server: { middlewares: { use: (handler: (req: any, res: any, next: () => void) => void) => void } }) {
      server.middlewares.use((req, res, next) => {
        if (req.method !== "POST" || !req.url?.startsWith("/api/v1/client-error-log")) {
          next();
          return;
        }

        let raw = "";

        req.on("data", (chunk: Buffer | string) => {
          raw += chunk.toString();
          if (raw.length > 1_000_000) {
            raw = raw.slice(0, 1_000_000);
          }
        });

        req.on("end", () => {
          try {
            const payload = raw ? JSON.parse(raw) : {};
            const occurredAt = typeof payload.occurredAt === "string" && payload.occurredAt ? payload.occurredAt : new Date().toISOString();
            const line = [
              `${occurredAt} ERROR`,
              `type=${payload.type ?? "-"}`,
              `broker=${payload.broker ?? "-"}`,
              `url=${payload.url ?? "-"}`,
              `source=${payload.source ?? "-"}`,
              `line=${payload.line ?? 0}`,
              `column=${payload.column ?? 0}`,
              `ua=${payload.userAgent ?? "-"}`,
              `msg=${payload.message ?? "-"}`,
              `stack=${payload.stack ?? "-"}`,
            ].join(" ");

            fs.mkdirSync(logDir, { recursive: true });
            fs.appendFileSync(logFile, `${line}\n`, { encoding: "utf-8" });

            res.statusCode = 200;
            res.setHeader("Content-Type", "application/json; charset=utf-8");
            res.end(JSON.stringify({ status: "ok", message: "웹 오류 로그 저장 완료" }));
          } catch (error) {
            res.statusCode = 500;
            res.setHeader("Content-Type", "application/json; charset=utf-8");
            res.end(
              JSON.stringify({
                status: "error",
                message: "웹 오류 로그 저장 실패",
                detail: error instanceof Error ? error.message : String(error),
              })
            );
          }
        });
      });
    },
  };
}

export default defineConfig({
  plugins: [react(), webClientErrorLogPlugin()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  }
});