import React from "react";
import ReactDOM from "react-dom/client";
import { App } from "@/app/App";
import { installGlobalClientErrorLogger } from "@/shared/lib/client-error-logger";
import "@/shared/ui/styles/global.css";

installGlobalClientErrorLogger();

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);